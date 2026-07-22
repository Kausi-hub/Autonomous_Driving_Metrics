import streamlit as st

from src.stats_utils.session import get_model


model = get_model()

software = model.software


st.title(
    "Software Integration Validation"
)


c1,c2,c3,c4 = st.columns(4)


with c1:

    st.metric(
        "Build Success",
        f"{software.build_success_rate:.1%}"
    )


with c2:

    st.metric(
        "Unit Tests",
        f"{software.unit_test_pass_rate:.1%}"
    )


with c3:

    st.metric(
        "Static Analysis",
        software.static_analysis_score
    )


with c4:

    st.metric(
        "Status",
        software.integration_status
    )