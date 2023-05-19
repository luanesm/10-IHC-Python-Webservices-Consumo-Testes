from flask_restful import Resource, abort, reqparse

bancos = {
    '1': {'Nome': 'MySQL', 'Ano': '1995'},
    '2': {'Nome': 'Oracle', 'Ano': '1978'},
    '3': {'Nome': 'Postgres', 'Ano': '1994'}
}


class BancoTodas(Resource):
    def get(self):
        return bancos


class Banco(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('Nome')
        self.parser.add_argument('Ano')

    def get(self, id):
        if id not in bancos:
            abort(404, message="Banco com o ID {} não encontrado.".format(id))
        return bancos[id]

    def post(self, id):
        if id in bancos:
            abort(400, message="Banco com o ID {} já existe.".format(id))

        args = self.parser.parse_args()
        banco = {'Nome': args['Nome'], 'Ano': args['Ano']}
        bancos[id] = banco
        return {'message': 'Banco adicionado.', 'banco': banco}, 201

    def put(self, id):
        if id not in bancos:
            abort(404, message="Banco com o ID {} não encontrado.".format(id))

        args = self.parser.parse_args()
        bancos[id]['Nome'] = args['Nome']
        bancos[id]['Ano'] = args['Ano']
        return {'message': 'Banco atualizado.', 'banco': bancos[id]}

    def delete(self, id):
        if id not in bancos:
            abort(404, message="Banco com o ID {} não encontrado.".format(id))

        del bancos[id]
        return {'message': 'Banco excluído.'}
