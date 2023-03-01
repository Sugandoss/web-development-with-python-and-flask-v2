from flask import Flask, render_template, jsonify
from database import load_jobs, load_job_from_id

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
  print("id in show jobs", id)
  # return jsonify(load_job_from_id(id))
  jobs = load_job_from_id(id)
  if not jobs:
    return "Not Found", 404
  return render_template("jobpage.html", job=jobs)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
