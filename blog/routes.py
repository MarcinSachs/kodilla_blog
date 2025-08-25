
from flask import render_template, redirect, request, url_for, flash, session
from blog import app
from blog.forms import EntryForm
from blog.models import Entry, db

from blog.forms import LoginForm
import functools


def login_required(view_func):
    @functools.wraps(view_func)
    def check_permissions(*args, **kwargs):
        if session.get('logged_in'):
            return view_func(*args, **kwargs)
        return redirect(url_for('login', next=request.path))
    return check_permissions


@app.route("/")
def index():
    all_posts = Entry.query.filter_by(
        is_published=True).order_by(Entry.pub_date.desc())
    return render_template("homepage.html", all_posts=all_posts)


@app.route("/new-post", methods=["GET", "POST"])
@app.route("/edit-post/<int:entry_id>", methods=["GET", "POST"])
@login_required
def create_or_edit_entry(entry_id=None):
    if entry_id:  # Edycja istniejącego posta
        # Używamy get_or_404 zamiast filter_by.first_or_404()
        entry = Entry.query.get_or_404(entry_id)
        form = EntryForm(obj=entry)
    else:  # Tworzenie nowego posta
        entry = None
        form = EntryForm()

    if form.validate_on_submit():
        if entry:  # Edycja
            # Populate zamiast przypisywania poszczególnych pól
            form.populate_obj(entry)
            flash("Post updated successfully!", "success")
        else:  # Tworzenie
            new_entry = Entry(
                title=form.title.data,
                body=form.body.data,
                is_published=form.is_published.data
            )
            db.session.add(new_entry)
            flash("New post created successfully!", "success")

        db.session.commit()
        return redirect(url_for("index"))
    # Przekazujemy entry_id do szablonu
    return render_template("entry_form.html", form=form, entry_id=entry_id)


@app.route("/login/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    errors = None
    next_url = request.args.get('next')
    if request.method == 'POST':
        if form.validate_on_submit():
            session['logged_in'] = True
            session.permanent = True  # Use cookie to store session.
            flash('You are now logged in.', 'success')
            return redirect(next_url or url_for('index'))
        else:
            errors = form.errors
    return render_template("login_form.html", form=form, errors=errors)


@app.route('/logout/', methods=['GET', 'POST'])
def logout():
    if request.method == 'POST':
        session.clear()
        flash('You are now logged out.', 'success')
    return redirect(url_for('index'))
