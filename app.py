import streamlit as st
import folium
from streamlit.components.v1 import html

# Título do aplicativo
st.title('Mapa com Folium no Streamlit')

# Criar o mapa
m = folium.Map(location=[-23.5505, -46.6333], zoom_start=12)

# Adicionar um marcador
folium.Marker(
    location=[-23.5505, -46.6333],
    popup='São Paulo',
    icon=folium.Icon(color='blue')
).add_to(m)

# Mostrar o mapa
map_html = m._repr_html_()
html(map_html, height=500)