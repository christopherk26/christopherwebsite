import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="christopherkurdoghlian", page_icon=":evergreen_tree:", layout="wide")

with st.sidebar:
    selected = option_menu (
        menu_title = None,
        options=["Home", "Projects", "Contact"],
        default_index = 0,
        icons = [" ", " ", " "],
        #orientation = "horizontal",
    )

# hide_streamlit_style = """
# <style>
#     #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0rem;}
# </style>

# """
# st.markdown(hide_streamlit_style, unsafe_allow_html=True)


def local_css (file_name):
    with open (file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

img_christopher = Image.open("images/christopher.png")


if selected == "Home":
    # ---- HEADER SECTION ----
    with st.container():
        st.title("Welcome to the offical website of Christopher Kurdoghlian")
    # st.write("""
    #         Christopher Kurdoghlian is currently a Student at California Polytechnic State University Pomona, (CPP), and is studying
    #         Computer Science and minoring in Data Science. He currently resides in La Canada, California. Christopher has two sibilings,
    #         Sarah and Kevork. Christopher enjoys biking, running, LEGO, yoga, reading, and podcasts. 
    #          """)

    with st. container(): st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header ("About")
        st.write(
            """
            Christopher Kurdoghlian is currently a Student at California Polytechnic State University Pomona, (CPP), studying
            Computer Science and minoring in Data Science. He currently resides in La Canada, California. Christopher has two sibilings,
            Sarah and Kevork. Christopher enjoys biking, running, LEGO, yoga, reading, and podcasts. Christopher has included a contact page
            and a page for viewing some of the various projects he has worked on.
            """
        )

    with right_column:
        st.image(img_christopher, width = 400)