from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from  streamlit import st
from langchain_core.prompts import PromptTemplate, load_prompt
load_dotenv()
model = ChatAnthropic()

st.header("research Tool")
paper_input = st.selectbox(" Select Research paper Name", ["Attention is All you Need", "BERT: Pre-training on DEEP Bidirectional transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"])

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

template = load_prompt('template.json')

if st.button('summarize'):
    chain = template | model
    result = chain.invoke({
        "paper": paper_input,
        "style": style_input,
        "length": length_input
    })
    st.write(result.content)