import oracledb

def conectar_oracle():
    user = 'rm570841'
    dsn = 'oracle.fiap.com.br:1521/orcl'
    password = input('Informe a sua senha: ')
    try:
        conn = oracledb.connect(user=user, dsn=dsn, password=password)
        print('Conectado com sucesso!')
        return conn
    except Exception as erro:
        print(f'Erro ao conectar: {erro}')
        return None

def testar_conexao():
    conn = conectar_oracle()
    if conn:
        cursor = conn.cursor()
        cursor.execute('SELECT sysdate FROM dual')
        resultado = cursor.fetchone()
        print(f'Teste ok: {resultado[0]}')
        cursor.close()
        conn.close()


if __name__ == '__main__':
    print('Teste')
    testar_conexao()