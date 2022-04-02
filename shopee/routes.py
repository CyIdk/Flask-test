from os import CLD_CONTINUED
from shopee import app
from flask import render_template, url_for, request, redirect, flash
import random
from datetime import *
from shopee.models import Products, Courses, db

products = [
    {
        'pid': 1, 'name': 'apple', 'origin': 'Hong Kong',
        'description': 'big red apple', 'quantity': '10',
        'unit_price': '6.0'
    }
]

@app.route("/")
def home():
    return render_template(
        "home.html"
    )

@app.route('/products')
def index_products():
    prodducts=Products.query.all()
    rows=random.choise(products)
    return render_template(
        'index.html',
        rows=products
    )


@app.route('/products/<int:pid>')
def product_detail(pid):
    
    return render_template(
        'details.html',
        info=Products.query.filter_by(pid=pid).first()
        # info=products[pid]
    )

@app.route("/courses/")
def index_courses():
    return render_template(
        "courses/courses.html",
        courses=Courses.query.all()
    )

@app.route("/courses/<int:c_id>/")
def course_details(c_id):
    return render_template(
        "courses/course_details.html",
        info=Courses.query.filter_by(c_id=c_id).first()
    )

@app.route("/courses/add/", methods=['POST', 'GET'])
def add_course():

    if request.method == "POST":
        c_name = request.form['courseName']
        start_date = date(year=int(request.form['start-year']), 
        month=int(request.form['start-month']), day=int(request.form['start-day']))
        end_date = date(year=int(request.form['end-year']), 
        month=int(request.form['end-month']), day=int(request.form['end-day']))
        instructor = request.form['instructor']
        description = request.form['description']

    course = Courses(c_name=c_name,start_date=start_date, end_date=end_date,
        instructor=instructor, description=description)
    db.session.add(course)
    db.session.commit()

    flash("Record was successfully added.")

    return redirect(url_for('index_courses'))
    # render_template(
    #     "courses/create.html"
    # )

@app.route("/courses/edit/")
def edit_course():
    return render_template(
        "courses/edit.html"
    )

@app.route("/courses/delete/")
def delete_course():
    return "Course Successfully Deleted"
    