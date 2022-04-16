#from flaskext.mysql import MySQL
from flask import Flask, render_template, request, redirect, flash, session, send_from_directory

from models import Usuario
from dao import UsuarioDao
from flask_mysqldb import  MySQL

app = Flask(__name__)



app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'mf'
app.config['MYSQL_PORT'] = 3306
db = MySQL(app)
usuario_dao = UsuarioDao(db)


app.secret_key = 'engenharia'



@app.route('/')
def index():
    
    return render_template('Financa_Pessoal.html')



#login 
@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    if proxima == None:
        proxima=''
    return render_template('login.html',proxima=proxima)


#código pra verificar se estar logado
#if 'usuario_logado' not in session or session['usuario_logado']==None:
#    return redirect('/login?proxima=index')


#------------------------------------------------------------------------------
@app.route('/autenticar', methods=['POST',])
def autenticar():
    usuario=usuario_dao.busca_por_id(request.form['usuario'])
    if usuario: 
     if 'usuario._senha' == request.form['senha']:
        session['usuario_logado']=request.form['usuario']
        flash(request.form['usuario'] + 'logado com sucesso!')
        proxima_pagina = request.form['proxima']
        if proxima_pagina == 'None':
            return redirect('/')
        else:    
            return redirect('/{}'.format(proxima_pagina))
    else:
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
    senha = request.form['password']
    email = request.form['email']
    cpf = request.form['cpf']

    cadastro = Usuario(nome,senha,email,cpf)
    return redirect('/login')


#-------------------------------------------------------------------
@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuario logado')
    return redirect('/login')


# Rota para inserir imagens nos html
@app.route('/img/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('img', nome_arquivo)




if __name__ == '__main__':
    app.run(debug=True)    
