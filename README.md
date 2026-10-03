# multi-agent-document-system
Multi-agent AI system built with FastAPI, LangGraph, Gemini and n8n that processes client proposal PDFs and logs audited results to Google Sheets.
# Multi-Agent Document System

> An AI-powered pipeline that takes a client proposal PDF, processes it through a team of specialized agents, and logs the audited result to Google Sheets, automatically.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688)
![LangGraph](https://img.shields.io/badge/LangGraph-Multi--Agent-orange)
![n8n](https://img.shields.io/badge/n8n-Automation-red)
![Gemini](https://img.shields.io/badge/Google-Gemini-4285F4)

---

## 🎥 Demo

https://lnkd.in/p/dnjEbzjc

---

##  Overview

Handling client proposals manually is slow and error-prone. This project automates the whole flow:

1. A client uploads a PDF through an **n8n form**.
2. n8n sends the file to a **FastAPI** backend (`/process-document`).
3. A **multi-agent system** (built with LangGraph and Gemini) processes the document step by step.
4. The final output and audit log are saved to a **Google Sheet** automatically.

---

##  Architecture

```
Client uploads PDF
        │
        ▼
   n8n Form Trigger
        │
        ▼
 FastAPI  /process-document
        │
        ▼
 ┌──────────────────────────────┐
 │   LangGraph Multi-Agent Flow │
 │  Guardrail → Intake →        │
 │  Requirements → Research →   │
 │  Drafting → Audit            │
 └──────────────────────────────┘
        │
        ▼
 Google Sheets (Audit Logs)
```

<!-- TODO: Add an architecture / workflow image here (optional) -->
<!-- ![Architecture](images/architecture.png) -->

---

##  Agents

| Agent | Responsibility |
|-------|----------------|
| **Guardrail Agent** | Checks the document for unsafe or malicious content before processing |
| **Intake Agent** | Reads the PDF and extracts the raw text and metadata |
| **Requirements Agent** | Extracts key client requirements and objectives |
| **Research Agent** | Adds relevant context and best practices |
| **Drafting Agent** | Drafts the final structured output |
| **Audit Agent** | Reviews the output and records an audit log |

---

##  Screenshots

### 1. Backend: FastAPI (Swagger UI)

<img width="1917" height="947" alt="image" src="https://github.com/user-attachments/assets/53acca09-966c-487a-9482-01b499f8f8ef" />


### 2. Automation: n8n Workflow

<img width="1917" height="1012" alt="image" src="https://github.com/user-attachments/assets/84c5174c-862e-4267-9be8-972c548b7bd6" />


### 3. Upload Form

<img width="1917" height="932" alt="image" src="https://github.com/user-attachments/assets/5a35233b-5ac3-4c2d-8128-b364b12bc3dd" />


---

## 🛠️ Tech Stack

- **Language:** Python
- **Backend:** FastAPI, Uvicorn
- **Agent Framework:** LangGraph, LangChain
- **LLM:** Google Gemini (`langchain-google-genai`)
- **Automation:** n8n
- **UI:** Streamlit
- **Storage / Logs:** Google Sheets

---

##  Project Structure

<!-- Adjust this to match your actual folders -->
```
Agents/
├── agents/
│   ├── api.py
│   ├── graph.py
│   ├── state.py
│   ├── guardrail_agent.py
│   ├── intake_agent.py
│   ├── requirements_agent.py
│   ├── research_agent.py
│   ├── drafting_agent.py
│   └── audit_agent.py
├── n8n/
│   └── workflow.json
├── images/
├── app.py
├── .env.example
└── README.md
```

---

##  Installation

**1. Clone the repository**
```bash
git clone https://github.com/hassanalighulam7-spec/multi-agent-document-system.git
cd multi-agent-document-system
```

**2. Create a virtual environment and install dependencies**
```bash
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
```

**3. Set up environment variables**

Copy `.env.example` to `.env` and add your own keys:
```env
GOOGLE_API_KEY=your_gemini_api_key_here
MODEL_NAME=your_gemini_model_name
```

---

##  Usage

**Start the API**
```bash
uvicorn agents.api:api_app --reload --port 8000
```
Open the interactive docs at: `http://127.0.0.1:8000/docs`

**(Optional) Start the Streamlit UI**
```bash
streamlit run app.py
```

**n8n workflow**
1. Open n8n and import `n8n/workflow.json`.
2. Connect your own Google Sheets credentials.
3. Point the HTTP Request node to `http://localhost:8000/process-document`.
4. Open the form URL, upload a PDF, and watch the result appear in your Google Sheet.

---

##  Future Improvements

- Human-in-the-loop review dashboard
- Support for more document types (DOCX, scanned PDFs)
- Role-based access control and stronger security checks
- Docker deployment

---

##  Author

**Ghulam Hassan**
BS Cyber Security student | Exploring AI automation and secure AI systems

- GitHub: (https://github.com/hassanalighulam7-spec)
- LinkedIn:(https://www.linkedin.com/in/ghulamhassan-cyber/)

---

⭐ If you found this project useful, consider giving it a star!
