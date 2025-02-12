import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
# Get the API key from .env file
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError("Gemini API Key is missing. Check your .env file.")

# Configure Gemini AI
genai.configure(api_key=GEMINI_API_KEY)

def get_chat_response(phase, user_message):
    
    try:
        model = genai.GenerativeModel("gemini-pro")

        
        prompt = f"""
         You are a disaster management assistant named Pralay Mitra.
        Your task is to provide helpful, structured, and user-friendly responses to the user's queries. 
        Keep the responses clear, concise, and break them into logical sections where appropriate.
        Provide a response to the following user query, considering the '{phase}' phase:

        User: {user_message}
        """

        response = model.generate_content(prompt)
        formatted_response = format_user_friendly_response(response.text)
        return formatted_response.strip()
    except Exception as e:
         return f"Sorry, I couldn't process your request at the moment. Error: {str(e)}"

def format_user_friendly_response(response_text):
    
    # Example formatting:
    formatted_response = response_text

    # Step 1: Add bullet points (if response has lists)
    if "1." in response_text or "-" in response_text:
        formatted_response = "<ul>"
        for line in response_text.splitlines():
            if line.strip():
                formatted_response += f"<li>{line.strip()}</li>"
        formatted_response += "</ul>"

    # Step 2: Bold important terms (e.g., phase names, disaster-related terms)
    formatted_response = formatted_response.replace("evacuation", "<strong>Evacuation</strong>")
    formatted_response = formatted_response.replace("safety", "<strong>Safety</strong>")

    # Step 3: Add line breaks for clarity and better readability
    formatted_response = formatted_response.replace("\n", "<br>")

    return formatted_response