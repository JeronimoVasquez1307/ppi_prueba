import streamlit as st

# Título de la aplicación
st.title("Perfil de Usuario")

# Botón para mostrar el perfil del usuario
if st.button("Mostrar Perfil"):
    st.subheader("Perfil del Usuario")
    st.write("Nombre: Juan")
    st.write("Apellido: Pérez")
    st.write("Género: Masculino")
    st.write("Género Favorito: Aventuras")
    st.write(f"Correo Electrónico: {st.session_state.correo}")
    st.subheader("Juegos Calificados")
    st.write("5")  
    st.subheader("Juegos Finalizados")
    st.write("10")  
    st.write(f'Estado {st.session_state.logged_in}')
