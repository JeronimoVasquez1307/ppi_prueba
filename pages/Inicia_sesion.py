"""Módulo con todo lo necesario para el inicio de sesión de un usuario
además de manejar el cierre de sesión"""

# importar las liberías requeridas
import streamlit as st # pip install streamlit
import gspread # pip install gspread
# pip install oauth2cliente
from streamlit import session_state
from oauth2client.service_account import ServiceAccountCredentials

# Título de la aplicación
st.title("Login")

# Formulario de login
correo = st.text_input("Correo")
contrasena = st.text_input("Contraseña", type="password")

def obtener_nombre_usuario(user_correo):
    """
    Obtiene el nombre de usuario correspondiente a un correo específico desde una hoja de Google Sheets.

    Parámetros:
    - user_correo (str): El correo del usuario cuyo nombre se desea obtener.

    Retorna:
    - str: El nombre del usuario si se encuentra, o None si el correo no se encuentra en la hoja.
    """

    # Configuración de autenticación y acceso a Google Sheets
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive.file"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    cliente = gspread.authorize(creds)
    hoja = cliente.open("Usuarios_bd").sheet1

    # Obtiene todos los datos de la hoja
    data = hoja.get_all_values()

    # Busca el nombre del usuario correspondiente al correo
    for row in data[1:]:  # Saltar la primera fila que son encabezados
        if row[5] == user_correo:  # Suponiendo que el correo está en la sexta columna
            return row[0]  # Suponiendo que el nombre está en la primera columna

    return None  # Si no se encuentra el correo en la hoja

def obtener_apellido_usuario(user_correo):
    """
    Obtiene el nombre de usuario correspondiente a un correo específico desde una hoja de Google Sheets.

    Parámetros:
    - user_correo (str): El correo del usuario cuyo nombre se desea obtener.

    Retorna:
    - str: El nombre del usuario si se encuentra, o None si el correo no se encuentra en la hoja.
    """

    # Configuración de autenticación y acceso a Google Sheets
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive.file"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    cliente = gspread.authorize(creds)
    hoja = cliente.open("Usuarios_bd").sheet1

    # Obtiene todos los datos de la hoja
    data = hoja.get_all_values()

    # Busca el nombre del usuario correspondiente al correo
    for row in data[1:]:  # Saltar la primera fila que son encabezados
        if row[5] == user_correo:  # Suponiendo que el correo está en la sexta columna
            return row[1]  # Suponiendo que el nombre está en la primera columna

    return None  # Si no se encuentra el correo en la hoja

def obtener_genero_usuario(user_correo):
    """
    Obtiene el nombre de usuario correspondiente a un correo específico desde una hoja de Google Sheets.

    Parámetros:
    - user_correo (str): El correo del usuario cuyo nombre se desea obtener.

    Retorna:
    - str: El nombre del usuario si se encuentra, o None si el correo no se encuentra en la hoja.
    """

    # Configuración de autenticación y acceso a Google Sheets
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive.file"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    cliente = gspread.authorize(creds)
    hoja = cliente.open("Usuarios_bd").sheet1

    # Obtiene todos los datos de la hoja
    data = hoja.get_all_values()

    # Busca el nombre del usuario correspondiente al correo
    for row in data[1:]:  # Saltar la primera fila que son encabezados
        if row[5] == user_correo:  # Suponiendo que el correo está en la sexta columna
            return row[5]  # Suponiendo que el nombre está en la primera columna

    return None  # Si no se encuentra el correo en la hoja

def obtener_fecha_usuario(user_correo):
    """
    Obtiene el nombre de usuario correspondiente a un correo específico desde una hoja de Google Sheets.

    Parámetros:
    - user_correo (str): El correo del usuario cuyo nombre se desea obtener.

    Retorna:
    - str: El nombre del usuario si se encuentra, o None si el correo no se encuentra en la hoja.
    """

    # Configuración de autenticación y acceso a Google Sheets
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive.file"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    cliente = gspread.authorize(creds)
    hoja = cliente.open("Usuarios_bd").sheet1

    # Obtiene todos los datos de la hoja
    data = hoja.get_all_values()

    # Busca el nombre del usuario correspondiente al correo
    for row in data[1:]:  # Saltar la primera fila que son encabezados
        if row[5] == user_correo:  # Suponiendo que el correo está en la sexta columna
            return row[2]  # Suponiendo que el nombre está en la primera columna

    return None  # Si no se encuentra el correo en la hoja

def obtener_sexo_usuario(user_correo):
    """
    Obtiene el nombre de usuario correspondiente a un correo específico desde una hoja de Google Sheets.

    Parámetros:
    - user_correo (str): El correo del usuario cuyo nombre se desea obtener.

    Retorna:
    - str: El nombre del usuario si se encuentra, o None si el correo no se encuentra en la hoja.
    """

    # Configuración de autenticación y acceso a Google Sheets
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive.file"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    cliente = gspread.authorize(creds)
    hoja = cliente.open("Usuarios_bd").sheet1

    # Obtiene todos los datos de la hoja
    data = hoja.get_all_values()

    # Busca el nombre del usuario correspondiente al correo
    for row in data[1:]:  # Saltar la primera fila que son encabezados
        if row[5] == user_correo:  # Suponiendo que el correo está en la sexta columna
            return row[3]  # Suponiendo que el nombre está en la primera columna

    return None  # Si no se encuentra el correo en la hoja

def validar_credenciales(user_correo, user_contrasena):
    """
    Valida las credenciales de un usuario en una hoja de Google Sheets.

    Parámetros:
    - user_correo (str): El correo del usuario.
    - user_contrasena (str): La contraseña del usuario.

    Retorna:
    - bool: True si las credenciales son válidas, False en caso contrario.
    """

    # Configuración de autenticación y acceso a Google Sheets
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive.file",
        "https://www.googleapis.com/auth/drive.file"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    cliente = gspread.authorize(creds)
    hoja = cliente.open("Usuarios_bd").sheet1

    # Obtiene todos los datos de la hoja
    data = hoja.get_all_values()

    # Recorre los datos y verifica las credenciales
    for row in data[1:]:  # Saltar la primera fila que son encabezados
        if row[5] == user_correo and row[6] == user_contrasena:  # Suponiendo que el correo está en la sexta columna y la contraseña en la séptima
            return True  # Credenciales válidas

    return False  # Credenciales inválidas

# Variable para controlar si el usuario ha iniciado sesión



if st.button("Iniciar sesión"):
   
    if validar_credenciales(correo, contrasena):
        st.success("Inicio de sesión exitoso")
        st.session_state['correo'] = correo
        st.session_state['logged_in']  = True
        st.session_state.nombre = obtener_nombre_usuario
        st.session_state.apellido = obtener_apellido_usuario
        st.session_state.generofav = obtener_genero_usuario
        st.session_state.sexo = obtener_sexo_usuario
        st.session_state.fecha = obtener_fecha_usuario
        if st.session_state['logged_in']:
            nombre_usuario = obtener_nombre_usuario(correo)
            if nombre_usuario:
                st.write(f"Bienvenido, {nombre_usuario}")
            else:
                 st.warning("No se pudo obtener el nombre del usuario")
    else:
        st.error("Usuario o contraseña incorrectos")
        st.session_state['logged_in'] = False

    # Verificar si el usuario ha iniciado sesión



if st.session_state['logged_in'] == True:
    if st.button("Cerrar sesión"):
        
       st.session_state['logged_in']  = False




