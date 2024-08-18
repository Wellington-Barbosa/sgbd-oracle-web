from flask import current_app as app
from flask import render_template, request, redirect, url_for, flash
from .models import parse_tnsnames
import cx_Oracle

@app.route('/', methods=['GET', 'POST'])
def login():
    # Mapeando o caminho do arquivo TNSNAMES.ora
    tnsnames_path = 'C:/Oracle64/product/11.2.0/client_1/network/admin/TNSNAMES.ora'
    databases = parse_tnsnames(tnsnames_path)

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        database = request.form['database']

        dsn = cx_Oracle.makedsn(DB_HOST, DB_PORT, service_name=database)
        try:
            connection = cx_Oracle.connect(username, password, dsn)
            flash('Conectado com sucesso!', 'success')
            # Redirecionando para outra página ou prossiga com a aplicação
        except cx_Oracle.DatabaseError as e:
            flash(f'Erro ao conectar: {str(e)}', 'danger')

    return render_template('index.html', databases=databases)