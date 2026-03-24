class Pagamento: 

    def __init__(self, nome, categoria, curso, valor, data, hora):
        self.nome = nome
        self.categoria = categoria
        self.curso = curso
        self.valor = valor
        self.data = data
        self.hora = hora

    def __str__(self):
        return f"{self.nome} | {self.categoria} | {self.curso} | R${self.valor} | {self.data_hora}"