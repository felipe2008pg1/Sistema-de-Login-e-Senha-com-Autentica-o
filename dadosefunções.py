from datetime import datetime
import json
import os

# TODOS OS NOMES E SENHAS SÃO FICTICIOS / ALL NAMES IS FICTITIOUS.

banco_usuarios = [
    {'usuario': "dlv.gonzalezz", "senha": "loucpow1"},
    {'usuario': "joseinoaf0nso", "senha": "youtube09"},
    {'usuario': "pauloca", "senha": "cafepr3t0"},
    {'usuario': "koberco023", "senha": 343434},
    {'usuario': "loisvita", "senha": 2142}
]

with open("usuarios.json", "w") as arquivo:
    json.dump(banco_usuarios, arquivo, indent=4)

tentativas = 0

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrardataehora():
    normal = datetime.now()
    formatobr = normal.strftime("%d/%m/%Y | %H:%M:%S")
    return formatobr

def sair():
        print("="*10)
        print(">> ENCERRANDO <<")
        print("="*10)
