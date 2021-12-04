#!/usr/bin/env python
# coding: utf-8

# In[ ]:




# from multiapp import MultiApp
# import streamlit as st
# import numpy as np
# import pandas as pd

# add_selectbox = st.sidebar.radio(
#     "Select the type of SEARCH METHOD",
#     ("SIMILARITY SEARCH Method", "FAISS Method")
# )

# st.markdown('<style>body{background-color: #FFFEF2;}</style>',unsafe_allow_html=True)

# if add_selectbox == 'SIMILARITY SEARCH Method' :
#  st.title("Images using Similarity Search Method")
#  st.write("-------------------------------------------------------------------------------------------------")
#  def get_data():
#     return pd.read_csv(r'C:\Users\prana\Downloads\img\Faiss_n.csv')
#  n=1
#  df = get_data()
#  images = df['0'].unique()
#  #images1 = df['second']
#  st.subheader("Choose an image from the below list : ")
#  pic = st.selectbox('Choices : ', images)
#  st.subheader("**_IMAGE_** selected by the **_USER!_**")
#  st.image(pic,width=None)
#  #st.write('Hello, *World!* :kissing_closed_eyes:')
#  #st.subheader("BELOW ARE THE")
#  st.subheader('How Many Images do you want to see?')
#  z = st.radio(
#     'Select the Number',
#     (1,2,3,4,5,6,7,8,9,10))
#  st.subheader("SIMILAR IMAGES OF THE **_SELECTED IMAGE :_**")
#  for index, row in df.iterrows():
#      if row['0']==pic:
#         while n < z+1:
#             st.image(row[n], use_column_width=None, caption=row[n])
#             n+=1
            
# elif add_selectbox == 'FAISS Method':
#  st.title("Images using FAISS Method")
#  st.write("-------------------------------------------------------------------------------------------------")
#  def get_data():
#     return pd.read_csv(r'C:\Users\prana\Downloads\img\Faiss_n.csv')
#  n=1
#  df = get_data()
#  images = df['0'].unique()
#  #images1 = df['second']
#  st.subheader("Choose an image from the below list : ")
#  pic = st.selectbox('Choices:', images)
#  st.subheader("**_IMAGE_** selected by the **_USER!_**")
#  st.image(pic,width=None)


#  z = st.slider('How many images do you want to see?', 1, 10, 5)
#  st.write("-------------------------------------------------------------------------------------------------")
#  st.subheader("SIMILAR IMAGES OF THE **_SELECTED IMAGE :_**")
#  for index, row in df.iterrows():
#      if row['0']==pic:
#          while n < z+1:
            
#              st.image(row[n], use_column_width=None, caption=row[n])
#              n+=1

            


# if genre == '1': 
#     st.image(row[1], use_column_width=None, caption=row[1])
#     #st.write('You selected comedy.')
#     else if genre == '2': 
#     st.image(row[2], use_column_width=None, caption=row[2])
#     #st.write("You didn't select comedy.")


# In[ ]:


import streamlit as st
from PIL import Image
import pandas as pd
import glob
import os
from multiapp import MultiApp
       
add_selectbox = st.sidebar.radio(
    "Select the type of SEARCH METHOD",
    ("SIMILARITY SEARCH Method", "FAISS Method", "Upload image")
)
  
 
def load_image(image_file):
    img = Image.open(image_file)
    return img


def asearch():
    st.title("Images using Artistic Style Similarity Search Method")
    st.write("-------------------------------------------------------------------------------------------------")
    
    def get_data():
        return pd.read_csv(r'C:\Users\prana\Downloads\img\Faiss.csv')
       
    n = 1
    df = get_data()
    images = df['0'].unique()
    st.subheader("Choose an image from the dropdown : ")
    pic = st.selectbox('Choices : ', images)
    st.image(pic, width=None)
    
    st.subheader('How Many Images do you want to see?')
    z = st.slider('How many images do you want to see?', 1, 10, 1)
    st.subheader("Similar Products you may want to buy")
    for index, row in df.iterrows():
        if row['0'] == pic:     
            while n < z + 1:
                st.image(row[str(n)], width=100, caption=row[str(n)])
                n += 1

def fbfa():
    st.title("Images using Facebook FAISS")
    st.write("-------------------------------------------------------------------------------------------------")

    def get_data():
        return pd.read_csv(r'C:\Users\prana\Downloads\img\Faiss.csv')

    n = 1
    df = get_data()
    images = df['0'].unique()
    st.subheader("Choose an image from the below menu: ")
    pic = st.selectbox('Choices : ', images)
    st.image(pic, width=None)
    z = st.slider('Similar images to be shown?', 1, 10, 1)
    st.subheader("Similar Products")
    for index, row in df.iterrows():
        if row['0'] == pic:
            while n < z + 1:
                st.image(row[str(n)], width=100, caption=row[str(n)])
                n += 1


def uploadImage():
    st.title("Upload Image")
    st.write("-------------------------------------------------------------------------------------------------")
    def get_data():
        return pd.read_csv(r'C:\Users\prana\Downloads\img\Faiss.csv')
    n = 1
    df = get_data()
    images = df['0'].unique()
    st.subheader("Upload an image below: ")
    try:
        pic = st.file_uploader("Upload file", ["png", "jpg"])
        st.image(pic, width=None)
        z = st.slider('Similar images to be shown?', 1, 10, 1)
        st.subheader("Similar Products")
        for index, row in df.iterrows():
            if os.path.basename(str(row['0'])) == str(pic.name):         
                while n < z + 1:
                    st.image(row[str(n)], width=100, caption=row[str(n)])
                    n += 1
    except:
        print("Empty File!")
    
               
if add_selectbox == 'SIMILARITY SEARCH Method' :
    asearch()   
elif add_selectbox == 'FAISS Method':
    fbfa()   
elif add_selectbox == 'Upload image':
    uploadImage()  

