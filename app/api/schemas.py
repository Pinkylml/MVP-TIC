from pydantic import BaseModel, Field, validator
from typing import Dict, Optional, List

# S1 to S7 Identifiers based on model
# ["S1_Comunicacion_Esp", "S2_Compromiso_Etico", "S3_Trabajo_Equipo_Liderazgo", 
# "S4_Resp_Social", "S5_Gestion_Proyectos", "S6_Aprendizaje_Digital", "S7_Ingles"]

class PredictionInput(BaseModel):
    # Soft Skills (1-5 Likert Scale)
    s1_comunicacion: float = Field(..., alias="S1", ge=1, le=5)
    s2_compromiso: float = Field(..., alias="S2", ge=1, le=5)
    s3_trabajo_equipo: float = Field(..., alias="S3", ge=1, le=5)
    s4_resp_social: float = Field(..., alias="S4", ge=1, le=5)
    s5_gestion_proyectos: float = Field(..., alias="S5", ge=1, le=5)
    s6_aprendizaje_digital: float = Field(..., alias="S6", ge=1, le=5)
    s7_ingles: float = Field(..., alias="S7", ge=1, le=5)
    
    age: int = Field(..., alias="Edad", ge=15, le=100)
    gender: int = Field(..., alias="Genero_bin", description="0: Female, 1: Male") # Adjust if needed
    
    career: str = Field(..., alias="Carrera", description="Name of the career/faculty")
    
    # Optional manual override for technical skills/topics
    # E.g. {"python": 1, "data analysis": 1}
    # These keys must match the model's feature names exactly OR be handled by user knowledge
    technical_skills: Dict[str, float] = Field(default_factory=dict)

    def to_model_dict(self) -> Dict[str, float]:
        """
        Converts input to the flat dictionary expected by XGBoost.
        Automatically loads technical skills based on career.
        """
        from core.career_vectors import CareerVectorLoader
        
        data = {
            "S1_Comunicacion_Esp": self.s1_comunicacion,
            "S2_Compromiso_Etico": self.s2_compromiso,
            "S3_Trabajo_Equipo_Liderazgo": self.s3_trabajo_equipo,
            "S4_Resp_Social": self.s4_resp_social,
            "S5_Gestion_Proyectos": self.s5_gestion_proyectos,
            "S6_Aprendizaje_Digital": self.s6_aprendizaje_digital,
            "S7_Ingles": self.s7_ingles,
            "Edad": float(self.age),
            "Genero_bin": float(self.gender),
        }
        
        # Load technical skills vector for the selected career
        career_vector = CareerVectorLoader.get_vector_for_career(self.career)
        data.update(career_vector)
        
        # Handle Career One-Hot
        # Model expects: "carrera_clean_SOFTWARE", "carrera_clean_COMPUTACIÓN", etc.
        clean_career = self.career.strip().upper()
        career_key = f"carrera_clean_{clean_career}"
        data[career_key] = 1.0
        
        # Add/override with manual technical skills if provided
        for k, v in self.technical_skills.items():
            data[k] = v
            
        return data

class SurvivalOutput(BaseModel):
    mu: float
    percentiles: Dict[str, float]
    survival_curve: List[Dict[str, float]]
