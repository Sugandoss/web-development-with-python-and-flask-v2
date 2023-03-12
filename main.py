from flask import Flask, render_template, jsonify, request
from database import load_jobs, load_job_from_id, store_form_in_db

app = Flask(__name__)

# open_positions = [{
#   'id': 1,
#   'title': 'Data Scientist',
#   'location': 'Bangalore, India',
#   'salary': '1,20,000'
# }, {
#   'id': 2,
#   'title': 'Data Analyst',
#   'location': 'Delhi, India',
#   'salary': '2,20,000'
# }, {
#   'id': 3,
#   'title': 'Full Stack Developer',
#   'location': 'Bangalore, India',
#   'salary': '12,20,000'
# }, {
#   'id': 4,
#   'title': 'Backend Engineer',
#   'location': 'Remote',
# }]


@app.route('/')
def jovian_careers():
  #return "hello world"
  return render_template("home.html",
                         openpositions=load_jobs(),
                         company_name="Jovian")


# The above jovian_careers() function returns a html page
# If we want a json or api format, we can use jsonify
@app.route('/api/openpositions')
def json_format_jovian_careers():
  jobs = load_jobs()
  return jsonify(jobs)


#Here, <id> takes the id from the browser as the user request
@app.route("/job/<id>")
def show_jobs(id):

  # return jsonify(load_job_from_id(id))
  jobs = load_job_from_id(id)
  if not jobs:
    return "Not Found", 404
  return render_template("jobpage.html", job=jobs)

@app.route("/api/job/<id>")
def show_json_format_job(id):
  jobs = load_job_from_id(id)
  return jsonify(jobs)

  
@app.route("/job/<id>/apply", methods=['post'])
def show_form(id):
  #Get all the arguments after `?` from the browser url after submitting the form
  #data = request.args
  #request.form is being used when we use methods=['post']
  data = request.form
  jobs = load_job_from_id(id)
  store_form_in_db(id, data)
  return render_template("application_submitted.html",
                         application=data,
                         job=jobs)
  #return jsonify(data)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
