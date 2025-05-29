# GPT Researcher Demo

This is a **demo project** showcasing the capabilities of [GPT Researcher](https://docs.gptr.dev/docs/welcome), a powerful autonomous agent designed to perform comprehensive online research on a given topic and generate structured reports.

## 🧠 What is GPT Researcher?

[GPT Researcher](https://docs.gptr.dev/docs/welcome) is an AI tool that:

* Searches the web for high-quality sources on a topic.
* Synthesizes the information.
* Produces a well-structured research report.

This demo integrates GPT Researcher with:

* 🧹 **FastAPI** — for building a lightweight backend.
* 🗾️ **Gradio** — for an intuitive and interactive frontend interface.

---

## 🚀 Features

* Input any topic through the Gradio interface.
* See how GPT Researcher autonomously conducts research.
* Receive structured research output in real time.

---

## ⚙️ Requirements

* Python **3.12** or higher

---

## 📦 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/lezhdz98/demo-gpt-researcher.git
   cd demo-gpt-researcher
   ```

2. **Create a virtual environment**

   ```bash
   python3.12 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file** in the root directory with the following content:

   ```ini
   OPENAI_API_KEY=
   TAVILY_API_KEY=
   ```

   > Replace the blank values with your actual API keys.

---

## 🏁 Running the App

### ▶️ Run the Backend (FastAPI)

```bash
uvicorn fastapi_server:app --reload
```

### 🗾️ Run the Frontend (Gradio)

In a separate terminal (with your virtual environment activated), run:

```bash
python gradio_front.py
```

The Gradio interface will launch in your browser.

---


## 📚 References

* [GPT Researcher Documentation](https://docs.gptr.dev/docs/welcome)

---


