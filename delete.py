import pandas as pd
import streamlit as st
from database import view_all_data, view_only_club_id, delete_data


def delete():
    result = view_all_data()
    # st.write(result) 
    df = pd.DataFrame(result, columns=["club_id","name","shortform","league","ranking","value"]) 
    with st.expander("View all clubs"):
        st.dataframe(df)

    list_of_clubs = [i[0] for i in view_only_club_id()]
    selected_club = st.selectbox("Task to Delete", list_of_clubs)
    st.warning("Do you want to delete ::{}".format(selected_club))
    if st.button("Delete club"):
        delete_data(selected_club)
        st.success("Club entry has been deleted successfully")
    new_result = view_all_data()
    df = pd.DataFrame(new_result, columns=["club_id","name","shortform","league","ranking","value"]) 
    with st.expander("Updated club data"):
        st.dataframe(df)