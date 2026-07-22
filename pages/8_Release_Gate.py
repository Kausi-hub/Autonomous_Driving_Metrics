import streamlit as st

from src.stats_utils.session import get_model


model = get_model()


st.title(
    "Release Gate Assessment"
)


release = model.release


if release.decision == "PASS":

    st.success(
        "Release Gate PASSED"
    )

else:

    st.error(
        "Release Gate FAILED"
    )


st.metric(
    "Release Score",
    f"{release.score:.1f}"
)


st.write(
"Decision:"
)

st.write(
release.decision
)