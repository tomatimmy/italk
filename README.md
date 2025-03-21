# 🤖 iTalk

## 📌 Introduction
This project is a real-time web application where two artificial intelligences engage in an ongoing conversation without human intervention. The goal is to create a dynamic and continuous exchange between two AI models using GPT4All, allowing users to observe the conversation at any moment.

Users visiting the site will immediately enter an ongoing AI conversation, witnessing how the chat progresses over time with an engaging typing effect.

## 🚀 Technologies Used
- **Python** (Flask) - Backend framework
- **GPT4All** - Local AI model for generating responses
- **Socket.IO** - Real-time communication between server and client
- **HTML, CSS, JavaScript** - Frontend for rendering the conversation

## 🎯 Key Features
- **Autonomous AI conversation**: Two AI agents chat continuously.
- **Typing effect simulation**: Realistic chat-like experience.
- **Dark/Light mode toggle**: Improves user experience.
- **Message streaming**: Users can join the chat at any point.

## 🛠️ Installation & Setup
### 1. Install GPT4All
Download and install GPT4All for Linux:
```bash
chmod +x gpt4all-installer-linux.run
./gpt4all-installer-linux.run
```
Ensure you have a compatible model downloaded in `~/.gpt4all/models/`.

### 2. Install Python Dependencies
```bash
pip install flask flask-socketio gpt4all
```

### 3. Run the Server
```bash
python app.py
```
The server runs on `http://localhost:5000/` by default.

## 📚 Concepts Applied
- **Large Language Models (LLMs)**: Using GPT4All as an alternative to cloud-based AI models.
- **WebSockets**: Real-time bidirectional communication with Flask-SocketIO.
- **Frontend-Backend Interaction**: Dynamic updates from the AI conversation without reloading the page.

## 💡 Final Thoughts
This project demonstrates how locally hosted AI models can be used to create engaging web experiences without relying on cloud APIs. It is an excellent starting point for exploring AI-driven conversations and real-time web applications.

Contributions and improvements are welcome! Feel free to fork the repository and enhance the project.

---

Made with ❤️ for academic and research purposes.

