import os
import requests
# ВСТАВЬТЕ эти строки:
from mcp.server.mcpserver import MCPServer
mcp = MCPServer("Telegram_Spark_Server")

# Булуттагы чөйрө өзгөрмөлөрүнөн токендерди алуу
BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "8945339905:AAFGzyQuOtD3sQwOK3wAb4cmTrf2ObtYkBY")
CHANNEL_ID = os.environ.get("TELEGRAM_CHANNEL_ID", "@nuraaly_bot")

@mcp.tool()
def post_to_telegram(text: str) -> str:
    """Даярдалган текстти Телеграм каналга жарыялайт."""
    if not BOT_TOKEN or not CHANNEL_ID:
        return "Ката: Токен же каналдын ID'си орнотулган жок."

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHANNEL_ID, "text": text, "parse_mode": "HTML"}

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return "Маалымат Телеграм каналга ийгиликтүү жарыяланды!"
    except Exception as e:
        return f"Пост чыгарууда ката кетти: {str(e)}"

if __name__ == "__main__":
    # Gemini Spark интернет аркылуу туташуусу үчүн SSE транспорту колдонулат
    port = int(os.environ.get("PORT", 8000))
    mcp.run(transport="sse", host="0.0.0.0", port=port)
