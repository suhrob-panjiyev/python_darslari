from inspect import markcoroutinefunction
import json
import streamlit as st
import pandas as pd

tabel=pd.DataFrame({"Column 1": [1,2,3,4,5,6,7], "Column 2": [11,12,13,14,15,16,17]})

st.title("Salom! Men streamlit web app man.")
st.subheader("Salom men subheader man.")
st.header("Salom men header man.")
st.text("Salom men text man.")
# st.markdown("")


st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown('''
...     :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
...     :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
st.markdown("Here's a bouquet &mdash;\
...             :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")


st.markdown(''' :yellow[sariq rang] :blue[ko'k rang]  :red[qizil rang] __ :rainbow[rainbow rang] ''')


json={"a":"1,2,3", "b": "4, 5, 6"}
st.json(json)

code="""
print("hello world")
def funct():
    return 0; """
st.code(code, language="python")

st.write("## H2")

st.metric(label="Wind Speed", value="120ms⁻¹", delta="1.4ms⁻¹")

st.table(tabel)
st.dataframe(tabel)

# )))))))))))))))))))))))))))))))))))))))))))

st.markdown("""
 :red[IMDb top filmlar]
""")

code="""
print("Salom dunyo!")
def abd():
    return 0;
a+b=c
bu yer string type, yani
faqat malumot beradi.
"""
st.code(code, language="python")

st.metric(label="salom",
          value="alik",
          delta="-25ms²"
          )
st.metric(label="Dushanba", value="Quyoshli", delta="20m/s²")

st.image("foto.jpg", caption="Bu dasturchining rasmi")
st.audio("xcho.mp3")
st.video("video.mp4")