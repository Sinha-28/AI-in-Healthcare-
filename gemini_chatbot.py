import google.generativeai as genai
import textwrap
import time
from config import GEMINI_API_KEY

def format_text(text):
    """Format the response text for better readability."""
    return textwrap.fill(text, width=80)

def chat_with_gemini():
    # Configure Gemini with API key from config.py
    genai.configure(api_key=GEMINI_API_KEY)
    
    # Configuration options - moved to model initialization
    generation_config = {
        "temperature": 0.7,
        "top_p": 1,
        "top_k": 32,
        "max_output_tokens": 4096,
    }
    
    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        # Add other safety settings as needed
    ]
    
    # Initialize the model with configuration
    model = genai.GenerativeModel(
        'gemini-1.5-flash',
        generation_config=generation_config,
        safety_settings=safety_settings
    )
    
    print("Welcome to Ai Health Chatbot!")
    print("Type 'quit' to exit the conversation.\n")
    
    # Start a chat session - now without the config parameters
    chat = model.start_chat(history=[])
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
            
        if not user_input.strip():
            print("Please enter a message.")
            continue
            
        try:
            print("AI is thinking...")
            start_time = time.time()
            
            # Send the user's message to Gemini
            response = chat.send_message(user_input)
            
            end_time = time.time()
            response_time = end_time - start_time
            
            formatted_response = format_text(response.text)
            print(f"\nAI Heathcare Assistant (responded in {response_time:.2f}s):")
            print(formatted_response + "\n")
            
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    chat_with_gemini()
