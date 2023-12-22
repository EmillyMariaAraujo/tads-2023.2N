import streamlit as st
from plot.interactive import plot_line_1

st.title ('Strack Price App')

# Sidebar
st.sidebar.header('User')
symbol = st.sidebar.text_input('Escolha um ativo:', 'AAPL ')

# Plot
fig= plot_line_1(symbol)
st.plotly_chart(fig)