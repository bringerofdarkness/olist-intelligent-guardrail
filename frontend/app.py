import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# -----------------------------
# Page setup
# -----------------------------
st.set_page_config(
    page_title="Olist AI | Logistics Intelligence",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------
# Session state
# -----------------------------
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "result" not in st.session_state:
    st.session_state.result = None
if "active_view" not in st.session_state:
    st.session_state.active_view = "predictor"

# -----------------------------
# Premium dark UI CSS
# -----------------------------
st.markdown(
    """
    <style>
    :root {
        --bg: #040b18;
        --panel: #081427;
        --panel-2: #0c1b33;
        --panel-3: #0f223f;
        --line: rgba(148, 163, 184, 0.15);
        --text: #f8fafc;
        --muted: #94a3b8;
        --blue: #2563eb;
        --blue-2: #3b82f6;
        --green: #22c55e;
        --green-2: #16a34a;
        --purple: #7c3aed;
        --gold: #f59e0b;
        --red: #ef4444;
        --pink: #fb7185;
        --cyan: #22d3ee;
    }

    .stApp {
        background:
            radial-gradient(circle at top left, rgba(37,99,235,0.10), transparent 25%),
            radial-gradient(circle at top right, rgba(124,58,237,0.08), transparent 20%),
            linear-gradient(180deg, #030712 0%, #040b18 100%);
        color: var(--text);
    }

    .block-container {
        max-width: 1380px;
        padding-top: 1.2rem;
        padding-bottom: 2rem;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #06101f 0%, #020817 100%);
        border-right: 1px solid rgba(148,163,184,0.12);
        min-width: 330px;
        max-width: 330px;
    }

    [data-testid="stSidebar"] .block-container {
        padding-top: 1.2rem;
        padding-left: 1rem;
        padding-right: 1rem;
    }

    [data-testid="stHeader"] {
        background: rgba(0,0,0,0);
    }

    .brand-wrap {
        padding: 0.5rem 0 1rem 0;
        margin-bottom: 0.5rem;
    }

    .brand-title {
        font-size: 2.2rem;
        font-weight: 800;
        line-height: 1;
        letter-spacing: -0.02em;
        color: white;
        margin-bottom: 0.35rem;
    }

    .brand-subtitle {
        color: #94a3b8;
        font-size: 1rem;
    }

    .nav-pill {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        background: linear-gradient(90deg, #2563eb, #4338ca);
        border: 1px solid rgba(255,255,255,0.08);
        color: white;
        font-weight: 700;
        border-radius: 14px;
        padding: 0.95rem 1rem;
        margin: 0.6rem 0 1.2rem 0;
        box-shadow: 0 10px 30px rgba(37,99,235,0.22);
    }

    .view-switch-note {
        color: #94a3b8;
        font-size: 0.9rem;
        margin-top: -0.45rem;
        margin-bottom: 0.85rem;
    }

    .section-label {
        color: #cbd5e1;
        font-size: 0.9rem;
        font-weight: 700;
        letter-spacing: 0.04em;
        margin: 1.1rem 0 0.9rem 0;
        padding-bottom: 0.7rem;
        border-bottom: 1px solid rgba(148,163,184,0.16);
        text-transform: uppercase;
    }

    .control-card {
        background: linear-gradient(180deg, rgba(15,23,42,0.72), rgba(8,20,39,0.88));
        border: 1px solid rgba(148,163,184,0.14);
        border-radius: 16px;
        padding: 0.8rem 0.9rem 0.55rem 0.9rem;
        margin-bottom: 0.85rem;
    }

    .control-label {
        display: flex;
        align-items: center;
        gap: 0.65rem;
        color: #e2e8f0;
        font-weight: 600;
        margin-bottom: 0.55rem;
        font-size: 1rem;
    }

    .icon-box {
        width: 34px;
        height: 34px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        border-radius: 10px;
        font-size: 1rem;
    }

    .icon-green { background: rgba(34,197,94,0.16); color: #4ade80; }
    .icon-purple { background: rgba(124,58,237,0.16); color: #a78bfa; }
    .icon-gold { background: rgba(245,158,11,0.16); color: #fbbf24; }
    .icon-cyan { background: rgba(34,211,238,0.16); color: #67e8f9; }
    .icon-blue { background: rgba(59,130,246,0.16); color: #60a5fa; }

    .tip-card {
        margin-top: 1rem;
        background: linear-gradient(180deg, rgba(12,27,51,0.95), rgba(8,20,39,0.95));
        border: 1px solid rgba(148,163,184,0.14);
        border-radius: 16px;
        padding: 1rem;
        color: #dbeafe;
    }

    .tip-card strong {
        color: #a3e635;
    }

    .switch-card {
        background: linear-gradient(180deg, rgba(15,23,42,0.72), rgba(8,20,39,0.88));
        border: 1px solid rgba(148,163,184,0.14);
        border-radius: 16px;
        padding: 0.75rem 0.8rem;
        margin-bottom: 1rem;
    }

    .top-tabs {
        margin-bottom: 0.8rem;
    }

    .status-card {
        border-radius: 18px;
        padding: 1.4rem;
        min-height: 175px;
        border: 1px solid rgba(255,255,255,0.08);
        box-shadow: inset 0 1px 0 rgba(255,255,255,0.03);
    }

    .safe-card {
        background: linear-gradient(135deg, rgba(22,163,74,0.32), rgba(6,78,59,0.38));
        border-color: rgba(34,197,94,0.22);
    }

    .risk-card {
        background: linear-gradient(135deg, rgba(239,68,68,0.28), rgba(127,29,29,0.32));
        border-color: rgba(239,68,68,0.26);
    }

    .status-badge {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 58px;
        height: 58px;
        border-radius: 14px;
        font-size: 1.7rem;
        margin-right: 0.9rem;
        vertical-align: top;
        box-shadow: 0 10px 25px rgba(0,0,0,0.18);
    }

    .safe-badge {
        background: radial-gradient(circle at top left, #4ade80, #16a34a);
        color: white;
    }

    .risk-badge {
        background: radial-gradient(circle at top left, #fb7185, #ef4444);
        color: white;
    }

    .status-title {
        display: inline-block;
        vertical-align: top;
    }

    .status-title h2 {
        margin: 0;
        padding: 0;
        font-size: 2rem;
        line-height: 1.15;
        color: white;
        font-weight: 800;
    }

    .status-title p {
        margin: 0.45rem 0 0 0;
        color: rgba(255,255,255,0.92);
        font-size: 1.05rem;
    }

    .action-strip {
        margin-top: 1rem;
        background: rgba(15, 23, 42, 0.45);
        border: 1px solid rgba(148,163,184,0.14);
        border-radius: 12px;
        padding: 0.9rem 1rem;
        color: #cbd5e1;
        font-size: 1rem;
    }

    .main-shell {
        background: linear-gradient(180deg, rgba(3,7,18,0.12), rgba(3,7,18,0.03));
        border-radius: 24px;
    }

    .metric-shell {
        background: linear-gradient(180deg, rgba(12,27,51,0.9), rgba(10,20,35,0.9));
        border: 1px solid rgba(148,163,184,0.13);
        border-radius: 18px;
        padding: 1rem 1.1rem;
        min-height: 122px;
        box-shadow: 0 10px 25px rgba(2,6,23,0.26);
    }

    .metric-label {
        color: #cbd5e1;
        font-size: 0.95rem;
        margin-bottom: 0.55rem;
    }

    .metric-value {
        color: white;
        font-size: 2rem;
        font-weight: 800;
        line-height: 1.15;
        margin-bottom: 0.45rem;
    }

    .metric-delta {
        display: inline-flex;
        align-items: center;
        gap: 0.35rem;
        border-radius: 999px;
        padding: 0.22rem 0.65rem;
        font-size: 0.86rem;
        font-weight: 700;
    }

    .delta-red { background: rgba(239,68,68,0.14); color: #f87171; }
    .delta-green { background: rgba(34,197,94,0.14); color: #4ade80; }
    .delta-gold { background: rgba(245,158,11,0.14); color: #fbbf24; }
    .delta-purple { background: rgba(124,58,237,0.14); color: #c4b5fd; }

    .panel {
        background: linear-gradient(180deg, rgba(10,20,35,0.95), rgba(8,20,39,0.98));
        border: 1px solid rgba(148,163,184,0.12);
        border-radius: 20px;
        padding: 1rem 1rem 0.5rem 1rem;
        margin-top: 0.6rem;
        box-shadow: 0 12px 30px rgba(2,6,23,0.24);
    }

    h1, h2, h3 {
        color: white !important;
        letter-spacing: -0.02em;
    }

    .subtitle {
        color: #cbd5e1;
        font-size: 1.1rem;
        margin-top: -0.4rem;
        margin-bottom: 0.9rem;
    }

    .tab-caption {
        color: #f8fafc;
        font-weight: 700;
        margin-bottom: 0.6rem;
        font-size: 1.45rem;
    }

    div[data-testid="stMetric"] {
        background: transparent;
        border: none;
        padding: 0;
    }

    div[data-baseweb="input"] > div,
    div[data-baseweb="base-input"] > div {
        background: #071224 !important;
        border: 1px solid rgba(148,163,184,0.18) !important;
        border-radius: 12px !important;
        color: white !important;
    }

    input {
        color: white !important;
    }

    .stNumberInput button {
        color: white !important;
    }

    .stSlider [data-baseweb="slider"] > div > div:nth-child(2) {
        background: linear-gradient(90deg, #22c55e, #8b5cf6) !important;
    }

    .stButton > button {
        width: 100%;
        border: 0;
        border-radius: 14px;
        min-height: 3.35rem;
        background: linear-gradient(90deg, #2563eb 0%, #7c3aed 100%);
        color: white;
        font-weight: 800;
        font-size: 1rem;
        box-shadow: 0 10px 25px rgba(79,70,229,0.28);
        transition: all 0.25s ease;
    }

    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 14px 30px rgba(79,70,229,0.38);
        border: 0;
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 1.1rem;
        border-bottom: 1px solid rgba(148,163,184,0.14);
    }

    .stTabs [data-baseweb="tab"] {
        color: #cbd5e1;
        font-weight: 700;
        padding-left: 0;
        padding-right: 0;
        padding-top: 0.35rem;
        padding-bottom: 0.75rem;
    }

    .stTabs [aria-selected="true"] {
        color: #60a5fa !important;
    }

    div[role="radiogroup"] {
        gap: 0.6rem;
    }

    div[role="radiogroup"] label {
        background: rgba(15,23,42,0.82) !important;
        border: 1px solid rgba(148,163,184,0.14) !important;
        border-radius: 12px !important;
        padding: 0.55rem 0.8rem !important;
    }

    div[role="radiogroup"] label p {
        color: #e2e8f0 !important;
        font-weight: 600 !important;
    }

    .stAlert {
        border-radius: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Sidebar UI
# -----------------------------
with st.sidebar:
    st.markdown(
        """
        <div class="brand-wrap">
            <div class="brand-title">olist</div>
            <div class="brand-subtitle">AI Logistics Intelligence</div>
        </div>
        <div class="nav-pill">🏠 <span>Dashboard</span></div>
        <div class="section-label">System Controls</div>
        <div class="view-switch-note">Switch between live prediction and analytics on the same page.</div>
        """,
        unsafe_allow_html=True,
    )

    view_option = st.radio(
        "Workspace",
        ["🚀 Intelligent Predictor", "📊 Executive Analytics"],
        index=0 if st.session_state.active_view == "predictor" else 1,
        label_visibility="collapsed",
    )
    st.session_state.active_view = "predictor" if "Predictor" in view_option else "analytics"

    olist_categories = [
        "bed_bath_table", "health_beauty", "sports_leisure", "furniture_decor",
        "computers_accessories", "housewares", "watches_gifts", "telephony",
        "garden_tools", "auto", "toys", "cool_stuff", "perfumery", "baby"
    ]

    st.markdown('<div class="section-label">Input Parameters</div>', unsafe_allow_html=True)

    st.markdown(
        '<div class="control-card"><div class="control-label"><span class="icon-box icon-blue">📦</span>Product Category</div></div>',
        unsafe_allow_html=True,
    )
    selected_product = st.selectbox(
        "Product Category (Dataset Native)",
        olist_categories,
        label_visibility="collapsed",
    )

    st.markdown(
        '<div class="control-card"><div class="control-label"><span class="icon-box icon-green">📍</span>Distance (KM)</div></div>',
        unsafe_allow_html=True,
    )
    dist = st.number_input("Distance (KM)", value=450.0, label_visibility="collapsed")

    st.markdown(
        '<div class="control-card"><div class="control-label"><span class="icon-box icon-purple">👜</span>Weight (Grams)</div></div>',
        unsafe_allow_html=True,
    )
    weight = st.number_input("Weight (Grams)", value=1500.0, label_visibility="collapsed")

    st.markdown(
        '<div class="control-card"><div class="control-label"><span class="icon-box icon-gold">💰</span>Price ($)</div></div>',
        unsafe_allow_html=True,
    )
    price = st.number_input("Price ($)", value=120.0, label_visibility="collapsed")

    st.markdown('<div class="section-label">Risk Controls</div>', unsafe_allow_html=True)

    st.markdown(
        '<div class="control-label"><span class="icon-box icon-cyan">🛡️</span>Seller Risk Factor</div>',
        unsafe_allow_html=True,
    )
    seller_rel = st.slider("Seller Risk Factor", 0.0, 1.0, 0.05, label_visibility="collapsed")

    st.markdown(
        '<div class="control-label"><span class="icon-box icon-blue">🌐</span>Regional Risk Factor</div>',
        unsafe_allow_html=True,
    )
    state_risk = st.slider("Regional Risk Factor", 0.0, 1.0, 0.10, label_visibility="collapsed")

    submit = st.button("🚀  RUN AI DIAGNOSTICS")

    st.markdown(
        """
        <div class="tip-card">
            <strong>Tip:</strong> Adjust the parameters to see how risk changes in real time.
        </div>
        """,
        unsafe_allow_html=True,
    )

# -----------------------------
# Backend call
# -----------------------------
if submit:
    payload = {
        "distance_km": dist,
        "price": price,
        "freight_value": 25.0,
        "product_weight_g": weight,
        "product_photos_qty": 1,
        "purchase_hour": 14,
        "purchase_day_of_week": 1,
        "purchase_month": 4,
        "category_short": selected_product,
        "seller_reliability": seller_rel,
        "state_late_avg": state_risk,
    }

    try:
        res = requests.post("http://127.0.0.1:8000/predict", json=payload, timeout=10)
        res.raise_for_status()
        st.session_state.result = res.json()
        st.session_state.submitted = True
    except Exception:
        st.session_state.result = None
        st.session_state.submitted = True

# -----------------------------
# Single-page content with switchable views
# -----------------------------
if st.session_state.active_view == "predictor":
    st.markdown('<div class="tab-caption">Predictive Delivery Guardrail</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Real-time risk assessment for global logistics.</div>', unsafe_allow_html=True)

    result = st.session_state.result

    col1, col2 = st.columns([1.1, 1], gap="large")

    with col1:
        if st.session_state.submitted and result:
            prob = float(result["probability"])
            is_high = result["risk_status"] == "High"

            if is_high:
                st.markdown(
                    f"""
                    <div class="status-card risk-card">
                        <div>
                            <span class="status-badge risk-badge">⚠️</span>
                            <span class="status-title">
                                <h2>HIGH RISK DETECTED</h2>
                                <p>Confidence Score: {prob*100:.1f}%</p>
                            </span>
                        </div>
                        <div class="action-strip"><strong>Action:</strong> Flag for priority handling.</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(
                    f"""
                    <div class="status-card safe-card">
                        <div>
                            <span class="status-badge safe-badge">✅</span>
                            <span class="status-title">
                                <h2>ORDER IS SAFE</h2>
                                <p>Confidence Score: {(1-prob)*100:.1f}%</p>
                            </span>
                        </div>
                        <div class="action-strip"><strong>Action:</strong> Proceed with standard logistics.</div>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
        elif st.session_state.submitted and not result:
            st.error("Backend offline. Please start FastAPI in Terminal 1.")
        else:
            st.markdown(
                f"""
                <div class="status-card safe-card" style="opacity:0.88;">
                    <div>
                        <span class="status-badge safe-badge">✨</span>
                        <span class="status-title">
                            <h2>READY FOR ANALYSIS</h2>
                            <p>Run diagnostics to generate a live delivery risk assessment for <strong>{selected_product}</strong>.</p>
                        </span>
                    </div>
                    <div class="action-strip"><strong>Action:</strong> Tune the parameters and launch diagnostics.</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    with col2:
        gauge_value = 44.7
        bar_color = "#22c55e"
        if result:
            gauge_value = float(result["probability"]) * 100
            bar_color = "#ef4444" if gauge_value >= 65 else "#22c55e"

        fig = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=gauge_value,
                number={"font": {"size": 40, "color": "#f8fafc"}},
                gauge={
                    "axis": {"range": [0, 100], "tickcolor": "#cbd5e1", "tickwidth": 1},
                    "bar": {"color": bar_color, "thickness": 0.34},
                    "bgcolor": "rgba(255,255,255,0)",
                    "borderwidth": 0,
                    "steps": [{"range": [0, 100], "color": "rgba(255,255,255,0.12)"}],
                },
                domain={"x": [0, 1], "y": [0, 1]},
            )
        )
        fig.update_layout(
            height=330,
            margin=dict(t=10, b=0, l=20, r=20),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font={"color": "#f8fafc", "family": "sans-serif"},
        )
        st.plotly_chart(fig, use_container_width=True)

else:
    st.markdown('<div class="tab-caption">Strategic Analytics</div>', unsafe_allow_html=True)

    c1, c2, c3, c4 = st.columns(4, gap="medium")

    with c1:
        st.markdown(
            """
            <div class="metric-shell">
                <div class="metric-label">Avg Delivery</div>
                <div class="metric-value">12.4 Days</div>
                <div class="metric-delta delta-red">↓ 1.2</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            """
            <div class="metric-shell">
                <div class="metric-label">Success Rate</div>
                <div class="metric-value">92.7%</div>
                <div class="metric-delta delta-green">↑ 0.5%</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            """
            <div class="metric-shell">
                <div class="metric-label">Seller Risk</div>
                <div class="metric-value">Low</div>
                <div class="metric-delta delta-gold">● Stable</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c4:
        st.markdown(
            """
            <div class="metric-shell">
                <div class="metric-label">Efficiency</div>
                <div class="metric-value">88%</div>
                <div class="metric-delta delta-purple">↑ 2%</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    chart_col1, chart_col2 = st.columns([1.25, 1], gap="large")

    with chart_col1:
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.markdown("#### Regional Risk Correlator")
        df = pd.DataFrame({"Dist": [100, 500, 1000, 2500], "Risk": [2, 10, 25, 85]})
        area = px.area(df, x="Dist", y="Risk")
        area.update_traces(line=dict(color="#2f7df6", width=3), fillcolor="rgba(47,125,246,0.32)")
        area.update_layout(
            height=300,
            margin=dict(t=20, b=20, l=10, r=10),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="#e2e8f0"),
            xaxis=dict(
                title="Distance (KM)",
                showgrid=False,
                zeroline=False,
                color="#cbd5e1",
            ),
            yaxis=dict(
                title="Risk",
                gridcolor="rgba(148,163,184,0.12)",
                zeroline=False,
                color="#cbd5e1",
            ),
        )
        st.plotly_chart(area, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with chart_col2:
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.markdown("#### Top Risk Factors")
        donut = px.pie(
            values=[45, 25, 30],
            names=["Sellers", "Distance", "Other"],
            hole=0.62,
        )
        donut.update_traces(
            textinfo="percent",
            textfont_size=16,
            marker=dict(colors=["#60a5fa", "#fca5a5", "#2563eb"], line=dict(color="#081427", width=2)),
        )
        donut.update_layout(
            height=300,
            margin=dict(t=20, b=20, l=10, r=10),
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="#e2e8f0"),
            legend=dict(
                orientation="v",
                bgcolor="rgba(0,0,0,0)",
                font=dict(color="#e2e8f0"),
            ),
        )
        st.plotly_chart(donut, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
