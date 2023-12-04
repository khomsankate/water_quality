import streamlit as st
import numpy as np
from joblib import load

# สร้างเพจให้ผู้ใช้อัพโหลดไฟล์โมเดล
st.title("Water Quality Prediction App")


# ให้ผู้ใช้อัพโหลดไฟล์โมเดล
uploaded_file = st.file_uploader("Choose a model file (.pkl)", type=["pkl"])

# ถ้าไฟล์ถูกอัพโหลด
if uploaded_file is not None:
    # โหลดโมเดล
    loaded_model = load(uploaded_file)

    # สร้างเพจที่ให้ผู้ใช้กรอกค่า
    st.header("Enter Water Quality Parameters")

    ph = st.number_input('Enter PH:', min_value=0.0, max_value=14.0, value=7.0)
    hardness = st.number_input('Enter Hardness:', min_value=47.0, value=323.0)
    solids = st.number_input('Enter Solids:', min_value=323.0, value=61227.0)
    chloramines = st.number_input('Enter Chloramines:', min_value=1.0, value=13.0)
    sulfate = st.number_input('Enter Sulfate:', min_value=129.0, value=481.0)
    conductivity = st.number_input('Enter Conductivity:', min_value=181.0, value=753.0)
    organic_carbon = st.number_input('Enter Organic Carbon:', min_value=2.0, value=28.0)
    trihalomethanes = st.number_input('Enter Trihalomethanes:', min_value=0.0, value=124.0)
    turbidity = st.number_input('Enter Turbidity:', min_value=1.0, value=6.0)

    # ปุ่มทำนาย
    predict_button = st.button('Predict Water Quality')

    # ถ้าผู้ใช้กดทำนาย
    if predict_button:
        # ให้โมเดลทำนาย
        input_data = np.array([[ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity]])
        prediction = loaded_model.predict(input_data)

        # แสดงผลลัพธ์
        if prediction[0] == 0:
            st.error("This Water Quality is Non-Potable")
        else:
            st.success('This Water Quality is Potable')
else:
    st.warning("Please upload a valid model file (.pkl)")
