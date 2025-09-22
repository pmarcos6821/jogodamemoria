import csv
import os

ARQUIVO_REGISTRO = "dados_jogadores.csv"

def registrar_jogador(nome):
    if not os.path.exists(ARQUIVO_REGISTRO):
        with open(ARQUIVO_REGISTRO, mode='w', newline='') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(["Nome", "Resultado", "Tempo (s)"])
    print(f"Bem-vindo, {nome}! Boa sorte no jogo.")

def salvar_resultado(nome, resultado, tempo):
    with open(ARQUIVO_REGISTRO, mode='a', newline='') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow([nome, resultado, tempo])
