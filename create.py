import streamlit as st
from database import add_data
def create():
    col1, col2 = st.columns(2)
    with col1:
        club_id = st.text_input("Club Number")
        name = st.text_input("Club Name:")
        shortform = st.text_input("Club shortform:")
    with col2:
        league = st.selectbox("league", ["La Liga", "Premier League", "Bundesliga", "Ligue 1"])
        ranking = st.text_input("Club ranking")
        value = st.text_input("Club value")
    if st.button("Add Club Details"):
        add_data(club_id,name,shortform,league,ranking,value)
        st.success("Successfully added club with Number: {}".format(club_id))