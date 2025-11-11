import streamlit as st

st.title("Hello Streamlit depuis Colab")
st.write("🚀 Ceci est un déploiement via ngrok")

# 3. Importer et configurer ngrok
from pyngrok import ngrok, conf

# Remplacer ici par ton propre authtoken
conf.get_default().auth_token = "35Kjxwa0KMsM3xhQSJVnIMKPk2Z_2E18ihCB5KQbpZDQkACXy"



# 5. Créer le tunnel
public_url = ngrok.connect(8501)
print("🚀 Lien vers votre app Streamlit :", public_url)
