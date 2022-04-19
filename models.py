
class Usuario:
    def __init__(self,nome,senha,email,id=None):
        self._id=id
        self._nome=nome
        self._senha=senha
        self._email=email

