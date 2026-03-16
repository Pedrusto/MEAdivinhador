# ============================================================
# PARTE 3 — Implementação de BFS (Busca em Largura)
# PARTE 5 — Comparação entre BFS e DFS
# Responsável: José Gabriel Dâmaso Barbosa
# ============================================================

import time
from collections import deque
from arvore import construir_arvore
from dfs import dfs


def bfs(raiz):
    """
    Percorre a árvore de decisão usando BFS (busca em largura).

    Como funciona:
    - Usa uma FILA (queue) — estrutura FIFO: o primeiro a entrar é o primeiro a sair.
    - Visita todos os nós de um nível antes de passar para o próximo nível.
    - Garante encontrar a resposta mais rasa (com menos perguntas) primeiro.

    Retorna uma lista com a ordem de visita dos nós.
    """
    if raiz is None:
        return []

    print("\n" + "=" * 50)
    print("  BFS — Busca em Largura")
    print("=" * 50)
    print("Estrutura usada: FILA (deque)")
    print("Comportamento: visita nível por nível antes de descer\n")

    ordem_visita = []
    fila = deque([raiz])    # Inicializa a fila com a raiz
    contador = 0
    nivel_atual = 0
    nos_nivel_atual = 1
    nos_proximo_nivel = 0

    print(f"  --- Nível {nivel_atual} (Raiz) ---")

    while fila:
        node = fila.popleft()   # Remove o primeiro da fila (FIFO)
        contador += 1
        nos_nivel_atual -= 1

        if node.is_leaf():
            label = f"RESPOSTA: {node.answer}"
        else:
            label = f"PERGUNTA: {node.question}"

        ordem_visita.append(label)
        print(f"  Visita #{contador:02d} → {label}")

        if not node.is_leaf():
            if node.yes is not None:
                fila.append(node.yes)
                nos_proximo_nivel += 1
            if node.no is not None:
                fila.append(node.no)
                nos_proximo_nivel += 1

        if nos_nivel_atual == 0 and fila:
            nivel_atual += 1
            nos_nivel_atual = nos_proximo_nivel
            nos_proximo_nivel = 0
            print(f"\n  --- Nível {nivel_atual} ---")

    print(f"\n  Total de nós visitados: {contador}")
    return ordem_visita


# ============================================================
# PARTE 5 — Comparação entre BFS e DFS
# ============================================================

def comparar_algoritmos(raiz):
    """
    Executa BFS e DFS na mesma árvore e compara:
    - Ordem de visita dos nós
    - Quantidade de nós explorados
    - Tempo de execução
    """
    print("\n" + "=" * 50)
    print("  COMPARAÇÃO: DFS vs BFS")
    print("=" * 50)

    inicio = time.perf_counter()
    ordem_dfs = dfs(raiz)
    tempo_dfs = time.perf_counter() - inicio

    print()

    inicio = time.perf_counter()
    ordem_bfs = bfs(raiz)
    tempo_bfs = time.perf_counter() - inicio

    print("\n" + "=" * 50)
    print("  RELATÓRIO COMPARATIVO")
    print("=" * 50)

    print(f"\n  {'Métrica':<35} {'DFS':>10} {'BFS':>10}")
    print("  " + "-" * 55)
    print(f"  {'Nós visitados':<35} {len(ordem_dfs):>10} {len(ordem_bfs):>10}")
    print(f"  {'Tempo de execução (ms)':<35} {tempo_dfs*1000:>9.4f} {tempo_bfs*1000:>9.4f}")

    print("\n  Ordem de visita DFS:")
    for i, n in enumerate(ordem_dfs, 1):
        print(f"    {i:02d}. {n}")

    print("\n  Ordem de visita BFS:")
    for i, n in enumerate(ordem_bfs, 1):
        print(f"    {i:02d}. {n}")

    print("\n" + "=" * 50)
    print("  ANÁLISE E RESPOSTAS")
    print("=" * 50)

    analise = """
  1. Qual algoritmo encontra uma resposta mais rápido em árvores PROFUNDAS?
     → DFS, pois desce diretamente por um ramo sem explorar os outros níveis.
       Em uma árvore profunda, o DFS chega a uma folha com muito menos
       iterações do que o BFS, que precisa processar TODOS os nós nível a nível.

  2. Qual algoritmo consome mais MEMÓRIA?
     → BFS, pois precisa armazenar na fila todos os nós de um nível antes
       de descer. Em uma árvore larga, a fila pode crescer exponencialmente.
       O DFS usa uma pilha que cresce apenas com a profundidade do caminho atual.

  3. Em que tipo de problema BFS seria preferível?
     → Quando a solução está próxima da raiz (rasa) ou quando queremos
       garantir o MENOR NÚMERO DE PASSOS para chegar à resposta.
       Exemplo: menor número de perguntas para adivinhar o animal.

  4. Em que tipo de problema DFS seria preferível?
     → Quando a solução está em um nível profundo da árvore, ou quando
       queremos explorar UM caminho completo de cada vez.
       Exemplo: verificar se existe algum caminho válido, resolver labirintos,
       ou quando a memória disponível é limitada.
    """
    print(analise)


# --- Teste rápido ao executar este arquivo diretamente ---
if __name__ == "__main__":
    arvore = construir_arvore()
    comparar_algoritmos(arvore)
