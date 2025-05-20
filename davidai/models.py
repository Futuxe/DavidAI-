from pydantic import BaseModel

class CodeRequest(BaseModel):
    prompt: str
    language: str

class CodeResponse(BaseModel):
    generated_code: str
