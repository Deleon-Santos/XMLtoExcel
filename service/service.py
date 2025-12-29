# service.py
import xmltodict
import pandas as pd
from io import BytesIO


def processar_xml_bytes(xml_bytes):
    json_arquivo = xmltodict.parse(xml_bytes)

    infor_nfe = (
        json_arquivo.get('nfeProc', {}).get('NFe', {}).get('infNFe')
        or json_arquivo.get('NFe', {}).get('infNFe')
    )

    if not infor_nfe:
        return []

    numero_nfe = infor_nfe.get('@Id', 'não informado')
    emitente = infor_nfe.get('emit', {}).get('xNome', 'não informado')
    destinatario = infor_nfe.get('dest', {}).get('xNome', 'não informado')

    total_nfe = (
        infor_nfe.get("total", {})
                 .get("ICMSTot", {})
                 .get("vNF", "não informado")
    )

    valor_pago = (
        infor_nfe.get("pag", {})
                 .get("detPag", {})
                 .get("vPag", "não informado")
    )

    produtos = infor_nfe.get("det", [])
    if isinstance(produtos, dict):
        produtos = [produtos]

    linhas = []

    for item in produtos:
        prod = item.get("prod", {})
        linhas.append({
            "n°_nfe": numero_nfe,
            "emitente": emitente,
            "destinatario": destinatario,
            "produto": prod.get("xProd", "não informado"),
            "quantidade": prod.get("qCom", "não informado"),
            "valor_unitario": prod.get("vUnCom", "não informado"),
            "valor_total_item": prod.get("vProd", "não informado"),
            "valor_total_nfe": total_nfe,
            "valor_pago": valor_pago
        })

    return linhas


def gerar_excel_em_memoria(lista_arquivos):
    tabela_final = []

    for arquivo in lista_arquivos:
        linhas = processar_xml_bytes(arquivo.getvalue())
        tabela_final.extend(linhas)

    if not tabela_final:
        return None

    df = pd.DataFrame(tabela_final)

    buffer = BytesIO()
    df.to_excel(buffer, index=False)
    buffer.seek(0)

    return buffer
