import pymysql

mysql_host = 'localhost'
mysql_conn = pymysql.connect(
  host=mysql_host,
  port=3306,
  user='root',
  passwd='Y$p98@bc',
  db='blog_db',
  charset='utf8'

)

def conn_mysqldb():
  if not mysql_conn.open:
    mysql_conn.ping(reconnect=True)
  return mysql_conn