import streamlit as st

# Título de la aplicación
st.title("Perfil de Usuario")

# Botón para mostrar el perfil del usuario
if st.session_state.logged_in:
    if st.button("Mostrar Perfil"):
        st.subheader("Perfil del Usuario")
        st.write(f"Nombre: {st.session_state.nombre}")
        st.write(f"Apellido: {st.session_state.apellido}")
        st.write(f"Género: {st.session_state.sexo}")
        st.write(f"Género Favorito: {st.session_state.generofav}")
        st.write(f"Correo Electrónico: {st.session_state.correo}")
        st.subheader("Juegos Calificados")
        st.write("5")  
        st.subheader("Juegos Finalizados")
        st.write("10")  
        st.write(f'Estado {st.session_state.logged_in}')

else:
    st.warning("Para ver tu perfil debes iniciar sesión")
