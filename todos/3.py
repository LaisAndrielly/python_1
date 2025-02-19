import json

# Exemplo de dados em JSON (faturamento diário)
dados_faturamento = '''{
    "faturamento_diario": [
        {"dia": 1, "valor": 200},
        {"dia": 2, "valor": 300},
        {"dia": 3, "valor": 250},
        {"dia": 4, "valor": 400},
        {"dia": 5, "valor": 150},
        {"dia": 6, "valor": 0},
        {"dia": 7, "valor": 100},
        {"dia": 8, "valor": 450},
        {"dia": 9, "valor": 350}
    ]
}'''

dados = json.loads(dados_faturamento)


valores = [item['valor'] for item in dados['faturamento_diario'] if item['valor'] > 0]
menor_faturamento = min(valores)
maior_faturamento = max(valores)
media_faturamento = sum(valores) / len(valores)


dias_acima_da_media = len([valor for valor in valores if valor > media_faturamento])


print(f"Menor faturamento: R${menor_faturamento}")
print(f"Maior faturamento: R${maior_faturamento}")
print(f"Dias acima da média: {dias_acima_da_media}")
