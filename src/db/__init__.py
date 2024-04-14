import os

from dotenv import load_dotenv
from sqlmodel import create_engine

load_dotenv()

__DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(__DATABASE_URL)
