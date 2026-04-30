from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "AI First CRM HCP Module"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True

    DATABASE_URL: str

    GROQ_API_KEY: str
    GROQ_MODEL: str = "gemma2-9b-it"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()