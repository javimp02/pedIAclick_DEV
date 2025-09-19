import streamlit as st
from openai import OpenAI

OPENAI_KEY_IMAGES = st.secrets.get("OPENAI_API_KEY_IMAGES", "")
client_images = OpenAI(api_key=OPENAI_KEY_IMAGES)

st.title("Prueba de generación de imagen")

prompt_img = "Un gato jugando al ajedrez, estilo ilustración colorida y alegre"

try:
    response = client_images.images.generate(
        model="gpt-image-1",
        prompt=prompt_img,
        size="1024x1024"
    )
    
    st.write("Respuesta completa de la API:", response)

    # Intentar obtener URL si existe
    if response.data and len(response.data) > 0:
        image_url = response.data[0].get("url") or response.data[0].get("b64_json")
        if image_url:
            st.success("✅ Imagen generada correctamente")
            st.image(image_url, caption="Imagen generada por DALL·E")
        else:
            st.error("⚠️ No se encontró URL ni base64 en la respuesta")
    else:
        st.error("⚠️ La respuesta de la API no contiene datos")

except Exception as e:
    st.error(f"⚠️ Error al generar la imagen: {e}")
