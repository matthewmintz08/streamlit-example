import streamlit as st
import pandas as pd
from io import StringIO
import ezdxf

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    doc = ezdxf.readfile(uploaded_file)
