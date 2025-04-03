import streamlit as st
from datetime import datetime, timedelta

st.title("QuickAppointment")

feedback = st.feedback("Test")


services = st.selectbox("Select the service you want to book:",
                          ["", "Dental Checkup", "Eye Examination", "General Consultation"])



appointment_datetime = st.date_input("Enter a Date")
appointment_time = st.time_input("Enter a Time")


terms = st.checkbox("I agree to the terms and conditions.", value=False)

if st.button("Book Appointment"):
    # Violation: Assumes correct format without validation or user feedback
    try:
        datetime.strptime(appointment_datetime, '%Y-%m-%d %H:%M')
        st.success("Your appointment has been booked.")
    except ValueError:
        st.error("Please enter the date and time in the correct format.")