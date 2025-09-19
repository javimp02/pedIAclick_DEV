import streamlit as st
from openai import OpenAI
import base64

# Configurar cliente de OpenAI con la API Key de imágenes
OPENAI_KEY_IMAGES = st.secrets.get("OPENAI_API_KEY_IMAGES", "")
client_images = OpenAI(api_key=OPENAI_KEY_IMAGES)

st.title("Prueba de generación de imagen")

# Prompt de ejemplo
prompt_img = "Un gato jugando al ajedrez, estilo ilustración colorida y alegre"

try:
    # Generar imagen
    response = client_images.images.generate(
        model="gpt-image-1",
        prompt=prompt_img,
        size="1024x1024"
    )

    st.write("Respuesta completa de la API:", response)

    # Obtener el objeto de imagen
    if response.data and len(response.data) > 0:
        image_obj = response.data[0]

        # Priorizar URL, si no hay usar base64
        if image_obj.url:
            st.success("✅ Imagen generada correctamente")
            st.image(image_obj.url, caption="Imagen generada por DALL·E")
        elif image_obj.b64_json:
            st.success("✅ Imagen generada correctamente")
            # Convertir base64 a bytes y mostrar
            image_bytes = base64.b64decode(image_obj.b64_json)
            st.image(image_bytes, caption="Imagen generada por DALL·E")
        else:
            st.error("⚠️ No se encontró URL ni base64 en la respuesta")
    else:
        st.error("⚠️ La respuesta de la API no contiene datos")

except Exception as e:
    st.error(f"⚠️ Error al generar la imagen: {e}")
