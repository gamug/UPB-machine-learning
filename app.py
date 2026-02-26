import folium
import streamlit as st
import streamlit.components.v1 as components
from streamlit_folium import st_folium


import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from src.utils import get_config_vars, get_metrics_plot, charge_models
from src.datasets import get_dataset_data
from src.model import apply_model

st.set_page_config(
    page_title="Salinidad del agua subterranea"
)
if 'pipeline' not in st.session_state:
    st.session_state.le, st.session_state.pipeline = charge_models('DecisionTree')
if "last_option" not in st.session_state:
    st.session_state.last_option = None


config_vars = get_config_vars()

page = st.sidebar.radio("Salinity Model", config_vars['pages'])

if page == "Readme":
    st.markdown(config_vars['readme'], unsafe_allow_html=True)
if page == "Model":
    model = st.sidebar.selectbox("Model", config_vars['models'])
    st.sidebar.dataframe(config_vars['model_metrics'])
    m = folium.Map(location=[11.5, -73.0], zoom_start=8)
    # Añadir herramienta de popup de coordenadas
    m.add_child(folium.LatLngPopup())
    # Renderizar mapa y capturar eventos
    output = st_folium(m, width=800, height=500)
    if st.session_state.last_option != model:
        st.session_state.last_option = model
        st.session_state.le, st.session_state.pipeline = charge_models(model)
    # Mostrar categoría de sal
    if output["last_clicked"]:
        lat = output["last_clicked"]["lat"]
        lon = output["last_clicked"]["lng"]
        salt_category = apply_model(st.session_state.pipeline, st.session_state.le, lat, lon)
        st.markdown(f"## {salt_category}")
if page == "Model Metrics":
    model1 = st.sidebar.selectbox("Model1", config_vars['models'])
    st.sidebar.markdown("Comparar contra")
    model2 = st.sidebar.selectbox("Model2", config_vars['models'])
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"## Métricas en validación cruzada para el modelo {model1}")
        st.markdown("### Curva ROC")
        components.html(get_metrics_plot(model1, 'roc'), height=417, width=400, scrolling=True)
        st.markdown("### Curva Violín")
        components.html(get_metrics_plot(model1, 'violin'), height=417, width=400, scrolling=True)
    with col2:
        st.markdown(f"## Métricas en validación cruzada para el modelo {model2}")
        st.markdown("### Curva ROC")
        components.html(get_metrics_plot(model2, 'roc'), height=417, scrolling=True)
        st.markdown("### Curva Violín")
        components.html(get_metrics_plot(model2, 'violin'), height=417, scrolling=True)
if page == "Data":
    html = '<p>Para consultar más detalle sobre el pipeline de procesamiento de datos remitirse al <a href="https://github.com/gamug/guajira-salinity">repositorio de GitHub</a></p>'
    st.markdown(html, unsafe_allow_html=True)
    dataset = st.sidebar.selectbox("Dataset", config_vars['datasets'])
    show = st.sidebar.selectbox("Show", config_vars['datasets_disposables'])
    disposable = get_dataset_data(dataset, show)
    if show=='Data':
        st.dataframe(disposable)
    elif show=='Profiling':
        components.html(disposable, height=800, scrolling=True)