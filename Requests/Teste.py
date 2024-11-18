import requests

# requisicao = requests.get("https://testeinstagram-4d882-default-rtdb.firebaseio.com/.json")
# print(requisicao)
# print(requisicao.json())

# informacoes = '{"Nome":"Victor"}'
# requisicao = requests.post("https://testeinstagram-4d882-default-rtdb.firebaseio.com/.json",data=informacoes)
# print(requisicao)
# print(requisicao.json())

informacoes = '{"Nome":"Victor", "Sobrenome":"Antunes","Idade":"21","Curso":"Analise e Desenvolvimento de Sistemas"}'
requisicao = requests.patch("https://testeinstagram-4d882-default-rtdb.firebaseio.com/-OC-hlZGe17CQZZRkP13.json",data=informacoes)
print(requisicao)
print(requisicao.json())

# informacoes = '{"Nome":"Wesley", "Sobrenome":"Silva","Idade":"12"}'
# requisicao = requests.delete("https://testeinstagram-4d882-default-rtdb.firebaseio.com/-OBgJGJ714dEyKnr_aFs.json",data=informacoes)
# print(requisicao)
# print(requisicao.json())

# https://docs.awesomeapi.com.br/api-de-moedas

# https://console.firebase.google.com/project/testeinstagram-4d882/database/testeinstagram-4d882-default-rtdb/data/~2F?hl=pt-br