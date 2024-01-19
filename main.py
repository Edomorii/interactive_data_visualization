import streamlit as st
import pandas as pd
import plotly.express as px

def interactive():
    # INTERACTIVE CHART, source : https://finance.yahoo.com/quote/NESN.SW/history?p=NESN.SW
    nestle_data = pd.read_csv('NESN.SW.csv')
    
    nestle_data['Date'] = pd.to_datetime(nestle_data['Date'])
    fig = px.line(nestle_data, x='Date', y='Adj Close', title='Nestlé S.A. Stock Price')

    fig.update_traces(mode='lines', hoverinfo='x+y')

    fig.update_layout(
        xaxis_title='Date',
        yaxis_title='Close Price (CHF)',
        xaxis_fixedrange=True,
        yaxis_fixedrange=True,
        plot_bgcolor='white',   
        paper_bgcolor='white',  
        xaxis_showgrid=False,   
        yaxis_showgrid=False,
        xaxis_linecolor='black', 
        yaxis_linecolor='black', 
        xaxis_ticks='outside',  
        yaxis_ticks='outside' 
    )

    st.plotly_chart(fig)

if __name__ == "__main__":
    interactive()
