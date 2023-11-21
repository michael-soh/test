import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

st.subheader("Hi, I am Michael :wave:")
st.title("I am a Programmer")
st.write(
    "I am looking for ways to use Python to solve business problems.")
st.write("[Contact Me](https://www.instagram.com/mike.szh/)")

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_coding = load_lottieurl("https://lottie.host/2e884639-ec85-4043-81ca-7c61198fce26/xyngItoH2R.json")
img_lottie_animation = Image.open(requests.get("https://media.istockphoto.com/id/1179235120/photo/athletic-woman-climbing-on-overhanging-cliff-rock-with-sunset-sky-background.jpg?s=2048x2048&w=is&k=20&c=2LxasRuFEeF_b-JUJkFZLG7rUEsK1vORT0adrBemY4E=", stream=True).raw)
# img_lottie_animation1 = Image.open("abc.jpg")
size = (480, 343)
img_lottie_animation = img_lottie_animation.resize(size) ### EDITED LINE

st.write("---") # adds a line across the screen
left_column, right_column = st.columns(2)
with left_column:
    st.header("What I do")
    st.write("##")  # adds a gap
    st.write(
            """
            I am a programmer who:
            - looks for a way to leverage the power of Python.
            - love challengers.
            - believe that everyone can learn Programming.
            - strive to be a better self.

            """
    )
with right_column:
    st_lottie(lottie_coding, height=300)


st.write("---")
st.header("My Photos")
st.write("##")
left_column1, right_column1, left_column2, right_column2 = st.columns(4)
with left_column1:
    st.image(img_lottie_animation, width=300, use_column_width=True)
with left_column2:
    st.image(img_lottie_animation, width=300, use_column_width=True)
with right_column1:
    st.image(img_lottie_animation, width=300,use_column_width=True)
with right_column2:
    st.image(img_lottie_animation, width=300, use_column_width=True)