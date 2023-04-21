import streamlit as st 
import webbrowser

# Here is the title of the page
st.title("Klik hier onder vir SGA en KURR. AFHANDELING")

# Define the URL that the button should redirect to
url = "https://drive.google.com/drive/folders/1pi7vv0BvG5-s9o-j27jFWoiXI82Agarg?usp=share_link"

# Create a button with a label "Go to Example.com"
if st.button("KLIK HIER"):
    webbrowser.open_new_tab(url)






