# -*- coding: utf-8 -*-
"""
总页面代码：All_pages.py
"""

import streamlit as st
from streamlit_option_menu import option_menu
import User_interface
import Home_page
import Add_patients_interface
import datetime

def current_time():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

st.sidebar.markdown(f'<div style="text-align:center">{current_time()}</div>', unsafe_allow_html=True)

# 添加用户类型选择框
user_type = st.sidebar.selectbox("", options=["Administrator user", "Ordinary user"])

with st.sidebar:
    menu = ["Homepage", "Patient data", "Add patient"]
    selected = option_menu(menu_title="Menu", options=menu,
                         icons=['house', 'person lines fill', "bar-chart"],
                         menu_icon="list", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#add8e6"},
        "icon": {"color": "orange", "font-size": "18px"},
        "nav-link": {"font-size": "20px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#add8e6", "font-weight": "normal"},
    })

if selected == "Homepage":
    Home_page.Home_file()
elif selected == "Patient data":
    User_interface.User_file()
elif selected == "Add patient":
    Add_patients_interface.Add_patients_file()
