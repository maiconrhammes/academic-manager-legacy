import json

def carregar_dados():
    try:
        with open("dados.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {"alunos": [], "disciplinas": [], "matriculas": []}

def salvar_dados(dados):
    with open("dados.json", "w", encoding="utf-8") as f:
        json.dump(dados, f)
