import streamlit as st
from pathlib import Path
from src.engine.metrics_engine import MetricsEngine

# Page Configuration

st.set_page_config(
    page_title="Autonomous Driving Release Readiness",
    page_icon="🚗",
    layout="wide"
)

# Project Paths

PROJECT_ROOT = (Path(__file__)
    .resolve()
    .parent
)

DATA_PATH = PROJECT_ROOT / "data" / "raw"

# Session State Initialization

def initialize_session():

    if "initialized" not in st.session_state:

        engine = MetricsEngine(DATA_PATH)
        model = engine.run()
        st.session_state.engine = engine
        st.session_state.model = model
        st.session_state.initialized = True

initialize_session()

# Sidebar Navigation

st.sidebar.title("🚗 Release Readiness")
st.sidebar.success("Metrics Engine Loaded")
model = st.session_state.model
st.sidebar.subheader("Filters")

program = st.sidebar.selectbox("Vehicle Program", ["All", "Program A", "Program B", "Program C"])
test_phase = st.sidebar.multiselect(
    "Validation Phase", ["Software", "HIL", "Bench", "Vehicle"],
    default=["Software", "HIL", "Bench", "Vehicle"]
)

st.session_state.filters = {"program": program, "test_phase": test_phase}

# Home Page

st.title("Autonomous Driving Release Readiness Dashboard")

st.markdown(
"""
### System Overview

This application provides a unified view of:

- Perception performance
- Planning safety metrics
- Control performance
- Software validation
- HIL validation
- Bench testing
- Vehicle readiness
- Release decision
"""
)

# Executive Summary Cards

col1, col2, col3, col4 = st.columns(4)

with col1: st.metric("Release Score", f"{model.release.score:.1f}")
with col2: st.metric("Decision", model.release.decision)
with col3: st.metric("Pass Rate", f"{model.statistics.pass_rate:.1%}")
with col4: st.metric("Recommendation", model.statistics.recommendation)

st.divider()
st.info(
"""
Use the navigation menu on the left to explore:
- Executive Dashboard
- Release Gate
- Software Integration
- HIL Validation
- Bench Validation
- Vehicle Validation
"""
)