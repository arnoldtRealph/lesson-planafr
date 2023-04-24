import streamlit as st
import pandas as pd
import os

def main():
    st.set_page_config(page_title="School Photos")
    
    # create directory for photos and comments if they don't exist
    if not os.path.exists("photos"):
        os.makedirs("photos")
    if not os.path.exists("comments"):
        os.makedirs("comments")
    
    # list all the uploaded photos
    photos = os.listdir("photos")
    
    # display all the uploaded photos and their comments
    for file in photos:
        st.image(f"photos/{file}", use_column_width=True, caption=file.split(".")[0])
        comment_file = f"comments/{file}.csv"
        if os.path.exists(comment_file):
            comments = pd.read_csv(comment_file, header=None)
            for comment in comments[0]:
                st.write(comment)
        else:
            st.write("No comments yet.")
    
    # allow the administrator to upload a new photo
    uploaded_file = st.file_uploader("Upload a photo", type=["png", "jpg"])
    if uploaded_file is not None:
        file_path = f"photos/{uploaded_file.name}"
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success("Photo uploaded successfully.")
        
    # allow users to leave a comment on a photo
    comment = st.text_input("Leave a comment")
    file = st.selectbox("Select a photo to comment on", photos)
    if st.button("Submit", key=f"{file}-comment") and comment != "":
        comment_file = f"comments/{file}.csv"
        with open(comment_file, "a") as f:
            f.write(comment + "\n")
        st.success("Comment submitted successfully.")
    
if __name__ == "__main__":
    main()
