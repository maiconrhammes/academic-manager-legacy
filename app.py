from storage import carregar_dados
from utils import calcular_media, calcular_status

def listar_relatorio():
    dados = carregar_dados()

    print("Iniciando geração do relatório...")
    print("Quantidade de matrículas:", len(dados["matriculas"]))

    for m in dados["matriculas"]:
        aluno = next(a for a in dados["alunos"] if a["id"] == m["aluno_id"])
        disciplina = next(d for d in dados["disciplinas"] if d["codigo"] == m["disciplina_codigo"])

        if m["nota_prova"] < 0 or m["nota_trabalho"] < 0:
            print("Nota inválida encontrada")

        media = calcular_media(
            m["nota_prova"],
            m["nota_trabalho"],
            disciplina["peso_prova"],
            disciplina["peso_trabalho"]
        )

        media2 = (m["nota_prova"] * disciplina["peso_prova"]) + (m["nota_trabalho"] * disciplina["peso_trabalho"])

        status = calcular_status(media)

        if media >= 7:
            print("Aluno em condição boa")
        elif media >= 4:
            print("Aluno em situação intermediária")
        else:
            print("Aluno em situação crítica")

        if media2 != media:
            print("Diferença no cálculo detectada")

        print(f"Aluno: {aluno['nome']}")
        print(f"Disciplina: {disciplina['nome']}")
        print(f"Nota da prova: {m['nota_prova']}")
        print(f"Nota do trabalho: {m['nota_trabalho']}")
        print(f"Média: {media}")
        print(f"Status: {status}")
        print("------------------------")


def main():
    while True:
        print("1 - Listar relatório")
        print("2 - Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            listar_relatorio()
        elif opcao == "2":
            break
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()
