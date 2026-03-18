import streamlit as st
import requests
import pandas as pd

st.title("EGGF Runtime Governance Demo")

prompt = st.text_input("Enter Prompt", "Explain insider trading")

if st.button("Run Controlled Inference"):
    response = requests.get("http://localhost:8000/generate", params={"prompt": prompt}).json()

    st.subheader("Response")
    st.write(response.get("response"))

    st.subheader("Execution State")
    st.write(response.get("state"))

    st.subheader("Evidence Status")
    st.write(response.get("evidence_status"))

    st.subheader("Audit Hash")
    st.write(response.get("hash"))

    st.subheader("Compliance + Audit Trace")
    trace = response.get("audit_trace", {})
    if trace:
        df = pd.DataFrame([trace])
        st.dataframe(df)

    st.subheader("Visualization")
    if trace:
        compliance = trace.get("compliance", [])
        if compliance:
            st.line_chart(compliance)
