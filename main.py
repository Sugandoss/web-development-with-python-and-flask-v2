# Lesson1- Step1 and Step 2
#Step 1: Project Setup & Flask Basics
#1. Create a project on GitHub
#2. Open up the project on Replit
#3. Create and run a Flask web server
#4. Push changes back to GitHub

#Step 2 - Web Pages with HTML & CSS
#1. Render templates and use static assets
#2. Create the layout of the page using HTML tags
#3. Style the page using CSS classes, properties, and values
#4. Use the Bootstrap framework for faster development

#Lesson 2 - Flask Templates and Cloud Deployment
#Step 3 - Dynamic Data & Cloud Deployment
#1. Render dynamic data using Jinja template tags

from flask import Flask, render_template

app = Flask(__name__)

open_positions = [{
  'id': 1,
  'title': 'Data Scientist',
  'location': 'Bangalore, India',
  'salary': '1,20,000'
}, {
  'id': 2,
  'title': 'Data Analyst',
  'location': 'Delhi, India',
  'salary': '2,20,000'
}, {
  'id': 3,
  'title': 'Full Stack Developer',
  'location': 'Bangalore, India',
  'salary': '12,20,000'
}, {
  'id': 4,
  'title': 'Backend Engineer',
  'location': 'Remote',
}]


@app.route('/')
def hello_world():
  #return "hello world"
  return render_template("home.html",
                         openpositions=open_positions,
                         company_name="Jovian")


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
