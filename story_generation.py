# Importing necessary classes from the 'langchain' package
from langchain.chat_models import ChatOpenAI as OpenAI
from langchain import PromptTemplate, LLMChain

# Define a function called 'generate_story' that takes a scenario string as input
def generate_story(scenario):
    """
    Generate a short funny story based on a given scenario using the OpenAI GPT-3.5 Turbo model.
    
    Parameters:
    scenario (str): The scenario or context for the story.
    
    Returns:
    str: The generated story text.
    """
    
    # Define a template for the story prompt
    # The template has a CONTEXT section to specify the scenario
    template = """You are a funny story teller;
    you can generate a short funny story of less than 100 words based on a simple narrative;
    CONTEXT : {scenario}
    STORY:"""
    
    # Create a PromptTemplate object using the defined template
    prompt = PromptTemplate(template=template, input_variables=["scenario"])
    
    # Initialize the LLMChain object with the OpenAI GPT-3.5 Turbo model and the prompt
    story_llm = LLMChain(llm=OpenAI(model_name="gpt-3.5-turbo", temperature=1), prompt=prompt, verbose=True)
    
    # Generate the story using the predict method of the LLMChain object
    # The 'verify' parameter is set to False, meaning the prompt won't be verified before sending to the model
    story = story_llm.predict(scenario=scenario, verify=False)
    
    # Return the generated story
    return story
