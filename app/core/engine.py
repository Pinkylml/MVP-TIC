import numpy as np
import pandas as pd
import xgboost as xgb
from scipy.stats import norm
from .loader import ModelLoader

class SurvivalEngine:
    def __init__(self):
        self.loader = ModelLoader
        # Metadata
        meta = self.loader.get_metadata()
        self.scale = meta["scale"]
        self.dist = meta["dist"]
        
    def _get_booster(self):
        return self.loader.get_booster()

    def align_features(self, input_data: dict) -> pd.DataFrame:
        """
        Align input dictionary to model's feature names.
        Missing features are filled with 0.
        """
        booster = self._get_booster()
        model_features = booster.feature_names
        
        # Create DataFrame from input
        df = pd.DataFrame([input_data])
        
        # Reindex to match model features, filling missing with 0
        df_aligned = df.reindex(columns=model_features, fill_value=0)
        
        # Ensure correct order
        df_aligned = df_aligned[model_features]
        
        return df_aligned

    def predict(self, input_data: dict) -> dict:
        """
        Predict survival curve from input dictionary.
        
        Returns dict with:
        - mu: predicted log-time (μ)
        - percentiles: dict mapping percentile names to time values
        - survival_curve: array of (time, S(t)) pairs
        """
        # 1. Align features
        df = self.align_features(input_data)
        
        # 2. Create DMatrix with explicit feature names
        # Production Fix: Clearly tell XGBoost what the feature names are
        dmatrix = xgb.DMatrix(data=df, feature_names=list(df.columns))
        
        # 3. Get prediction - USE output_margin=True to get real μ (log-time)
        # Without output_margin, XGBoost returns transformed time (not log)
        mu = self._get_booster().predict(dmatrix, output_margin=True)[0]
        
        print(f"[DEBUG] μ (margin/log-time): {mu}")
        
        # 4. Calculate survival curve S(t)
        # Based on AFT formula from evaluation notebook (line 482):
        # S(t) = 1 - Φ((log(t) - μ) / σ)
        times = np.linspace(0.1, 60, 120)  # 0.1 to 60 months
        z = (np.log(times) - mu) / self.scale
        
        if self.dist == "normal":
            F = norm.cdf(z)
        else:
            F = norm.cdf(z)  # fallback to normal
        
        S_t = 1.0 - F
        S_t = np.clip(S_t, 1e-9, 1.0)
        
        # 5. Calculate percentiles from survival curve
        # For percentile p, find time t where S(t) = 1-p
        percentiles = {}
        for p_name, p_value in [("p25", 0.25), ("p50", 0.50), ("p75", 0.75), ("p90", 0.90)]:
            target_survival = 1.0 - p_value
            # Find closest time where S(t) <= target
            idx = np.where(S_t <= target_survival)[0]
            if len(idx) > 0:
                percentiles[p_name] = float(times[idx[0]])
            else:
                percentiles[p_name] = float(times[-1])  # If never reaches, use max time
        
        # 6. Format survival curve for output
        survival_curve_output = [{"t": float(t), "S_t": float(s)} for t, s in zip(times, S_t)]
        
        results = {
            "mu": float(mu),
            "percentiles": percentiles,
            "survival_curve": survival_curve_output
        }
        
        return results
