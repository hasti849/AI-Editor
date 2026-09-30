from ninja import NinjaAPI
from app.api.v1.prompts import router as prompts_router
from app.api.v1.collections import router as collections_router
from app.api.v1.users import router as users_router
from app.api.v1.saved_prompts import router as saved_prompts_router

# Initialize the v1 API
api_v1 = NinjaAPI(version="1.0.0", title="Minimalist Prompt Showcase API - v1", description="API for Curated Prompts and Collections")

# Register routers under v1
api_v1.add_router("/prompts/", prompts_router)
api_v1.add_router("/collections/", collections_router)
api_v1.add_router("/users/", users_router)
api_v1.add_router("/saved-prompts/", saved_prompts_router)

# We can define api_v2 = NinjaAPI(version="2.0.0") later if needed
