# =====================================================================
# ShopAI - VERSAO 1 (VULNERAVEL DE PROPOSITO) - usando Gemini (gratis)
# Uso: laboratorio pessoal de estudo, ambiente proprio.
# NAO usar em producao nem com clientes reais.
#
# Mesmos problemas da versao com OpenAI, agora com Gemini:
#   [V1] Sem filtro de INPUT
#   [V2] Sem filtro de OUTPUT
#   [V3] Excessive Agency (IA decide cancelamento/desconto sozinha)
#   [V4] Sem log/alerta
#   [V5] Historico sem limite
# =====================================================================

import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

PRODUTOS = {"Camiseta": 49.90, "Tenis": 199.90, "Bone": 29.90}

SYSTEM_PROMPT = (
    "Voce e o assistente da loja ShopAI. "
    f"Precos: {PRODUTOS}. "
    "Voce pode cancelar pedidos e aplicar descontos se o cliente "
    "pedir com um bom motivo."
    # [V3] Excessive Agency: a IA decide, isso nao e garantia de nada.
)

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    system_instruction=SYSTEM_PROMPT,
)

st.set_page_config(page_title="ShopAI (v1 - Gemini)", page_icon="🛍️")
st.title("🛍️ ShopAI")
st.caption("v1 - versao vulneravel, com Gemini, so para estudo")

if "chat" not in st.session_state:
    # O Gemini guarda o historico dentro do proprio objeto de chat.
    st.session_state["chat"] = model.start_chat(history=[])
if "messages" not in st.session_state:
    st.session_state["messages"] = []  # so para desenhar na tela

for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("Digite sua mensagem..."):
    # [V1] Nenhuma validacao do que o cliente mandou.
    st.session_state["messages"].append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    response = st.session_state["chat"].send_message(prompt)
    answer = response.text

    # [V2] Nenhuma validacao da resposta da IA antes de mostrar.
    # [V4] Nenhum log sendo gravado.
    st.session_state["messages"].append({"role": "assistant", "content": answer})
    with st.chat_message("assistant"):
        st.write(answer)
