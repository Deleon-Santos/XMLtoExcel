import streamlit as st
from service.service import gerar_excel_em_memoria

st.set_page_config(
    page_title="XML NFe → Excel",
    page_icon="📊",
    layout="centered"
)

st.title("📊 Conversor XML NFe → Excel")
st.write("Arraste os arquivos XML e gere sua planilha completa.")

st.divider()

arquivos_xml = st.file_uploader(
    "📂 Arraste os arquivos XML aqui",
    type=["xml"],
    accept_multiple_files=True
)

if arquivos_xml:
    st.info(f"📄 {len(arquivos_xml)} arquivo(s) carregado(s)")

    if st.button("Gerar Planilha"):
        progresso = st.progress(0)
        status = st.empty()

        for i in range(len(arquivos_xml)):
            progresso.progress((i + 1) / len(arquivos_xml))
            status.text(f"Processando {i + 1} de {len(arquivos_xml)} arquivos...")

        buffer_excel = gerar_excel_em_memoria(arquivos_xml)

        progresso.empty()
        status.empty()

        if buffer_excel:
            st.success("✅ Planilha gerada com sucesso!")

            st.download_button(
                label="⬇️ Baixar Excel",
                data=buffer_excel,
                file_name="tabela_nfe.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        else:
            st.error("Nenhum dado válido encontrado nos XMLs.")
