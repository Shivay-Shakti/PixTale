import streamlit as st
from env_config import load_environment
from image_to_text import image2text
from story_generation import generate_story
from text_to_speech import text2speech

load_environment()

def main():
    # Set the page configuration using Streamlit
    st.set_page_config(page_title="Visual Story Generator", page_icon="🧊", layout="centered", initial_sidebar_state="expanded")

    # Add a header to the Streamlit app
    st.header("Your Image Into Story")

    # Upload file using Streamlit's file_uploader widget
    uploaded_file = st.file_uploader("Choose an image...", type="jpg")

    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Print the uploaded file object to the console (mostly for debugging)
        print(uploaded_file)

        # Read the uploaded file as bytes
        bytes_data = uploaded_file.getvalue()

        # Write the bytes data to a local file
        with open("uploaded_image.jpg", "wb") as f:
            f.write(bytes_data)

        # Display the uploaded image using Streamlit
        st.image(bytes_data, caption='Uploaded Image.', use_column_width=True)

        # Assume image2text and generate_story are functions you've defined elsewhere
        scenario = image2text("uploaded_image.jpg")
        story = generate_story(scenario)

        # Convert the story to speech (using the text2speech function you've defined elsewhere)
        text2speech(story)

        # Display the scenario and story in expandable sections
        with st.expander("scenario"):
            st.write(scenario)
        with st.expander("story"):
            st.write(story)

        # Play the generated audio
        st.audio("audio.flac")


# Entry point for the script
if __name__ == "__main__":
    main()
