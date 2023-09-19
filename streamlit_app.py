# Import necessary modules and functions
import streamlit as st
from image_to_text import image2text
from story_generation import generate_story
from text_to_speech import text2speech

def main():
    """Main function to run the Streamlit app."""
    # Configure the Streamlit page
    st.set_page_config(page_title="Visual Story Generator", page_icon="🧊", layout="centered", initial_sidebar_state="expanded")

    # Sidebar for user API Credentials
    with st.sidebar:
        st.header("API Credentials")
        
        # For Hugging Face
        st.markdown("[Get a Hugging Face API Key](https://huggingface.co/Salesforce/blip-image-captioning-base)")
        hugging_face_key = st.text_input("Hugging Face API Key", type="password")
        
        # For OpenAI
        st.markdown("[Get an OpenAI API Key](https://platform.openai.com/account/api-keys)")
        openai_key = st.text_input("OpenAI API Key", type="password")

    # Validate API Keys
    if not hugging_face_key or not openai_key:
        st.warning("Please enter valid API keys for both Hugging Face and OpenAI to proceed.")
        return

    # Main Header
    st.header("Your Image Into Story")

    # File Uploader
    uploaded_file = st.file_uploader("Choose an image...", type="jpg")

    if uploaded_file is not None:
        # Read and Display Image
        bytes_data = uploaded_file.getvalue()
        st.image(bytes_data, caption='Uploaded Image.', use_column_width=True)

        # Image to Text
        with st.spinner("Converting image to text..."):
            scenario = image2text("uploaded_image.jpg")
        
        # Generate Story
        with st.spinner("Generating story..."):
            story = generate_story(scenario, openai_key)  # Assuming you modify generate_story to accept an API key

        # Text to Speech
        with st.spinner("Converting text to speech..."):
            text2speech(story, hugging_face_key)

        # Display Scenario and Story
        with st.expander("Scenario"):
            st.write(scenario)
        with st.expander("Story"):
            st.write(story)

        # Play Audio
        st.audio("audio.flac")

# Entry point for the script
if __name__ == "__main__":
    main()
