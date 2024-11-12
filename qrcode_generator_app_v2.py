import streamlit as st
from decode_qrcode_page import decode_qrcode_page
from qrcode_generator2 import generate_qrcode_page


options = ["GENERATE QR CODE", "DECODE QR CODE", "ABOUT ME"]
page_selection = st.sidebar.selectbox("Menu", options)

if page_selection == "GENERATE QR CODE":
    generate_qrcode_page()
elif page_selection == "DECODE QR CODE":
    decode_qrcode_page()
elif page_selection == "ABOUT ME":
    st.write ("Hi! My name is Aenna. I made this App")

