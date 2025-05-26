# 🤖 ChatGPT Clone using Groq LLaMA3 & Streamlit

An AI-powered chat assistant built with **LangChain**, **Groq's LLaMA3 model**, and **Streamlit**, designed to simulate a real-time ChatGPT-style interaction with memory, conversation summarization, and a user-friendly interface.

---

## Live Deployment
You can access the live version of the project at: [Live Link](https://chat-gpt.streamlit.app)

---

## ✨ Features

- 💬 Real-time chatbot interface
- 🧠 Memory-enabled conversation via `ConversationSummaryMemory`
- 🔑 Secure Groq API key input from sidebar
- 📝 One-click conversation summary
- 🔁 Reset conversation at any time
- 📱 Responsive and minimalistic UI

---

<!--## 📸 Demo Preview

> ![ChatGPT Clone Screenshot](https://i.imgur.com/N7yVZfO.png)  
> 
-->


## 🔧 Tech Stack

- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [Groq LLaMA3](https://console.groq.com/)
- Python 3.10+

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/shivamshar03/conversational-ai.git
cd conversational-ai
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
streamlit run app.py
```

> ✅ You'll be prompted to enter your **Groq API Key** in the sidebar.

---

## 🔐 Environment Setup (Optional)

To store your Groq API Key securely using a `.env` file:

1. Install `python-dotenv`:
   ```bash
   pip install python-dotenv
   ```

2. Create a `.env` file:
   ```env
   GROQ_API_KEY=your_actual_api_key_here
   ```

3. Modify your app to load this key using `os.getenv()` and `load_dotenv()`.

---

## 📁 File Structure

```
chatgpt-groq-clone/
│
├── app.py                 # Streamlit App for Chat Interface
├── requirements.txt       # Python dependencies
├── README.md              # Documentation
└── .venv/                 # Virtual environment (optional)
```

---

## 📦 Example `requirements.txt`

```txt
streamlit
streamlit-chat
langchain
langchain-groq
python-dotenv
```

---

## 🧠 How It Works

- **ConversationChain** from LangChain manages the chat logic.
- **ChatGroq** connects to the LLaMA3 model via your Groq API key.
- **ConversationSummaryMemory** retains and summarizes conversation context.
- Chat messages are displayed using `streamlit-chat`.

---

## ✅ To-Do & Enhancements

- 🎙️ Voice input/output integration
- 🌙 Add dark/light mode toggle
- 📁 Export conversation as `.txt` or `.pdf`
- 🗃️ Persistent database for chat history
- 🌐 Multi-language support

---

## 👨‍💻 Author

**Shivam Sharma**  
🎓 AI/ML Enthusiast | Python Developer  
📫 [LinkedIn](https://www.linkedin.com/in/shivam-sharma-ab489721b)

---

## 📝 License

This project is licensed under the [MIT License](LICENSE).
