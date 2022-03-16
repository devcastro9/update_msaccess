"""
    Conexion a la base de datos MS Access
"""
import adodbapi as db

def main():
    constr = 'Provider=Microsoft.ACE.OLEDB.12.0;Data Source=PARAMETROS.mdb'
    sql = "select * from gc_parametros_sistema"
    header = '| '
    conn = db.connect(constr)
    with conn.cursor() as c:
        c.execute(sql)
        for d in c.description:
            header += d[0] + ' | '
        print(header)
        result = c.fetchmany(1)
        for i in result:
            print(i)
    conn.close

if __name__ == "__main__":
    main()