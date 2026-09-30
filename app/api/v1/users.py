from ninja import Router
from django.shortcuts import get_object_or_404
from typing import List
from app.models import User
from .schemas import UserSchema, UserUpdateSchema

router = Router(tags=["Users"])

@router.get("/", response=List[UserSchema])
def list_users(request):
    """
    Get a list of all users.
    """
    return User.objects.all()

@router.get("/{user_id}", response=UserSchema)
def get_user(request, user_id: str):
    """
    Get a single user by ID.
    """
    return get_object_or_404(User, id=user_id)

@router.put("/{user_id}", response=UserSchema)
def update_user(request, user_id: str, payload: UserUpdateSchema):
    """
    Update user details.
    """
    user = get_object_or_404(User, id=user_id)
    for attr, value in payload.dict(exclude_unset=True).items():
        setattr(user, attr, value)
    user.save()
    return user

@router.delete("/{user_id}")
def delete_user(request, user_id: str):
    """
    Delete a user.
    """
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return {"success": True}
