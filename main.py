import time
import random
import math
import matplotlib.pyplot as plt

from bubble_sort import bubble_sort
from merge_sort  import merge_sort, movimentos as mov_merge
from quick_sort  import quick_sort

def gerar_vetor(n):
    return [random.randint(1, 1_000_000) for _ in range(n)]

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