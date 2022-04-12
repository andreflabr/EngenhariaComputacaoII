from flaskext.mysql import MySQL
from flask import Flask, render_template, request, redirect, flash, session, send_from_directory


app = Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'mf'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()


app.secret_key = 'engenharia'

@app.route('/')
def index():
    cursor.execute('select * from cliente')
    data = cursor.fetchone()
    print(data)
    return render_template('Financa_Pessoal.html')



#login 
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'mestra' == request.form['senha']:
        session['usuario_logado']=request.form['usuario']
        flash(request.form['usuario'] + 'logado com sucesso!')
        return redirect('/')
    else:
        flash('Não logado, tente novamente')
        return render_template('/login.html')    

@app.route('/Novo_Cadastro')
def NovoCadastro():
    return render_template('Novo_Cadastro.html')


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
