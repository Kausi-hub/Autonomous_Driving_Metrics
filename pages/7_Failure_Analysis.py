import streamlit as st

from src.stats_utils.session import get_model


model=get_model()

analysis=model.failure_analysis


st.title(
    "Failure Analysis & Scenario Risk"
)


st.subheader(
    "Top Failure Modes"
)


for item in analysis.top_failures:

    st.write(
        f"{item.failure}: {item.count}"
    )


st.subheader(
    "Scenario Risk Ranking"
)


for item in analysis.risk_ranking:

    st.write(
        item.scenario,
        item.risk
    )


st.success(
    analysis.recommendation
)