import streamlit as st
from config import Menu, Extras, Drinks
import os


def setSidebar():
    # Sidebar Menu    
    st.sidebar.title("🍔 Burger Menu")
    burgerTypeCompnent()
    ExtraCompnent()   
    drinkComponent()

def burgerTypeCompnent():
    st.sidebar.markdown("### Available Burger Sizes:")
    burgerMenu = Menu.split("\n")
    for item in burgerMenu:
        st.sidebar.markdown(item.strip())    


def ExtraCompnent():
    st.sidebar.markdown("### Available Extras:")
    extras = Extras.split("\n")
    for item in extras:
        st.sidebar.markdown(item.strip())      

def drinkComponent():
    st.sidebar.markdown("### Available Drinks:")
    drinks = Drinks.split("\n")
    for item in drinks:
        st.sidebar.markdown(item.strip())    

def setbg():
    return