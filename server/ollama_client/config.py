from dotenv import load_dotenv
import os

load_dotenv()

host = os.getenv('OLLAMA_HOST')
model = os.getenv('OLLAMA_MODEL')
