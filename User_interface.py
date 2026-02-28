# -*- coding: utf-8 -*-
"""
医患操作代码：User_interface.py
📊🌍
"""

# User_interface.py

import streamlit as st
# import numpy as np
import pandas as pd


def User_file():
    # 添加箭头指示标识
    # 添加自定义 CSS 来增大标签字体 
    st.markdown(""" 
    <style>
        .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
            font-size: 20px;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # 添加箭头指示标识 
    st.markdown('<span  class="arrow">➤ Patient data</span> <p class="font"></p>', unsafe_allow_html=True)
    # st.title("Patient data")
    tab1 = st.tabs(["📑 total"])
    # tab1, tab2, tab3 = st.tabs(["&#128214; total", "&#128451; male", "&#128209; female"])
    path_total = r'E:\2025年科研\3月29日-乳腺癌\7-前端界面py\乳腺癌数据\(乳腺癌)页面展示表\Breast_cancer_20-23.xlsx'  
    data_total = pd.read_excel(path_total)
    # 假设要格式化的列名为 'Date'
    data_total['Date'] = data_total['Date'].apply(lambda x: '{:.0f}'.format(x))
    # 使用 dataframe() 方法显示，并指定宽度和高度
    tab1[0].dataframe(data_total, width=1400, height=710)

