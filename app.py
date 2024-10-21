import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmltemplates import css, user_template, bot_template
from langchain_community.llms import HuggingFaceHub

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_chunks(raw_text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=500,
        chunk_overlap=100,
        length_function=len
    )
    chunks = text_splitter.split_text(raw_text)
    return chunks

@st.cache_data
def get_vectorstore(text_chunks):
    #embeddings = OpenAIEmbeddings()
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

def get_conv_chain(vectorstore):
    #llm=ChatOpenAI()
    llm = HuggingFaceHub(repo_id="google/flan-t5-base", model_kwargs={"temperature":0.5, "max_length":512})
    memory=ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conv_chain=ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory 
    )
    return conv_chain

def handle_user_input(user_input):
    response=st.session_state.conv({'question': user_input})
    st.session_state.chat_history=response['chat_history']
    for i,message in enumerate(st.session_state.chat_history):
        if i%2==0:
            st.write(user_template.replace("{{MSG}}",message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace("{{MSG}}",message.content), unsafe_allow_html=True)

def main():
    load_dotenv()
    st.set_page_config(page_title="Multi-PDF Interaction Chatbot", page_icon="icon.jpg")
    st.write(css, unsafe_allow_html=True)

    if "conv" not in st.session_state:
        st.session_state.conv=None
        st.session_state.chat_history=[]

    st.header("Chat with multiple PDFs :books:")
    user_question = st.text_input("Ask any question about your document(s)")
    if user_question:
        handle_user_input(user_question)


    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader("Upload your documents here and click on 'Process'", accept_multiple_files=True)
        if st.button("Process"):
            if pdf_docs:
                with st.spinner("Processing..."):
                    try:
                        # Extract text from PDFs
                        raw_text = get_pdf_text(pdf_docs)
                        print("raw text generated")
                            
                        # Split text into chunks
                        text_chunks = get_chunks(raw_text)
                        print("text chunk")
                                            
                        # Create vector store from text chunks
                        vectorstore = get_vectorstore(text_chunks)
                        print("vectorstore")
                        
                        # Create conversation chain
                        st.session_state.conv=get_conv_chain(vectorstore)
                        print("conv chain")

                    except Exception as e:
                        st.error(f"An error occurred: {str(e)}")

           


if __name__ == "__main__":
    main()
