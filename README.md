# Lista 10 — Análise Experimental de Algoritmos de Ordenação

Trabalho prático da disciplina **Fundamentos da Teoria da Computação e Análise de Algoritmos**  
PUC-Campinas — Engenharia de Software — Prof. José Guilherme Picolo

**Autores:**  
Hugo Daniel Bosada Rodrigues — RA: 23909586  
Letícia Lima da Silva — RA: 23918691

---

## Algoritmos implementados

| Algoritmo | Complexidade média | Complexidade pior caso |
|---|---|---|---|
| Bubble Sort | O(n²) | O(n²) | 
| Merge Sort | O(n log n) | O(n log n) |
| Quick Sort | O(n log n) | O(n²) |

---

## Como executar

### Pré-requisitos
- Python 3.x instalado
- Biblioteca matplotlib

### Instalando dependências
```bash
pip install matplotlib
```

### Clonando o repositório
```bash
git clone https://github.com/seu-usuario/lista10-ordenacao
cd lista10-ordenacao
```

### Rodando
```bash
python main.py
```

O programa vai:
1. Gerar vetores aleatórios de 1.000, 10.000 e 100.000 elementos
2. Rodar cada algoritmo 3 vezes por tamanho
3. Exibir no terminal os tempos de execução, média, desvio padrão e trocas
4. Gerar o arquivo `grafico_ordenacao.png` com a comparação visual

---

## Estrutura do projeto

```
lista10-ordenacao/
├── bubble_sort.py    # Bubble Sort — Hugo
├── merge_sort.py     # Merge Sort — Hugo
├── quick_sort.py     # Quick Sort — Letícia
└── main.py           # Execução dos testes e geração do gráfico- Hugo e Letícia
```
