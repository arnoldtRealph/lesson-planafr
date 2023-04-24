import streamlit as st
import webbrowser
from streamlit_extras.colored_header import colored_header
from streamlit_lottie import st_lottie
import requests
from streamlit_extras.app_logo import add_logo


# add app logo
add_logo("IMAGES/wapen.png", height=150)

# Define lottie url
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# using streamlit extras colored reader
colored_header(
    label="BRIEFHOOF",
    description="U kan hierdie dokument aflaai en stoor op u toestel vir toekomstige gebruik:.",
    color_name="blue-70",
)

lottie_coding = load_lottieurl("https://assets8.lottiefiles.com/private_files/lf30_odansovk.json")

# Here is the title of the page
st.write("Klik hieronder die BRIEFHOOF")


st.write("[KLIK HIER](https://drive.google.com/drive/folders/1j2aw8V6ySOmlVPODERkvBEU39o7ydAXC?usp=share_link)")

st_lottie(lottie_coding, height = 200 , key="coding")







