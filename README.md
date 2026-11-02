# 🚀 Nova Smart Knowledge Assistant

Nova Smart Knowledge Assistant is a simple generative AI web application powered by **Amazon Nova 2 Lite** through **Amazon Bedrock**.  
The application allows users to ask questions and receive structured AI-generated explanations instantly.

This project demonstrates how **Amazon Nova foundation models** can be integrated into web applications to build intelligent assistants for learning and knowledge retrieval.

 # 🌟 Features 

- Ask questions through a simple web interface
- AI-generated explanations in real time
- Structured responses with headings, bullet points, and formatting
- Powered by Amazon Nova through Amazon Bedrock

 # 🧠 How It Works
User → Web Interface → Flask Backend → Amazon Bedrock → Nova 2 Lite → Response

1. User enters a question in the web interface.
2. The Flask backend sends the query to Amazon Bedrock.
3. Amazon Bedrock invokes the **Nova 2 Lite** foundation model.
4. The model generates a structured response.
5. The answer is returned and displayed in the UI.

## 🛠 Tech Stack

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python (Flask)
- **AI Model:** Amazon Nova 2 Lite
- **Platform:** Amazon Bedrock
- **Libraries:** boto3, flask, flask-cors
- 
## 📦 Project Structure
nova-smart-knowledge-assistant
│
├── app.py
├── index.html
├── requirements.txt
└── README.md

## ▶️ How to Run the Project
1️⃣ Install dependencies
pip install flask flask-cors boto3

2️⃣ Run the backend server
python app.py

3️⃣ Open the frontend
Open index.html in your browser.

💡 Example Questions
Try asking:
* Explain artificial intelligence
* Summarize climate change
* What is machine learning?
* Compare machine learning and deep learning

## 🎯 Use Case
This project demonstrates how generative AI can help students and learners quickly understand complex topics through AI-generated explanations.

## 🏆 Hackathon Submission
Built for the Amazon Nova Hackathon.
It showcases how developers can build intelligent assistants using Amazon Nova foundation models through Amazon Bedrock.

## 📌 Future Improvements
* Support document uploads for summarization
* Add voice interaction
* Integrate conversation memory
* Expand to multimodal inputs
