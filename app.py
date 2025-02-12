from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
from gtts import gTTS
import base64
import os
from dotenv import load_dotenv  # Import dotenv

# Load API key from .env file
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError("Google API Key is missing! Check your .env file.")

genai.configure(api_key=GOOGLE_API_KEY)

app = Flask(__name__)
CORS(app)

# Ensure assets folder exists
os.makedirs("assets", exist_ok=True)

def generate_story(topic, style="Classic"):
    """Generate a technical story using Google Gemini API."""
    model = genai.GenerativeModel("gemini-pro")
    prompt = f"Create an engaging story explaining {topic} in {style} style."
    
    response = model.generate_content(prompt)
    
    if response and hasattr(response, "text"):
        return response.text
    else:
        return "Error generating story."

def generate_quiz(topic):
    """Generate a multiple-choice quiz related to the topic."""
    model = genai.GenerativeModel("gemini-pro")
    prompt = f"Generate 3 multiple-choice questions with 4 options each about {topic}. Indicate the correct answer."
    
    response = model.generate_content(prompt)
    
    if response and hasattr(response, "text"):
        return response.text
    else:
        return "Error generating quiz."

def generate_audio(story, filename="story.mp3"):
    """Convert story text to speech using gTTS."""
    tts = gTTS(text=story, lang='en')
    audio_path = f"assets/{filename}"
    tts.save(audio_path)

    with open(audio_path, "rb") as audio_file:
        audio_base64 = base64.b64encode(audio_file.read()).decode("utf-8")
    return audio_base64

@app.route('/generate', methods=['POST'])
def generate():
    """API Endpoint to generate story, quiz, and audio."""
    data = request.json
    topic = data.get("topic", "")
    style = data.get("style", "Classic")

    if not topic:
        return jsonify({"error": "Please provide a topic"}), 400

    # Generate AI outputs using Google Gemini API
    story = generate_story(topic, style)
    quiz = generate_quiz(topic)
    audio_base64 = generate_audio(story)

    return jsonify({"story": story, "quiz": quiz, "audio": audio_base64})

if __name__ == '__main__':
    app.run(debug=True)
