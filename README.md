# 🤖 EMAM ChatBot 💬

A chatbot built with **FastAPI** (backend) and **Streamlit** (frontend), powered by **LangChain + Cohere**.  
It supports session-based memory so the conversation flows naturally.

---

## 📂 Project Structure
```

├── main.py       # FastAPI backend (chat API with Cohere)
├── app.py        # Streamlit frontend (chat UI)
├── requirements.txt
├── .gitignore
└── README.md

````

---

## 🚀 Features
- ✅ FastAPI backend for chat requests  
- ✅ Streamlit chat interface with modern UI  
- ✅ Session-based conversation history  
- ✅ Secure API key handling using `.env` (locally) or **Streamlit Secrets** (cloud)  
- ✅ Powered by **LangChain Cohere** (`command-a-03-2025` model)  

---

## 🛠️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/chatbot-deployment.git
cd chatbot-deployment
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure API key

Create a `.env` file in the root directory:

```ini
TOGETHER_API_KEY=your_api_key_here
```

⚠️ Do **not** commit `.env` to GitHub — it should stay private.
On **Streamlit Cloud**, set the key under **App Settings → Secrets**.

---

## ▶️ Running the Project

### Start FastAPI (Backend)

```bash
uvicorn main:app --reload
```

Runs the API at: `http://127.0.0.1:8000/chat`

### Start Streamlit (Frontend)

In another terminal:

```bash
streamlit run app.py
```

Opens the chatbot UI in your browser.

---

## 🌐 Deployment

* **Streamlit Cloud** → Deploy `app.py` (frontend). Use Secrets Manager for your API key.
* **Railway / Render / Heroku** → Deploy `main.py` (backend).
* Optionally: host backend + frontend separately for production.


---

## 📜 License

This project is for educational/demo purposes.
Feel free to fork and extend it!

```

---

👉 Do you want me to also **generate `requirements.txt`** for this project so Streamlit Cloud installs everything automatically?
```
