import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="christopherkurdoghlian", page_icon=":evergreen_tree:", layout="wide")

with st.sidebar:
    linkedin_url = "https://www.linkedin.com/in/christopher-kurdoghlian-77b20927a/"
    st.markdown(f'<a href="{linkedin_url}" target="_blank" style="text-decoration: none; color: inherit;"><img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="25" height="25" style="vertical-align: middle; margin-right: 10px;">`LinkedIn`</a>', unsafe_allow_html=True)
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


img_flower = Image.open("images/flower.png")
img_christopher = Image.open("images/chris.JPG")


if selected == "Home":
    # ---- HEADER SECTION ----
    with st.container():
        st.title("Welcome to the website of Christopher Kurdoghlian")
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
        st.image(img_christopher, width = 300)

if selected == "Contact":
    with st.container():
        st.title("Contact")

        left_column, right_column = st.columns(2)
        with left_column:
            st.write('<a href="christopherkurdoghlian@gmail.com">christopherkurdoghlian@gmail.com</a>', unsafe_allow_html=True)
        with right_column:
            st.image(img_flower, width = 500)

if selected == "Projects":
    st.title("Projects")
    st.write("""Here are some of the projects I have worked on over the years.""")
    with st. container(): st.write("---")
    left_column, middle_column, right_column = st.columns(3)
    with left_column:
        st.header ("Physics Game")
        st.write(
            """
            This was a game I wrote in javascript using my knowledge of physics. See how many points you can score!
            """
        )
    with middle_column:
        st.header ("3D rendering")
        st.write(
            """
            This was a 3-D rendering project I worked on when I was interested in computer graphics. It uses webgl2.
            """
        )
        st.write('<a href="christopherk26.github.io">3D rendering demonstration</a>', unsafe_allow_html=True)
        
    with right_column:
        st.header ("Black-Scholes Options pricing")
        st.write(
            """
            I have been interested in finance and markets since 2019 and eventually learned about quantitative finance. 
            This project shows how option contracts vary in price based on the parameters of the Black-Scholes equation.
            """
        )