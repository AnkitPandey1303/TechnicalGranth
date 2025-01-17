import streamlit as st

st.title('Welcome to Technical Granth')
st.header('This channel is specially created for all those who are eager to learn about software, the latest technology, and technical updates. On our channel, you’ll find videos on the following topics:')
st.subheader('Welcome to Python Quiz')

name = st.text_input('Enter your Name') # text_input() function is used to take input from the user
fname = st.text_input('Enter your Father name') # text_input() function is used to take input from the user
address = st.text_area('Enter your Comments') # text_area() function is used to take input from the user
classdata = st.selectbox('Select your Class', ['5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', 'BCA', 'Btech',]) # selectbox() function is used to create a dropdown list
button = st.button('Submit') # button() function is used to create a button
if button:
    st.markdown(f"""
Name : {name}
Father Name : {fname}
Address : {address}
Class : {classdata}
    """)
