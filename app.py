from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import New_Pet, Edit_Pet
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'secret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


connect_db(app)

@app.route('/')
def home():
    """Show the homepage sorted by availability and alphabetically"""
    pets = Pet.query.order_by(Pet.available.desc(), Pet.name).all()
    return render_template('home.html', pets=pets)

@app.route('/add', methods=['GET','POST'])
def add_pet():
    """Show the Add Pet Form and handle the post request"""
    form = New_Pet()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        with app.app_context():
            db.session.add(new_pet)
            db.session.commit()
        return redirect('/')

    else:
        return render_template('add_pet.html', form=form)

@app.route('/<int:pet_id>', methods=['GET','POST'])
def show_pet_details(pet_id):
    """Show details of each pet as well as the edit form"""
    pet = Pet.query.get(pet_id)
    form = Edit_Pet(obj=pet)
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.add(pet)
        db.session.commit()
        flash('Pet updated','notif')
        return redirect(f'/{pet.id}') 
    else:
        return render_template('pet_details.html', pet=pet, form=form)
