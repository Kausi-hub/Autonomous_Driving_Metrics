import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --------------------------------------------------
# Metrics
# --------------------------------------------------

precision = 0.917
recall = 0.952
lane_error = 0.187
ttc = 0.9
pass_rate = 0.20
release_recommendation = "FAIL"

risk_table = [
    {"scenario": "Emergency Braking", "risk": "HIGH"},
    {"scenario": "Highway Merge", "risk": "MEDIUM"},
    {"scenario": "Lane Change", "risk": "MEDIUM"},
    {"scenario": "Pedestrian Crossing", "risk": "MEDIUM"},
    {"scenario": "Construction Zone", "risk": "LOW"}
]

top_failures = [
    ("Unsafe TTC", 3),
    ("Poor Detection Precision", 1),
    ("Missed Pedestrian", 1)
]

pass_rate_ci = {
    "lower": 0.036,
    "upper": 0.624
}

# --------------------------------------------------
# Page Setup
# --------------------------------------------------

st.set_page_config(
    page_title="Autonomous Validation Dashboard",
    layout="wide"
)

st.title("🚗 Autonomous Driving Validation Dashboard")

# --------------------------------------------------
# KPI Metrics
# --------------------------------------------------

st.subheader("Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Precision", f"{precision:.3f}")

with col2:
    st.metric("Recall", f"{recall:.3f}")

with col3:
    st.metric("Lane Error", f"{lane_error:.3f}")

with col4:
    st.metric("Min TTC", f"{ttc:.2f} sec")

# --------------------------------------------------
# Executive Summary
# --------------------------------------------------

st.subheader("Executive Summary")

st.write("**Scenario Coverage:** 5")
st.write("**Highest Risk Area:** Emergency Braking")
st.write("**Most Common Failure Mode:** Unsafe TTC")

if release_recommendation == "PASS":
    st.success(f"Release Recommendation: {release_recommendation}")
else:
    st.error(f"Release Recommendation: {release_recommendation}")

# --------------------------------------------------
# Summary Cards
# --------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Scenario Pass Rate",
        f"{pass_rate*100:.1f}%"
    )

with col2:
    st.metric(
        "95% CI Lower",
        f"{pass_rate_ci['lower']*100:.1f}%"
    )

with col3:
    st.metric(
        "95% CI Upper",
        f"{pass_rate_ci['upper']*100:.1f}%"
    )

# --------------------------------------------------
# Scenario Risk Ranking
# --------------------------------------------------

st.subheader("Scenario Risk Ranking")

risk_df = pd.DataFrame(risk_table)
st.dataframe(
    risk_df,
    use_container_width=True
)

# --------------------------------------------------
# Top Failure Modes
# --------------------------------------------------

st.subheader("Top Failure Modes")

failure_df = pd.DataFrame(
    top_failures,
    columns=["Failure Mode", "Count"]
)

st.table(failure_df)

# --------------------------------------------------
# Radar Chart
# --------------------------------------------------

st.subheader("System Capability Assessment")

radar = go.Figure()

radar.add_trace(
    go.Scatterpolar(
        r=[92, 90, 85, 94],
        theta=[
            "Perception",
            "Planning",
            "Control",
            "Safety"
        ],
        fill="toself",
        name="Performance"
    )
)

radar.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 100]
        )
    ),
    showlegend=False
)

st.plotly_chart(
    radar,
    use_container_width=True
)

# --------------------------------------------------
# Load Planning Data
# --------------------------------------------------

try:
    planning_df = pd.read_csv("data/raw/planning.csv")

    st.subheader("Time To Collision Trend")

    ttc_chart = px.line(
        planning_df,
        x="timestamp",
        y="ttc",
        title="Time To Collision"
    )

    st.plotly_chart(
        ttc_chart,
        use_container_width=True
    )

    st.subheader("Lane Error Trend")

    lane_chart = px.line(
        planning_df,
        x="timestamp",
        y="lane_error",
        title="Lane Error"
    )

    st.plotly_chart(
        lane_chart,
        use_container_width=True
    )

except Exception as e:
    st.warning(
        f"Unable to load planning.csv: {e}"
    )