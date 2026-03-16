from arvore import construir_arvore


def jogar(raiz):
    """
    Simula um jogo de adivinhação estilo Akinator.

    Regras:
    - Começa na raiz da árvore
    - Faz perguntas ao usuário (s/n)
    - Navega pela árvore conforme as respostas
    - Para quando chega em um nó folha (resposta final)
    """
    print("\n" + "=" * 50)
    print("  BEM-VINDO AO MINI AKINATOR!")
    print("  Pense em um personagem... eu vou adivinhar!")
    print("=" * 50)

    node_atual = raiz
    perguntas_feitas = 0

    while not node_atual.is_leaf():
        while True:
            resposta = input(f"\n{node_atual.question} (s/n): ").strip().lower()
            if resposta in ("s", "n"):
                break
            print("  ⚠  Por favor, responda apenas 's' (sim) ou 'n' (não).")

        perguntas_feitas += 1

        if resposta == "s":
            node_atual = node_atual.yes
        else:
            node_atual = node_atual.no

    print(f"\n  🤔 Você pensou em: {node_atual.answer}")

    while True:
        acertou = input("\n  Acertei? (s/n): ").strip().lower()
        if acertou in ("s", "n"):
            break
        print("  ⚠  Por favor, responda apenas 's' ou 'n'.")

    if acertou == "s":
        print(f"\n  🎉 Acertei! Respondi em {perguntas_feitas} pergunta(s).")
    else:
        print("\n  😅 Errei! Ainda não aprendi esse personagem.")

    return acertou == "s"


if __name__ == "__main__":
    arvore = construir_arvore()
    jogar(arvore)
