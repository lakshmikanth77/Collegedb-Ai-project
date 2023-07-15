# import streamlit as st
# from openai_helper import get_answer

# st.title("College database generative query system")

# question = st.text_input("Question:")

# if question:
#     answer = get_answer(question)
#     st.text("Answer:")
#     st.write(answer)

import streamlit as st
from openai_helper import get_answer

# Set the page configuration
st.set_page_config(page_title="College DB Query System", 
                   page_icon="🎓", 
                   layout="wide", 
                   initial_sidebar_state="collapsed")

st.title("College database generative Ai system")

# Add a sidebar for input
with st.sidebar:
    st.header("Ask a Question")
    st.write("Please input your question related to the college database in the text box below:")
    question = st.text_input("")

# Check if the text box isn't empty before getting the answer
if question:
    answer = get_answer(question)

    # Use markdown for displaying answer
    st.markdown("---") # Horizontal line
    st.subheader("Answer:")
    st.markdown(answer)
else:
    st.warning('Please input a question in the sidebar.')

