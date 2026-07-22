import streamlit as st


def get_model():

    if "model" not in st.session_state:
        st.error("Metrics model not initialized")
        st.stop()
    return st.session_state.model

def get_filters(): return st.session_state.get("filters", {})