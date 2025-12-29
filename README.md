
# 📄 XMLtoExcel – Conversor de NF-e (XML) para Excel
![imagem de xml para excel](./img/XMLto.png)
[Deploy Aqui](https://xmltoxlsx.streamlit.app/)
---

## Visão Geral

O **XMLtoExcel** é um conversor desenvolvido em Python para transformar arquivos **XML de Nota Fiscal Eletrônica (NF-e)** em uma **planilha Excel (.xlsx)** organizada.

Ele extrai automaticamente:

- Dados da NFe  
- Emitente  
- Destinatário  
- Produtos (nome, quantidade, valores)  
- Total da nota e valor pago  

Ideal para auditorias, conferências, controles internos e análises.

---

## Funcionalidades

✔ Processa **todos os XML** da pasta `/xml`  
✔ Suporta NF-e com 1 ou vários produtos  
✔ Extrai valores totais e pagamentos (`vNF` e `vPag`)  
✔ Gera arquivo Excel automaticamente  
✔ Script simples e direto, pronto para uso  

---

## 🛠 Tecnologias

- Python 3.12+
- xmltodict
- pandas
- openpyxl
- streamlit

---

## 📥 Instalação

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/SEU_USUARIO/XMLtoExcel.git
cd XMLtoExcel

---

