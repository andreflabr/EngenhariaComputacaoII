
class Usuario:
    def __init__(self, nome, sobrenome, email, senha, id=None):
        self._id=id
        self._nome=nome
        self._sobrenome=sobrenome
        self._email=email
        self._senha=senha
        
# class Usuario:
#     def __init__(self, nome, sobrenome, email, senha, idcliente=None):
#         self._idcliente=idcliente
#         self._nome=nome
#         self._sobrenome=sobrenome
#         self._email=email
#         self._senha=senha
