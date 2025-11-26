import xmltodict
import pandas as pd
import os


def processar_xml(arquivo_nome):
    with open(f'xml/{arquivo_nome}', 'rb') as arquivo_xml:
        json_arquivo = xmltodict.parse(arquivo_xml)
        infor_nfe = (
            json_arquivo.get('nfeProc', {}).get('NFe', {}).get('infNFe')
            or json_arquivo.get('NFe', {}).get('infNFe')
        )

        if not infor_nfe:
            print(f"Arquivo inválido ou estrutura desconhecida: {arquivo_nome}")
            return []

        # Informações gerais
        numero_nfe = infor_nfe.get('@Id', 'não informado')
        emitente = infor_nfe.get('emit', {}).get('xNome', 'não informado')
        destinatario = infor_nfe.get('dest', {}).get('xNome', 'não informado')

        # Total da nota
        total_nfe = (
            infor_nfe.get("total", {})
                     .get("ICMSTot", {})
                     .get("vNF", "não informado")
        )

        # Valor pago
        valor_pago = (
            infor_nfe.get("pag", {})
                     .get("detPag", {})
                     .get("vPag", "não informado")
        )

        # Produtos
        produtos = infor_nfe.get("det", [])

        # Normaliza caso tenha apenas um produto (algumas notas são assim)
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


def gerar_excel():
    if not os.path.exists("xml"):
        print("Erro: a pasta 'xml' não existe.")
        return

    arquivos = os.listdir("xml")
    if not arquivos:
        print("Nenhum XML encontrado na pasta 'xml'.")
        return

    tabela_final = []
    for arquivo in arquivos:
        if arquivo.lower().endswith(".xml"):
            print(f"Processando {arquivo}...")
            linhas = processar_xml(arquivo)
            tabela_final.extend(linhas)

    if not tabela_final:
        print("Nenhum dado encontrado nos arquivos XML.")
        return

    df = pd.DataFrame(tabela_final)
    df.to_excel("tabela_nfe.xlsx", index=False)

    print("\nPlanilha gerada com sucesso!")
    print("Arquivo criado: tabela_nfe.xlsx")


if __name__ == "__main__":
    gerar_excel()
