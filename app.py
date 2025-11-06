import streamlit as st
import pandas as pd
import plotly.express as px

# --- Título del dashboard ---
st.header("🚗 Dashboard de anuncios de autos.")

# --- Cargar los datos ---
car_data = pd.read_csv('vehicles_us.csv')

# --- Mostrar información general ---
st.write("Panel interactivo que permite explorar los datos de anuncios de vehículos. Puedes visualizar la distribución del odómetro y la relación entre precio y año del vehículo.")

# --- Creacion de histograma con Checkbook ---
build_hist = st.checkbox('Mostrar histograma del odómetro')
if build_hist:
    st.write("Creación de un histograma para el odómetro.")
    fig = px.histogram(car_data, x="odometer", title="Distribución del odómetro")
    st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox('Mostrar gráfico de dispersión (Precio vs Año)')
if build_scatter:
    st.write("Creación de un gráfico de dispersión: precio vs año del vehículo.")
    fig2 = px.scatter(car_data, x="model_year", y="price", color="condition", title="Precio vs Año del vehículo")
    st.plotly_chart(fig2, use_container_width=True)