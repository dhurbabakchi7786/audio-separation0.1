import streamlit as st

st.title('Audio Separation')


uploaded_file = st.file_uploader("Choose an audio file", type=['wav', 'mp3'])

if uploaded_file is not None:
    
    st.success('File Retain Successfully')

    st.subheader('Original Audio')
    st.audio(uploaded_file)

    st.subheader('Processed Audio')
    if st.button('Start Processing'):
        
        st.write('Processing... please wait...')
