import sqlalchemy
from sqlalchemy import create_engine, text
import os
#engine = create_engine("mariadb+pymysql://user:pass@some_mariadb/dbname?charset=utf8mb4")

conn_string = os.environ['DB_CONN_STRING']
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


def load_job_from_id(id):
  print("inside load jobs from id", id)
  with engine.connect() as conn:
    sql_stmt = f'''select * from jobs where id = {id}'''
    result = conn.execute(text(sql_stmt))
    rows = result.all()
    print("rows", rows)
    if len(rows) == 0:
      return None
    else:
      return rows[0]

def store_form_in_db(job_id, data):
  with engine.connect() as conn:
    sql_stmt= f'''insert into applications(job_id, full_name, email, linkedin_url, education, work_experience, resume_url) values({job_id}, '{data['full_name']}', '{data['email']}', '{data['url']}', '{data['education']}',  '{data['work_experience']}', '{data['resumeurl']}' )'''
    #print(sql_stmt)
    conn.execute(text(sql_stmt))
      
    # conn.execute(sql_stmt, job_id=job_id,
    #              full_name=data['full_name'],
    #              email=data['email'],
    #              linkedin_url=data['url'],
    #              education=data['education'],
    #              work_experience=data['work_experience'],
    #              resume_url=data['resumeurl'])
  