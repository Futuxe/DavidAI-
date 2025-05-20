# ai_engine.py
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class CodeRequest(BaseModel):
    prompt: str
    language: str

@router.post("/")
def generate_code(request: CodeRequest):
    code_map = {
        "python": f"# Kod wygenerowany w Pythonie\nprint('{request.prompt}')",
        "cpp": f"// Kod w C++\n#include<iostream>\nint main() {{ std::cout << \"{request.prompt}\"; return 0; }}",
        "java": f"// Kod w Javie\npublic class Main {{ public static void main(String[] args) {{ System.out.println(\"{request.prompt}\"); }} }}"
    }
    return {"generated_code": code_map.get(request.language.lower(), "// Nieobsługiwany język")}
