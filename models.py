
class Usuario:
    def __init__(self, nome, sobrenome, email, senha, id=None):
        self._id=id
        self._nome=nome
        self._sobrenome=sobrenome
        self._email=email
        self._senha=senha

class Despesas:
    def __init__(self,tipo,valor,data,clienteId=None,id=None):
        self._id = id
        self._tipo = tipo
        self._valor = valor
        self._data = data
        self._clienteId = clienteId

class Entrada:
    def __init__(self,tipo_entrada,valor_entrada,data_entrada,id=None):
        self._id = id
        self._tipo_entrada = tipo_entrada
        self._valor_entrada = valor_entrada
        self._data_entrada = data_entrada

        
        
      