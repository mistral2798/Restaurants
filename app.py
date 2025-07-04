import streamlit as st
import pandas as pd

rest = pd.read_excel('rest.xlsx')
rest['Итог'] = rest['Итог'].round(1)
rest['Дата посещения'] = rest['Дата посещения'].dt.to_period('D')
st.title('Витрина посещенных ресторанов')

st.dataframe(rest, hide_index=True, use_container_width=True)