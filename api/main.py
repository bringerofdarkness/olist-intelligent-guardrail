from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import joblib
import pandas as pd
import os

# 1. Initialize App
app = FastAPI(
    title="Olist Intelligent Guardrail API",
    description="Industry-standard API for real-time delivery delay prediction.",
    version="1.0.0"
)

# 2. Correct File Paths (Moving up to the root folder)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'robust_ensemble_model.joblib')
PREPROCESSOR_PATH = os.path.join(BASE_DIR, 'preprocessor_v3.joblib')

try:
    model = joblib.load(MODEL_PATH)
    preprocessor = joblib.load(PREPROCESSOR_PATH)
    print("Model and Preprocessor loaded successfully.")
except Exception as e:
    print(f"CRITICAL ERROR: Could not load artifacts. {e}")

# 3. Input Schema
class OrderInput(BaseModel):
    distance_km: float = Field(..., example=450.5)
    price: float = Field(..., example=120.0)
    freight_value: float = Field(..., example=25.5)
    product_weight_g: float = Field(..., example=1500.0)
    product_photos_qty: int = Field(default=1, example=3)
    purchase_hour: int = Field(..., ge=0, le=23)
    purchase_day_of_week: int = Field(..., ge=0, le=6)
    purchase_month: int = Field(..., ge=1, le=12)
    category_short: str = Field(..., example="health_beauty")
    seller_reliability: float = Field(..., example=0.07)
    state_late_avg: float = Field(..., example=0.12)

@app.post("/predict")
async def predict_delay(order: OrderInput):
    try:
        # Convert input to dict and add engineered features
        data = order.model_dump()
        data['logistics_stress'] = (data['distance_km'] * data['product_weight_g']) / 1000
        data['freight_ratio'] = data['freight_value'] / (data['price'] + 1)
        data['category_risk_score'] = data['state_late_avg'] 

        # Inference
        df_input = pd.DataFrame([data])
        processed_data = preprocessor.transform(df_input)
        
        # Note: CatBoost/Ensemble might return a list or array
        probability = model.predict_proba(processed_data)[0][1]
        
        # Use our optimal threshold (0.65)
        prediction = 1 if probability >= 0.65 else 0
        
        return {
            "prediction": "Late" if prediction == 1 else "On Time",
            "probability": round(float(probability), 4),
            "risk_status": "High" if probability >= 0.65 else "Low"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def home():
    return {"status": "active", "path": "F:/Self Project/olist-intelligent-guardrail"}