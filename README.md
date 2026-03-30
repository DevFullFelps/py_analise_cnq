# 📊 Auditoria de Custos de Não-Qualidade (CNQ) na Usinagem

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

## 📝 Sobre o Projeto
Este projeto foi desenvolvido para simular um cenário real de uma indústria de usinagem de peças fundidas (focada em componentes de motores elétricos). O objetivo é analisar um lote de 1.000 inspeções anuais para identificar onde estão os maiores gargalos financeiros devido a peças com defeito.

O dashboard calcula a **Perda Real** baseada no status da peça:
* **Refugo:** 100% de perda do custo unitário.
* **Retrabalho:** 30% de perda do custo unitário (custo de processo).
* **Finalizado:** 0% de perda.

## 🎯 Funcionalidades
* **Cálculo de Regras de Negócio:** Uso de `np.select` para criar colunas condicionais de prejuízo.
* **KPIs com Metas:** Exibição do prejuízo total e peças refugadas em relação a metas estipuladas pelo setor de gestão.
* **Análise de Pareto:** Identificação de quais componentes, materiais e defeitos geram mais custos.
* **Visualização Temporal:** Ordenação lógica dos meses do ano para análise de picos de problemas na produção.

## 🛠️ Como rodar o projeto localmente

1. Clone o repositório:
```bash
git clone [https://github.com/DevFullFelps/analise_dados.git](https://github.com/DevFullFelps/analise_dados.git)