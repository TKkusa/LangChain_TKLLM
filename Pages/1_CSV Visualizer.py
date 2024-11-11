import streamlit as st
import pandas as pd

# Title of the app
st.title('CSV File Visualizer')

# Create a drag-and-drop file uploader
uploaded_file = st.file_uploader('Drag and drop a CSV file here or choose from your desktop', type='csv')

if uploaded_file is not None:
    # Add a button to upload and process the file
    if st.button('Upload and Visualize'):
        # Read the CSV file into a pandas DataFrame
        data = pd.read_csv(uploaded_file)
        st.write(data)
else:
    st.write('Please upload a CSV file to proceed.')


