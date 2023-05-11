from model import extractValue
import streamlit as st
import numpy as np
import cv2

def saveImage(byteImage):
    nparr = np.fromstring(byteImage, np.uint8)
    imgFile = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
   
    return imgFile

st.set_page_config(
    page_title = 'Vibrio Counting',
    page_icon = '🦠'
)

st.header("Vibrio Counting Using Image")
st.subheader("Upload Image First")
fileUpload = st.file_uploader("Choose a file", type = ['jpg', 'png'])

if fileUpload:
    file = fileUpload.read()
    path = saveImage(file)

    st.subheader("Uploaded Image")
    imageUploadedHolder = st.empty()
    imageUploadedHolder.image(path)

    imageResults, vibrioResult = extractValue(path)

    st.subheader("Result Image")
    imageDetectedHolder = st.empty() 
    imageDetectedHolder.image(imageResults)

    st.subheader("Vibrio Result")
    st.text(f"Black : {vibrioResult['black']*10}")
    st.text(f"Yellow : {vibrioResult['yellow']*10}")
    st.text(f"Green : {vibrioResult['green']*10}")