from flask import current_app as app
from flask import session, render_template, request, redirect, url_for, flash
from tnsnames_parser import extrair_dados_tnsnames
import oracledb

# Habilita o modo thick, necessário para suportar versões antigas do Oracle Database
oracledb.init_oracle_client(lib_dir=r"C:\instantclient_23_4")  # Altere para o caminho correto do Instant Client

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        session.pop('message', None)  # Certifique-se de limpar qualquer mensagem anterior ao acessar a tela de login

    message = session.pop('message', None)  # Retira a mensagem da sessão se houver
    tnsnames_path = 'C:/Users/wellington.barbosa/Documents/GitHub/sgbd-oracle-web/app/files/TNSNAMES.ora'
    databases = extrair_dados_tnsnames(tnsnames_path)

    databases_dict = {db['NOME']: {'host': db['HOST'], 'port': db['PORT'], 'service_name': db['SERVICE_NAME']} for db in databases}

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        database = request.form['database']

        db_info = databases_dict.get(database)
        if db_info:
            dsn = f"(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST={db_info['host']})(PORT={db_info['port']}))(CONNECT_DATA=(SERVICE_NAME={db_info['service_name']})))"
            try:
                connection = oracledb.connect(user=username, password=password, dsn=dsn)
                flash('Conectado com sucesso!', 'success')
                return redirect(url_for('dashboard'))
            except oracledb.DatabaseError as e:
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
    # Limpa a sessão do usuário
    session.clear()
    session['message'] = 'Logout realizado com sucesso!'
    return redirect(url_for('login'))

