import streamlit as st

st.title("Pigi ganteng😜🤟")
st.write(
    "Ayo kita belajar pelositi dengan bahasa Python gaskennn)."
)
st.image("view/IMG-20250423-WA0014.jpg")


st.tittle("Aplikasi Sederhana")
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis sebuah angka:", value=0, step=1)

if (angka % 2) == 0:
    st.write(f"{angka} adalah Bilangan Genap")
else:
    st.write(f"{angka} adalah Bilangan Ganjil")
    
