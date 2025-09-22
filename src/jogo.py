import random
import time
from config import GRID_SIZE, MAX_TENTATIVAS, FEEDBACK_DELAY

def gerar_pares():
    """Gera uma lista embaralhada de pares para o jogo."""
    total_cartas = GRID_SIZE[0] * GRID_SIZE[1]
    num_pares = total_cartas // 2
    imagens = [f"img_{i}" for i in range(num_pares)] * 2
    random.shuffle(imagens)
    return imagens

def mostrar_preview(pares):
    """Exibe os pares por 10 segundos para o jogador memorizar."""
    print("\n🧠 PREVIEW DOS PARES (memorize):")
    for i in range(0, len(pares), GRID_SIZE[1]):
        print(" | ".join(pares[i:i + GRID_SIZE[1]]))
    print("\nAguarde...")

def verificar_par(pares, pos1, pos2):
    """Verifica se duas posições formam um par."""
    return pares[pos1] == pares[pos2]

def mostrar_feedback_erro():
    """Simula o efeito de janela basculante ao errar um par."""
    print("❌ Par incorreto! Fechando cartas com efeito de janela basculante...")
    time.sleep(FEEDBACK_DELAY)

def iniciar_jogo(pares, tentativas_restantes):
    """Executa a lógica principal do jogo."""
    reveladas = [False] * len(pares)
    pares_restantes = len(pares) // 2

    while pares_restantes > 0:
        print("\n🃏 Estado atual:")
        for i in range(len(pares)):
            if reveladas[i]:
                print(f"[{pares[i]}]", end=" ")
            else:
                print(f"[{i}]", end=" ")
            if (i + 1) % GRID_SIZE[1] == 0:
                print()

        try:
            pos1 = int(input("\nEscolha a primeira carta (0 a {}): ".format(len(pares) - 1)))
            pos2 = int(input("Escolha a segunda carta (0 a {}): ".format(len(pares) - 1)))
        except ValueError:
            print("⚠️ Entrada inválida. Digite números válidos.")
            continue

        if pos1 == pos2 or not (0 <= pos1 < len(pares)) or not (0 <= pos2 < len(pares)):
            print("⚠️ Escolhas inválidas. Tente novamente.")
            continue

        if reveladas[pos1] or reveladas[pos2]:
            print("⚠️ Uma ou ambas as cartas já estão reveladas.")
            continue

        if verificar_par(pares, pos1, pos2):
            print("✅ Par encontrado!")
            reveladas[pos1] = True
            reveladas[pos2] = True
            pares_restantes -= 1
        else:
            mostrar_feedback_erro()
            par_id = frozenset([pares[pos1], pares[pos2]])
            tentativas_restantes[par_id] -= 1
            if tentativas_restantes[par_id] <= 0:
                print("💀 Você esgotou as tentativas para esse par.")
                return "derrota"

    return "vitoria"
