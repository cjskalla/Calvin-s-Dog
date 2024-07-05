import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import zscore


#Page Configuration
page = st.set_page_config(page_icon=":chart_with_upwards_trend:", 
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


tab = st.tabs(["💲 Crypto", "📈 Stocks", "💰 Private Investments"])

#Breakout Financial
with tab[0]:

    crypto_tab = st.tabs(["💲 Bitcoin", "💲 Etherum"])

    #Breakout Crypto
    with crypto_tab[0]:

        #Bitcoin Title
        st.markdown(
                """
                <h3 style="
                    text-align: center;
                    font-family: Forum;
                    font-weight: 400;
                    font-size: 200%;
                    ">
                    Bitcoin
                </h1>
                """,
                unsafe_allow_html=True
            )

        #Bring in the BTC Data
        df = pd.read_csv("BTCHistory.csv")


        # Plotting
        figure, ax = plt.subplots()
        figure.patch.set_facecolor('white')  # Set the figure background color to white

        figure = ax.plot(df['Date'], df['Volume(M)'], label = 'Volume(M)')
        figure = ax.plot(df['Date'], df['Close'], label = 'Close')

        # Adding labels and title
        figure = ax.set_xlabel('Date')
        figure = ax.set_ylabel('Amount')
        figure = ax.set_title('Line Chart of Metrics Over Time')
        figure = ax.legend(title='Metric')
        figure = ax.grid(True)


        st.pyplot(fig=figure,
                  use_container_width=False)

        st.table(df)

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
