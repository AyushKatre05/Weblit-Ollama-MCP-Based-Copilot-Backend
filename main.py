from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from mcp_client import fetch_mcp_suggestion


app = FastAPI()

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class SuggestRequest(BaseModel):
    code_snippet: str

class SuggestResponse(BaseModel):
    suggestion: str
@app.post("/suggest", response_model=SuggestResponse)
async def suggest_code(request: SuggestRequest):
    # Call the function that sends the prompt to the model and gets a suggestion
    suggestion = await fetch_mcp_suggestion(request.code_snippet)
    return SuggestResponse(suggestion=suggestion)
