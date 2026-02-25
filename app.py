
import streamlit as st
from datetime import datetime
import pytz

st.set_page_config(page_title="Mi Dashboard de Tiempo", page_icon="⏰")

st.title("⏰ Dashboard de Fecha y Hora")
st.write("Esta aplicación muestra la información temporal en tiempo real.")

# Selección de Zona Horaria (opcional, por defecto local)
timezone = st.selectbox("Selecciona tu zona horaria:", pytz.all_timezones, index=pytz.all_timezones.index('America/Santiago'))

# Obtener datos
now = datetime.now(pytz.timezone(timezone))
fecha_actual = now.strftime("%d/%m/%Y")
hora_actual = now.strftime("%H:%M:%S")

# Mostrar en columnas bonitas
col1, col2 = st.columns(2)

with col1:
    st.metric(label="Fecha Actual", value=fecha_actual)

with col2:
    st.metric(label="Hora Local", value=hora_actual)

st.divider()
st.write("Tip: Refresca la página para actualizar la hora.")
