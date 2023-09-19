# Importing the 'requests' library for making HTTP requests
import requests

def text2speech(message, api_key):
    """
    Convert a text message to speech using the Hugging Face Text-to-Speech API.
    
    Parameters:
    message (str): The text message to be converted to speech.
    api_key (str): The Hugging Face API key for authorization.
    
    Returns:
    None: Writes the generated audio to a file named 'audio.flac'.
    """
    
    # Define the API URL for the Hugging Face Text-to-Speech model
    API_URL = "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"
    
    # Set up the Authorization header using the provided API key
    headers = {"Authorization": f"Bearer {api_key}"}
    
    # Create a dictionary containing the text input
    payloads = {"inputs": message}

    # Make a POST request to the Hugging Face API
    response = requests.post(API_URL, headers=headers, json=payloads)
    
    # Check if the response is successful (HTTP status code 200)
    if response.status_code == 200:
        # If successful, write the audio content to an 'audio.flac' file
        with open('audio.flac', 'wb') as file:
            file.write(response.content)
    else:
        # If the request failed, print the status code and response content
        print(f"Failed to convert text to speech. Status code: {response.status_code}")
        print(f"Response: {response.json()}")
