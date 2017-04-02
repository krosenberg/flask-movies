from flask import Flask, render_template, request, redirect
from database import Database

app = Flask(__name__)
app.config.from_pyfile('server.cfg')

"""
Use the following commands to interact with the database:
  db.get() to get all of the reviews
  db.get(id) to get a single review
  db.create(title, text, rating) to add a new review. An id will be created automatically
  db.update(id, title, text, rating) to update a review. Must pass in all fields
  db.delete(id) to delete a review
"""
db = Database(app)

@app.route('/')
def show_all_reviews():
	return render_template('list.html', reviews=db.get())

@app.route('/<id>')
def single_review(id):
	return render_template('single.html', review=db.get(id))

@app.route('/new', methods=['GET', 'POST'])
def new_review():
	if request.method == 'GET':
		return render_template('form.html', new=True)
	else:
		title = request.form['title']
		rating = request.form['rating']
		text = request.form['text']
		db.create(title, text, rating)
		return redirect('/')

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit_review(id):
	if request.method == 'GET':
		r = db.get(id)
		return render_template(
			'form.html',
			new=False,
			id=r.id,
			rating=r.rating,
			title=r.title,
			text=r.text
		)
	else:
		id
		title = request.form['title']
		rating = request.form['rating']
		text = request.form['text']
		db.update(id, title, text, rating)
		return redirect('/')

@app.route('/delete/<id>', methods=['DELETE'])
def delete_review(id):
	db.delete(id)
	return 'Review was deleted'

if __name__ == '__main__':
	app.run(host="0.0.0.0")
