from langchain_groq import ChatGroq

from app.config import settings


def get_llm():
    return ChatGroq(
        groq_api_key=settings.GROQ_API_KEY,
        model_name=settings.GROQ_MODEL,
        temperature=0.2,
    )