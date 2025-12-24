import streamlit as st
import plotly.graph_objects as go

# 1. Konfigurasi Halaman
st.set_page_config(page_title="Legal Dashboard", layout="wide")

# 2. CSS yang Diperbaiki (Menggunakan Container Styling)
st.markdown("""
    <style>
    /* Background Utama */
    .stApp {
        background: linear-gradient(135deg, #e0eafc 0%, #cfdef3 100%);
    }
    .block-container { 
        padding-top: 5rem; /* Ubah angka ini (misal 5rem atau 80px) untuk jarak lebih jauh */
        padding-bottom: 2rem;
        padding-left: 3rem;
        padding-right: 3rem;

    /* Style untuk semua container yang berfungsi sebagai Card */
    [data-testid="stVerticalBlock"] > div:has(div[data-testid="stVerticalBlock"]) {
        background-color: white;
        border-radius: 20px;
        padding: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }
    
    /* Utility Styles */
    .label-text { color: #888; font-size: 0.8rem; font-weight: 600; text-transform: uppercase; margin-bottom: 0px;}
    .main-val { font-size: 2.2rem; font-weight: 700; margin: 0px; line-height: 1.2;}
    .sub-text { color: #888; font-size: 0.8rem; margin-top: 5px;}
    .percentage-up { color: #28a745; font-weight: bold; font-size: 0.9rem; text-align: right;}
    .percentage-down { color: #dc3545; font-weight: bold; font-size: 0.9rem; text-align: right;}
    
    .profile-circle {
        background-color: #6c5ce7;
        color: white;
        width: 45px;
        height: 45px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        margin-bottom: 10px;
    }

    /* Calendar styles */
    .cal-item { display: flex; align-items: center; margin-bottom: 15px; }
    .cal-time { width: 50px; color: #888; font-size: 0.8rem; }
    .cal-bar { width: 6px; height: 35px; border-radius: 3px; margin: 0 12px; }
    .cal-desc { font-size: 0.85rem; font-weight: 600; color: #333;}
    .cal-sub { color: #aaa; font-size: 0.75rem; }
    
    /* Menghilangkan padding default streamlit */
    .block-container { padding-top: 2rem; }
    </style>
    """, unsafe_allow_html=True)

# Fungsi Sparkline
def create_sparkline(data, color):
    fig = go.Figure(go.Scatter(y=data, mode='lines', line=dict(color=color, width=3), hoverinfo='skip'))
    fig.update_layout(
        xaxis=dict(visible=False), yaxis=dict(visible=False),
        margin=dict(l=0, r=0, t=0, b=0), height=40,
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', showlegend=False
    )
    return fig

# --- LAYOUT MULAI DI SINI ---

# BARIS 1: 3 KARTU ATAS
col1, col2, col3 = st.columns([1, 1.2, 1.2])

with col1:
    with st.container():
        st.markdown('<div class="profile-circle">PF</div>', unsafe_allow_html=True)
        st.markdown('<h2 style="margin:0;">Hello Peter</h2>', unsafe_allow_html=True)
        st.markdown('<p class="sub-text">New cases are waiting</p>', unsafe_allow_html=True)

with col2:
    with st.container():
        st.markdown('<p class="label-text">NEW CASES</p>', unsafe_allow_html=True)
        c2a, c2b = st.columns([1, 1])
        with c2a:
            st.markdown('<p class="main-val">104</p>', unsafe_allow_html=True)
        with c2b:
            st.plotly_chart(create_sparkline([10, 15, 12, 18, 14, 22], "#00d284"), config={'displayModeBar': False}, use_container_width=True)
        
        c2c, c2d = st.columns([1, 1])
        with c2c: st.markdown('<p class="sub-text">Trends last month</p>', unsafe_allow_html=True)
        with c2d: st.markdown('<p class="percentage-up">+14,88%</p>', unsafe_allow_html=True)

