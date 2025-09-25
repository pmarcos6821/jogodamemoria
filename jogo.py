import tkinter as tk
from PIL import Image, ImageTk
import random
import os
import time

# Caminho absoluto para a pasta de imagens
CAMINHO_IMAGENS = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "assets", "imagens")
)

# Verificação para garantir que o caminho existe
if not os.path.exists(CAMINHO_IMAGENS):
    raise FileNotFoundError(f"Pasta de imagens não encontrada: {CAMINHO_IMAGENS}")

# Configurações do jogo
PREVIEW_TIME = 3000  # milissegundos
MAX_TENTATIVAS = 40
TAMANHO_IMAGEM = (80, 80)
TEMPO_LIMITE = 600  # segundos (10 minutos)

class JogoMemoriaImagens:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Memória com Imagens")
        self.imagens = self.carregar_imagens()
        self.pares = self.gerar_pares()
        self.botoes = []
        self.revelados = []
        self.acertos = set()
        self.tentativas = 0
        self.inicio = None
        self.jogo_encerrado = False
        self.bloqueado = False

        self.label_info = tk.Label(root, text="Preview das imagens...", font=("Arial", 14))
        self.label_info.pack(pady=10)

        self.tabuleiro = tk.Frame(root)
        self.tabuleiro.pack()

        self.criar_tabuleiro(preview=True)
        self.root.after(PREVIEW_TIME, self.iniciar_jogo)

    def carregar_imagens(self):
        imagens = {}
        for nome in os.listdir(CAMINHO_IMAGENS):
            if nome.endswith(".png"):
                caminho = os.path.join(CAMINHO_IMAGENS, nome)
                chave = nome.replace(".png", "")
                img = Image.open(caminho).resize(TAMANHO_IMAGEM)
                imagens[chave] = ImageTk.PhotoImage(img)
        if "tampa" not in imagens:
            raise FileNotFoundError("A imagem 'tampa.png' é obrigatória para ocultar os quadrados.")
        return imagens

    def gerar_pares(self):
        nomes = [nome for nome in self.imagens.keys() if nome != "tampa"]
        selecionados = random.sample(nomes, 8)
        pares = selecionados * 2
        random.shuffle(pares)
        return pares

    def criar_tabuleiro(self, preview=False):
        for i in range(4):
            linha = []
            for j in range(4):
                idx = i * 4 + j
                nome = self.pares[idx]
                img = self.imagens[nome] if preview else self.imagens["tampa"]
                btn = tk.Button(self.tabuleiro, image=img, width=90, height=90,
                                command=lambda idx=idx: self.revelar(idx))
                btn.grid(row=i, column=j, padx=5, pady=5)
                btn.nome_imagem = nome
                linha.append(btn)
            self.botoes.append(linha)

    def iniciar_jogo(self):
        self.label_info.config(text="Encontre os pares!")
        for linha in self.botoes:
            for btn in linha:
                btn.config(image=self.imagens["tampa"])
        self.inicio = time.time()
        self.verificar_tempo_limite()

    def verificar_tempo_limite(self):
        if self.jogo_encerrado:
            return
        tempo_passado = time.time() - self.inicio
        if tempo_passado >= TEMPO_LIMITE:
            self.jogo_encerrado = True
            self.label_info.config(text="Jogador desclassificado pois esgotou o tempo limite de 10 minutos.")
        else:
            self.root.after(1000, self.verificar_tempo_limite)

    def revelar(self, idx):
        if self.jogo_encerrado or self.bloqueado or idx in self.acertos or idx in self.revelados:
            return

        i, j = divmod(idx, 4)
        nome = self.pares[idx]
        self.botoes[i][j].config(image=self.imagens[nome])
        self.revelados.append(idx)

        if len(self.revelados) == 2:
            self.bloqueado = True
            self.root.after(1000, self.verificar_par)

    def verificar_par(self):
        idx1, idx2 = self.revelados
        if idx1 != idx2 and self.pares[idx1] == self.pares[idx2]:
            self.acertos.update([idx1, idx2])
        else:
            for idx in self.revelados:
                i, j = divmod(idx, 4)
                self.botoes[i][j].config(image=self.imagens["tampa"])
        self.revelados = []
        self.tentativas += 1
        self.bloqueado = False
        self.verificar_fim()

    def verificar_fim(self):
        if self.jogo_encerrado:
            return
        if len(self.acertos) == 16:
            self.jogo_encerrado = True
            tempo_total = round(time.time() - self.inicio, 2)
            minutos = int(tempo_total // 60)
            segundos = int(tempo_total % 60)

            if tempo_total < 60:
                self.label_info.config(text=f"Você resolveu em {segundos} segundos, parabéns!")
            elif minutos <= 3:
                self.label_info.config(text=f"Sensacional, você resolveu em {minutos} minutos e {segundos} segundos!")
            else:
                self.label_info.config(text=f"Você resolveu em {minutos} minutos e {segundos} segundos, parabéns!")
        elif self.tentativas >= MAX_TENTATIVAS:
            self.jogo_encerrado = True
            self.label_info.config(text="Game Over! Você excedeu o número de tentativas.")

# Execução
if __name__ == "__main__":
    root = tk.Tk()
    jogo = JogoMemoriaImagens(root)
    root.mainloop()
