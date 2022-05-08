from models import Usuario

SQL_CRIA_CLIENTE = 'INSERT into cliente (nome,sobrenome,usuario,email,senha) values (%s, %s, %s, %s, %s)'
SQL_DELETA_CLIENTE = 'DELETE from cliente where id=%s'
SQL_ATUALIZA_CLIENTE = 'UPDATE cliente SET nome=%s,sobrenome=%s,usuario=%s,email=%s, senha=%s where id=%s '

SQL_USUARIO_POR_ID = 'SELECT idcliente,nome,sobrenome,usuario,email,senha from cliente where email=%s '
SQL_BUSCA_CLIENTE = 'SELECT id,nome,sobrenome,usuario,email,senha from cliente where id=%s '
#SQL_BUSCA_POR_ID ='SELECT id,nome,sobrenome,usuario,email,senha from cliente where id=%s'



def traduz_usuario(tupla):
    return Usuario(tupla[0],tupla[4],tupla[5])
    
class UsuarioDao:
    #Busca por id
    def busca_por_id(self,email):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_USUARIO_POR_ID,(email))
        dados = cursor.fetchone()
        cliente = traduz_usuario(dados) if dados else None
        return cliente 
        #return None  

    def __init__(self,db):
        self.__db=db
        #cria e atualiza usuario
    def salvar(self,cliente):
        cursor = self.__db.connection.cursor()

        if(cliente._id):
            cursor.execute(SQL_ATUALIZA_CLIENTE,(cliente._nome,cliente._sobrenome,cliente._usuario,cliente._email,cliente._senha, cliente._id))
        else:
            cursor.execute(SQL_CRIA_CLIENTE,(cliente._nome,cliente._sobrenome,cliente._usuario,cliente._email,cliente._senha))
            cursor._id = cursor.lastrowid

        self.__db.connection.commit()
        
        return cliente     
    #Deleta usuario
    def deletar_usuario(self,id):
        self.__db.connection.cursor().execute(SQL_DELETA_CLIENTE,(id,))
        self.__db.connection.commit()               

           
        
          