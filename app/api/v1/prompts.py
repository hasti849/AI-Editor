from ninja import Router
from django.shortcuts import get_object_or_404
from typing import List
from app.models import Prompt
from .schemas import PromptSchema

router = Router(tags=["Prompts"])

@router.get("/", response=List[PromptSchema])
def list_prompts(request):
    """
    Get a list of all curated prompts.
    """
    return Prompt.objects.all().select_related('collection')

@router.get("/{prompt_id}", response=PromptSchema)
def get_prompt(request, prompt_id: str):
    """
    Get a single prompt by its UUID.
    """
    prompt = get_object_or_404(Prompt, id=prompt_id)
    return prompt

