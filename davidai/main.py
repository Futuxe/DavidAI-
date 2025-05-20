import json
from fastapi import FastAPI, Header, HTTPException
from .models import CodeRequest, CodeResponse
from .utils import generate_code
from threading import Lock
from datetime import datetime, date

app = FastAPI()

API_KEY = "RJW(80)OP"
USAGE_FILE = "usage.json"
USAGE_LOCK = Lock()
LIMIT = 10

def load_usage():
    try:
        with open(USAGE_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_usage(data):
    with open(USAGE_FILE, "w") as f:
        json.dump(data, f)

def reset_if_needed(entry):
    today_str = date.today().isoformat()
    if entry.get("last_reset") != today_str:
        entry["count"] = 0
        entry["last_reset"] = today_str

@app.post("/generate/", response_model=CodeResponse)
async def generate_code_endpoint(
    request: CodeRequest,
    x_api_key: str = Header(None)
):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid or missing API key")

    with USAGE_LOCK:
        usage = load_usage()
        entry = usage.get(x_api_key, {"count": 0, "last_reset": date.today().isoformat()})

        reset_if_needed(entry)

        if entry["count"] >= LIMIT:
            raise HTTPException(status_code=403, detail="Free usage limit exceeded for today")

        entry["count"] += 1
        usage[x_api_key] = entry
        save_usage(usage)

    code = generate_code(request.prompt, request.language)
    return CodeResponse(generated_code=code)
