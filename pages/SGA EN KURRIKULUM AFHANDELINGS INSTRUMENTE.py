import streamlit as st
import webbrowser

# Here is the title of the page
st.title("Klik hier onder vir SGA en KURR. AFHANDELING")

if st.button("KLIK HIER"):
    # Open the link in a new tab
    webbrowser.open_new_tab("https://drive.google.com/drive/folders/1pi7vv0BvG5-s9o-j27jFWoiXI82Agarg?usp=share_link")
    st.success("Jou versoek was suksesvol!")








