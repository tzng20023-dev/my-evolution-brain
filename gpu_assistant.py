from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

# 狀態儲存容器
state = {"msg": "[2026-03-10 10:48] 系統就緒，等待 OpenClaw 指令..."}

@app.get("/", response_class=HTMLResponse)
async def index():
    # 網頁每 2 秒自動刷新，確保文字即時對應
    return f"""
    <html>
        <head><meta http-equiv="refresh" content="2"></head>
        <body style="background: #121212; color: #00ff41; font-family: 'Courier New', Courier, monospace; padding: 40px;">
            <div style="border: 2px solid #00ff41; padding: 20px; box-shadow: 0 0 15px #00ff41;">
                <h2 style="margin-top: 0;">> SYSTEM_MONITOR_ACTIVE</h2>
                <hr style="border: 0.5px solid #00ff41;">
                <p style="font-size: 22px;">{state['msg']}</p>
            </div>
        </body>
    </html>
    """

@app.post("/update")
async def update(text: str = Form(...)):
    state["msg"] = text
    print(f"[*] 收到文字對應請求: {text}")
    return {"status": "success", "received": text}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
