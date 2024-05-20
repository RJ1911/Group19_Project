# Core Pkgs
import streamlit as st 
from JobRecommendation.side_logo import add_logo
from JobRecommendation.sidebar import sidebar
import altair as alt
import plotly.express as px 
from streamlit_extras.switch_page_button import switch_page
from JobRecommendation.lottie_animation import load_lottieurl
# EDA Pkgs
import pandas as pd 
import numpy as np 
from datetime import datetime
from streamlit_lottie import st_lottie


st.set_page_config(layout="centered", page_icon='logo/logo2.png', page_title="HOMEPAGE")



url = load_lottieurl("https://assets5.lottiefiles.com/private_files/lf30_m075yjya.json")

# add_logo()
# sidebar()


st.markdown("<h1 style='text-align: center; font-family: Verdana, sans-serif; padding: 20px; border: 2px solid #758283; border-radius: 5px;'>Welcome!</h1>", unsafe_allow_html=True)

