import streamlit as st
import requests
import pandas as pd

st.set_page_config(
    page_title="Gallstone Prediction System",
    page_icon="🩺",
    layout="wide"
)

API_URL = "http://127.0.0.1:8000/predict"

# CUSTOM BUTTON STYLE


st.markdown("""
<style>

div[data-testid="stFormSubmitButton"] > button {
    background-color: #2196F3;
    color: white;
    font-size: 18px;
    font-weight: bold;
    border-radius: 10px;
    border: none;
    height: 50px;
}

div[data-testid="stFormSubmitButton"] > button:hover {
    background-color: #1565C0;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# HEADER

st.title("🩺 Gallstone Prediction System")

st.write(
    "Enter the patient's clinical and body measurement information "
    "to generate a Gallstone Status prediction."
)

st.divider()

# INPUT FORM

with st.form("prediction_form"):

    st.subheader("👤 Personal Information")

    col1, col2, col3 = st.columns(3)

    with col1:

        age = st.number_input(
            "Age",
            min_value=1,
            max_value=120,
            value=42
        )

    with col2:

        gender = st.selectbox(
            "Gender",
            options=[0, 1]
        )

    with col3:

        comorbidity = st.selectbox(
            "Comorbidity",
            options=[0, 1]
        )


    st.divider()


    st.subheader("🏥 Medical Conditions")

    col1, col2, col3 = st.columns(3)

    with col1:

        cad = st.selectbox(
            "Coronary Artery Disease (CAD)",
            [0, 1]
        )

        hypothyroidism = st.selectbox(
            "Hypothyroidism",
            [0, 1]
        )


    with col2:

        hyperlipidemia = st.selectbox(
            "Hyperlipidemia",
            [0, 1]
        )

        dm = st.selectbox(
            "Diabetes Mellitus (DM)",
            [0, 1]
        )


    with col3:

        hfa = st.selectbox(
            "Hepatic Fat Accumulation (HFA)",
            [0, 1]
        )


    st.divider()

    st.subheader("⚖️ Body Measurements")

    col1, col2, col3 = st.columns(3)


    with col1:

        height = st.number_input(
            "Height",
            min_value=0.0,
            value=172.0
        )

        weight = st.number_input(
            "Weight",
            min_value=0.0,
            value=84.5
        )

        bmi = st.number_input(
            "Body Mass Index (BMI)",
            min_value=0.0,
            value=28.6
        )


    with col2:

        tbw = st.number_input(
            "Total Body Water (TBW)",
            min_value=0.0,
            value=45.2
        )

        ecw = st.number_input(
            "Extracellular Water (ECW)",
            min_value=0.0,
            value=18.2
        )

        icw = st.number_input(
            "Intracellular Water (ICW)",
            min_value=0.0,
            value=27.0
        )


    with col3:

        ecf_tbw = st.number_input(
            "Extracellular Fluid / Total Body Water (ECF/TBW)",
            min_value=0.0,
            value=40.3
        )

        tbfr = st.number_input(
            "Total Body Fat Ratio (TBFR)",
            min_value=0.0,
            value=28.5
        )

        lm = st.number_input(
            "Lean Mass (LM)",
            min_value=0.0,
            value=71.5
        )


    st.divider()

    st.subheader("📊 Body Composition")

    col1, col2, col3 = st.columns(3)


    with col1:

        protein = st.number_input(
            "Protein",
            min_value=0.0,
            value=17.2
        )

        vfr = st.number_input(
            "Visceral Fat Rating (VFR)",
            min_value=0.0,
            value=12.0
        )

        bm = st.number_input(
            "Bone Mass (BM)",
            min_value=0.0,
            value=3.1
        )


    with col2:

        mm = st.number_input(
            "Muscle Mass (MM)",
            min_value=0.0,
            value=58.7
        )

        obesity = st.number_input(
            "Obesity",
            min_value=0.0,
            value=29.4
        )

        tfc = st.number_input(
            "Total Fat Content (TFC)",
            min_value=0.0,
            value=24.8
        )


    with col3:

        vfa = st.number_input(
            "Visceral Fat Area (VFA)",
            min_value=0.0,
            value=14.2
        )

        vma = st.number_input(
            "Visceral Muscle Area (VMA)",
            min_value=0.0,
            value=35.6
        )


    st.divider()

    st.subheader("🧪 Blood Test Results")

    col1, col2, col3 = st.columns(3)


    with col1:

        glucose = st.number_input(
            "Glucose",
            min_value=0.0,
            value=98.0
        )

        tc = st.number_input(
            "Total Cholesterol (TC)",
            min_value=0.0,
            value=205.0
        )

        ldl = st.number_input(
            "LDL",
            min_value=0.0,
            value=128.0
        )

        hdl = st.number_input(
            "HDL",
            min_value=0.0,
            value=48.0
        )


    with col2:

        triglyceride = st.number_input(
            "Triglyceride",
            min_value=0.0,
            value=145.0
        )

        ast = st.number_input(
            "AST",
            min_value=0.0,
            value=22.0
        )

        alt = st.number_input(
            "ALT",
            min_value=0.0,
            value=25.0
        )

        alp = st.number_input(
            "ALP",
            min_value=0.0,
            value=82.0
        )


    with col3:

        creatinine = st.number_input(
            "Creatinine",
            min_value=0.0,
            value=0.9
        )

        gfr = st.number_input(
            "GFR",
            min_value=0.0,
            value=102.5
        )

        crp = st.number_input(
            "CRP",
            min_value=0.0,
            value=1.8
        )

        hgb = st.number_input(
            "Hemoglobin (HGB)",
            min_value=0.0,
            value=14.2
        )

        vitamin_d = st.number_input(
            "Vitamin D",
            min_value=0.0,
            value=29.5
        )

    submitted = st.form_submit_button(
        "🔍 Predict Gallstone Status",
        use_container_width=True
    )



# PREDICTION


if submitted:


    # CREATE JSON DATA FOR FASTAPI

    data = {

        "Age": age,
        "Gender": gender,
        "Comorbidity": comorbidity,

        "CAD": cad,
        "Hypothyroidism": hypothyroidism,
        "Hyperlipidemia": hyperlipidemia,
        "DM": dm,

        "Height": height,
        "Weight": weight,
        "BMI": bmi,

        "TBW": tbw,
        "ECW": ecw,
        "ICW": icw,
        "ECF_TBW": ecf_tbw,
        "TBFR": tbfr,
        "LM": lm,

        "Protein": protein,
        "VFR": vfr,
        "BM": bm,
        "MM": mm,
        "Obesity": obesity,
        "TFC": tfc,
        "VFA": vfa,
        "VMA": vma,

        "HFA": hfa,

        "Glucose": glucose,
        "TC": tc,
        "LDL": ldl,
        "HDL": hdl,
        "Triglyceride": triglyceride,

        "AST": ast,
        "ALT": alt,
        "ALP": alp,

        "Creatinine": creatinine,
        "GFR": gfr,
        "CRP": crp,
        "HGB": hgb,
        "Vitamin_D": vitamin_d
    }



    # SEND DATA TO FASTAPI

    try:

        with st.spinner("Analyzing patient data..."):

            response = requests.post(
                API_URL,
                json=data,
                timeout=30
            )


        # SUCCESS
    

        if response.status_code == 200:

            result = response.json()


            prediction = result["prediction"]

            confidence = result["confidence"]

            positive_probability = (
                result["probabilities"]["positive"]
            )

            negative_probability = (
                result["probabilities"]["negative"]
            )


            # RESULT SECTION

            st.divider()

            st.header("📋 Prediction Result")

            col1, col2 = st.columns(2)


    
            # PREDICTION

            with col1:

                if prediction == 0:

                    st.error(
                        "### ⚠️ Gallstone Status: POSITIVE"
                    )

                else:

                    st.success(
                        "### ✅ Gallstone Status: NEGATIVE"
                    )


 
            # CONFIDENCE


            with col2:

                st.metric(
                    "Prediction Confidence",
                    f"{confidence:.2f}%"
                )



            # PROBABILITY BREAKDOWN

            st.subheader(
                "📊 Model Probability Breakdown"
            )


            st.write(
                f"**Gallstone Positive:** "
                f"{positive_probability:.2f}%"
            )

            st.progress(
                int(positive_probability)
            )


            st.write(
                f"**Gallstone Negative:** "
                f"{negative_probability:.2f}%"
            )

            st.progress(
                int(negative_probability)
            )


            with st.expander(
                "🔎 View Submitted Patient Data"
            ):

                st.dataframe(
                    pd.DataFrame([data]),
                    use_container_width=True
                )


            st.warning(
                "This prediction is generated by a "
                "machine-learning model and should not "
                "be considered a medical diagnosis."
            )


        else:

            st.error(
                "❌ FastAPI Backend Error"
            )

            try:

                error_detail = response.json()

                st.write(error_detail)

            except Exception:

                st.write(response.text)


    except requests.exceptions.ConnectionError:

        st.error(
            "❌ Cannot connect to FastAPI backend."
        )

        st.info(
            "Start the FastAPI server using:\n\n"
            "`uvicorn main:app --reload`"
        )


    except requests.exceptions.Timeout:

        st.error(
            "❌ The prediction request timed out."
        )


    except Exception as e:

        st.error(
            f"❌ Error: {str(e)}"
        )