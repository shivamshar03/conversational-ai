import streamlit as st
from streamlit_chat import message
from langchain_groq import ChatGroq
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationSummaryMemory

st.set_page_config(page_title="Chat GPT Clone", page_icon=":robot_face:")
st.markdown("<h1 style='text-align: center;'>How can I assist you? </h1>", unsafe_allow_html=True)
st.sidebar.title("😎 Your Assistant")

# Session State Vriables
if 'conversation' not in st.session_state:
    st.session_state['conversation'] = None
if 'messages' not in st.session_state:
    st.session_state['messages'] = []
if 'API_Key' not in st.session_state:
    st.session_state['API_Key'] = ''

#Sidebar Inputs
st.session_state['API_Key'] = st.sidebar.text_input("Enter your Groq API key", type="password")

summarise_button = st.sidebar.button("Summarise the Conversation")
reset_button = st.sidebar.button("Reset Conversation")

if summarise_button:
    if st.session_state['conversation'] is not None:
        st.sidebar.write("❤️ Summary of conversation:\n\n" + st.session_state['conversation'].memory.buffer)
    else:
        st.sidebar.warning("No conversation to summarise!")

if reset_button:
    st.session_state['conversation'] = None
    st.session_state['messages'] = []
    st.sidebar.success("Conversation reset!")

# Function to Get Response
def getresponse(user_input, api_key):
    if not api_key:
        return "⚠️ Please provide a valid API key."

    try:
        if st.session_state['conversation'] is None:
            llm = ChatGroq(
                temperature=0,
                model_name="llama3-8b-8192",
                api_key=api_key
            )
            st.session_state['conversation'] = ConversationChain(
                llm=llm,
                verbose=True,
                memory=ConversationSummaryMemory(llm=llm)
            )

        response = st.session_state['conversation'].predict(input=user_input)
        return response
    except Exception as e:
        return f"⚠️ An error occurred: {str(e)}"

#Chat Interface
response_container = st.container()
input_container = st.container()

with input_container:
    with st.form(key='chat_form', clear_on_submit=True):
        user_input = st.text_area("Your message:", key='input', height=100)
        submit_button = st.form_submit_button(label='Send')

        if submit_button and user_input.strip():
            st.session_state['messages'].append(user_input)
            model_response = getresponse(user_input, st.session_state['API_Key'])
            st.session_state['messages'].append(model_response)


with response_container:
    for i, msg in enumerate(st.session_state['messages']):
        if i % 2 == 0:
            message(msg, is_user=True, key=f"user_{i}")
        else:
            message(msg, key=f"ai_{i}")
