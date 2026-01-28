import sys
import os
import pandas as pd
import numpy as np

# Add app to path
sys.path.append(os.path.join(os.getcwd(), 'app'))

from core.engine import SurvivalEngine

def test_rsf_engine():
    print("🚀 Initializing RSF Survival Engine...")
    try:
        engine = SurvivalEngine()
        print("✅ Engine Initialized.")
        
        # Sample input following the new schema
        input_data = {
            "S1": 5.0, "S2": 5.0, "S3": 5.0, "S4": 5.0, 
            "S5": 5.0, "S6": 5.0, "S7": 5.0,
            "Edad": 24, "Genero_bin": 0,
            "Carrera": "(RRA20) SOFTWARE", # Must match mapeo_carrera.json exactly
            "technical_skills": {
                "react, revit": 1.0,
                "sql, python": 1.0
            }
        }
        
        print(f"📊 Running prediction for career: {input_data['Carrera']}")
        results = engine.predict(input_data)
        
        print("✅ Prediction SUCCESS!")
        print(f"Model Algorithm: {results.get('algo', 'RSF')}")
        print(f"p50 (Median insertion time): {results['percentiles']['p50']:.2f} months")
        print(f"p75: {results['percentiles']['p75']:.2f} months")
        
        # Check survival curve
        curve = results['survival_curve']
        print(f"📈 Survival curve points: {len(curve)}")
        print(f"S(t=12): {curve[24]['S_t']:.4f}") # Approx 12 months if 120 points for 60m
        
    except Exception as e:
        print(f"❌ Verification FAILED: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_rsf_engine()
