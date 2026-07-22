import streamlit as st

from src.stats_utils.session import get_model


model = get_model()

hil = model.hil


st.title(
    "Hardware In Loop Validation"
)


st.metric(
    "Coverage",
    f"{hil.coverage:.1%}"
)


st.metric(
    "Fault Injection",
    f"{hil.fault_injection_pass_rate:.1%}"
)


st.metric(
    "HIL Status",
    hil.hil_status
)