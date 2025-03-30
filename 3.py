import json

# Exemplo de dados em JSON
dados = '''
[
    {"dia": 1, "valor": 22174.1664},
    {"dia": 2, "valor": 24537.6698},
    {"dia": 3, "valor": 26139.6134},
    {"dia": 4, "valor": 0.0},
    {"dia": 5, "valor": 0.0},
    {"dia": 6, "valor": 26742.6612},
    {"dia": 7, "valor": 0.0}
]
'''

faturamento = json.loads(dados)

# Filtrar dias com faturamento
valores = [dia["valor"] for dia in faturamento if dia["valor"] > 0]

# Cálculos
menor = min(valores)
maior = max(valores)
media = sum(valores) / len(valores)
dias_acima_media = len([v for v in valores if v > media])

print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")
print(f"Dias acima da média: {dias_acima_media}")
print(f"Média: {media:.2f}")
print(f"Total: {sum(valores)}")
print(f"Percentual total: {100.00:.2f}%")
print(f"Percentual de cada estado:")


