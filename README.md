# 🧠 QueryMind: LLM-Powered Natural Language to SQL Engine

> Transform natural language into executable SQL queries using Large Language Models with schema awareness, self-healing correction, and real-time visualization.

---

## 🚀 Overview

QueryMind is an end-to-end **LLM-powered Natural Language to SQL engine** built using Streamlit and MySQL.  

It allows users to:
- Ask database questions in plain English
- Automatically generate optimized SQL queries
- Execute them safely
- Auto-correct errors
- Visualize results dynamically

The system intelligently grounds prompts using live database schema, ensuring accurate and context-aware SQL generation.

---

## 🎯 Key Features

### 🔹 1. Natural Language → SQL Generation
Convert human questions into executable SQL queries using an LLM.

Example:
```
Show top 5 customers by credit limit
```

Generated SQL:
```sql
SELECT customerName, creditLimit
FROM customers
ORDER BY creditLimit DESC
LIMIT 5;
```

---

### 🔹 2. Schema-Aware Prompt Engineering
- Live database schema is injected into the LLM prompt
- Reduces hallucinations
- Improves JOIN accuracy
- Enables multi-table reasoning

---

### 🔹 3. Secure Execution Layer
- Only `SELECT` queries allowed
- `DELETE`, `UPDATE`, `DROP` automatically blocked
- SQL cleaned before execution

---

### 🔹 4. Self-Healing SQL Engine (Auto Error Correction Loop)
If execution fails:
1. Database error is captured
2. Error + schema sent back to LLM
3. LLM generates corrected query
4. Query re-executed automatically

---

### 🔹 5. Query Explanation Mode
Optional toggle to:
- Display SQL explanation
- Understand query logic
- Improve learning experience

---

### 🔹 6. Dynamic Auto Visualization
- Detects numeric columns
- Automatically generates charts
- Supports aggregation queries

---

### 🔹 7. Professional Dual Panel UI
- 📂 Left Panel: Database, Tables, Schema
- 💬 Right Panel: Question Input + SQL Output
- 🎨 Clean dark theme
- 🚀 Modern SaaS-style interface

---

## 🏗️ System Architecture

```
User Question
      ↓
Schema-Aware Prompt Builder
      ↓
LLM SQL Generation
      ↓
SQL Cleaning & Safety Guard
      ↓
Query Execution
      ↓
If Error → Auto Correction Loop
      ↓
Final Output + Visualization
```

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Frontend UI | Streamlit |
| Backend | Python |
| Database | MySQL |
| Dataset Used | classicmodels / custom datasets |
| AI Engine | LLM (API-based) |
| Visualization | Streamlit Charts |
| Architecture Pattern | Schema-grounded Prompt + Self-healing loop |

---

## 📂 Project Structure

```
QueryMind/
│
├── app.py                 # Main Streamlit Application
├── db.py                  # Database connection & execution logic
├── llm.py                 # LLM API integration
├── prompt_builder.py      # Prompt engineering logic
├── requirements.txt
└── README.md
```

---

## 🧪 Example Test Queries

Try these:

- Show first 5 customers
- Count total orders per customer
- Show total payment received per customer
- Show top 5 products by total sales
- Show employee name and office city

---

## 🔐 Safety Mechanism

QueryMind ensures:
- Only SELECT queries execute
- SQL injection risk minimized
- Automatic error feedback correction

---

## 📊 Sample Output

✔ Generated SQL  
✔ Query Result Table  
✔ Automatic Chart  
✔ Optional Explanation  

---

## 🚀 How to Run

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Run Application

```bash
streamlit run app.py
```

---

## 💡 Why This Project Stands Out

✔ End-to-end working system  
✔ Real-world LLM integration  
✔ Self-correcting architecture  
✔ Schema grounding  
✔ Safe execution layer  
✔ Professional UI  
✔ Recruiter-ready  

---

## 📈 Future Improvements

- Multi-database support (PostgreSQL, SQLite)
- Authentication system
- Query history tracking
- Performance optimization layer
- Fine-tuned domain model
- Deployment to cloud (Streamlit Cloud / AWS)

---

## 👨‍💻 Author

**Pratham Soni**  
Built with passion for AI + Data Engineering 🚀

---

## ⭐ If You Like This Project

Give it a star ⭐ on GitHub and feel free to fork!

---

# 🔥 QueryMind – Making Databases Conversational
