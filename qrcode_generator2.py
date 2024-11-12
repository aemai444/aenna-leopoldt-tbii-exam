import streamlit as st
import segno
import time
import os

#add a banner
st.image("https://st5.depositphotos.com/17620692/62481/v/450/depositphotos_624810244-stock-illustration-dark-purple-abstract-banner-background.jpg")

def generate_qrcode_page():
    directory_path = "../images"
    os.makedirs(directory_path, exist_ok=True)
    #add a title
    st.title("QR CODE GENERATOR")

    #add a text box
    url = st.text_input("Please enter the url you want to encode")

    def generate_qrcode(url):
        qrcode = segno.make_qr(url)
        qrcode.to_pil(scale=5, dark="purple", light="blue").save("images/qrcode_streamlit.png")

    if url:
        with st.spinner("Generate QR code"):
            time.sleep(2)
        generate_qrcode(url)
        st.image("images/qrcode_streamlit.png",
                 caption="Here is your qr code")

    st.markdown("Made by Aenna")