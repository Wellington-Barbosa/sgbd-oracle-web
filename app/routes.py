from flask import current_app as app
from flask import render_template, request, redirect, url_for, flash
from tnsnames_parser import extrair_dados_tnsnames
import cx_Oracle

@app.route('/', methods=['GET', 'POST'])
def login():
    tnsnames_path = 'C:/Users/wellington.barbosa/Documents/GitHub/sgbd-oracle-web/app/files/TNSNAMES.ora'  # Altere para o caminho correto
    databases = extrair_dados_tnsnames(tnsnames_path)

    # Converta a lista de dicionários em um dicionário onde a chave é o nome do banco de dados
    databases_dict = {db['NOME']: {'host': db['HOST'], 'port': db['PORT']} for db in databases}

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        database = request.form['database']

        db_info = databases_dict.get(database)
        if db_info:
            dsn = cx_Oracle.makedsn(db_info['host'], db_info['port'], service_name=database)
            try:
                connection = cx_Oracle.connect(username, password, dsn)
                flash('Conectado com sucesso!', 'success')
                return redirect(url_for('dashboard'))
            except cx_Oracle.DatabaseError as e:
                flash(f'Erro ao conectar: {str(e)}', 'danger')
        else:
            flash('Banco de dados não encontrado.', 'danger')

    return render_template('index.html', databases=databases_dict.keys())

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/list_tables')
def list_tables():
    # Lógica para listar tabelas do banco de dados
    return render_template('list_tables.html')

@app.route('/execute_query', methods=['GET', 'POST'])
def execute_query():
    # Lógica para executar uma consulta
    return render_template('execute_query.html')

@app.route('/logout')
def logout():
    # Lógica para logout e redirecionamento para a tela de login
    return redirect(url_for('login'))
