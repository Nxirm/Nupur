from ast import Div
from distutils.log import info
import os
from re import I
from turtle import width
from click import style 
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from PIL import Image
import pandas as pd
import streamlit as st 
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from streamlit_option_menu import option_menu
import time
with st.sidebar:
    rad = option_menu(
        menu_title="NAVIGATION",
        options=["Home","Prediction", "Contact", "Appointment" ]
    )
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)





if rad == "Home":
    st.title("Description")
    st.image("diabetese2.jpg", width = 600)
    st.subheader("Diabetes Types")
    st.write("Here are a few different types of diabetes:")
    st.image("types1and2.jpg", caption="Types of diabetes")
    st.write("1.Type 1 diabetes is an autoimmune disease. The immune system attacks and destroys cells in the pancreas, where insulin is made. It’s unclear what causes this attack. About 10 percent of people with diabetes have this type.")
    st.write("2.Type 2 diabetes occurs when your body becomes resistant to insulin, and sugar builds up in your blood.")
    st.write("3.Prediabetes occurs when your blood sugar is higher than normal, but it’s not high enough for a diagnosis of type 2 diabetes")
    st.write("4.Gestational diabetes is high blood sugar during pregnancy. Insulin-blocking hormones produced by the placenta cause this type of diabetes.") 
    col1, col2 = st.columns(2)
    with col1:
        st.title("Symptoms")
        st.subheader("Symptoms in men")

        st.write("In addition to the general symptoms of diabetes, men with diabetes may have a decreased sex drive, erectile dysfunction (ED), and poor muscle strength.")
        st.subheader("Symptoms in women")
        st.write("Women with diabetes can also have symptoms such as urinary tract infections, yeast infections, and dry, itchy skin.")
    with col2:
        st.image("symptoms.jpg" ,width= 500, caption="Diabetes Symptons")
    
    st.subheader("Gestational diabetes")
    col3, col4 = st.columns(2)
    st.write("You’ll need to monitor your blood sugar level several times a day during pregnancy. If it’s high, dietary changes and exercise may or may not be enough to bring it down.")
    with col3:
        st.image("gestationaldiabetes.jpg", width = 300, caption="Gestational diabetes")
    with col4:
        st.image("gestationaldiabeteseerror.jpg", width = 300, caption= "Problems of gestational diabetes" )
    

elif rad == "Prediction":
    my_bar = st.progress(0)

    for percent_complete in range(100):
        time.sleep(0.001)
        my_bar.progress(percent_complete + 1)
    st.title('Diabetes Prediction')
    img1= Image.open("E:/diabetes/diabetese2.jpg")
    st.image(img1, use_column_width=True)
    


    df= pd.read_csv("E:/diabetes/diabetes.csv")
    st.subheader('Information of pre-exixting Data:')

    st.dataframe(df)
    st.write(df.describe())


    x=df.drop(['Outcome'], axis=1)
    y= df.iloc[:,-1]
    x_train,x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=0)




    def train_using_entropy(X_train, X_test, Y_train):
        #RAndom forest
        from sklearn.ensemble import RandomForestClassifier
        global forest
        forest=RandomForestClassifier(random_state=0, criterion="entropy", n_estimators=10)
        forest.fit(X_train,Y_train)   
        return forest
    if rad == "Prediction":

        def get_user_input():
            Pregnancies=st.number_input('Pregnancies',min_value=0,max_value=20)
            Glucose=st.number_input('Glucose',min_value=0,max_value=200)
            BloodPressure=st.number_input('blood_pressure',min_value=0,max_value=122)
            SkinThickness=st.number_input('SkinThickness',min_value=0,max_value=100)
            Insulin=st.number_input('Insulin',min_value=25,max_value=200)
            BodyMassindex=st.number_input('BMI',min_value=10,max_value=50)
            DiabetesPedigreeFunction=st.number_input('DiabetesPedigreeFunction',min_value=0,max_value=1)
            Age=st.number_input('Age',min_value=10, max_value=100)
            


            


            user_data={
                        'Pregnancies':Pregnancies,
                        'Glucose':Glucose,
                        'BloodPressure':BloodPressure,
                        'SkinThickness':SkinThickness,
                        'Insulin':Insulin,
                        'BMI':BodyMassindex,
                        'DiabetesPedigreeFunction':DiabetesPedigreeFunction,
                        'Age':Age,




                        }

                        
                    
        
            features=pd.DataFrame(user_data, index=[0])
            return features
                        
        user_input=get_user_input()
        #print(user_input)
        st.subheader('UserInput')
        st.write(user_input)

        RandomForestClassifier=RandomForestClassifier()
        RandomForestClassifier.fit(x_train,y_train)



        prediction=RandomForestClassifier.predict(user_input)

        st.subheader('Classification:')
        st.write(prediction)
        pred=str(prediction)


        st.write(str(accuracy_score(y_test,RandomForestClassifier.predict(x_test))*100)+'%')
        st.success("The prediction was sucessfull")



        st.write(pred)
        if pred=="[1]": 
            st.write("You have Diabetese!!!!!!!!!!")


        else: 
            st.write("You dont have Diabetese^^^^^")

    if rad== "Home":
        #bar chart 

        chart= st.bar_chart(df) 

elif rad == "Contact":
    st.title("You can contact by information given below")
    st.image("contact.jpg")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Contact number :91+ 123456789")
        st.subheader("Email adderss : anchospital@gmail.com")
        st.subheader("Address : abc road, abc area , abc locality ")
    with col2:
        st.image("map.png")
    
    




elif rad == "Appointment":
    st.title("Early detection saves life")
    st.image("appointment.jpg", width == 400)
    st.subheader("We are always here to help you. ")
    st.write("Book an appointment with us by clicking the below link")
    st.write("check out this [link](https://www.appointfix.com/book/Diabetes-Prediction)")



    









