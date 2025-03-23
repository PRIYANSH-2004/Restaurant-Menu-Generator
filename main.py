import streamlit as st
import langchian_helper

st.title("Restaurant Name Generator")

cuisine = st.sidebar.selectbox("Pick a Cuisine", (
    "Indian", "American", "Italian", "Mexican", "Arabic"
))



if cuisine:
    response = langchian_helper.generate_restaurant_name_and_items(cuisine)

    st.header(response['restaurant_name'])
    menu_items = response['menu_items'].split(',')
    st.write("*** MENU ITEMS ***")
    for item in menu_items:
        st.write('-', item)
