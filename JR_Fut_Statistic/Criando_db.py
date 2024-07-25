import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect('simulador_apostas.db')

# Criar um cursor
cursor = conn.cursor()

# Criar uma tabela
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tb_futebol (
        id INTEGER PRIMARY KEY,
        T_DATA                  TEXT(30),
        T_COMPETICAO            TEXT(30),
        T_TIMECASA              TEXT(30),
        N_RESULTADOCASA         INTERGER(10),
        T_TIMEVISITANTE         TEXT(30),
        N_RESULTADOVISITANTE    INTERGER(10),
        T_ESTRATEGIA_MERCADO    TEXT(30),
        N_APOSTA_VALOR          REAL(10),
        N_LUCRO_PREJUIZO        REAL(10),
        N_ODD                   REAL(10), 
        T_RESULTADO             TEXT(10),
        N_ROI                   INTERGER(10)
    )
''')

# Salvar (commit) as mudanças
conn.commit()

# Fechar a conexão
conn.close()