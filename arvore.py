class Node:

    def __init__(self, question=None, answer=None):
        self.question = question
        self.answer = answer
        self.yes = None
        self.no = None

    def is_leaf(self):
        """Retorna True se o nó for uma folha (resposta final)."""
        return self.answer is not None

    def __repr__(self):
        if self.is_leaf():
            return f"[Resposta: {self.answer}]"
        return f"[Pergunta: {self.question}]"


def construir_arvore():
 
    # --- Raiz ---
    raiz = Node(question="É um vilão?")

    # ── Ramo SIM: é vilão ──────────────────────────────────
    raiz.yes = Node(question="É da Marvel?")
    raiz.yes.yes = Node(answer="Thanos")
    raiz.yes.no  = Node(answer="Coringa")

    # ── Ramo NÃO: não é vilão ─────────────────────────────
    raiz.no = Node(question="É um personagem de série?")

    raiz.no.yes = Node(answer="Walter White")

    raiz.no.no = Node(question="O personagem faz magia?")

    raiz.no.no.yes = Node(question="É um personagem adulto?")
    raiz.no.no.yes.yes = Node(answer="Dumbledore")
    raiz.no.no.yes.no  = Node(answer="Elsa")

    raiz.no.no.no = Node(question="É uma princesa?")
    raiz.no.no.no.yes = Node(answer="Moana")

    raiz.no.no.no.no = Node(question="Usa armadura como superpoder?")
    raiz.no.no.no.no.yes = Node(answer="Homem de Ferro")
    raiz.no.no.no.no.no  = Node(answer="Anakin Skywalker")

    return raiz


def imprimir_arvore(node, prefixo="", lado="Raiz"):
    """Imprime a estrutura da árvore de forma visual no terminal."""
    if node is None:
        return
    print(f"{prefixo}{lado}: {node}")
    if not node.is_leaf():
        imprimir_arvore(node.yes, prefixo + "    ", "SIM →")
        imprimir_arvore(node.no,  prefixo + "    ", "NÃO →")


if __name__ == "__main__":
    print("=" * 50)
    print("  ESTRUTURA DA ÁRVORE DE DECISÃO (v2)")
    print("  Tema: Personagens de Filmes e Séries")
    print("=" * 50)
    arvore = construir_arvore()
    imprimir_arvore(arvore)
