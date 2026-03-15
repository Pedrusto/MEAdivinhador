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

    raiz = Node(question="É um vilão?")

    raiz.yes = Node(question="É da Marvel?")
    raiz.yes.yes = Node(answer="Thanos")
    raiz.yes.no  = Node(answer="Coringa")

    raiz.no = Node(question="Faz magia?")
    raiz.no.yes = Node(answer="Dumbledore")
    raiz.no.no  = Node(answer="Homem de Ferro")

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
    print("  ESTRUTURA DA ÁRVORE DE DECISÃO (v1)")
    print("  Tema: Personagens de Filmes e Séries")
    print("=" * 50)
    arvore = construir_arvore()
    imprimir_arvore(arvore)
