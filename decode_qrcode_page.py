import cv2
import streamlit as st
import numpy as np

def decode_qrcode_page():
    st.image(
        "https://st5.depositphotos.com/17620692/62481/v/450/depositphotos_624810244-stock-illustration-dark-purple-abstract-banner-background.jpg")
    st.header("Decode your QR Code")
    #add a file uploader widget
    qrcode = st.file_uploader("Upload your QR code:",
                     type=["jpg", "png", "jpeg"])

    #check you can place the image
    if qrcode:
        #annoying code to convert the uploaded qr code image into an image the decoder
        file_bytes = np.asarray(bytearray(qrcode.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes,1)

        #place the qrcode
        st.image(opencv_image)

        #decode the qrcode
        detector =cv2.QRCodeDetector()
        decoded_info, point, straight_qr = detector.detectAndDecode(opencv_image)
        st.write(f"Your Code contained {decoded_info}")