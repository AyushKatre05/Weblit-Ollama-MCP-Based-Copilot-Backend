import httpx
import logging

MCP_SERVER_URL = "http://localhost:11434"
DEFAULT_MODEL_NAME = "llama3.2"
DEFAULT_STREAM = False

async def fetch_mcp_suggestion(prompt: str) -> str:
    focused_prompt = f"use github copilot like code like whats the next suggestion only return 1-2 lines in response : {prompt}"
    
    payload = {"prompt": focused_prompt}

    headers = {"model": DEFAULT_MODEL_NAME, "stream": str(DEFAULT_STREAM).lower()}

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(f"{MCP_SERVER_URL}/api/generate", json=payload, headers=headers)
            response.raise_for_status()
            chunk = response.json()
            return chunk.get("response", "").strip()
    except Exception as e:
        logging.error(f"Error: {e}")
        return ""
