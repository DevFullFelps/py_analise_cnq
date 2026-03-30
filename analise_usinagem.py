import pandas as pd
import streamlit as st
import numpy as np


meta = 125200
meta_peca = 215

df_usinagem = pd.read_csv('inspecao_usinagem_1000.csv', encoding='utf-8', sep=',', low_memory=False)

df_usinagem['Componente'] = df_usinagem['Componente'].str.strip()
df_usinagem['Componente'] = df_usinagem['Componente'].str.title()


df_usinagem['Tipo_Defeito'] = df_usinagem['Tipo_Defeito'].str.strip()
df_usinagem['Tipo_Defeito'] = df_usinagem['Tipo_Defeito'].str.title()


df_usinagem['Material'] = df_usinagem['Material'].str.strip()
df_usinagem['Material'] = df_usinagem['Material'].str.title()


df_usinagem['Data'] = pd.to_datetime(df_usinagem['Data'], format="%Y-%m-%d")
df_usinagem['Componente'] = df_usinagem['Componente'].astype('category')
df_usinagem['Tipo_Defeito'] = df_usinagem['Tipo_Defeito'].astype('category')
df_usinagem['Material'] = df_usinagem['Material'].astype('category')
df_usinagem['Status'] = df_usinagem['Status'].astype('category')






df_usinagem['Mes'] = df_usinagem['Data'].dt.month_name()

mapeamento_meses = {
    'January': 'Janeiro', 'February': 'Fevereiro', 'March': 'Março',
    'April': 'Abril', 'May': 'Maio', 'June': 'Junho',
    'July': 'Julho', 'August': 'Agosto', 'September': 'Setembro',
    'October': 'Outubro', 'November': 'Novembro', 'December': 'Dezembro'
}


df_usinagem['Mes_pt'] = df_usinagem['Mes'].map(mapeamento_meses)

df_usinagem['Mes_pt'] = df_usinagem['Mes_pt'].astype('category')
df_usinagem['Mes'] = df_usinagem['Mes'].astype('category')

print(df_usinagem['Status'].unique())


condicoes = [
    (df_usinagem['Status'] == 'Finalizado'),
    (df_usinagem['Status'] == 'Retrabalho'),
    (df_usinagem['Status'] == 'Refugo')
]
resultados = [
    0,
    df_usinagem['Custo_Unitario_Defeito'] * 0.3,
    df_usinagem['Custo_Unitario_Defeito']
]

df_usinagem['Perda_Real'] = np.select(condicoes, resultados, default=0)


df_usinagem.info()



df_usinagem = df_usinagem.drop(columns=['Mes'])


prejuizo_total = df_usinagem['Perda_Real'].sum()
refugo_total = df_usinagem['Status'].value_counts()['Refugo']
print(refugo_total)

ordem_meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
                "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

tabela_perda_mes = (
    df_usinagem[['Mes_pt', 'Perda_Real']]
    .groupby('Mes_pt')
    .sum()
    .reset_index()
    .sort_values(by=['Perda_Real'], ascending=False)
)

tabela_perda_mes['Mes_pt'] = pd.Categorical(
    tabela_perda_mes['Mes_pt'],
    categories=ordem_meses,
    ordered=True
)

tabela_perda_mes = tabela_perda_mes.sort_values('Mes_pt')


tabela_componente_maior_perda = (
    df_usinagem[['Componente', 'Perda_Real']]
    .groupby('Componente')
    .sum()
    .sort_values(by=['Perda_Real'], ascending=False)
)

tabela_defeito_maior_perda = (
    df_usinagem[['Tipo_Defeito', 'Perda_Real']]
    .groupby('Tipo_Defeito')
    .sum()
    .sort_values(by=['Perda_Real'],ascending=False)
)

tabela_material_maior_perda = (
    df_usinagem[['Material', 'Perda_Real']]
    .groupby('Material')
    .sum()
    .sort_values(by=['Perda_Real'],ascending=False)
)

resultado = prejuizo_total - meta
resultado_peca = refugo_total - meta_peca

st.metric(
    f"Prejuizo Total (Meta: R${meta:.2f})",
    f"R${prejuizo_total:.2f}",
    f'{resultado:.2f} em relação a meta',
    delta_color='inverse'
)

st.metric(
    f"Peças Refugadas (Meta: {meta_peca})",
    refugo_total,
    f"{resultado_peca:+} em relação a meta",
    delta_color="inverse"
)

st.line_chart(
    tabela_perda_mes.set_index('Mes_pt')['Perda_Real']
)

st.bar_chart(tabela_componente_maior_perda)
st.bar_chart(tabela_defeito_maior_perda)
st.bar_chart(tabela_material_maior_perda)
