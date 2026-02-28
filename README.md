# 🤖 LangGraph Streaming Chatbot (GLM-5 + Streamlit)

A stateful AI chatbot built using LangGraph and powered by the GLM-5 large language model from Hugging Face.
The chatbot includes real-time streaming responses and a modern chat UI built with Streamlit.
<br>
## 🚀 Features

🧠 Stateful conversations using LangGraph<br>
💬 Message reducer with add_messages<br>
⚡ Real-time token streaming<br>
🖥️ Interactive chat UI using st.chat_message<br>
🗂️ Thread-based memory with InMemorySaver<br>
🔐 Environment variable support via .env<br>
🎲 Dynamic chatbot title (randomized greeting)<br>

## 🏗️ Tech Stack

LangGraph<br>
LangChain<br>
Hugging Face Endpoint<br>
GLM-5 Model<br>
Streamlit<br>
Python 3.10+<br>


## ⚙️ Installation
1️⃣ Clone the repository<br>
git clone https://github.com/your-username/langgraph-chatbot.git
cd langgraph-chatbot
2️⃣ Create Virtual Environment<br>
python -m venv myvenv

### Activate:
Windows<br>
myvenv\Scripts\activate

Mac/Linux<br>
source myvenv/bin/activate

3️⃣ Install Dependencies<br>
pip install -r requirements.txt

### 🔐 Environment Setup

Create a .env file in the root directory:<br>
HF_TOKEN=your_huggingface_api_key

The chatbot uses the following Hugging Face model:<br>
zai-org/GLM-5

Make sure your Hugging Face account has access.

▶️ Run the Application<br>
streamlit run app.py

Open in browser:<br>
http://localhost:8501



## ⚡ Streaming Implementation

Streaming is handled using:
chatbot.stream(...)

With:
stream_mode="messages"

In Streamlit:
st.write_stream(...)

This creates:<br>
Real-time token streaming<br>
Typing effect<br>
Smooth user experience<br>

### 🔄 Memory Handling

Two layers of memory:

🔹 Backend Memory<br>
LangGraph state<br>
Thread ID based<br>
InMemorySaver<br>

🔹 Frontend Memory<br>
st.session_state<br>
Stores role & content<br>
Used to reload chat on page refresh<br>
