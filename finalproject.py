#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 09:50:02 2023

@author: isabella
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Credit Card Acceptance Rate Explorer")
st.text("This app evaluates data that shows the likelihood of someone getting approved for a credit card based on several factors")
st.sidebar.title("Navigation")

def stats (dataframe):
       st.header("Data Statistics")
       st.write(dataframe.describe())

#def visual (dataframe):
       #figure out graphs here
       #st.header("Data Visualization")
       #fig, ax = plt.subplots (1,1)
       #ax.scatter(x=df[])

def page (dataframe): 
       st.header("Input Your Own Data")

uploaded_file = st.sidebar.file_uploader("Upload file here")

if uploaded_file: 
       
       df = pd.read_csv(uploaded_file)
       
options = st.sidebar.radio("Pages", options=["Data Statistics", "Data Visualization", "Input Your Own Data"])

if options == "Data Statistics":
       stats(df)

#if options == "Data Visualization":
       #visual(df)

if options == "Input Your Own Data":
       page(df)





import streamlit as st
import datetime
import pandas as pd 
import numpy as np 

#Multiple page configurations
st.set_page_config(
    page_title="Credit Card Eligibility", #Main.py file as main page
    page_icon="💳",
)

#Background image (WIP)
# st.markdown("""
#     <style>
#         .stApp {
#         background: url("");
#         background-size: cover;
#         }
#     </style>""", unsafe_allow_html=True)

st.title("Prediction of Credit Card approval")

st.sidebar.info("You are now on the eligibility page ✅")

st.write("""
        ### Check if you are eligible in seconds!✅💳
""")

#Get input from user
def input_features():

        #gender
        GENDER = st.selectbox("Select your Gender",("M","F"),index=None,placeholder="Select your option")

        #Birthday_count
        b_day = st.date_input("Your birthday date", min_value = datetime.date(1950,1,1))
        Birthday_count = np.abs((b_day - datetime.date.today()))
        Birthday_count = Birthday_count.days

        #Marital_status
        Marital_status = st.selectbox("Select your Marital status",("Single / not married","Married","Civil marriage","Separated","Widow"),index=None,placeholder="Select your option")

        #Children
        CHILDREN = st.slider("How many dependent children are currently under your care or support?",0,14)

        #Family_Members
        Family_Members = st.slider("How many number of family members?",0,15)


        #EDUCATION
        EDUCATION = st.selectbox("Select your Education level",("Lower secondary","Secondary / secondary special","Higher education","Academic degree","Incomplete higher"),index=None,placeholder="Select your option")

        #Employed_days
        employment_choice = st.selectbox('Choose your current employment status',('Employed','Unemployed'))
        min_date = datetime.date(1950,1,1)
        max_date = datetime.date.today()
        if employment_choice == 'Employed':
                #Employed_days
                em = st.date_input("Select your most recent employment date", min_value = min_date,max_value = max_date)
                Employed_days = (em - datetime.date.today())
                Employed_days = Employed_days.days
        if employment_choice == 'Unemployed':
                em = st.date_input("Select your the daterange of your unemployment", min_value = min_date,max_value=max_date)
                Employed_days = (datetime.date.today()- em)
                Employed_days = Employed_days.days

        #Type_Occupation
        Type_Occupation = st.selectbox("Select your Occupation type",("Laborers","Core staff","Managers","Sales staff","Drivers","High skill tech staff","Medicine staff","Accountants","Security staff","Cleaning staff","Cooking staff","Private service staff","Secretaries","Low-skill Laborers","Waiters/barmen staff","HR staff","IT staff","Realty agents"),index=None,placeholder="Select your option")

        #Annual_income
        Annual_income = st.slider("What is your total yearly earnings?",30000,1500000,step=5000)

        #Type_Income
        Type_Income = st.selectbox("Select your type of Income",("State servant","Pensioner","Commercial associate","Working"),index=None,placeholder="Select your option")

        #Car_owner
        Car_Owner = st.selectbox("Do you own ateast one car?",("Y","N"),index=None,placeholder="Select your option")

        #Propert_Owner
        Propert_Owner = st.selectbox("Do you own ateast one property?",("Y","N"),index=None,placeholder="Select your option")

        #Housing_type
        Housing_type = st.selectbox("Select your Housing type",("House / apartment","With parents","Rented apartment","Municipal apartment","Co-op apartment","Office apartment"),index=None,placeholder="Select your option")

        #Mobile_phone
        Mobile_phone = st.selectbox("Do you own a Mobile phone?",("Y","N"),index=None,placeholder="Select your option")


        #Work_Phone
        Work_Phone = st.selectbox("Do you own a Work phone?",("Y","N"),index=None,placeholder="Select your option")


        #Phone
        Phone = st.selectbox("Do you own atleast one phone number?",("Y","N"),index=None,placeholder="Select your option")


        #EMAIL_ID
        EMAIL_ID = st.selectbox("Do you have ateast one email ID created?",("Y","N"),index=None,placeholder="Select your option")


        # days to year conversion
        d = Birthday_count/365
        em_conv = Employed_days/365

        data = { 
                'GENDER':GENDER,
                'Car_Owner':Car_Owner,
                'Propert_Owner':Propert_Owner,
                'CHILDREN':CHILDREN,
                'Annual_income':Annual_income,
                'Type_Income':Type_Income,
                'EDUCATION':EDUCATION,
                'Marital_status': Marital_status,    
                'Housing_type'  : Housing_type,
                'Birthday_count'   :Birthday_count,
                'Employed_days'      :Employed_days,
                'Mobile_phone'       : Mobile_phone,
                'Work_Phone'         :Work_Phone,
                'Phone'              :Phone,
                'EMAIL_ID'           :EMAIL_ID,
                'Type_Occupation'    :Type_Occupation,
                'Family_Members' :Family_Members,
                'Age_conv': d,
                'Employed years': em_conv
                }
                                        
        user_input = pd.DataFrame(data,index=[0])
        return user_input

#Create a new dataframe for user input features
df = input_features()

#Prediction button
if st.button('Check my approval'):
        #will improve this section once the model part is ready,
        # until then this is just a example message when you click the button for prediction
        st.success('You are eligible')

