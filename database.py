import sqlalchemy
from sqlalchemy import create_engine, text

#engine = create_engine("mariadb+pymysql://user:pass@some_mariadb/dbname?charset=utf8mb4")

conn_string = "mysql+pymysql://0ms0pp77tssls7xg2bp0:pscale_pw_VAj893PyINRtPzZSW4wbDKHAkGrgVxOrvr5MY39Ki6A@ap-south.connect.psdb.cloud/careers?charset=utf8mb4"
engine = create_engine(conn_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    result_dict_list = []
    for row in result.all():
      result_dict_list.append(row._mapping)

  return result_dict_list
