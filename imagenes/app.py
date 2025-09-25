import requests
import streamlit as st
from openai import OpenAI
import base64


#########################################################################################################################
# CONFIG
#########################################################################################################################

OPENAI_KEY_IMAGES = st.secrets.get("OPENAI_API_KEY_IMAGES", "")

client_images = OpenAI(api_key=OPENAI_KEY_IMAGES)


def generar_imagen_dalle(prompt_img: str):
    try:
        with open("assets/referencia.jpeg", "rb") as f:
            response = client_images.images.edit(
            model="gpt-image-1",
            image=f,
            prompt=prompt_img,
            size="1024x1024"
            )
            
        image_obj = response.data[0]
        if image_obj.url:
            return image_obj.url
        elif image_obj.b64_json:
            return base64.b64decode(image_obj.b64_json)
        else:
            st.error("⚠️ La API no devolvió URL ni imagen base64.")
            return None
    except Exception as e:
        st.error(f"⚠️ Error al generar la imagen: {e}")
        return None



