import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

st.markdown(
        """
        <h3 style="
            text-align: center;
            font-family: Forum;
            font-weight: 400;
            font-size: 300%;
            ">
            General Financial Data
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
                Learn about Stocks and Cryptocurrency through Data !!
            </p>
            """,
            unsafe_allow_html=True
        )




# Define the connection parameters
server = 'CALVIN_PC\CALVINDATA'       # e.g., 'localhost' or 'server_name'
database = 'FinancialSpend'   # e.g., 'my_database'
username = 'CalvinHP'   # e.g., 'my_username'
password = 'HPlaptop2024!'   # e.g., 'my_password'
driver = 'ODBC Driver 17 for SQL Server'  # Make sure this matches the installed ODBC driver

# Create the connection string
connection_string = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}"

# Create the SQLAlchemy engine
engine = create_engine(connection_string)










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
