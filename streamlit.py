#pip install streamlit --installing lib
#streamlit run #app.py   -- running app

import streamlit as st
import joblib

def main():
    html_temp = """
    <div style="background-color:black;padding:16px">
    <h2 style="color:lightblue;text-align:center"> Medical Insurance Cost Prediction </h2>
    </div>
    
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)
    
    # load the model
    model = joblib.load('RFC_Model')
    p1 = st.slider("Age",18,100)
    
    s1=st.selectbox("Gender",("Male","Female"))
    
    if s1=="Male":
        p2=1
    else:
        p2=0

    p3 = st.number_input("BMI")
    p4 = st.slider("CHILDREN",0,4) 
    
    s2=st.selectbox("Smoker",("Yes","No"))
    
    if s2=="Yes":
        p5=1
    else:
        p5=0
    
        p6 = st.slider("Region [1-4]",1,4)
    
    if st.button('Result'):
        prediction = model.predict([[p1,p2,p3,p4,p5,p6]])
       
        st.balloons()
        st.success('Medical Insurance Cost is {} '.format(round(prediction[0],2)))    
    
if __name__ == '__main__':
    main()
    
