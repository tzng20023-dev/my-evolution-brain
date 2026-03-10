# 🧠 My Evolution Brain (v2.0)

> **Status: ACTIVE** | **Connection: REST API** | **Security: ED25519**

這是一個具備「自主進化」能力的 AI 系統中心。透過 Google Gemini API 與自定義 REST 協議，實現邏輯吞噬與硬體效能監控。

## 🚀 核心功能
* **REST 穩定通訊**：採用 `v1beta` 官方路徑，避開傳統 SDK 限制。
* **自動模型偵測**：啟動時自動掃描可用模型（Flash/Pro），確保連線不中斷。
* **GPU 效能監控**：即時回傳顯存與核心溫度，維持運算巔峰。
* **系統看板同步**：自動將 AI 進化紀錄噴射至 `localhost:8000` 監控面板。

## 🛠️ 安裝與啟動
1. 建立環境變數 `.env` 並填入 `GEMINI_API_KEY`。
2. 啟動看板服務：`python app.py` (啟動 Flask 伺服器)。
3. 啟動大腦：`python brain_v2.py`。

## 🛡️ 安全宣言
本專案僅用於技術研究與進化學習，語音助理無物化女性切勿多做聯想。
