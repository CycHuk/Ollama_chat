from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Chat(BaseModel):
    id: Optional[str] = None
    created_at: Optional[datetime] = None
    title: Optional[str] = None
    can_user_write: Optional[bool] = None
    response_by: Optional[str] = None

    def to_dict(self):
        return self.dict(exclude={"created_at"})