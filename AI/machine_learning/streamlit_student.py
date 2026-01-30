import streamlit as st
import pandas as pd
import joblib


# MODELNI YUKLASH

model = joblib.load("student_model.pkl")

st.set_page_config(page_title="Talaba Bashorati", page_icon="🎓")
st.title("🎓 Talabaning O‘tish / O‘tmasligini Bashorat qilish")

st.write("Quyidagi ma’lumotlarni kiriting va natijani oling 👇")


# INPUTLAR

age = st.slider("Yosh", min_value=15, max_value=22, value=18)

traveltime = st.selectbox(
    "Maktabga borish vaqti",
    options=[1, 2, 3, 4],
    format_func=lambda x: {
        1: "Juda yaqin",
        2: "Yaqin",
        3: "Uzoq",
        4: "Juda uzoq"
    }[x]
)

health = st.slider("Sog‘liq darajasi (1 = yomon, 5 = yaxshi)", 1, 5, 3)

absences = st.number_input(
    "Qoldirilgan darslar soni",
    min_value=0,
    max_value=100,
    value=15
)

alcohol_level = st.slider(
    "Alkogol darajasi",
    min_value=0.0,
    max_value=5.0,
    value=1.0
)

parent_education_avg = st.slider(
    "Ota-ona ta’lim darajasi (o‘rtacha)",
    min_value=1.0,
    max_value=5.0,
    value=2.0
)

social_activity = st.slider(
    "Ijtimoiy faollik",
    min_value=1.0,
    max_value=5.0,
    value=4.0
)

academic_risk = st.slider(
    "Akademik xavf darajasi",
    min_value=0.0,
    max_value=5.0,
    value=2.0
)

paid = st.selectbox("Pullik darslar", ["yes", "no"])
activities = st.selectbox("Darsdan tashqari faoliyat", ["yes", "no"])
higher = st.selectbox("Oliy ta’lim olish istagi", ["yes", "no"])


# BASHORAT

if st.button("📊 Natijani ko‘rish"):
    input_df = pd.DataFrame([{
        "age": age,
        "traveltime": traveltime,
        "health": health,
        "absences": absences,
        "alcohol_level": alcohol_level,
        "parent_education_avg": parent_education_avg,
        "social_activity": social_activity,
        "academic_risk": academic_risk,
        "paid": paid,
        "activities": activities,
        "higher": higher
    }])

    prediction = model.predict(input_df)[0]
    confidence = model.predict_proba(input_df)[0][prediction]

    st.markdown("---")

    if prediction == 1:
        st.success(f"✅ **Talaba O‘TDI!**\n\nIshonchlilik: **{confidence*100:.2f}%**")
    else:
        st.error(f"❌ **Talaba O‘TA OLMADI**\n\nIshonchlilik: **{confidence*100:.2f}%**")
