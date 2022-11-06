import streamlit as st
import pandas as pd
import numpy as np
import pickle  #to load a saved model
# import base64  #to open .gif files in streamlit app

# @st.cache(suppress_st_warning=True)
# def get_fvalue(val):
#     feature_dict = {"No":1,"Yes":2}
#     for key,value in feature_dict.items():
#         if val == key:
#             return value

# def get_value(val,my_dict):
#     for key,value in my_dict.items():
#         if val == key:
#             return value

app_mode = st.sidebar.selectbox('Select Page',['Home','Prediction']) #two pages

if app_mode=='Home':
    st.title('DEFAULT PREDICTION')  
elif app_mode=='Prediction':
    st.subheader('Please fill all necessary informations below:')
    st.sidebar.header("Informations about the client :")

    # Informations
    Limit_bal = st.sidebar.slider('Limit Balance',0,100000,0,100)

    gender_dict = {"Male":1,"Female":2}
    Gender = st.sidebar.radio('Gender',tuple(gender_dict.keys()))
    Sex_Female, Sex_Male = 0,0
    if Gender == 'Male':
        Sex_Male = 1
    elif Gender == 'Female':
        Sex_Female = 1

    edu={'Graduate':1,'Under graduate':2,'High school':3, 'Others':0}
    Education=st.sidebar.radio('Education',tuple(edu.keys()))
    Edu_Graduate, Edu_HighSchool, Edu_Others, Edu_Undergraduate = 0,0,0,0
    if Education == 'Graduate':
        Edu_Graduate = 1
    elif Education == 'Under graduate':
        Edu_Undergraduate = 1
    elif Education == 'High school':
        Edu_HighSchool = 1
    elif Education == 'Others':
        Edu_Others =1

    mary={'Married':1,'Single':2,'Others':0}
    Marrital_status=st.sidebar.radio('Marrital status',tuple(mary.keys()))
    Marriage_Married, Marriage_Others, Marriage_Single = 0,0,0
    if Marrital_status == 'Married':
        Marriage_Married = 1
    elif Marrital_status == 'Single':
        Marriage_Others = 1
    elif Marrital_status == 'Others':
        Marriage_Single = 1

    Age = st.sidebar.slider('Age',18,100,18,1)

    bill_amt_1 = st.sidebar.slider('Bill amount 1',0,100000,0,)
    bill_amt_2 = st.sidebar.slider('Bill amount 2',0,100000,0,)
    bill_amt_3 = st.sidebar.slider('Bill amount 3',0,100000,0,)
    bill_amt_4 = st.sidebar.slider('Bill amount 4',0,100000,0,)
    bill_amt_5 = st.sidebar.slider('Bill amount 5',0,100000,0,)
    bill_amt_6 = st.sidebar.slider('Bill amount 6',0,100000,0,)

    pay_amt_1 = st.sidebar.slider('Pay amount 1',0,100000,0,)
    pay_amt_2 = st.sidebar.slider('Pay amount 2',0,100000,0,)
    pay_amt_3 = st.sidebar.slider('Pay amount 3',0,100000,0,)
    pay_amt_4 = st.sidebar.slider('Pay amount 4',0,100000,0,)
    pay_amt_5 = st.sidebar.slider('Pay amount 5',0,100000,0,)
    pay_amt_6 = st.sidebar.slider('Pay amount 6',0,100000,0,)

    data1 = {
        'Age':Age,
        'Gender':[Sex_Female, Sex_Male ],
        'Education': [Edu_Graduate,Edu_HighSchool, Edu_Others, Edu_Undergraduate],
        'Married': [Marriage_Married , Marriage_Others, Marriage_Single],
        'Limit Balance': Limit_bal,
        'Bill amount 1':bill_amt_1,'Bill amount 2':bill_amt_2,
        'Bill amount 3':bill_amt_3,'Bill amount 4':bill_amt_4,
        'Bill amount 5':bill_amt_5,'Bill amount 6':bill_amt_6,
        'Pay amount 1': pay_amt_1,'Pay amount 2': pay_amt_2,
        'Pay amount 3': pay_amt_3,'Pay amount 4': pay_amt_4,
        'Pay amount 5': pay_amt_5,'Pay amount 6': pay_amt_6
    }

    feature_list=[Limit_bal,Age,
                  bill_amt_1,bill_amt_2,bill_amt_3,bill_amt_4,bill_amt_5,bill_amt_6,
                  pay_amt_1,pay_amt_2,pay_amt_3,pay_amt_4,pay_amt_5,pay_amt_6,
                  data1['Gender'][0],data1['Gender'][1],
                  data1['Education'][0],data1['Education'][1],data1['Education'][2],data1['Education'][3],
                  data1['Married'][0],data1['Married'][1],data1['Married'][2]
                ]

    single_sample = np.array(feature_list).reshape(1,-1)

    if st.button("Predict"):
        loaded_model = pickle.load(open('model.pkl', 'rb'))
        prediction = loaded_model.predict(single_sample)
        if prediction[0] == 0 :
            st.success( 'According to our Calculations, this customer will not default')
        elif prediction[0] == 1 :
            st.error('According to our Calculations, this customer will default')



