import streamlit as st

st.title("Sistema de Chamados")

#Criar lista de Chamados
if "Chamados" not in st.session_state:
    st.session_state.chamados = []

#Abrir Chamado    
st.subheader("Abrir Chamado")
titulo = st.text_input("Título do Chamado")
descricacao = st.text_area("Descrição do Serviço")

#Botão
if st.button("Abrir Chamado"):
    if titulo != "" and descricacao != "":
        chamado = {
            "titulo": titulo,
            "descricao": descricacao,
            "status": "Aberto"
        }
        st.session_state.chamados.append(chamado)
        st.success("Chamado aberto com sucesso")