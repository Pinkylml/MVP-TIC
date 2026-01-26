import xgboost as xgb
import os
from pathlib import Path

class ModelLoader:
    _instance = None
    _booster = None
    
    # Hardcoded metadata from analysis
    DISTRIBUTION = "normal"
    SCALE = 2.8551127078884506  # ✅ CORRECT value from model metadata

    @classmethod
    def get_booster(cls):
        if cls._booster is None:
            # Path relative to this file: 
            # this file is in .../mvp_app/core/loader.py
            # model is in .../05_Evaluatin/artifacts_xgb/refined_best/...
            # We want to go up from core (1) -> mvp_app (2) -> 06_evaluating (3) -> TIC-workspace (4) -> 05_Evaluatin
            
            # Using absolute path logic based on common project root if possible, or relative
            # Ideally, valid from mvp_app root.
            
            # Production path: relative to app root
            base_path = Path(__file__).resolve().parent.parent # app root
            model_path = base_path / "models" / "model.json"
            
            if not model_path.exists():
                 raise FileNotFoundError(f"Model not found at: {model_path}")

            cls._booster = xgb.Booster()
            cls._booster.load_model(str(model_path))
            
        return cls._booster

    @classmethod
    def get_metadata(cls):
        return {
            "dist": cls.DISTRIBUTION,
            "scale": cls.SCALE
        }
