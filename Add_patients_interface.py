# -*- coding: utf-8 -*-
"""
Add_patients_interface.py
"""

import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
from joblib import load

def Add_patients_file():
    # 添加箭头指示标识
    st.markdown('<span class="arrow">➤ Add patients</span> <p class="font"></p>', unsafe_allow_html=True)
    # 在代码开头添加 CSS 样式
    st.markdown(""" 
    <style>
        /* 方法1：针对所有输入框的标签 */
        div[data-testid="stNumberInput"] label p {
            font-size: 18px !important;
            font-weight: bold !important;
        }
        /* 增大所有 number_input 的输入框字体 */
        .stNumberInput input {
            font-size: 18px !important;
        }
    </style>
    """, unsafe_allow_html=True)
    # 初始化状态
    if "show_data" not in st.session_state:
        st.session_state.show_data = False

        # 创建一个头部的选项菜单
    with st.container():
        selected_option = option_menu("prediction", ["total"],
                                       icons=['people'],
                                       menu_icon="broadcast", default_index=0,
                                       orientation="horizontal",  # 水平布局
                                       styles={
                                           "container": {"text-align": "center", "background-color": "#add8e6"},  # 浅蓝色背景
                                           "icon": {"color": "black", "font-size": "24px"},
                                           "nav-link": {"font-size": "18px", "text-align": "center", "margin": "0px", "--hover-color": "#eee"},
                                           "nav-link-selected": {"background-color": '#003366', "font-weight": "bold"},  # 选中之后的背景色
                                       })


    # 根据选择的选项显示内容
    if selected_option == "total":
        # st.markdown("""<h4 style='text-align: center;'>请输入患者详细信息</h4>""", unsafe_allow_html=True)
    
        # 获取用户输入的数据
        user_input = []
    
        # 输入部分
        input_cols = st.columns(4)  # 每行4列
    
        # 年龄
        with input_cols[0]:
            user_input.append(st.number_input("age：", min_value=0, max_value=120, value=56))  # 原值: 58
    
        # CA15-3
        with input_cols[1]:
            user_input.append(st.number_input("CA15-3：", value=8.8))  # 原值: 3.5
    
        # CEA
        with input_cols[2]:
            user_input.append(st.number_input("CEA：", value=3.24))  # 原值: 0.26
    
        # Baso#
        with input_cols[3]:
            user_input.append(st.number_input("Baso#：", value=0.05))  # 原值: 0.01
    
        # 继续添加新的指标
        input_cols = st.columns(4)
        with input_cols[0]:
            user_input.append(st.number_input("Baso%：", value=0.7))  # 原值: 0.4
        with input_cols[1]:
            user_input.append(st.number_input("Eos#：", value=0.18))  # 原值: 0.08
        with input_cols[2]:
            user_input.append(st.number_input("Eos%：", value=2.4))  # 原值: 3.1
        with input_cols[3]:
            user_input.append(st.number_input("Hb：", value=139))  # 原值: 126
    
        # 继续所有其它指标
        input_cols = st.columns(4)
        with input_cols[0]:
            user_input.append(st.number_input("Hct：", value=43.3))  # 原值: 40
        with input_cols[1]:
            user_input.append(st.number_input("Lymph#：", value=2.75))  # 原值: 1.05
        with input_cols[2]:
            user_input.append(st.number_input("Lymph%：", value=37))  # 原值: 40.5
        with input_cols[3]:
            user_input.append(st.number_input("MCH：", value=29.6))  # 原值: 28.8
    
        input_cols = st.columns(4)
        with input_cols[0]:
            user_input.append(st.number_input("MCHC：", value=321))  # 原值: 315
        with input_cols[1]:
            user_input.append(st.number_input("MCV：", value=92.1))  # 原值: 91.5
        with input_cols[2]:
            user_input.append(st.number_input("MPV：", value=11.9))  # 原值: 12.8
        with input_cols[3]:
            user_input.append(st.number_input("Mono#：", value=0.52))  # 原值: 0.21
    
        input_cols = st.columns(4)
        with input_cols[0]:
            user_input.append(st.number_input("Mono%：", value=7))  # 原值: 8.1
        with input_cols[1]:
            user_input.append(st.number_input("Neut#：", value=3.93))  # 原值: 1.24
        with input_cols[2]:
            user_input.append(st.number_input("Neut%：", value=52.9))  # 原值: 47.9
        with input_cols[3]:
            user_input.append(st.number_input("P-LCR：", value=40.9))  # 原值: 47.8
    
        input_cols = st.columns(4)
        with input_cols[0]:
            user_input.append(st.number_input("PCT：", value=0.26))  # 原值: 0.23
        with input_cols[1]:
            user_input.append(st.number_input("PDW：", value=16.8))  # 原值: 19.9
        with input_cols[2]:
            user_input.append(st.number_input("PLT：", value=221))  # 原值: 176
        with input_cols[3]:
            user_input.append(st.number_input("RBC：", value=4.7))  # 原值: 4.37
    
        input_cols = st.columns(4)
        with input_cols[0]:
            user_input.append(st.number_input("RDW-CV：", value=13.8))  # 原值: 14.3
        with input_cols[1]:
            user_input.append(st.number_input("WBC：", value=7.43))  # 原值: 2.59
    
        # 将用户输入的数据转换为表格形式
        table_data = {
            "item": [
                "age", "CA15-3", "CEA", "Baso#",
                "Baso%", "Eos#", "Eos%", "Hb",
                "Hct", "Lymph#", "Lymph%", "MCH",
                "MCHC", "MCV", "MPV", "Mono#",
                "Mono%", "Neut#", "Neut%", "P-LCR",
                "PCT", "PDW", "PLT", "RBC",
                "RDW-CV", "WBC"
            ],
            "value": [
                user_input[0],
                user_input[1], user_input[2], user_input[3],
                user_input[4], user_input[5], user_input[6], user_input[7],
                user_input[8], user_input[9], user_input[10], user_input[11],
                user_input[12], user_input[13], user_input[14], user_input[15],
                user_input[16], user_input[17], user_input[18], user_input[19],
                user_input[20], user_input[21], user_input[22], user_input[23],
                user_input[24], user_input[25],
            ],
        }
    
        # 将表格数据转换为每行包含四个指标及其值
        formatted_table_data = []
        for i in range(0, len(table_data["item"]), 4):
            row = []
            # 添加指标和数值
            for j in range(4):
                if i + j < len(table_data["item"]):
                    row.append(table_data["item"][i + j])
                    row.append(table_data["value"][i + j])
                else:
                    row.append("")  # 如果没有值，添加一个空字符串
            formatted_table_data.append(row)
    
        # 创建DataFrame
        df = pd.DataFrame(formatted_table_data, columns=["item 1", "value 1", "item 2", "value 2", "item 3", "value 3", "item 4", "value 4"])
        # ⭐ 关键：增大 DataFrame 字体
        st.markdown(""" 
        <style>
            /* 增大 DataFrame 所有文本 */
            .stDataFrame {
                font-size: 18px !important;
            }
         
            /* 仅增大表头 */
            .stDataFrame th {
                font-size: 20px !important;
                font-weight: bold !important;
            }
        </style>
        """, unsafe_allow_html=True)
         
        df = df.fillna("")  # 将NaN替换为""，这样在显示时不会出现NaN
    
        # 使用st.markdown函数自定义表格样式
        st.markdown("""
        <style>
            .dataframe {
                border: 2px solid black; /* 加粗外框 */
                border-collapse: collapse;
                width: 100%; /* 表格宽度 */
            }
            .dataframe th, .dataframe td {
                text-align: center; /* 数据居中 */
                padding: 8px; /* 内边距 */
            }
            .dataframe tr:nth-child(even) {
                background-color: #f2f2f2; /* 白灰相间 */
            }
        </style>
        """, unsafe_allow_html=True)
    
        col11, col22, col33 = st.columns(3)
        # 展示已选择的数据的按钮
        with col11:
            if st.button("View"):
                st.session_state.show_data = not st.session_state.show_data  # 切换显示状态
    
        # 如果显示状态为真，显示数据表
        if st.session_state.show_data:
            st.write(df.to_html(classes='dataframe', index=False, escape=False), unsafe_allow_html=True)
    
        # 加载模型
        current_dir = Path(__file__).parent
        model_path = current_dir / "IBC_data" / "XGBoost_model.joblib"
        model = load(model_path)
    
        # 添加一些空行以分隔表格和按钮
        st.write("")  # 添加一行空行
        st.write("")  
    
        @st.dialog("Results Form")
        def predict_dialog():
            # 将用户输入转换为NumPy数组或适当格式进行预测
            input_data = [user_input]  # 根据实际需要调整输入格式
            prediction = model.predict(input_data)  # 进行预测
            # 显示预测结果
            result = "Breast cancer (Positive)" if prediction[0] == 1 else "Breast cancer (Negative)"
    
            # 假设表格文件名为table1.csv和table2.csv
            current_dir = Path(__file__).parent
            df1_path = current_dir / "IBC_data" / "乳腺癌9.xlsx"
            df1 = pd.read_excel(df1_path)
            current_dir = Path(__file__).parent
            df2_path = current_dir / "IBC_data" / "Breast_cancer_20-23.xlsx"
            df2 = pd.read_excel(df2_path)
    
            # 使用merge函数将两个表格按照CA15-3和WBC列合并
            merged_df = pd.merge(df1, df2, on=['CA15-3', 'WBC', 'Lymph#'], how='inner')
    
            # 筛选匹配的行
            if not merged_df.empty:
                # 使用CA15-3和WBC进行匹配
                match_row = merged_df[(merged_df['CA15-3'] == user_input[1]) & (merged_df['WBC'] == user_input[25])]  # 从user_input中获取WBC输入值
    
                if not match_row.empty:
                    report_data = {
                        "Date": [match_row.iloc[0]['Date']],  # 从匹配行中获得Date值
                        "Patient ID": [match_row.iloc[0]['Patient ID']],
                        "Patient Type": [match_row.iloc[0]['Patient Type']],  # 从匹配行中获得Patient Type值
                        "Gender": [match_row.iloc[0]['Gender']],
                        "Age": [user_input[0]],
                        "Clinical diagnosis": [result],
                    }
    
                    # 将报告数据转换为DataFrame
                    report_df = pd.DataFrame(report_data)
    
                    # 显示标题
                    st.markdown("<h4 style='text-align: center;'>Hospital Clinical Diagnosis Report</h4>", unsafe_allow_html=True)
    
                    # 使用st.write显示表格
                    st.write(report_df.to_html(index=False, escape=False), unsafe_allow_html=True)
    
                    st.write("")
                    st.write("Diagnosis: ", result)
    
                    # 在表格下面的按钮
                    col1, col2, col3, col4 = st.columns(4)  # 创建四列
    
                    with col1:
                        confirm_button = st.button("Confirm", key="confirm_button")  # 将确认按钮放在左侧
    
                    with col4:
                        cancel_button = st.button("Cancel", key="cancel_button")  # 将取消按钮放在右侧
    
                    if confirm_button:
                        st.write("You have confirmed the operation.")
                        # 此处可添加确认后的操作，比如数据存储等
    
                    if cancel_button:
                        st.write("You have canceled the operation.")
                else:
                    st.write("No matching data.")
            else:
                st.write("No matching data.")
    
        with col33:
            # 主程序启动：当点击“填写信息”按钮时，调用弹出框
            if st.button("View diagnostic results"):
                predict_dialog()



        

        


