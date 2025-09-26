import unittest
from main import JogoMemoriaImagens
import tkinter as tk

class TestJogoMemoria(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.jogo = JogoMemoriaImagens(self.root)

    def test_gerar_pares_tem_16_elementos(self):
        pares = self.jogo.gerar_pares()
        self.assertEqual(len(pares), 16)

    def test_gerar_pares_tem_8_pares(self):
        pares = self.jogo.gerar_pares()
        contagem = {}
        for nome in pares:
            contagem[nome] = contagem.get(nome, 0) + 1
        for nome, qtd in contagem.items():
            self.assertEqual(qtd, 2)

    def tearDown(self):
        self.root.destroy()

if __name__ == "__main__":
    unittest.main()