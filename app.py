from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd

# FASTAPI APP

app = FastAPI(
    title="Gallstone Prediction API",
    description="API for predicting Gallstone Status",
    version="1.0"
)

try:
    model = joblib.load("gallstone.pkl")
except Exception as e:
    raise RuntimeError(f"Error loading model: {e}")


class GallstoneInput(BaseModel):

    Age: float
    Gender: int
    Comorbidity: int
    CAD: int
    Hypothyroidism: int
    Hyperlipidemia: int
    DM: int

    Height: float
    Weight: float
    BMI: float

    TBW: float
    ECW: float
    ICW: float
    ECF_TBW: float
    TBFR: float
    LM: float

    Protein: float
    VFR: float
    BM: float
    MM: float
    Obesity: float
    TFC: float
    VFA: float
    VMA: float

    HFA: int

    Glucose: float
    TC: float
    LDL: float
    HDL: float
    Triglyceride: float

    AST: float
    ALT: float
    ALP: float

    Creatinine: float
    GFR: float
    CRP: float
    HGB: float
    Vitamin_D: float


# ==================================================
# HOME ENDPOINT
# ==================================================

@app.get("/")
def home():

    return {
        "message": "Gallstone Prediction API is running"
    }


# ==================================================
# PREDICTION ENDPOINT
# ==================================================

@app.post("/predict")
def predict(data: GallstoneInput):

    try:

        input_data = pd.DataFrame([{

            "Age": data.Age,
            "Gender": data.Gender,
            "Comorbidity": data.Comorbidity,
            "Coronary Artery Disease (CAD)": data.CAD,
            "Hypothyroidism": data.Hypothyroidism,
            "Hyperlipidemia": data.Hyperlipidemia,
            "Diabetes Mellitus (DM)": data.DM,

            "Height": data.Height,
            "Weight": data.Weight,
            "Body Mass Index (BMI)": data.BMI,

            "Total Body Water (TBW)": data.TBW,
            "Extracellular Water (ECW)": data.ECW,
            "Intracellular Water (ICW)": data.ICW,

            "Extracellular Fluid/Total Body Water (ECF/TBW)": data.ECF_TBW,

            "Total Body Fat Ratio (TBFR) (%)": data.TBFR,

            "Lean Mass (LM) (%)": data.LM,

            "Body Protein Content (Protein) (%)": data.Protein,

            "Visceral Fat Rating (VFR)": data.VFR,

            "Bone Mass (BM)": data.BM,

            "Muscle Mass (MM)": data.MM,

            "Obesity (%)": data.Obesity,

            "Total Fat Content (TFC)": data.TFC,

            "Visceral Fat Area (VFA)": data.VFA,

            "Visceral Muscle Area (VMA) (Kg)": data.VMA,

            "Hepatic Fat Accumulation (HFA)": data.HFA,

            "Glucose": data.Glucose,

            "Total Cholesterol (TC)": data.TC,

            "Low Density Lipoprotein (LDL)": data.LDL,

            "High Density Lipoprotein (HDL)": data.HDL,

            "Triglyceride": data.Triglyceride,

            "Aspartat Aminotransferaz (AST)": data.AST,

            "Alanin Aminotransferaz (ALT)": data.ALT,

            "Alkaline Phosphatase (ALP)": data.ALP,

            "Creatinine": data.Creatinine,

            "Glomerular Filtration Rate (GFR)": data.GFR,

            "C-Reactive Protein (CRP)": data.CRP,

            "Hemoglobin (HGB)": data.HGB,

            "Vitamin D": data.Vitamin_D

        }])


 
        # PREDICTION

        prediction = model.predict(input_data)[0]

        probabilities = model.predict_proba(input_data)[0]


        # ==========================================
        # YOUR CURRENT MODEL LOGIC
        #
        # Class 0 = POSITIVE
        # Class 1 = NEGATIVE
        # ==========================================

        positive_probability = float(probabilities[0] * 100)

        negative_probability = float(probabilities[1] * 100)


        # RESULT
        # ==========================================

        if prediction == 0:

            result = "POSITIVE"

            confidence = positive_probability

        else:

            result = "NEGATIVE"

            confidence = negative_probability



        # RETURN JSON RESPONSE


        return {

            "prediction": int(prediction),

            "result": result,

            "confidence": round(confidence, 2),

            "probabilities": {

                "positive": round(
                    positive_probability,
                    2
                ),

                "negative": round(
                    negative_probability,
                    2
                )
            }

        }


    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )