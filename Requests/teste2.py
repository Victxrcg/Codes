# from InquirerPy import inquirer

# # Pergunta de texto
# nome = inquirer.text("Qual é o seu nome?").execute()

# # Pergunta de seleção
# cor = inquirer.select("Qual é a sua cor favorita?", choices=["Azul", "Verde", "Vermelho"]).execute()

# # Pergunta de confirmação
# continuar = inquirer.confirm("Você deseja continuar?").execute()

# # Exibe as respostas
# print(f"Nome: {nome}")
# print(f"Cor favorita: {cor}")
# print(f"Deseja continuar? {continuar}")


from InquirerPy import inquirer

idade = inquirer.password("Qual é a sua idade?").execute()

