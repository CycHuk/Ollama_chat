from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Message(BaseModel):
    id: Optional[int] = None
    chat_id: Optional[str] = None
    writer: Optional[str] = None
    message: Optional[str] = None
    created_at: Optional[datetime] = None

    def to_dict(self):
        return self.dict(exclude={"created_at"})