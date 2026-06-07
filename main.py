import time
import random
import math
import matplotlib.pyplot as plt

from bubble_sort import bubble_sort

def gerar_vetor(n):
    return [random.randint(1, 1_000_000) for _ in range(n)]

# ── Merge Sort inline (com contador resetável) ──────────────
def merge_sort(arr):
    movimentos = [0]
    def _merge(a):
        if len(a) <= 1:
            return a
        mid = len(a) // 2
        left  = _merge(a[:mid])
        right = _merge(a[mid:])
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i]); i += 1
            else:
                result.append(right[j]); j += 1
            movimentos[0] += 1
        result.extend(left[i:])
        result.extend(right[j:])
        movimentos[0] += len(left[i:]) + len(right[j:])
        return result
    resultado = _merge(arr)
    return resultado, movimentos[0]

# ── Quick Sort inline (com contador resetável) ──────────────
def quick_sort(arr):
    trocas = [0]
    def _quick(a):
        if len(a) <= 1:
            return a
        pivot = a[len(a) // 2]
        left   = [x for x in a if x < pivot]
        middle = [x for x in a if x == pivot]
        right  = [x for x in a if x > pivot]
        trocas[0] += len(a)
        return _quick(left) + middle + _quick(right)
    resultado = _quick(arr)
    return resultado, trocas[0]

# ── Execução ─────────────────────────────────────────────────
tamanhos   = [1000, 10000, 100000]
algoritmos = {
    'Bubble Sort': bubble_sort,
    'Merge Sort' : merge_sort,
    'Quick Sort' : quick_sort
}

resultados = {}

print(f"{'Algoritmo':<15} {'Tamanho':>10} {'Exec1(s)':>10} {'Exec2(s)':>10} {'Exec3(s)':>10} {'Média(s)':>10} {'DesvPad':>10} {'Trocas':>12}")
print("-" * 95)

for nome, func in algoritmos.items():
    resultados[nome] = {'tamanhos': [], 'medias': []}
    for tam in tamanhos:
        if nome == 'Bubble Sort' and tam == 100000:
            print(f"{nome:<15} {tam:>10} {'N/C':>10} {'N/C':>10} {'N/C':>10} {'N/C':>10} {'N/C':>10} {'N/C':>12}")
            continue

        vetor_original = gerar_vetor(tam)
        tempos = []
        trocas_total = 0

        for _ in range(3):
            v = vetor_original.copy()
            t0 = time.perf_counter()
            resultado = func(v)
            t1 = time.perf_counter()
            tempos.append(round(t1 - t0, 6))
            if isinstance(resultado, tuple):
                trocas_total = resultado[1]

        media  = round(sum(tempos) / 3, 6)
        desvio = round(math.sqrt(sum((t - media)**2 for t in tempos) / 2), 6)
        print(f"{nome:<15} {tam:>10} {tempos[0]:>10} {tempos[1]:>10} {tempos[2]:>10} {media:>10} {desvio:>10} {trocas_total:>12}")

        resultados[nome]['tamanhos'].append(tam)
        resultados[nome]['medias'].append(media)

# Gráfico
plt.figure(figsize=(10, 6))
for nome, dados in resultados.items():
    plt.plot(dados['tamanhos'], dados['medias'], marker='o', label=nome)

plt.title('Comparação de Algoritmos de Ordenação')
plt.xlabel('Tamanho do vetor')
plt.ylabel('Tempo médio (s)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('grafico_ordenacao.png', dpi=150)
plt.show()
print("Gráfico salvo!")