import streamlit as st
from src.stats_utils.session import get_model

st.set_page_config(page_title="Executive Dashboard", layout="wide")
model = get_model()
st.title("Executive Dashboard")

# KPI Cards

c1,c2,c3,c4 = st.columns(4)

with c1: st.metric("Release Score", f"{model.release.score:.1f}")

with c2: st.metric("Decision", model.release.decision)

with c3: st.metric("Pass Rate", f"{model.statistics.pass_rate:.1%}")

with c4: st.metric("Recommendation", model.statistics.recommendation)

# Domain Summary

st.subheader("System Metrics")

col1,col2,col3 = st.columns(3)

with col1:
    st.write("### Perception")
    st.metric( "F1 Score", f"{model.perception.f1:.3f}")
    st.metric("Miss Rate", f"{model.perception.miss_rate:.3f}")

with col2:
    st.write("### Planning")
    st.metric("Lane Error", f"{model.planning.lane_error:.3f}")
    st.metric("Min TTC", f"{model.planning.min_ttc:.3f}")

with col3:
    st.write("### Control")
    st.metric("Tracking Error", f"{model.control.tracking_error:.3f}")
    st.metric("Average Jerk", f"{model.control.avg_jerk:.3f}")