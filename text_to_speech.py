import requests
import os

def text2speech(message):
    API_URL = "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"
    headers = {"Authorization": f"Bearer {os.environ.get('HUGGINGFACEHUB_API_KEY')}"}
    payloads = {"inputs": message}

    # Making a POST request to the Text-to-Speech API
    response = requests.post(API_URL, headers=headers, json=payloads)
    
    # Check if the status code indicates success (HTTP 200)
    if response.status_code == 200:
        # If successful, write the audio content to a file
        with open('audio.flac', 'wb') as file:
            file.write(response.content)
    else:
        # If not successful, print the status code and response content
        print(f"Failed to convert text to speech. Status code: {response.status_code}")
        print(f"Response: {response.json()}")

 
#scenario=image2text("https://github.com/Shivay-Shakti/Image2Audio/blob/8bb59e51c19387693bdd0299c16c596ab59f647b/cats.jpg") #updating with remote file url for the path
#story = generate_story(scenario)
#text2speech(story)