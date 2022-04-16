from models Usuario

SQL_CRIA_CLIENTE = 'INSERT into cliente (nome,senha,email,cpf) values (%s,%s,%s,%s)'
SQL_DELETA_CLIENTE = 'DELETE from cliente where id=%s'
SQL_ATUALIZA_CLIENTE = 'UPDATE cliente SET nome=%s, senha=%s, email=%s, cpf=%s where id=%s '

class UsuarioDao:
    def __init__(self,db):
        self.__db=db

        def salvar(self,cliente):
        cursor = self.__db.connection.cursor()

        if(cliente._id):
            cursor.execute(SQL_ATUALIZA_CLIENTE,(cliente._nome,cliente._senha,cliente._email, cliente._cpf,cliente._id))
        else:
             cursor.execute(SQL_CRIA_CLIENTE,(cliente._nome,cliente._senha,cliente._email, cliente._cpf))
             cursor._id = cursor.lastrowid

        self.__db.connection.commit()
        return cliente    