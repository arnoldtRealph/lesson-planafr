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

# using streamlit extras colored eader
colored_header(
    label="PRE-AND POST MODERATION TOOL:",
    description="U kan hierdie dokument aflaai en stoor op u toestel vir toekomstige gebruik:.",
    color_name="yellow-70",
)
lottie_coding = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_VAj8qSTBG9.json")

# Here is the title of the page
st.write("Klik hieronder om die dokumente af te laai:")


st.write("[KLIK HIER](https://drive.google.com/drive/folders/1HGDkPeJgMlTLYuYpj28Wy_-t_S8aHVfz?usp=share_link)")

st_lottie(lottie_coding, height = 200 , key="coding")


