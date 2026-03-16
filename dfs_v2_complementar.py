# ============================================================
# PARTE 2 — Implementação de DFS (Busca em Profundidade)
# Responsável: Pedro Augusto Ferreira de Oliveira
# VERSÃO 2 — Adicionado: contagem por tipo de nó, busca por resposta e resumo final
# ============================================================

from arvore import construir_arvore


def dfs(raiz):
    """
    Percorre a árvore de decisão usando DFS (busca em profundidade).

    Como funciona:
    - Usa uma PILHA (stack) — estrutura LIFO: o último a entrar é o primeiro a sair.
    - Vai o mais fundo possível em um ramo antes de voltar e explorar outro.
    - Naturalmente segue o caminho SIM até o fim, depois volta para explorar NÃO.

    Retorna uma lista com a ordem de visita dos nós.
    """
    if raiz is None:
        return []

    print("\n" + "=" * 50)
    print("  DFS — Busca em Profundidade")
    print("=" * 50)
    print("Estrutura usada: PILHA (stack)")
    print("Comportamento: vai fundo em um ramo antes de explorar outro\n")

    ordem_visita = []
    pilha = [raiz]          # Inicializa a pilha com a raiz
    contador = 0

    while pilha:
        node = pilha.pop()  # Remove o topo da pilha (último inserido)
        contador += 1

        if node.is_leaf():
            label = f"RESPOSTA: {node.answer}"
        else:
            label = f"PERGUNTA: {node.question}"

        ordem_visita.append(label)
        print(f"  Visita #{contador:02d} → {label}")

        # Empilha NÃO primeiro para que SIM seja processado antes
        # (pilha é LIFO, então o último empilhado é o primeiro visitado)
        if not node.is_leaf():
            if node.no is not None:
                pilha.append(node.no)
            if node.yes is not None:
                pilha.append(node.yes)

    print(f"\n  Total de nós visitados: {contador}")
    return ordem_visita


def dfs_recursivo(node, caminho=None, todos_caminhos=None):
    """
    Versão recursiva do DFS — percorre mostrando cada caminho completo
    da raiz até cada folha.

    Formato de saída: pergunta → pergunta → resposta
    """
    if caminho is None:
        caminho = []
    if todos_caminhos is None:
        todos_caminhos = []

    caminho_atual = caminho + [node]

    if node.is_leaf():
        partes = []
        for n in caminho_atual:
            if n.is_leaf():
                partes.append(f"RESPOSTA: {n.answer}")
            else:
                partes.append(n.question)
        todos_caminhos.append(partes)
        return todos_caminhos

    if node.yes:
        dfs_recursivo(node.yes, caminho_atual, todos_caminhos)
    if node.no:
        dfs_recursivo(node.no, caminho_atual, todos_caminhos)

    return todos_caminhos


def mostrar_caminhos_dfs(raiz):
    """Exibe todos os caminhos possíveis da raiz até as folhas usando DFS recursivo."""
    print("\n" + "=" * 50)
    print("  DFS — Caminhos completos (raiz → folha)")
    print("=" * 50)

    caminhos = dfs_recursivo(raiz)
    for i, caminho in enumerate(caminhos, 1):
        print(f"\n  Caminho {i}:")
        print("  " + " → ".join(caminho))


# ============================================================
# NOVO — Estatísticas da árvore via DFS
# ============================================================

def contar_nos(raiz):
    """
    Percorre a árvore com DFS e conta separadamente:
    - Total de nós
    - Quantidade de perguntas (nós internos)
    - Quantidade de respostas (folhas)
    """
    if raiz is None:
        return

    print("\n" + "=" * 50)
    print("  DFS — Estatísticas da Árvore")
    print("=" * 50)

    pilha = [raiz]
    total = 0
    perguntas = 0
    respostas = 0

    while pilha:
        node = pilha.pop()
        total += 1

        if node.is_leaf():
            respostas += 1
        else:
            perguntas += 1
            if node.no is not None:
                pilha.append(node.no)
            if node.yes is not None:
                pilha.append(node.yes)

    print(f"  Total de nós     : {total}")
    print(f"  Nós de pergunta  : {perguntas}")
    print(f"  Nós de resposta  : {respostas}")


# ============================================================
# NOVO — Busca por uma resposta específica via DFS
# ============================================================

def buscar_resposta(raiz, alvo):
    """
    Usa DFS para encontrar o caminho até uma resposta específica.
    Retorna e imprime o caminho percorrido até chegar no personagem buscado.

    Exemplo: buscar_resposta(arvore, "Coringa")
    → É um vilão? → É da Marvel? → RESPOSTA: Coringa
    """
    if raiz is None:
        return None

    pilha = [(raiz, [])]  # cada item é (nó atual, caminho até ele)

    while pilha:
        node, caminho = pilha.pop()
        caminho_atual = caminho + [node]

        if node.is_leaf():
            if node.answer.lower() == alvo.lower():
                # Encontrou — monta e imprime o caminho
                partes = []
                for n in caminho_atual:
                    if n.is_leaf():
                        partes.append(f"RESPOSTA: {n.answer}")
                    else:
                        partes.append(n.question)
                print("\n" + "=" * 50)
                print(f"  DFS — Caminho até '{alvo}'")
                print("=" * 50)
                print("  " + " → ".join(partes))
                return caminho_atual
        else:
            if node.no is not None:
                pilha.append((node.no, caminho_atual))
            if node.yes is not None:
                pilha.append((node.yes, caminho_atual))

    print(f"\n  Personagem '{alvo}' não encontrado na árvore.")
    return None


# --- Teste rápido ao executar este arquivo diretamente ---
if __name__ == "__main__":
    arvore = construir_arvore()

    # Funções da versão 1
    dfs(arvore)
    mostrar_caminhos_dfs(arvore)

    # Funções novas da versão 2
    contar_nos(arvore)
    buscar_resposta(arvore, "Coringa")
    buscar_resposta(arvore, "Anakin Skywalker")
