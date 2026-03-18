# EGGF Runtime Kernel (RCEK)

Enterprise GenAI Governance Fabric (EGGF-nXt) — Runtime Execution Control Kernel for probabilistic AI systems.

---

## 🚀 What This Is

EGGF is a **runtime control plane for AI inference** that enforces compliance **during generation**, not after.

Unlike traditional guardrails, EGGF operates inside the inference loop:

IIM → CEE → RESE → ECC → CRIM

---

## 🧠 Core Capabilities

- Token-level runtime control (pre-sampling)
- Compliance-driven execution state transitions
- Evidence-based output enforcement
- Agent permission validation (DAG + DFS)
- Tamper-proof audit logging (hash chain)
- Multi-token controlled generation

---

## 🏗️ Architecture

Prompt → LLM → EGGF Kernel → Modified Output → Audit + Hash

---

## ⚙️ Setup

pip install -r requirements.txt

---

## 🧪 Run Demo

python scripts/demo.py

---

## 🌐 Run API

uvicorn api.app_v2:app --reload

---

## 🖥️ Run UI

streamlit run ui/streamlit_app.py

---

## 📊 API Output

response | state | audit_trace | hash | evidence_status

---

## 🧠 Positioning

Runtime Operating System for AI Governance

---

## 📌 Status

MVP Complete | Demo Ready | Enterprise Prototype
