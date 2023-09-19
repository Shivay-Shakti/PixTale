from langchain.chat_models import ChatOpenAI as OpenAI
from langchain import PromptTemplate, LLMChain

def generate_story(scenario):
    template = """You are a funny story teller;
    you can generate a short funny story of less than 100 words based on a simple narrative;
    CONTEXT : {scenario}
    STORY:"""  
    prompt = PromptTemplate(template=template, input_variables=["scenario"])
    story_llm = LLMChain(llm=OpenAI(model_name="gpt-3.5-turbo", temperature=1), prompt=prompt, verbose=True)
    story = story_llm.predict(scenario=scenario, verify=False)
    return story

