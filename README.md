# 🧠 Jogo da Memória 6x6

Um jogo da memória interativo desenvolvido em Python, com uma grade de 6x6 cartas. O objetivo é encontrar os pares corretos com o menor número de tentativas possível.

---

## 🎯 Objetivo

- O jogador deve clicar em dois cards por vez para encontrar pares iguais.
- Se os pares forem corretos, eles permanecem revelados e fixos.
- Se forem errados, os cards se fecham com um efeito de "janela basculante".
- Cada par pode ser tentado até **3 vezes**. Após isso, o par é considerado perdido.
- Se o jogador esgotar todas as tentativas disponíveis para todos os pares, o jogo termina em **Game Over**.

---

## 🧩 Pré-visualização

- Ao iniciar o jogo, é exibido um **preview de 10 segundos** com todos os pares revelados.
- O jogador deve memorizar as posições antes que os cards sejam ocultados.
- Após o tempo, o jogo começa com as regras descritas acima.

---

## 👤 Registro de Jogador

- Antes de iniciar, o jogador digita seu nome.
- O sistema registra:
  - Nome
  - Tempo total de resolução
  - Número de vitórias
- Esses dados são armazenados para montar um histórico de desempenho.

---

## 🚀 Como executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/pmarcos6821/jogodamemoria.git
   cd jogodamemoria
