import streamlit as st
import pandas as pd
import datetime

# Configuração da página
st.set_page_config(page_title="Controlo de Frota - Manutenção", layout="wide")

# Função para carregar a base de veículos (Simulada por agora)
@st.cache_data
def carregar_veiculos():
    # Quando tiver o seu ficheiro pronto, usaremos: pd.read_csv('veiculos.csv')
    # Por agora, usamos dados fictícios baseados nos seus ficheiros para testar
    dados = {
        'FROTA': ['11067', '41040', '31069', '41044'],
        'DESCRIÇÃO': ['VW/GOL 1.0 CITY', 'TRATOR AGRICOLA NEW H.', 'SCANIA T 112 CAVALO', 'ESCAVADEIRA HID. CASE'],
        'PLACA': ['AKP-9413', 'AAA-0012', 'AAM-1H08', 'S/PLACA']
    }
    return pd.DataFrame(dados)

df_veiculos = carregar_veiculos()

st.title("🚜 Controlo de Troca de Óleo e Manutenção")
st.markdown("---")

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Nova Troca de Óleo")
    
    # O utilizador digita apenas a FROTA
    frota_input = st.text_input("Nº da Frota (Pesquisa):")
    
    if frota_input:
        # Procura o veículo na base de dados
        veiculo_encontrado = df_veiculos[df_veiculos['FROTA'] == frota_input]
        
        if not veiculo_encontrado.empty:
            descricao = veiculo_encontrado.iloc[0]['DESCRIÇÃO']
            placa = veiculo_encontrado.iloc[0]['PLACA']
            
            st.success(f"Veículo encontrado: **{descricao}** (Placa: {placa})")
            
            # Formulário para registar a troca
            with st.form("form_troca_oleo"):
                data_troca = st.date_input("Data da Troca", datetime.date.today())
                km_atual = st.number_input("Quilometragem (KM) / Horímetro", min_value=0, step=1)
                tipo_oleo = st.text_input("Observações / Filtros / Tipo de Óleo")
                
                submit = st.form_submit_button("Registar Troca")
                
                if submit:
                    st.info(f"Troca registada com sucesso para a frota {frota_input} com {km_atual} KM!")
                    # No próximo passo, faremos este botão guardar a informação num ficheiro de histórico
        else:
            st.error("Frota não encontrada na base de dados.")

with col2:
    st.subheader("Últimas Trocas Registadas")
    # Aqui vamos construir a tabela que mostra o histórico depois de começarmos a guardar os dados
    st.write("Ainda não há registos nesta sessão.")