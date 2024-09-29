import streamlit as st
import os
from PIL import Image 
import google.generativeai as genai

genai.configure(api_key='<api key>'
model=genai.GenerativeModel('gemini-1.5-flash')

def get_gemini_response(Input,Image,propmt):
    response=model.generate_content((Input,Image[0],input_prompt))
    return response.text

def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data=uploaded_file.getvalue()
        image_parts=[
            {
                'mime_type':uploaded_file.type,
                'data':bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError('No file was uploaded')

st.set_page_config(page_title='invoice generator')
st.sidebar.header('Robobill')
st.sidebar.write('Made by Aarushi')
st.sidebar.write('Powered by Google Gemini AI')
st.header('Robobill')

st.subheader('Manage your expenses with Robobill')
input=st.text_input('What do you want me to do?',key='input')
uploaded_file=st.file_uploader('Choose an image',type=['jpg','jpeg','png'])
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
st.image(image,caption='uploaded image',use_column_width=True)
submit=st.button("Let's go")

input_prompt="""
You are an expert in reading invoices,we are going to upload an image of an invoice and you will have to answer any tupe of questions that the user asks you.
You have to greet the user first.Make sure to keep the fonts uniform and give the items list in a point-wise format.
at the end,make sure to repear the name of our app "robobill" and ask the user to use it again.
"""
if submit:
    image_data=input_image_details(uploaded_file)
    response=get_gemini_response(input_prompt,image_data,input)
    st.subheader("Here's what you need to know!")
    st.write(response)





