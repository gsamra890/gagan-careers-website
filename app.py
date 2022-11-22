from flask import Flask, render_template

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Maryland',
  'salary': '$60,000'
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Washington',
  'salary': '$80,000'
}, {
  'id': 3,
  'title': 'Tableau Developer',
  'location': 'Remote',
  'salary': '$100,000'
}, {
  'id': 4,
  'title': 'Python Developer',
  'location': 'Remote'
}]


@app.route("/api/jobs")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Gagan')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
