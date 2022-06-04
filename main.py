#from flaskext.mysql import MySQL
from flask import Flask, render_template, request, redirect, flash, session, send_from_directory
from markupsafe import re

from dao import UsuarioDao, DespesasDao, EntradaDao
from flask_mysqldb import  MySQL

from models import Usuario, Despesas, Entrada

app = Flask(__name__)
app.secret_key = 'engenharia'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'mf'
app.config['MYSQL_PORT'] = 3306
db = MySQL(app)
usuario_dao = UsuarioDao(db)
despesas_dao = DespesasDao(db)
entrada_dao = EntradaDao(db)



@app.route('/')
@app.route('/index')
def index():
    lista = despesas_dao.listar()
    
    return render_template('Dashboard.html',despesas = lista)




#login 
@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    if proxima == None:
        proxima=''
    return render_template('login.html',proxima=proxima)





#------------------------------------------------------------------------------
@app.route('/autenticar', methods=['POST',])
def autenticar():    
    usuario=usuario_dao.busca_por_id(request.form['usuario'])
    if usuario: 
        if usuario._senha == request.form['senha']:
            session['usuario_logado']=request.form['usuario']            
            session['cliente_id'] = usuario._id           
            flash(request.form['usuario'] + ' logado com sucesso!','sucesso')
            proxima_pagina = request.form['proxima']
            if proxima_pagina == 'None':
                return redirect('/')
            else:    
                return redirect('/{}'.format(proxima_pagina))
    
    flash('Não logado, tente novamente')
    return render_template('/login')    
#-------------------------------------------------------------------

#REGISTRO DE USUÁRIO
@app.route('/registro')
def registro():
    proxima2= request.args.get('proxima2')
    return render_template('Novo_Cadastro.html',proxima2=proxima2)

#Crud - create do usuario
@app.route('/salvarUsuario', methods=['POST',])
def salvarUsuario():
    
    nome = request.form['name']
    sobrenome = request.form['lastname']
    email = request.form['email']
    senha = request.form['password']
    # nome = request.form['name']
    # sobrenome = request.form['lastname']
    # usuario = request.form['username']
    # email = request.form['email']
    # senha = request.form['password']
    

    cadastro = Usuario(nome,sobrenome,email,senha)
    
    usuario_dao.salvar(cadastro)
    return redirect('/login')


#-------------------------------------------------------------------
@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    
    flash('Nenhum usuario logado','error')
    return redirect('/login')


# Rota para inserir imagens nos html
@app.route('/img/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('img', nome_arquivo)
#------------------------------------------------------------------
@app.route('/transacoes')

def transacoes():
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect('/login?proxima=index')
    #flash('Transação feita com sucesso','sucesso')
    return render_template('transacoes.html',titulo = 'Adicione valores')

#---------------------------------------------------------------
#Saldo
# @app.route('/saldo')
# def saldo():
#     return render_template('Saldo.html',titulo = "Insira seu saldo")

#Crud - create do saldo
# @app.route('/salvarSaldo', methods=['POST',])
# def salvarSaldo():
#     # tipo = request.form['tipo']
#     # valor = request.form['valor']

#     saldo = Saldo(tipo,valor)

#-----------------despesas--------------------------------
#Despesas
@app.route('/despesas')


def despesas():
    #código pra verificar se estar logado
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect('/login?proxima=index')
   
    return render_template('despesas.html', titulo = "Gerencie suas despesas")

@app.route('/salvarDespesas', methods=['POST',])
def salvarDespesas():
    
    tipo = request.form['tipo']
    valor = request.form['valor']
    data = request.form['data']
    clienteId = session['cliente_id']
    print(clienteId)
    
    #despesas = Despesas(tipo,valor,data,clienteId)   
    #print (despesas._tipo,despesas._valor,despesas._data)
    #despesas_dao.salvar(despesas)
    flash(' Despesa salva com sucesso!','sucesso')
    return redirect('/despesas')

#deletar despesas
@app.route('/deletar/<int:id>')
def deletar(id):
    despesas_dao.deletar(id)
    return redirect('/')
#--------------------------------------------------
#update despesas
@app.route('/editar/<int:id>')
def editar(id):
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect('/login?proxima=editar')
    lista = despesas_dao.busca_por_id(id)    
    return render_template('editarDespesas.html', titulo = 'Editar despesas!',despesas = lista)  
    
@app.route('/editarDespesas', methods=['POST',])
def atualizar():
    
    tipo = request.form['tipo']
    valor = request.form['valor']
    data = request.form['data']
    id = request.form['id']
    despesas = Despesas(tipo,valor,data,id)
    
    despesas_dao.salvar(despesas)
    flash(' Despesa atualizada com sucesso!','sucesso')
    return redirect('/')      

#-----------------Entradas--------------------------------
#entradas
@app.route('/entradas')
def entrada():
    #código pra verificar se estar logado
    if 'usuario_logado' not in session or session['usuario_logado']==None:
        return redirect('/login?proxima=index')
   
    return render_template('entradas.html', titulo = "Gerencie suas Entradas")

@app.route('/salvarEntrada', methods=['POST',])
def salvarEntrada():
    
    tipo_entrada = request.form['tipo_entrada']
    valor_entrada = request.form['valor_entrada']
    data_entrada = request.form['data_entrada']
    
    entrada = Entrada(tipo_entrada,valor_entrada,data_entrada)
    
    entrada_dao.salvar(entrada)
    flash(' Entrada salva com sucesso!','sucesso')
    return redirect('/')  




if __name__ == '__main__':
    app.run(debug=True)    
 

 
