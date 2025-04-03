import streamlit as st
import pandas as pd
import numpy as np
from tornado.options import options

st.title("SurveyMaster")
question_types = ["Text", "Multiple Choice", "Rating"]

survey_name = st.selectbox("Type of Survey:", options=question_types)
questions = []

if st.button("Add Question"):
    questions.append(st.text_input(f"Question {len(questions) + 1}:"))

st.header("Distribution Settings")
email_list = st.text_area("Enter emails (separated by commas):")



st.header("Collect Responses")
testArray = [10,1,0,2,11,20,6]

test = pd.DataFrame({
    "Water Quality": np.array(testArray),
    "Test": np.array(testArray)

})
newTest = test.T.reset_index()
st.write(newTest)

responses = pd.DataFrame({
    "Q1": np.random.choice(["Yes", "No"], 10),
    "Q2": np.random.randint(1, 6, 10)
})
st.write(responses)

st.header("Results Analysis")
st.bar_chart(responses["Q2"])