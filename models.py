
class Usuario:
    def __init__(self, nome, sobrenome, email, senha, id=None):
        self._id=id
        self._nome=nome
        self._sobrenome=sobrenome
        self._email=email
        self._senha=senha



class Despesas:
     def __init__(self,tipo,valor,data,id=None):
        self._id = id
        self._tipo = tipo
        self._valor = valor
        self._data = data
        
        
        
        
        
    #                                    0
    # def __init__(self,tipo,valor,data,id=None):
    #     self._tipo = tipo
    #     self._valor = valor
    #     self._data = data
    #     self._id = id