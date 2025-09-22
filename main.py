import time
from config import PREVIEW_TIME, MAX_TENTATIVAS
from utils.registro import registrar_jogador, salvar_resultado
from src.jogo import gerar_pares, mostrar_previewfrom 

def main():
    # 1. Solicita nome do jogador
    nome = input("Digite seu nome para iniciar o jogo: ")
    registrar_jogador(nome)

    # 2. Gera os pares e mostra preview
    pares = gerar_pares()
    mostrar_preview(pares)
    time.sleep(PREVIEW_TIME)  # Aguarda 10 segundos

    # 3. Oculta os pares e inicia o jogo
    tentativas_restantes = {par: MAX_TENTATIVAS for par in pares}
    inicio = time.time()
    resultado = iniciar_jogo(pares, tentativas_restantes)

    # 4. Finaliza e salva resultado
    fim = time.time()
    tempo_total = round(fim - inicio, 2)
    salvar_resultado(nome, resultado, tempo_total)

    if resultado == "vitoria":
        print(f"Parabéns, {nome}! Você venceu em {tempo_total} segundos.")
    else:
        print(f"Game Over, {nome}. Tente novamente!")

if __name__ == "__main__":
    main()

