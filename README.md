# AI-First CRM HCP Module – Log Interaction System

## Overview

This project is an AI-first Customer Relationship Management (CRM) module designed for life sciences field representatives to log interactions with Healthcare Professionals (HCPs).

The system allows users to log interactions via:
- Structured manual form
- AI-powered conversational interface

It uses LangGraph and Groq LLM to intelligently extract, summarize, and recommend next actions.

---

## Features

### Core Functionality
- Log HCP interactions manually (structured form)
- Log interactions using AI chat (natural language)
- View all interactions in dashboard
- Edit and update interactions
- Delete interactions

### AI Capabilities
- Automatic entity extraction (HCP, hospital, product)
- AI-generated summaries
- Sentiment detection
- Follow-up detection
- Next best action recommendation

---

## LangGraph Agent & Tools

The LangGraph agent acts as the decision-making layer that processes user input and selects the appropriate tool.

### Implemented Tools:

1. **Log Interaction Tool**
2. **Edit Interaction Tool**
3. **Summarize Interaction Tool**
4. **Extract Entities Tool**
5. **Recommend Next Action Tool**

---

## Tech Stack

### Frontend
- React (Vite)
- Redux Toolkit
- Axios
- Google Inter Font

### Backend
- FastAPI (Python)
- SQLAlchemy ORM
- MySQL Database

### AI Layer
- LangGraph (Agent Framework)
- Groq LLM (`llama-3.3-70b-versatile`)

---

## Project Structure
```
ai-first-crm-hcp-module/
├── backend/
│ ├── app/
│ │ ├── models/
│ │ ├── schemas/
│ │ ├── crud/
│ │ ├── routes/
│ │ ├── agent/
│ │ ├── database.py
│ │ ├── config.py
│ │ └── main.py
│
├── frontend/
│ ├── src/
│ │ ├── components/
│ │ ├── features/
│ │ ├── pages/
│ │ ├── app/
│ │ └── services/

```
## Backend Setup

## ⚙️ Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Environment Variables
```text
DATABASE_URL=mysql+pymysql://root:password@localhost:3306/hcp_crm_db
GROQ_API_KEY=your_api_key
GROQ_MODEL=llama-3.3-70b-versatile
```

# API Endpoints

## Interaction APIs
```text
POST   /api/interactions
GET    /api/interactions
GET    /api/interactions/{id}
PUT    /api/interactions/{id}
DELETE /api/interactions/{id}
```
## AI Agent APIs
```
POST /api/agent/ask
POST /api/agent/chat-log
```
## LangGraph Tool APIs
```
POST /api/agent/tools/log-interaction
POST /api/agent/tools/edit-interaction
POST /api/agent/tools/summarize-interaction
POST /api/agent/tools/extract-entities
POST /api/agent/tools/recommend-next-action
```
## Example: AI Chat Log
```
POST /api/agent/chat-log

{
  "message": "I met Dr. Sharma at Apollo Hospital. He was interested in CardioPlus and requested follow-up."
}
```
## How to Use the Application (User Workflow)

This application is designed for **field representatives in life sciences** to log and manage interactions with Healthcare Professionals (HCPs).

---

### 1. Log Interaction using AI Chat

- Navigate to **AI Chat Logger**
- Enter interaction in natural language:

  Example:
  "I met Dr. Sharma at Apollo Hospital. He showed interest in CardioPlus and requested follow-up."

- Click **"Log with AI"**

System will:
- Extract HCP name, hospital, and product
- Detect sentiment (positive/neutral/negative)
- Identify follow-up requirements
- Generate summary
- Save data into CRM automatically

---

### 2. Log Interaction using Structured Form

- Navigate to **Structured Log Form**
- Enter details manually:
  - HCP Name
  - Specialty
  - Organization
  - Interaction Type
  - Notes, etc.

- Click **"Save Interaction"**

Used when precise manual entry is required

---

### 3. View Interactions

- All logged interactions appear in the **Dashboard**
- Each card shows:
  - Doctor name
  - Organization
  - Summary
  - Sentiment
  - Follow-up status

---

### 4. Edit Interaction

- Click **Edit** on any interaction
- Update fields like:
  - Notes
  - Sentiment
  - Follow-up date

- Save changes

---

### 5. Delete Interaction

- Click **Delete**
- Confirm removal

---

### 6. AI Assistance (Business Value)

The system helps:
- Convert unstructured conversations into structured CRM data
- Reduce manual data entry effort
- Improve follow-up tracking
- Provide actionable insights for sales representatives

## Author
Kusam Bharath