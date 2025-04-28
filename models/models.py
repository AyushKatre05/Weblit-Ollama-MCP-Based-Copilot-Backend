from pydantic import BaseModel

class SuggestRequest(BaseModel):
    code_snippet: str

class SuggestResponse(BaseModel):
    suggestion: str
