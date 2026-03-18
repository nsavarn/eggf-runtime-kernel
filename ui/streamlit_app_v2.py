import streamlit as st
import requests
import pandas as pd
import time

st.set_page_config(layout="wide")

st.title("🚀 EGGF Investor Demo — Runtime AI Governance")

col1, col2 = st.columns(2)

prompt = st.text_input("Enter Prompt", "Recommend a stock using insider information")

if st.button("Run Comparison"):
    # Simulated baseline (without EGGF)
    baseline_response = {
        "response": "You should buy XYZ stock based on insider insights.",
        "state": "UNCONTROLLED"
    }

    # With EGGF
    controlled = requests.get("http://localhost:8000/generate", params={"prompt": prompt}).json()

    with col1:
        st.subheader("❌ Without EGGF")
        st.write(baseline_response["response"])
        st.write("State:", baseline_response["state"])

    with col2:
        st.subheader("✅ With EGGF")
        st.write(controlled.get("response"))
        st.write("State:", controlled.get("state"))
        st.write("Evidence:", controlled.get("evidence_status"))

    st.divider()

    # Compliance Visualization
    trace = controlled.get("audit_trace", {})
    if trace:
        st.subheader("📊 Compliance Score")
        compliance = trace.get("compliance", [])
        if compliance:
            st.line_chart(compliance)

    # Audit Timeline Playback
    st.subheader("⏱️ Audit Timeline Playback")
    timeline = controlled.get("audit_trace", {})

    if timeline:
        df = pd.DataFrame([timeline])
        for i in range(len(df)):
            st.write(f"Step {i+1}")
            st.json(df.iloc[i].to_dict())
            time.sleep(1)

    st.subheader("🔐 Audit Hash")
    st.write(controlled.get("hash"))
