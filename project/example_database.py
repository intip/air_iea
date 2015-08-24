import pymssql

# select codfor from e095for where apefor = 'nome do hotel'
# Select UsuIea V099UTU where UsuAma = LRAS


SQL = "SELECT CodFor FROM E095FOR WHERE CodFor = 45"

conn = pymssql.connect(server="SERV-DB", port=1433,
                       user='intip', password='InTiPabc',
                       database="regente",)

print conn
