
class Skibidi_Games:
    def __init__(self):
        self.games = []
    def cadastrar_jogos(self, titulo):
        if not titulo:
            raise ValueError("Titulo inválido")
        self.games.append(titulo)
    def remover_jogos(self, titulo):
        if not titulo:
            raise ValueError("Titulo inválido")
        self.games.remove(titulo)
    def quantidade_jogos(self):
        return len(self.games)