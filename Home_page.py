# -*- coding: utf-8 -*-
"""
首页代码：Home_page.py
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def Home_file():
    # 添加箭头指示标识
    st.markdown('<span class="arrow">➤ Homepage</span> <p class="font"></p>', unsafe_allow_html=True)  # 箭头和标题

    # 假设patient_counts是一个字典，包含你需要的指标
    patient_counts = {
        "Number of outpatients": 457,
        "Number of admissions": 342,
        "Waiting for diagnosis": 118,
        "Number of discharges": 104
    }
    
    # 自定义CSS样式
    st.markdown("""
    <style>
        .metric-box {
            background-color: #E0E0E0;  /* 灰色背景 */
            padding: 10px;               /* 内边距 */
            border-radius: 5px;          /* 边角圆润 */
            text-align: center;           /* 内容居中 */
        }
        .metric-label {
            font-size: 20px;             /* 标签字体大小 */
            color: #333;                 /* 标签字体颜色 */
        }
        .metric-value {
            font-size: 28px;             /* 数值字体大小 */
            font-weight: bold;           /* 数值加粗 */
            color: #111;                 /* 数值字体颜色 */
        }
    </style>
    """, unsafe_allow_html=True)
    
    # 调整指标列的显示
    cols = st.columns(4)  # 根据需要调整列数
    for i, (label, value) in enumerate(patient_counts.items()):
        with cols[i]:
            st.markdown(f"""
            <div class="metric-box">
                <div class="metric-label">{label}</div>
                <div class="metric-value">{value}</div>
            </div>
            """, unsafe_allow_html=True)
    st.write("")

    col1, col2, col3 = st.columns(3)
    
    # 图表相同尺寸设置
    figure_size = (8, 6)  # 设定一致的图表尺寸

    with col1:
        # 绘制临床诊断饼状图
        current_dir = Path(__file__).parent
        file_path = current_dir / "IBC_data" / "Breast_cancer_20-23.xlsx"
        df = pd.read_excel(file_path)
        
        diagnosis_counts = df['Clinical diagnosis'].value_counts()
        
        labels = ['Negative', 'Positive']
        sizes = [diagnosis_counts.get(0, 0), diagnosis_counts.get(1, 0)]  # 处理可能不存在的索引
        
        # 修改颜色为浅蓝色和深蓝色
        colors = ['#003366', '#add8e6',]  # 浅蓝色和深蓝色
        explode = (0, 0.1)
        
        # 绘制饼状图
        plt.figure(figsize=(8, 6))  # 设置图表尺寸
        plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90, textprops={'fontsize': int(plt.rcParams['font.size']*1.5)})
        plt.axis('equal')  # 使饼状图为圆形
        plt.title('Positive and Negative Status of the Patient', fontsize=25)
        
        # 设置图表背景色
        plt.gcf().patch.set_facecolor('#F0F0F0')  # 设置为与公告相同的背景
        
        # 使用 Streamlit 显示 Matplotlib 图表
        st.pyplot(plt)


    with col2:
        # 读取Excel文件
        current_dir = Path(__file__).parent
        file_path2 = current_dir / "IBC_data" / "Breast_cancer_20-23.xlsx"
        df = pd.read_excel(file_path2, engine='openpyxl')
        
        # 对 Patient Type 列进行分类
        patient_types = df['Patient Type'].value_counts()
        
        # 绘制柱状图
        plt.figure(figsize=(8, 6))  # 设置图表尺寸
        # 使用不同深浅的蓝色
        colors = ['#003366', '#00509E', '#add8e6', '#66B2FF']  # 深蓝色到浅蓝色的组合
        ax = patient_types.plot(kind='bar', color=colors[:len(patient_types)])
        ax.tick_params(axis='x',  labelsize=int(plt.rcParams['font.size']*0.75)) 
        plt.title('Patient Type Distribution', fontsize=25)
        plt.xlabel('Patient Type', fontsize=18)
        plt.ylabel('Count', fontsize=18)
        plt.xticks(rotation=0)  # 旋转横坐标的值，使其竖着显示
        
        # 在柱状图的顶部标上数据
        for i in range(len(patient_types)):
            # ax.text(i, patient_types[i], str(patient_types[i]), ha='center', va='bottom')
            ax.text(i, 
            patient_types[i],
            str(patient_types[i]),
            ha='center',
            va='bottom',
            fontsize=int(plt.rcParams['font.size']*1.1)) 
        
        # 设置柱状图的背景色
        plt.gcf().patch.set_facecolor('#F0F0F0')  # 设置为与指标列相同的灰色背景
        
        # 使用 Streamlit 显示 Matplotlib 图表
        st.pyplot(plt)


    with col3:
        # 读取Excel文件
        current_dir = Path(__file__).parent
        file_path3 = current_dir / "IBC_data" / "Breast_cancer_20-23.xlsx"
        df = pd.read_excel(file_path3, engine='openpyxl')

        # 提取Age列，进行处理
        age_data = df['Age']
        sorted_age_data = age_data.sort_values()

        # 统计年龄分布
        age_counts = sorted_age_data.value_counts().sort_index()

        # 绘制年龄分布线图
        plt.figure(figsize=figure_size)
        plt.plot(age_counts.index, age_counts.values, marker='o')  # 使用线图并添加点
        plt.xlabel('Age', fontsize=18)
        plt.ylabel('Number of people', fontsize=18)
        plt.title('Patient Age Distribution Line Graph', fontsize=25)
        
        # 设置图表背景色
        plt.gcf().patch.set_facecolor('#F0F0F0')  # 设置为与指标列相同的灰色背景

        # 使用 Streamlit 显示 Matplotlib 图表
        st.pyplot(plt)



    # 添加公告和反馈功能
    st.markdown("""
        <style>
        .announcement-title {
            font-size: 19px; /* 公告标题字体大小 */
        }
        .announcement-content {
            font-size: 17px; /* 公告内容字体大小 */
        }
        </style>
    """, unsafe_allow_html=True)

    # 使用容器包裹公告内容
    with st.container():
        # 创建两列布局
        col1, col2 = st.columns([1, 0.5])  # 设置第一列占用1份，第二列占用0.5份
        
        # 在左侧列显示公告内容
        with col1:
            st.markdown( 
              """
              <style>
                 .feedback-title {font-size:20px !important;}
                 .feedback-textarea label {font-size:20px !important;}
              </style>
              """,
              unsafe_allow_html=True,
            )
         
            st.markdown('<div class="feedback-title">Feedback</div>', unsafe_allow_html=True)
            feedback = st.text_area("",  placeholder="Please enter your feedback here:", height=60)
    
            if st.button("Submit"):
                if feedback:
                    st.success("Thank you for your feedback!")
                else:
                    st.warning("Please provide feedback")

        with col2: 
            # 读取Excel文件
            file_path1 = r'IBC_data\Breast_cancer_20-23.xlsx' 
            df = pd.read_excel(file_path1,  engine='openpyxl')
            
            # 提取性别列 
            gender_counts = df['Gender'].value_counts()
            
            # 设置颜色
            colors = ['#add8e6', '#003366']  # 浅蓝和深蓝
            
            # 绘制饼图（标签放在内部）
            plt.figure(figsize=(8,  6))
            wedges, texts, autotexts = plt.pie( 
                gender_counts,
                labels=None,  # 不显示外部标签
                autopct='%1.1f%%',
                startangle=90,
                colors=colors[:len(gender_counts)],
                textprops={'fontsize': 18, 'color': 'black'},  # 设置百分比文字样式 
                pctdistance=0.8,  # 控制百分比文字的位置（0.8表示距离中心80%）
            )
            
            # 添加图例（代替外部标签）
            plt.legend( 
                wedges,
                gender_counts.index, 
                title="Gender",
                loc="center left",
                bbox_to_anchor=(0.85, 0, 0.5, 1),  # 将图例放在右侧 
            )
            
            plt.title('Gender  Ratio')
            plt.axis('equal')   # 确保饼图是圆形 
            plt.gcf().patch.set_facecolor('#F0F0F0')   # 设置背景色 
            
            # 显示图表 
            st.pyplot(plt) 


# 调用函数以运行页面
if __name__ == "__main__":
    Home_file()




