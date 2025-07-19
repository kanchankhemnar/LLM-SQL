# 🧠 LLM-SQL V2 – Natural Language to SQL Assistant

LLM-SQL is a smart assistant that converts **natural language questions** into **SQL queries** and executes them on a real database.  
Built with **Streamlit**, **Gemini 2.5 Flash**, and **SQLite**, it's designed to help **non-technical users** generate insights from data without writing SQL.

🔗 **Live App:** [llm-sql-v2.streamlit.app](https://llm-sql-v2.streamlit.app)

---

## 💡 Features

- ✅ Convert plain English into executable SQL queries using **Gemini 2.5 Flash**
- ✅ Interact with a real **SQLite database**
- ✅ Choose from **sample questions** or enter your own
- ✅ Display query results with smart formatting
- ✅ Show full database on demand
- ✅ Secure Gemini API key via **Streamlit secrets**

---

## 🛠️ Tech Stack

| Layer         | Tech                |
|---------------|---------------------|
| 🧠 LLM         | Gemini 2.5 Flash (via `google-genai`) |
| 🎛️ Backend     | Python, SQLite      |
| 🎨 Frontend    | Streamlit           |
| 🔐 Secrets     | Streamlit Cloud Secrets |
| 📦 Packaging   | requirements.txt    |
| ☁️ Deployment  | Streamlit Cloud     |

---

## 📦 How It Works

1. User asks a question (e.g., _“Who scored highest?”_)
2. The prompt + schema are sent to Gemini LLM
3. Gemini returns a valid SQL query (e.g., `SELECT ...`)
4. The app runs the query on `student.db` using SQLite
5. Results are shown in a clean UI (list or table)

---

## 🧪 Sample Questions

- Who scored more than 80 marks?
- Give the student with the highest marks
- List all students in section A
- What is the average marks of students in section B?
- Show top 3 students with highest marks

---

## 🚀 Getting Started (Local)

```bash
git clone https://github.com/kanchankhemnar/LLM-SQL.git
cd llm-sql

# Create virtual env (optional)
pip install -r requirements.txt

# Add secrets
mkdir .streamlit
echo "GEMINI_API_KEY = 'your-api-key'" > .streamlit/secrets.toml

# Run locally
streamlit run app.py
```
🤖 Prompt Engineering
The app uses a carefully designed prompt that:

Informs the model about the table schema

Instructs it to return only valid SQL

Avoids extra explanation or markdown

Prompt includes table name, column types, and sample Q&A

✨ Screenshots
![image](https://github.com/user-attachments/assets/e8869d89-15ea-42be-b5e5-696579b64a37)
![image](https://github.com/user-attachments/assets/bff157d9-4cf7-40b8-9488-e7fabd70c9a6)
![image](https://github.com/user-attachments/assets/bdcb9e26-16e0-4d23-870a-21584a48b481)
![image](https://github.com/user-attachments/assets/9b9c04fd-abbb-42e3-8e4a-b05de435d506)
![image](https://github.com/user-attachments/assets/23e835e6-2bbf-4cef-8ce3-c9c39b10435b)


Built With ❤️ by Kanchan Khemnar
