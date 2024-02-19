import streamlit as st
from PIL import Image

def load_custom_css():
    st.markdown("""
        <style>
        .sidebar .sidebar-content {
            background-color: #F0F2F6;
        }
        .upload-btn, .custom-btn {
            display: block;
            margin: 10px 0px;
            padding: 10px;
            border-radius: 5px;
            border: 1px solid #ccc;
            cursor: pointer;
            text-align: center;
            background-color: #eee;
            color: #333;
        }
        .upload-btn:hover, .custom-btn:hover {
            background-color: #ddd;
        }
        /* Additional CSS for improvements */
        .stApp {
            background-color: #EFF3F6;
            color: #333;
        }
        .stButton>button {
            border: 1px solid #4CAF50;
            color: white;
            background-color: #4CAF50;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        </style>
    """, unsafe_allow_html=True)

def main():
    load_custom_css()
    
    st.title("Lead Ingestion and Risk Assessment App")

    # Sidebar
    st.sidebar.title("Navigation")

    # About section in the sidebar
    with st.sidebar.expander("About"):
        st.write("""
            This app streamlines the lead management process for Counter-Insider Threat (C-InT) analysts by automating the ingestion, processing, and preliminary risk assessment of leads from various sources.
            It's designed to be intuitive and user-friendly, making it easier for analysts to manage leads efficiently and effectively.
        """)

    # Option selection
    upload_option = st.sidebar.radio("Choose an upload option:", 
                                     ('None', 'Upload PDF', 'Social Media Post', 'Upload Image', 'Upload Video'))
    
    # Implement the rest of your app logic here

    
    # Reset option
    if st.sidebar.button('Reset Selection'):
        # This resets the selected option to 'None'
        st.session_state.upload_option = 'None'
    
    # Conditional display based on selection
    if upload_option == 'Upload PDF':
        pdf_file = st.sidebar.file_uploader("Upload PDF", type=['pdf'])
        if pdf_file:
            st.success("PDF uploaded successfully!")
            # PDF processing logic here
            
    elif upload_option == 'Social Media Post':
        social_media_post = st.sidebar.text_area("Paste your social media post", height=100)
        if social_media_post:
            st.success("Social media post captured!")
            # Social media post processing logic here
            
    elif upload_option == 'Upload Image':
        image_file = st.sidebar.file_uploader("Upload Image", type=['jpg', 'jpeg', 'png'])
        if image_file:
            image = Image.open(image_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)
            st.success("Image uploaded successfully!")
            # Image processing logic here
            
    elif upload_option == 'Upload Video':
        video_file = st.sidebar.file_uploader("Upload Video", type=['mp4', 'mov', 'avi', 'mpeg'])
        if video_file:
            file_details = {"FileName": video_file.name, "FileType": video_file.type, "FileSize": video_file.size}
            st.write(file_details)
            st.success("Video uploaded successfully!")
            # Video processing logic here

    # Ensure that the upload_option is stored in session state for reset functionality
    if upload_option != 'None':
        st.session_state.upload_option = upload_option

    # Analyze Risk and Generate Report buttons remain the same

if __name__ == "__main__":
    main()
