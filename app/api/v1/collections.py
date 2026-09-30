from ninja import Router
from django.shortcuts import get_object_or_404
from typing import List
from app.models import Collection
from .schemas import CollectionSchema

router = Router(tags=["Collections"])

@router.get("/", response=List[CollectionSchema])
def list_collections(request):
    """
    Get a list of all curated collections/packs.
    """
    return Collection.objects.filter(is_active=True)

@router.get("/{collection_id}", response=CollectionSchema)
def get_collection(request, collection_id: str):
    """
    Get a single collection by its UUID.
    """
    collection = get_object_or_404(Collection, id=collection_id, is_active=True)
    return collection
