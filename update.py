import pandas as pd
import streamlit as st
from database import view_all_data, view_only_club_id, edit_data


def update():
    result = view_all_data()
    # st.write(result) 
    df = pd.DataFrame(result, columns=["club_id","name","shortform","league","ranking","value"]) 
    with st.expander("Current club and their values"):
        st.dataframe(df)
    list_of_clubs = [i[0] for i in view_only_club_id()]
    selected_club = st.selectbox("CLub to Edit", list_of_clubs)
    # selected_result = get_dealer(selected_dealer)
    # st.write(selected_result)
    if selected_club:
        new_value=st.text_input("Enter value:")
        # Layout of Create
        if st.button("Update Club value"):
            edit_data(new_value, selected_club)
            st.success("Successfully updated value of club :: {} to :: {}".format(selected_club, new_value))

    result2 = view_all_data()
    df2 = pd.DataFrame(result2, columns=["club_id","name","shortform","league","ranking","value"])
    with st.expander("Updated Club data"):
        st.dataframe(df2)