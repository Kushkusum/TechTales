import streamlit as st
import requests
import base64

# Flask API Endpoint
API_URL = "http://127.0.0.1:5000/generate"

# Streamlit UI Customization
st.set_page_config(
    page_title="TechTales – AI Storyteller",
    page_icon="📖",
    layout="wide"
)

# Title & Subtitle
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>📖 TechTales – AI Storyteller</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size:18px;'>Transform complex technical topics into engaging stories!</p>", unsafe_allow_html=True)
st.divider()  

# UI Layout - Input Section
col1, col2 = st.columns([2, 1])

with col1:
    topic = st.text_input("🔍 Enter a Technical Topic:", placeholder="Neural Networks, Blockchain, etc.", help="Type a technical concept for the AI to generate a story.")
    
with col2:
    story_style = st.selectbox("Choose a storytelling style:", [
    "Classic", "Sci-Fi", "Fantasy", "Detective", "Mythology", 
    "Cyberpunk", "Historical Fiction", "Superhero", "Survival Thriller", 
    "Steampunk", "Comedy", "Space Exploration", "Mystery", 
    "Pirate Adventure", "Time Travel"
])

st.markdown("---")  # Separator line

# Generate button
if st.button("✨ Generate AI Story", use_container_width=True):
    if topic:
        with st.spinner("🎤 Crafting your AI-powered story..."):
            response = requests.post(API_URL, json={"topic": topic, "style": story_style})

            if response.status_code == 200:
                data = response.json()

                # Display Story
                st.markdown("## 📖 Story")
                st.write(data["story"])

                # Display Quiz inside Expander
                with st.expander("🎯 Take the Quiz"):
                    st.write(data["quiz"])

                # Play AI Narration
                st.markdown("## 🎙️ Listen to the Story")
                audio_base64 = data.get("audio", "")
                if audio_base64:
                    audio_bytes = base64.b64decode(audio_base64)
                    st.audio(audio_bytes, format="audio/mp3")

            else:
                st.error("🚨 Something went wrong. Please try again.")

    else:
        st.warning("⚠️ Please enter a topic first.")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:14px;'>Made with ❤️ using AI & Streamlit</p>", unsafe_allow_html=True)
