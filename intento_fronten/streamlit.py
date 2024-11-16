import streamlit as st
import pandas as pd

# Título
st.title("Formación de Grupos - Datathon")

# Subida de archivo con datos de participantes
st.sidebar.header("Carga de Datos")
archivo = st.sidebar.file_uploader("Sube un archivo CSV con los datos de los participantes", type=["csv"])

if archivo:
    # Leer y mostrar los datos
    datos = pd.read_csv(archivo)
    st.write("Datos cargados:")
    st.dataframe(datos)

    # Simulación: Formar grupos (puedes integrar aquí el código de tus compañeros)
    st.header("Grupos Formados")
    num_grupos = len(datos) // 4
    grupos = [datos.iloc[i * 4: (i + 1) * 4] for i in range(num_grupos)]
    
    # Mostrar grupos
    for i, grupo in enumerate(grupos):
        st.subheader(f"Grupo {i + 1}")
        st.dataframe(grupo)
else:
    st.write("Por favor, sube un archivo para comenzar.")