with col3:
    with st.container():
        st.markdown('<p class="label-text">NEW TASKS</p>', unsafe_allow_html=True)
        c3a, c3b = st.columns([1, 1])
        with c3a:
            st.markdown('<p class="main-val">34</p>', unsafe_allow_html=True)
        with c3b:
            st.plotly_chart(create_sparkline([20, 18, 22, 15, 19, 12], "#ff4b5c"), config={'displayModeBar': False}, use_container_width=True)
            
        c3c, c3d = st.columns([1, 1])
        with c3c: st.markdown('<p class="sub-text">Trends last month</p>', unsafe_allow_html=True)
        with c3d: st.markdown('<p class="percentage-down">-5,67%</p>', unsafe_allow_html=True)

st.write("") # Spasi antar baris

# BARIS 2: KONTEN UTAMA
col_main, col_cal = st.columns([2, 1])

with col_main:
    with st.container():
        h1, h2 = st.columns([1, 1])
        h1.markdown('<p class="label-text">CASE TYPE BREAKDOWN</p>', unsafe_allow_html=True)
        h2.markdown('<p style="text-align:right; color:#888; font-size:0.8rem;">Full report ></p>', unsafe_allow_html=True)
        
        ch1, ch2 = st.columns([1.5, 1])
        with ch1:
            # Bar Chart
            fig_bar = go.Figure(go.Bar(
                x=['Product', 'Trademark', 'Patent', 'Copyright', 'Gray market'],
                y=[76, 48, 16, 5, 3],
                marker_color=['#1e90ff', '#ff4757', '#a55eea', '#ffa502', '#2ed573'],
                width=0.3
            ))
            fig_bar.update_layout(
                margin=dict(l=0, r=0, t=20, b=0), height=250,
                paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                yaxis=dict(gridcolor='#eee')
            )
            st.plotly_chart(fig_bar, use_container_width=True, config={'displayModeBar': False})
            
        with ch2:
            items = [("Product", 76, "#1e90ff"), ("Trademark", 48, "#ff4757"), 
                     ("Patent", 16, "#a55eea"), ("Copyright", 0, "#ffa502"), ("Gray market", 0, "#2ed573")]
            st.write("")
            for name, val, color in items:
                st.markdown(f"""
                    <div style="display:flex; justify-content:space-between; margin-bottom:12px; border-bottom:1px solid #f8f9fa;">
                        <div style="display:flex; align-items:center;">
                            <div style="width:8px; height:8px; background:{color}; border-radius:50%; margin-right:10px;"></div>
                            <span style="font-size:0.9rem; color:#444;">{name}</span>
                        </div>
                        <span style="font-weight:700;">{val}</span>
                    </div>
                """, unsafe_allow_html=True)

with col_cal:
    with st.container():
        st.markdown("""
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:10px;">
                <p class="label-text">MY CALENDAR</p>
                <div style="background:#6c5ce7; color:white; width:22px; height:22px; border-radius:50%; text-align:center; line-height:22px; font-size:14px;">+</div>
            </div>
            <p style="font-size:0.8rem; font-weight:700; color:#444; margin-bottom:15px;">MON 16</p>
            <div class="cal-item">
                <div class="cal-time">7:00</div>
                <div class="cal-bar" style="background:#2ed573;"></div>
                <div><div class="cal-desc">Meeting for case 1</div><div class="cal-sub">7:00 - 8:30</div></div>
            </div>
            <div class="cal-item">
                <div class="cal-time">11:00</div>
                <div class="cal-bar" style="background:#1e90ff;"></div>
                <div><div class="cal-desc">Meeting for case 2</div><div class="cal-sub">11:00 - 12:30</div></div>
            </div>
            <p style="font-size:0.8rem; font-weight:700; color:#444; margin-top:20px; margin-bottom:15px;">TUE 17</p>
            <div class="cal-item">
                <div class="cal-time">14:00</div>
                <div class="cal-bar" style="background:#ffa502;"></div>
                <div><div class="cal-desc">Meeting for case 3</div><div class="cal-sub">14:00 - 15:30</div></div>
            </div>
        """, unsafe_allow_html=True)


