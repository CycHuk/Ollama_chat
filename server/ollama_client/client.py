from ollama import Client
from .config import host

client = Client(
  host=host,
)