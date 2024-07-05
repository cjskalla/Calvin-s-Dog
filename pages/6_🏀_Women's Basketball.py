import streamlit as st
import pandas as pd

#Page Configuration
page = st.set_page_config(page_icon=":basketball:", 
                layout="wide"
                )

#Title
st.markdown(
        """
        <h3 style="
            text-align: center;
            font-family: Forum;
            font-weight: 400;
            font-size: 300%;
            ">
            Women's Basketball
        </h1>
        """,
        unsafe_allow_html=True
    )


#About
st.markdown("""
            <p
            style="
                text-align: center;
                padding-top: 0px;
                padding-bottom: -100px
                color: rgb(102, 67, 70);
            ">
                Learn about the Women's Basketball through Data !!
            </p>
            """,
            unsafe_allow_html=True
        )


#C 2024
st.markdown("""
            <p
            style="
                text-align: center;
                padding-top: 50px;
                padding-bottom: -100px
                color: rgb(102, 67, 70);
            ">
                <em>© 2024 </em>
            </p>
            """,
            unsafe_allow_html=True
        )
