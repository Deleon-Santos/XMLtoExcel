import xmltodict
import pandas as pd
import os
import json

def xml_to_excel(arquivo_nome, valores):
    
    with open(f'xml/{arquivo_nome}', 'rb', encoding='utf-8') as arquivo_xml:
        json_arquivo = xmltodict.parse(arquivo_xml)
        # Convert the ordered dictionary to a JSON string
        json_string = json.dumps(json_arquivo, indent=4)
        print(json_string)

        infor_nfe = json_arquivo['nfeProc']['NFe']['infNFe'] if 'nfeProc' in json_arquivo else json_arquivo['NFe']['infNFe']
        dados_nfe = infor_nfe['@Id'] if '@Id' in infor_nfe else 'nao informado'
        dados_emitente = infor_nfe['emit'] if 'emit' in infor_nfe else 'nao informado'  
        dados_destinatario = infor_nfe['dest'] if 'dest' in infor_nfe else 'nao informado'
        dados_produtos = infor_nfe['det'] if 'det' in infor_nfe else 'nao informado'
        dados_totais = infor_nfe['total']['ICMSTot'] if 'total' in infor_nfe and 'ICMSTot' in infor_nfe['total'] else 'nao informado'
        dados_transporte = infor_nfe['transp'] if 'transp' in infor_nfe else 'nao informado'
        valores.append([dados_nfe, dados_emitente, dados_destinatario, dados_produtos, dados_totais, dados_transporte])


    
    
arquivo  = os.listdir('xml')
colunas = ['n°_nfe', 'emitente', 'destinatario', 'produtos', 'totais', 'transporte']
valores = []

for file in arquivo:
    arquivo_nome = file
    xml_to_excel(arquivo_nome, valores)


tabela_excel = pd.DataFrame(valores, columns=colunas)