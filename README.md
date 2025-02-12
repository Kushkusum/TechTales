# 📖 TechTales – AI Storyteller for Technical Concepts
🚀 Transform complex technical topics into engaging stories with AI!

## 🌟 Project Overview
TechTales is an AI-powered storytelling application that takes a technical concept and transforms it into an engaging story format. It also generates a quiz based on the topic and provides AI-powered narration of the story.

## 🎯 Key Features
✅ AI-Generated Storytelling – Converts technical topics into engaging stories

✅ Multiple Storytelling Styles – Choose from Classic, Sci-Fi, Fantasy, Detective, Mythology, and more

✅ Interactive Quiz – Generates multiple-choice questions related to the topic

✅ AI Voice Narration – Converts the story into speech using gTTS

✅ User-Friendly UI – Built with Streamlit for an interactive experience

✅ Flask API Backend – Processes requests and handles AI generation



## ⚙️ Tech Stack Used
**Frontend**

Streamlit – Interactive UI for user inputs and displaying results

**Backend**

Flask – Handles API requests and AI processing

OpenAI API (or alternate LLM) – Generates stories and quizzes

gTTS (Google Text-to-Speech) – Converts stories into speech




## 📌 Installation & Setup Guide
1️⃣ Clone the Repository
    
    git clone https://github.com/your-username/TechTales.git
    cd TechTales
    
2️⃣ Set Up Virtual Environment
      
      python -m venv venv
      source venv/bin/activate   # For macOS/Linux
      venv\Scripts\activate      # For Windows
      
3️⃣ Install Required Dependencies

    pip install -r requirements.txt
    
4️⃣ Add API Keys in .env

Create a .env file in the root directory and add your API key:

    API_KEY=your_api_key_here

5️⃣ Run the Flask Backend
        
        python app.py
        
🚀 Flask server will start on: http://127.0.0.1:5000

6️⃣ Run the Streamlit Frontend

Open a new terminal and run:

    streamlit run app_ui.py

🔹Streamlit UI will open in your browser!


## 🎥 How It Works?
1️⃣ Enter a technical topic in the UI

2️⃣ Choose a storytelling style

3️⃣ Click "Generate Story"

4️⃣ AI creates a story & quiz

5️⃣ Listen to AI narration of the story

6️⃣ Attempt the quiz and check answers


## 🎨 Future Enhancements
🔹 More storytelling styles

🔹 Background animations & effects

🔹 More quiz interactivity (hints, scores, timer)

🔹 Export story as PDF/eBook

