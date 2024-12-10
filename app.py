from flask import Flask, render_template, request, redirect, url_for
from markupsafe import Markup
import re
from config import Config
from models import db, Entry

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

URL_REGEX = re.compile(r'(https?://[^\s]+)')

def make_links(text):
    return Markup(re.sub(URL_REGEX, r'<a href="\1" target="_blank">\1</a>', text))

@app.route('/')
def index():
    entries = Entry.query.all()
    return render_template('index.html', entries=entries, make_links=make_links)

@app.route('/add', methods=['GET', 'POST'])
def add_entry():
    if request.method == 'POST':
        date = request.form['date']
        content = request.form['content']
        new_entry = Entry(date=date, content=content)
        db.session.add(new_entry)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_entry.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_entry(id):
    entry = Entry.query.get_or_404(id)
    if request.method == 'POST':
        entry.date = request.form['date']
        entry.content = request.form['content']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit_entry.html', entry=entry)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_entry(id):
    entry = Entry.query.get_or_404(id)
    db.session.delete(entry)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
