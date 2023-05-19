from flask import Flask
from flask_restful import Api
from BancoRest import BancoTodas, Banco

app = Flask(__name__)
api = Api(app)

api.add_resource(BancoTodas, '/bancos')
api.add_resource(Banco, '/bancos/<string:id>')

if __name__ == '__main__':
    app.run(debug=True)
