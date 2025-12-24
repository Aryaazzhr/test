pip install plotly
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# Konfigurasi Halaman
st.set_page_config(page_title="Dashboard Case Management", layout="wide")

# --- CUSTOM CSS ---
# Digunakan untuk membuat tampilan card, background, dan font yang mirip dengan gambar
st.markdown("""
    <style>
    /* Background aplikasi */
    .stApp {
        background: linear-gradient(135deg, #e0eafc 0%, #cfdef3 100%);
    }
    
    /* Style untuk Card Umum */
    .custom-card {
        background-color: white;
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        height: 100%;
    }
    
    /* Text Styles */
    .label-text { color: #888; font-size: 0.8rem; font-weight: 600; text-transform: uppercase; }
    .main-val { font-size: 2.2rem; font-weight: 700; margin: 10px 0; }
    .sub-text { color: #888; font-size: 0.85rem; }
    .percentage-up { color: #28a745; font-weight: bold; }
    .percentage-down { color: #dc3545; font-weight: bold; }
    
    /* Profile Circle */
    .profile-circle {
        background-color: #6c5ce7;
        color: white;
        width: 40px;
        height: 40px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        margin-bottom: 15px;
    }

    /* Calendar styles */
    .cal-item {
        display: flex;
        align-items: center;
        margin-bottom: 15px;
    }
    .cal-time { width: 60px; color: #888; font-size: 0.85rem; }
    .cal-bar { width: 6px; height: 35px; border-radius: 3px; margin: 0 15px; }
    .cal-desc { font-size: 0.9rem; font-weight: 500; }
    .cal-sub { color: #aaa; font-size: 0.75rem; }
    </style>
    """, unsafe_allow_html=True)

# --- FUNGSI UNTUK SPARKLINE (Grafik Kecil) ---
def create_sparkline(data, color):
    fig = go.Figure()
    fig.add_trace(go.Scatter(y=data, mode='lines', line=dict(color=color, width=3), hoverinfo='skip'))
    fig.update_layout(
        sparklines=dict(data=data, type='line'),
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        margin=dict(l=0, r=0, t=0, b=0),
        height=50,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    return fig

# --- BARIS 1: 3 KOLOM ATAS ---
col1, col2, col3 = st.columns([1, 1.2, 1.2])

with col1:
    st.markdown("""
        <div class="custom-card">
            <div class="profile-circle">PF</div>
            <h3 style="margin-bottom:0;">Hello Peter</h3>
            <p class="sub-text">New cases are waiting</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    # Konten New Cases
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    c2_1, c2_2 = st.columns([1, 1])
    with c2_1:
        st.markdown('<p class="label-text">NEW CASES</p>', unsafe_allow_html=True)
        st.markdown('<p class="main-val">104</p>', unsafe_allow_html=True)
        st.markdown('<p class="sub-text">Trends last month</p>', unsafe_allow_html=True)
    with c2_2:
        spark_data = [10, 15, 12, 18, 14, 20, 25, 22]
        st.plotly_chart(create_sparkline(spark_data, "#00d284"), use_container_width=True, config={'displayModeBar': False})
        st.markdown('<p class="percentage-up" style="text-align:right;">+14,88%</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    # Konten New Tasks
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    c3_1, c3_2 = st.columns([1, 1])
    with c3_1:
        st.markdown('<p class="label-text">NEW TASKS</p>', unsafe_allow_html=True)
        st.markdown('<p class="main-val">34</p>', unsafe_allow_html=True)
        st.markdown('<p class="sub-text">Trends last month</p>', unsafe_allow_html=True)
    with c3_2:
        spark_data_task = [20, 18, 22, 15, 19, 12, 17, 10]
        st.plotly_chart(create_sparkline(spark_data_task, "#ff4b5c"), use_container_width=True, config={'displayModeBar': False})
        st.markdown('<p class="percentage-down" style="text-align:right;">-5,67%</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


# --- BARIS 2: KONTEN UTAMA ---
col_main, col_cal = st.columns([2, 1])

with col_main:
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    header_col1, header_col2 = st.columns([1, 1])
    header_col1.markdown('<p class="label-text" style="font-size:1rem;">CASE TYPE BREAKDOWN</p>', unsafe_allow_html=True)
    header_col2.markdown('<p style="text-align:right; color:#888; font-size:0.9rem; cursor:pointer;">Full report ></p>', unsafe_allow_html=True)
    
    # Grid untuk grafik dan list data
    chart_col, data_col = st.columns([1.5, 1])
    
    with chart_col:
        # Membuat Bar Chart dengan Plotly
        categories = ['Product', 'Trademark', 'Patent', 'Copyright', 'Gray market']
        values = [76, 48, 16, 5, 3] # Nilai contoh
        colors = ['#1e90ff', '#ff4757', '#a55eea', '#ffa502', '#2ed573']
        
        fig_bar = go.Figure(go.Bar(
            x=categories, y=values,
            marker_color=colors,
            width=0.2
        ))
        fig_bar.update_layout(
            margin=dict(l=0, r=0, t=20, b=0),
            height=300,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            yaxis=dict(gridcolor='#eee')
        )
        st.plotly_chart(fig_bar, use_container_width=True, config={'displayModeBar': False})
        
    with data_col:
        # List Kanan
        st.markdown("<br>", unsafe_allow_html=True)
        items = [
            ("Product", 76, "#1e90ff"),
            ("Trademark", 48, "#ff4757"),
            ("Patent", 16, "#a55eea"),
            ("Copyright", 0, "#ffa502"),
            ("Gray market", 0, "#2ed573"),
        ]
        for name, val, color in items:
            st.markdown(f"""
                <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:15px; border-bottom:1px solid #f8f9fa; padding-bottom:5px;">
                    <div style="display:flex; align-items:center;">
                        <div style="width:10px; height:10px; background:{color}; border-radius:50%; margin-right:10px;"></div>
                        <span style="color:#555;">{name}</span>
                    </div>
                    <span style="font-weight:700;">{val}</span>
                </div>
            """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_cal:
    st.markdown('<div class="custom-card">', unsafe_allow_html=True)
    st.markdown("""
        <div style="display:flex; justify-content:space-between; align-items:center;">
            <p class="label-text">MY CALENDAR</p>
            <div style="background:#6c5ce7; color:white; width:25px; height:25px; border-radius:50%; text-align:center; cursor:pointer; line-height:25px;">+</div>
        </div>
        <hr style="margin: 15px 0; border:0; border-top:1px solid #eee;">
        
        <p style="font-size:0.8rem; font-weight:700; color:#555; margin-bottom:15px;">MON 16</p>
        <div class="cal-item">
            <div class="cal-time">7:00</div>
            <div class="cal-bar" style="background:#2ed573;"></div>
            <div>
                <div class="cal-desc">Meeting for case 1</div>
                <div class="cal-sub">7:00 - 8:30</div>
            </div>
        </div>
        <div class="cal-item">
            <div class="cal-time">11:00</div>
            <div class="cal-bar" style="background:#1e90ff;"></div>
            <div>
                <div class="cal-desc">Meeting for case 2</div>
                <div class="cal-sub">11:00 - 12:30</div>
            </div>
        </div>
        
        <p style="font-size:0.8rem; font-weight:700; color:#555; margin-top:25px; margin-bottom:15px;">TUE 17</p>
        <div class="cal-item">
            <div class="cal-time">14:00</div>
            <div class="cal-bar" style="background:#ffa502;"></div>
            <div>
                <div class="cal-desc">Meeting for case 3</div>
                <div class="cal-sub">14:00 - 15:30</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
