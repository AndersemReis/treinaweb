from urllib import response
import requests
import json


def listar_tarefas():
    response = requests.get("http://localhost:3002/api/teste-consumo")
    tarefas = json.loads(response.content)
    print(response.content)
    return tarefas

def listar_tarefa_id(id):
    response = requests.get("http://localhost:3002/api/teste-consumo?id={id}")
    tarefa = json.loads(response.content)
    return tarefa

