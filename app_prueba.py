import streamlit as st
from openai import OpenAI

# 🔑 Tu API Key de imágenes
OPENAI_KEY_IMAGES = st.secrets.get("OPENAI_API_KEY_IMAGES", "")

# Cliente de OpenAI
client_images = OpenAI(api_key=OPENAI_KEY_IMAGES)

st.title("Prueba de generación de imagen")

prompt_img = "Un gato jugando al ajedrez, estilo ilustración colorida y alegre"

try:
    # Generar imagen
    response = client_images.images.generate(
        model="gpt-image-1",
        prompt=prompt_img,
        size="1024x1024"
    )
    
    # Obtener URL de la imagen
    image_url = response.data[0].url
    st.success("✅ Imagen generada correctamente")
    st.image(image_url, caption="Imagen generada por DALL·E")
    
except Exception as e:
    st.error(f"⚠️ Error al generar la imagen: {e}")
