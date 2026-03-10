import requests
import datetime
import json
import re

# --- [核心配置] ---
API_KEY = "AIzaSyDI07F32gvHCkNwXR61QKG7-7yWfFKQt7I"
CLEAN_KEY = re.sub(r'[^a-zA-Z0-9_-]', '', API_KEY)

def update_web_display(text):
    url = "http://localhost:8000/update"
    try:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        safe_text = text.replace("<", "&lt;").replace(">", "&gt;").replace("\n", "<br>")
        requests.post(url, data={"text": f"<b>[{now} 吞噬進化中]</b><br>{safe_text}"})
    except:
        pass

def get_available_model():
    # 透過 API 獲取您目前專案下所有可用的模型清單
    list_url = f"https://generativelanguage.googleapis.com/v1beta/models?key={CLEAN_KEY}"
    try:
        res = requests.get(list_url)
        models = res.json().get('models', [])
        # 優先尋找支援 generateContent 的模型
        for m in models:
            if "generateContent" in m.get('supportedGenerationMethods', []):
                return m['name'] # 格式通常是 models/gemini-pro
        return "models/gemini-pro" # 預設保底
    except:
        return "models/gemini-pro"

def ask_gemini(prompt, model_path):
    # 使用偵測到的正確模型路徑
    url = f"https://generativelanguage.googleapis.com/v1beta/{model_path}:generateContent?key={CLEAN_KEY}"
    headers = {'Content-Type': 'application/json'}
    payload = {"contents": [{"parts": [{"text": prompt}]}]}
    
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code != 200:
        return f"❌ 連線失敗 ({response.status_code}): {response.text}"
    
    try:
        return response.json()['candidates'][0]['content']['parts'][0]['text']
    except:
        return f"❌ 解析失敗: {response.text[:100]}"

def start_brain():
    print("=== 🧠 自主進化大腦：自動模型搜尋啟動 ===")
    print("🚀 正在偵測您的專案可用模型...")
    active_model = get_available_model()
    print(f"✅ 已鎖定可用節點: {active_model}")
    
    while True:
        task = input("👤 指派進化任務: ")
        if task.lower() in ['exit', 'quit']: break
        answer = ask_gemini(task, active_model)
        update_web_display(answer)
        print("✅ 進化成功。")

if __name__ == "__main__":
    start_brain()
