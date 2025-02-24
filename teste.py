def exibir_texto(data_extenso, *args, **kwargs):
    text = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    message = f"{data_extenso}\n\n{text}\n\n{meta_dados}"
    print(message)


exibir_texto(
    "Segunda-feira, 24 de fevereiro 2025",
    "teste",
    "teste",
    "teste",
    "teste",
    "teste",
    "teste",
    "teste",
    "teste",
    "teste",
    autor = "Marcos",
    ano = 1999
)