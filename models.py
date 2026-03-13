class Aluno:
    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email

    def mostrar(self):
        return self.nome + " - " + self.email


class Disciplina:
    def __init__(self, codigo, nome, peso_prova, peso_trabalho):
        self.codigo = codigo
        self.nome = nome
        self.peso_prova = peso_prova
        self.peso_trabalho = peso_trabalho


class Matricula:
    def __init__(self, aluno_id, disciplina_codigo, nota_prova, nota_trabalho):
        self.aluno_id = aluno_id
        self.disciplina_codigo = disciplina_codigo
        self.nota_prova = nota_prova
        self.nota_trabalho = nota_trabalho
