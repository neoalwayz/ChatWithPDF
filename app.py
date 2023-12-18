import streamlit as st
#import 

def main():
    st.set_page_config(page_title="Chat with Your Own PDFs", page_icon=":chat:")
    st.header("Chat with Your Own PDFs :books:")
    st.text_input("Ask question in context of the Document:")
    
    with st.sidebar:
        st.subheader("Your Documents")
        st.file_uploader("Upload Your PDFs here and Click on Process")
        st.button("Process")

if __name__ == '__main__':
    main()
    