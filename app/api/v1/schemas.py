from ninja import Schema
from typing import List, Optional
from datetime import datetime
from uuid import UUID

class CollectionSchema(Schema):
    id: UUID
    title: str
    description: Optional[str] = None
    cover_image: Optional[str] = None
    is_active: bool
    created_at: datetime

class PromptSchema(Schema):
    id: UUID
    title: str
    content: str
    collection_id: Optional[UUID] = None
    tags: List[str]
    created_at: datetime
    updated_at: datetime

class UserSchema(Schema):
    id: UUID
    username: str
    email: str
    gender: Optional[str] = None
    is_onboarded: bool

class UserUpdateSchema(Schema):
    username: Optional[str] = None
    email: Optional[str] = None
    gender: Optional[str] = None
    is_onboarded: Optional[bool] = None

class SavedPromptSchema(Schema):
    id: UUID
    user_id: UUID
    prompt_id: UUID
    saved_at: datetime
