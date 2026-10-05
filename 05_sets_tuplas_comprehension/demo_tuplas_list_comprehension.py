temperaturas = [
    ("Vitória", 32.5),
    ("São Paulo", 18.0),
    ("Manaus", 35.0),
    ("Curitiba", 12.5),
    ("Salvador", 29.0),
]

cidades_quentes = [cidade for cidade, temp in temperaturas if temp > 25]

print(cidades_quentes)

temperaturas_fahrenheit = [(temp * 9/5) + 32 for cidade, temp in temperaturas]

print(temperaturas_fahrenheit)

resumo_quente = [f"{cidade}: {temp}ºC" for cidade, temp in temperaturas if temp > 25]

print(resumo_quente)