from ninja import Router
from django.shortcuts import get_object_or_404
from typing import List
from app.models import SavedPrompt, User, Prompt
from .schemas import SavedPromptSchema

router = Router(tags=["Saved Prompts"])

@router.get("/", response=List[SavedPromptSchema])
def list_saved_prompts(request):
    """
    Get a list of all saved prompts.
    """
    return SavedPrompt.objects.all()

@router.post("/")
def create_saved_prompt(request, user_id: str, prompt_id: str):
    """
    Save a prompt for a user.
    """
    user = get_object_or_404(User, id=user_id)
    prompt = get_object_or_404(Prompt, id=prompt_id)
    
    saved_prompt, created = SavedPrompt.objects.get_or_create(user=user, prompt=prompt)
    if not created:
        return {"message": "Prompt already saved."}
    return {"id": str(saved_prompt.id), "user_id": str(user.id), "prompt_id": str(prompt.id)}

@router.get("/{saved_prompt_id}", response=SavedPromptSchema)
def get_saved_prompt(request, saved_prompt_id: str):
    """
    Get a saved prompt entry by ID.
    """
    return get_object_or_404(SavedPrompt, id=saved_prompt_id)

@router.delete("/{saved_prompt_id}")
def delete_saved_prompt(request, saved_prompt_id: str):
    """
    Delete a saved prompt entry.
    """
    saved_prompt = get_object_or_404(SavedPrompt, id=saved_prompt_id)
    saved_prompt.delete()
    return {"success": True}
