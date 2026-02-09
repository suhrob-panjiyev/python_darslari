import streamlit as st
import pandas as pd
import joblib
import os

st.set_page_config(
    page_title="Talaba natijasini bashorat qilish",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Talaba natijasini bashorat qilish")
st.write("Kiritilgan ko‘rsatkichlar asosida talabaning **G3 >= 10** bo‘lish ehtimolini bashorat qiladi.")

# ===== Yo'riqnoma (expander) =====
with st.expander("ℹ️ Yo‘riqnoma va eslatmalarni ko‘rish"):
    st.markdown("""
**Bu ilova nima qiladi?**  
Ushbu veb-ilova talabaning kiritilgan ko‘rsatkichlari asosida **yakuniy bahosi (G3) 10 dan yuqori bo‘lishi** ehtimolini bashorat qiladi.

**Qanday foydalaniladi?**
1. Yuqoridan **modelni tanlang** (Logistic Regression / Random Forest / SVM).
2. Pastdagi formaga kerakli qiymatlarni kiriting.
3. **“🔮 Bashorat qilish”** tugmasini bosing.
4. Natijada **“O‘TDI / O‘TMADI”** va (mavjud bo‘lsa) **ishonchlilik foizi** ko‘rsatiladi.

**Muhim eslatma:**  
Bu natija **ML modeli bashorati** bo‘lib, 100% kafolat bermaydi. Real baholash va qarorlar uchun qo‘shimcha tahlil kerak bo‘lishi mumkin.
""")

# ===== Modellar ro'yxati (fayl nomlarini moslang) =====
MODELS = {
    "Logistic Regression (eng yaxshi natija)": "lr_model.pkl",
    "Random Forest": "rf_model.pkl",
    "SVM": "svm_model.pkl",
}

st.subheader("🧠 Model tanlash")
model_name = st.selectbox("Qaysi modeldan foydalanamiz?", list(MODELS.keys()))
model_path = MODELS[model_name]

@st.cache_resource
def load_model(path: str):
    return joblib.load(path)

# Model fayli bor-yo'qligini tekshirish
if not os.path.exists(model_path):
    st.error(
        f"❌ Model fayli topilmadi: `{model_path}`\n\n"
        "Iltimos, `.pkl` fayl shu papkada borligini tekshiring."
    )
    st.stop()

model = load_model(model_path)

st.subheader("📌 Kirish ma'lumotlari")

# ===== Input form =====
with st.form("student_form"):
    age = st.number_input("Yosh", min_value=10, max_value=30, value=18, step=1)

    traveltime = st.selectbox(
        "Yo‘lga ketadigan vaqt (1-4)",
        [1, 2, 3, 4],
        index=0,
        help="1 = juda yaqin, 4 = juda uzoq"
    )

    health = st.selectbox(
        "Sog‘liq darajasi (1-5)",
        [1, 2, 3, 4, 5],
        index=2
    )

    absences = st.number_input(
        "Dars qoldirishlar soni (Absences)",
        min_value=0,
        max_value=200,
        value=5,
        step=1
    )

    alcohol_level = st.slider("Ichimlik darajasi (0-5)", 0.0, 5.0, 1.0, 0.5)
    parent_education_avg = st.slider("Ota-ona ta'limi o‘rtachasi (0-4)", 0.0, 4.0, 2.0, 0.5)
    social_activity = st.slider("Ijtimoiy faollik (1-5)", 1.0, 5.0, 3.0, 0.5)
    academic_risk = st.slider("Akademik xavf (0-5)", 0.0, 5.0, 1.0, 0.5)

    # Model "yes/no" bilan o'rgatilgan — shuning uchun ichki qiymatlar shunday qoladi.
    paid = st.selectbox("Pullik qo‘shimcha darsga qatnaydimi?", ["no", "yes"], index=0)
    activities = st.selectbox("To‘garak / qo‘shimcha faoliyat bormi?", ["no", "yes"], index=0)
    higher = st.selectbox("Oliy ta'limni davom ettirmoqchimi?", ["no", "yes"], index=1)

    submitted = st.form_submit_button("🔮 Bashorat qilish")

# ===== Prediction =====
if submitted:
    sample_df = pd.DataFrame([{
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

    pred = int(model.predict(sample_df)[0])

    conf = None
    if hasattr(model, "predict_proba"):
        proba = model.predict_proba(sample_df)[0][pred]
        conf = round(proba * 100, 2)

    st.markdown("---")
    st.write(f"✅ Tanlangan model: **{model_name}**")

    if pred == 1:
        st.success("🎉 Natija: **O‘TDI** (G3 >= 10)")
    else:
        st.error("⚠️ Natija: **O‘TMADI** (G3 < 10)")

    if conf is not None:
        st.info(f"📊 Ishonchlilik: **{conf}%**")

    st.caption(f"Model fayli: {model_path}")

st.markdown("---")
st.info("""
🎓 **Ilova haqida:**  
Bu tizim Machine Learning modeli yordamida talabaning o‘qish natijasini bashorat qiladi.  
Riskdagi talabalarni erta aniqlash va ta’lim sifatini oshirishga xizmat qiladi.  
Natijalar faqat taxminiy hisoblanadi.
""")
