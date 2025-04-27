import httpx

MCP_SERVER_URL = "http://localhost:5000"  # <-- Change to your MCP server address/port
MCP_MODEL_NAME = "llama3"  # <-- Name of model you want MCP to use

async def fetch_mcp_suggestion(prompt: str) -> str:
    payload = {
        "model": MCP_MODEL_NAME,
        "prompt": prompt,
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(f"{MCP_SERVER_URL}/api/generate", json=payload)
        response.raise_for_status()
        data = response.json()
    
    return data.get("response", "")
