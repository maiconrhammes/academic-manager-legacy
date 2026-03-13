def calcular_media(nota_prova, nota_trabalho, peso_prova, peso_trabalho):
    return nota_prova * peso_prova + nota_trabalho * peso_trabalho

def calc2(a, b, c, d):
    return a * c + b * d

def calcular_status(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação Parcial"
    elif media >= 4:
        return "Recuperação"
    else:
        return "Reprovado"
