import streamlit as st
import os

# Create a directory to store the uploaded pictures
if not os.path.exists('pictures'):
    os.makedirs('pictures')

# Define the function to upload pictures
def upload_picture():
    picture = st.file_uploader('Upload a picture', type=['jpg', 'jpeg', 'png'])
    if picture is not None:
        # Save the picture to the pictures directory
        with open(os.path.join('pictures', picture.name), 'wb') as f:
            f.write(picture.getbuffer())
        st.success('Picture uploaded successfully!')

# Define the function to delete pictures
def delete_picture(picture_path):
    os.remove(picture_path)
    st.success('Picture deleted successfully!')

# Define the function to display pictures and comments
def display_picture(picture_path, comments):
    # Display the picture
    st.image(picture_path, use_column_width=True)

    # Display the comments
    for comment in comments:
        st.write(comment)

# Define the main function
def main():
    # Check if the user is the administrator
    if 'is_admin' not in st.session_state:
        st.session_state['is_admin'] = False

    if not st.session_state['is_admin']:
        # Prompt the administrator to log in
        username = st.text_input('Username:')
        password = st.text_input('Password:', type='password')
        if username == 'admin' and password == 'password':
            st.session_state['is_admin'] = True
        else:
            st.warning('Incorrect username or password.')

    if st.session_state['is_admin']:
        # Allow the administrator to upload pictures
        upload_picture()

    # Get the list of pictures in the pictures directory
    pictures = os.listdir('pictures')

    if len(pictures) == 0:
        st.warning('No pictures uploaded yet!')
    else:
        # Display each picture and its comments
        for picture in pictures:
            # Get the picture path
            picture_path = os.path.join('pictures', picture)

            # Get the comments for the picture
            comments = st.session_state.get(picture_path, [])
            new_comment = st.text_input(f'Leave a comment for {picture}:')
            if new_comment:
                comments.append(new_comment)
                st.session_state[picture_path] = comments

            # Display the picture and comments
            display_picture(picture_path, comments)

            if st.session_state['is_admin']:
                # Allow the administrator to delete pictures
                if st.button(f'Delete {picture}'):
                    delete_picture(picture_path)

if __name__ == '__main__':
    main()
