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


## Backend Setup
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload

## Environment Variables
DATABASE_URL=mysql+pymysql://root:password@localhost:3306/hcp_crm_db
GROQ_API_KEY=your_api_key
GROQ_MODEL=llama-3.3-70b-versatile

# API Endpoints

## Interaction APIs
POST   /api/interactions
GET    /api/interactions
GET    /api/interactions/{id}
PUT    /api/interactions/{id}
DELETE /api/interactions/{id}

## AI Agent APIs
POST /api/agent/ask
POST /api/agent/chat-log

## LangGraph Tool APIs
POST /api/agent/tools/log-interaction
POST /api/agent/tools/edit-interaction
POST /api/agent/tools/summarize-interaction
POST /api/agent/tools/extract-entities
POST /api/agent/tools/recommend-next-action

## Example: AI Chat Log
POST /api/agent/chat-log

{
  "message": "I met Dr. Sharma at Apollo Hospital. He was interested in CardioPlus and requested follow-up."
}

## Author
Kusam Bharath