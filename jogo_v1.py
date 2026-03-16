from arvore import Node, construir_arvore
from bfs_comparacao import comparar_algoritmos


def jogar(raiz):
    """
    Simula um jogo de adivinhação estilo Akinator.

    Regras:
    - Começa na raiz da árvore
    - Faz perguntas ao usuário (s/n)
    - Navega pela árvore conforme as respostas
    - Para quando chega em um nó folha (resposta final)
    - Se errar, ativa o aprendizado incremental
    """
    print("\n" + "=" * 50)
    print("  BEM-VINDO AO MINI AKINATOR!")
    print("  Pense em um personagem... eu vou adivinhar!")
    print("=" * 50)

    node_atual = raiz
    perguntas_feitas = 0
    caminho = []

    while not node_atual.is_leaf():
        while True:
            resposta = input(f"\n{node_atual.question} (s/n): ").strip().lower()
            if resposta in ("s", "n"):
                break
            print("  ⚠  Por favor, responda apenas 's' (sim) ou 'n' (não).")

        caminho.append((node_atual, resposta))
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
        print("\n  😅 Errei! Mas posso aprender...")
        aprender(node_atual, caminho)

    return acertou == "s"


def aprender(node_errado, caminho):
    """
    Quando o sistema erra, pergunta ao usuário qual era o personagem
    e qual pergunta distingue o novo personagem do que foi previsto.

    Substitui o nó folha errado por um novo nó de pergunta,
    com dois filhos: o personagem novo e o personagem antigo.
    """
    print("\n" + "-" * 40)
    print("  MODO APRENDIZADO")
    print("-" * 40)

    personagem_certo = input("  Qual personagem você pensou? ").strip().capitalize()

    if not personagem_certo:
        print("  Tudo bem, não vou aprender desta vez.")
        return

    nova_pergunta = input(
        f"  Qual pergunta distingue '{personagem_certo}' de '{node_errado.answer}'?\n"
        f"  (ex: 'É da Marvel?'): "
    ).strip()

    if not nova_pergunta:
        print("  Pergunta inválida. Não vou aprender desta vez.")
        return

    resposta_novo = input(
        f"  Para '{personagem_certo}', a resposta para '{nova_pergunta}' é (s/n): "
    ).strip().lower()

    if resposta_novo not in ("s", "n"):
        print("  Resposta inválida. Não vou aprender desta vez.")
        return

    novo_no_pergunta = Node(question=nova_pergunta)
    novo_personagem  = Node(answer=personagem_certo)
    antigo           = Node(answer=node_errado.answer)

    if resposta_novo == "s":
        novo_no_pergunta.yes = novo_personagem
        novo_no_pergunta.no  = antigo
    else:
        novo_no_pergunta.yes = antigo
        novo_no_pergunta.no  = novo_personagem

    if caminho:
        pai, resposta_pai = caminho[-1]
        if resposta_pai == "s":
            pai.yes = novo_no_pergunta
        else:
            pai.no = novo_no_pergunta
        print(f"\n  ✅ Aprendi! Agora sei distinguir '{personagem_certo}' de '{antigo.answer}'.")
    else:
        print("  Não foi possível atualizar a árvore neste caso.")


def menu():
    arvore = construir_arvore()

    opcoes = {
        "1": ("Jogar (modo interativo)",   lambda: jogar(arvore)),
        "2": ("Comparar DFS vs BFS",       lambda: comparar_algoritmos(arvore)),
        "3": ("Reconstruir árvore padrão", lambda: reconstruir(arvore)),
        "0": ("Sair",                      None),
    }

    while True:
        print("\n" + "=" * 50)
        print("  MINI AKINATOR — Menu Principal")
        print("=" * 50)
        for chave, (descricao, _) in opcoes.items():
            print(f"  [{chave}] {descricao}")

        escolha = input("\n  Escolha uma opção: ").strip()

        if escolha == "0":
            print("\n  Até mais! 👋\n")
            break
        elif escolha in opcoes:
            _, acao = opcoes[escolha]
            acao()
        else:
            print("  ⚠  Opção inválida.")


def reconstruir(arvore_ref):
    nova = construir_arvore()
    arvore_ref.__dict__.update(nova.__dict__)
    print("\n  ✅ Árvore reconstruída para o estado original.")


if __name__ == "__main__":
    menu()
