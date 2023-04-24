import streamlit as st
import webbrowser
from streamlit_extras.colored_header import colored_header
from streamlit_lottie import st_lottie
import requests
from streamlit_extras.app_logo import add_logo
import streamlit_analytics

streamlit_analytics.start_tracking()
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
    label="Kurrikulum en SGA Afhandelings Instrumente:",
    description="U kan hierdie dokumente aflaai en stoor op u toestel vir toekomstige gebruik:.",
    color_name="blue-70",
)

lottie_coding = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_uqsv3ztj.json")

# Here is the title of the page
st.write("Klik hieronder vir SGA en KURR. AFHANDELINGS INSTRUMENTE")


st.write("[KLIK HIER](https://drive.google.com/drive/folders/1pi7vv0BvG5-s9o-j27jFWoiXI82Agarg?usp=share_link)")

st_lottie(lottie_coding, height = 200 , key="coding")


streamlit_analytics.stop_tracking()




