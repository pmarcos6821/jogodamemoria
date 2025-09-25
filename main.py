import tkinter as tk
import random
import time

# Configurações
PREVIEW_TIME = 3000  # milissegundos
MAX_TENTATIVAS = 30

class JogoMemoria:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Memória")
        self.pares = self.gerar_pares()
        self.botoes = []
        self.revelados = []
        self.acertos = set()
        self.tentativas = 0
        self.inicio = None

        self.label_info = tk.Label(root, text="Clique para iniciar o jogo!", font=("Arial", 14))
        self.label_info.pack(pady=10)

        self.tabuleiro = tk.Frame(root)
        self.tabuleiro.pack()

        self.criar_tabuleiro(preview=True)
        self.root.after(PREVIEW_TIME, self.iniciar_jogo)

    def gerar_pares(self):
        valores = list("A B C D E F G H".split()) * 2
        random.shuffle(valores)
        return valores

    def criar_tabuleiro(self, preview=False):
        for i in range(4):
            linha = []
            for j in range(4):
                idx = i * 4 + j
                texto = self.pares[idx] if preview else ""
                btn = tk.Button(self.tabuleiro, text=texto, width=6, height=3,
                                font=("Arial", 16), command=lambda idx=idx: self.revelar(idx))
                btn.grid(row=i, column=j, padx=5, pady=5)
                linha.append(btn)
            self.botoes.append(linha)

    def iniciar_jogo(self):
        self.label_info.config(text="Encontre os pares!")
        for linha in self.botoes:
            for btn in linha:
                btn.config(text="")
        self.inicio = time.time()

    def revelar(self, idx):
        if idx in self.acertos or idx in self.revelados:
            return

        i, j = divmod(idx, 4)
        self.botoes[i][j].config(text=self.pares[idx])
        self.revelados.append(idx)

        if len(self.revelados) == 2:
            self.root.after(1000, self.verificar_par)

    def verificar_par(self):
        idx1, idx2 = self.revelados
        if self.pares[idx1] == self.pares[idx2]:
            self.acertos.update([idx1, idx2])
        else:
            for idx in self.revelados:
                i, j = divmod(idx, 4)
                self.botoes[i][j].config(text="")
        self.revelados = []
        self.tentativas += 1
        self.verificar_fim()

    def verificar_fim(self):
        if len(self.acertos) == 16:
            tempo_total = round(time.time() - self.inicio, 2)
            self.label_info.config(text=f"Parabéns! Você venceu em {tempo_total} segundos com {self.tentativas} tentativas.")
        elif self.tentativas >= MAX_TENTATIVAS:
            self.label_info.config(text="Game Over! Você excedeu o número de tentativas.")

# Execução
if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoMemoria(root)
    root.mainloop()