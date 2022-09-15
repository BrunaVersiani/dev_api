from flask_restful import Resource
from flask import request
import json

lista_habilidades = ['Python', 'Java', 'Flask', 'Django', 'CShap']


class Habilidades(Resource):
    def get(self):
        return lista_habilidades

    def put(self, id):
        dados = json.loads(request.data)
        lista_habilidades[id] = dados
        return dados

    def delete(self, id):
        lista_habilidades.pop(id)
        return {'status': 'sucesso', 'messagem': 'Registro excluido'}

    def post(self):
        dados = json.loads(request.data)
        posicao = len(lista_habilidades)
        dados['id'] = posicao
        lista_habilidades.append(dados)
        return lista_habilidades[posicao]
