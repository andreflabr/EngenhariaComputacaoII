from models import Usuario, Despesas

SQL_CRIA_CLIENTE = 'INSERT into cliente (nome,sobrenome,email,senha) values (%s, %s, %s, %s)'
SQL_DELETA_CLIENTE = 'DELETE from cliente where id=%s'
SQL_ATUALIZA_CLIENTE = 'UPDATE cliente SET nome=%s,sobrenome=%s,usuario=%s,email=%s, senha=%s where id=%s '
SQL_USUARIO_POR_ID = 'SELECT idcliente,nome,sobrenome,email,senha from cliente where email=%s '
SQL_BUSCA_CLIENTE = 'SELECT id,nome,sobrenome,usuario,email,senha from cliente where id=%s '
#-----------------------------------------------------------------------------------------------------
SQL_ATUALIZA_DESPESAS = ''
SQL_CRIA_DESPESAS = 'INSERT into despesas (valor, dta_vencimento,tipodesp_idtipo) values (%s, %s, %s)'
SQL_DELETA_DESPESAS = 'DELETE from despesas where iddespesas=%s'


def traduz_usuario(tupla):    
   # return Usuario(tupla[1],tupla[2],tupla[3],tupla[4],tupla[5],tupla[0])
   return Usuario(tupla[1],tupla[2],tupla[3],tupla[4], tupla[0])
    
class UsuarioDao:
    
    
    def busca_por_id(self,email):
        cursor = self.__db.connection.cursor()
        cursor.execute(SQL_USUARIO_POR_ID,(email,))
        dados = cursor.fetchone()
        cliente = traduz_usuario(dados) if dados else None
        return cliente
          

    def __init__(self,db):
        self.__db=db
        #cria e atualiza usuario
    def salvar(self,cliente):
        cursor = self.__db.connection.cursor()

        if(cliente._id):
            #cursor.execute(SQL_ATUALIZA_CLIENTE,(cliente._idcliente,cliente._nome,cliente._sobrenome,cliente._email,cliente._senha, cliente._id))
            cursor.execute(SQL_ATUALIZA_CLIENTE,(cliente._nome,cliente._sobrenome,cliente._email,cliente._senha, cliente._id))
        else:
            cursor.execute(SQL_CRIA_CLIENTE,(cliente._nome,cliente._sobrenome,cliente._email,cliente._senha))
            #cursor.execute(SQL_CRIA_CLIENTE,(cliente._nome,cliente._sobrenome,cliente._usuario,cliente._email,cliente._senha))
            cursor._id = cursor.lastrowid

        self.__db.connection.commit()
        
        return cliente     
    #Deleta usuario
    def deletar_usuario(self,id):
        self.__db.connection.cursor().execute(SQL_DELETA_CLIENTE,(id,))
        self.__db.connection.commit()               


class DespesasDao:  
    def __init__(self,db):
        self.__db=db         
        
    def salvar(self,despesas):
        cursor = self.__db.connection.cursor()

        if(despesas._id):
           
            cursor.execute(SQL_ATUALIZA_DESPESAS,(despesas._tipo,despesas._valor,despesas._data, despesas._id))
        else:
            cursor.execute(SQL_CRIA_DESPESAS,(despesas._valor,despesas._data,despesas._tipo))
           
            cursor._id = cursor.lastrowid

        self.__db.connection.commit()
        
        return despesas