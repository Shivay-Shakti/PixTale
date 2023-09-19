# Importing required modules and functions
import streamlit as st
from image_to_text import image2text
from story_generation import generate_story
from text_to_speech import text2speech

def main():
    """
    Main function to run the Streamlit app.
    """
    # Configure the Streamlit app
    st.set_page_config(page_title="Visual Story Generator", page_icon="🧊", layout="centered", initial_sidebar_state="expanded")

    # Sidebar for API credentials
    with st.sidebar:
        st.header("API Credentials")
        hugging_face_key = st.text_input("Hugging Face API Key", type="password")
        # Add more fields for other APIs as needed

    # Main header
    st.header("Your Image Into Story")

    # File uploader for image
    uploaded_file = st.file_uploader("Choose an image...", type="jpg")

    if uploaded_file is not None:
        # Debugging: print uploaded file details
        print(uploaded_file)

        # Read uploaded file as bytes
        bytes_data = uploaded_file.getvalue()

        # Save the uploaded image locally
        with open("uploaded_image.jpg", "wb") as f:
            f.write(bytes_data)

        # Display uploaded image
        st.image(bytes_data, caption='Uploaded Image.', use_column_width=True)

        # Convert image to text and generate a story
        scenario = image2text("uploaded_image.jpg")  # Assuming this function is defined in another file
        story = generate_story(scenario)  # Assuming this function is defined in another file

        # Convert the generated story to speech
        # Using the user-provided Hugging Face API key
        text2speech(story, hugging_face_key)

        # Display the generated text and story
        with st.expander("Scenario"):
            st.write(scenario)
        with st.expander("Story"):
            st.write(story)

        # Play the generated audio
        st.audio("audio.flac")

# Entry point of the application
if __name__ == "__main__":
    main()
