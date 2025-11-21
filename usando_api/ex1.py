import requests

# URL do endpoint para criar uma nova postagem
url = "https://jsonplaceholder.typicode.com/posts"

# Dados que queremos enviar para o servidor (em formato de dicionário Python)
new_post_data = {
    "title": "Minha Nova Postagem via Python",
    "body": "Este é o corpo da postagem criada com a biblioteca Requests.",
    "userId": 1 
}

# Faz a requisição POST, passando os dados no parâmetro 'json'
response = requests.post(url, json=new_post_data)

# Um Status 201 significa "Created" (Criado)
if response.status_code == 201:
    created_resource = response.json()
    print("Recurso criado com sucesso (Status 201 Created)!")
    print("-" * 35)
    print(f"ID Atribuído pela API: {created_resource['id']}")
    print(f"Título Enviado: {created_resource['title']}")
else:
    print(f"Erro ao criar o recurso! Código de Status: {response.status_code}")