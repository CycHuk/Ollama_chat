from ollama import AsyncClient
from .config import host

client = AsyncClient(
  host=host,
)