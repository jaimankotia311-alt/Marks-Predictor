import joblib 
import streamlit as st 




from pathlib import Path

model = joblib.load(Path(__file__).parent / "Expected marks.joblib")


st.title("Marks Prediction")
st.markdown("Here you will pass down hours you studied and you will get predicted marks1 : ")

hours = st.text_input(label="Hours Studied", placeholder="Here you will enter the number of hours you studied and will ge the predicted marks: ")

if st.button("Predict : "):
    output= model.predict([[float(hours)]]) 
    st.write(f"The predicted marks are = {round(output [0])}")



# py -m streamlit run "C:\Users\Jay Mankotia\Desktop\AI ML\02 Hours Study SLR\ui.py"