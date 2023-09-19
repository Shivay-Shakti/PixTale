# Importing the 'requests' library for making HTTP requests and 'os' for environment variables
import requests
import os

# Define a function called 'text2speech' that takes a message string as input
def text2speech(message):
    """
    Convert a text message to speech using the Hugging Face Text-to-Speech API.
    
    Parameters:
    message (str): The text message to be converted to speech.
    
    Returns:
    None: Writes the generated audio to a file named 'audio.flac'.
    """
    
    # Define the API URL for the Hugging Face Text-to-Speech model
    API_URL = "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"
    
    # Set up the Authorization header using the API key from the environment variable
    headers = {"Authorization": f"Bearer {os.environ.get('HUGGINGFACEHUB_API_KEY')}"}
    
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

# Sample code for testing (commented out)
# scenario=image2text("https://...") # Updating with remote file URL for the path
# story = generate_story(scenario)
# text2speech(story)
