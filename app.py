from flask import Flask, request, render_template, redirect, flash
from models import db, connect_db,Pet
from forms import AddPet

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "sammydog"
connect_db(app)

@app.route('/')
def show_new_snack():
    pets = Pet.query.all()
    return render_template('home.html',pets=pets)

@app.route("/add", methods=['GET','POST'])
def view_AddPetform():
    form = AddPet()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data
        pet = Pet(name=name,species=species,photo_url=photo_url,age=age,notes=notes,available=available)
        db.session.add(pet)
        db.session.commit()
        flash(f"Created a new dog: name is {name} age is {age} species is {species}")
        return redirect('/')
    else:

        return render_template('add_pet_form.html',form=form)
    

@app.route('/pet/<int:pet_id>/edit',methods=["GET","POST"])
def view_pet_edit(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = AddPet(obj=pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect('/')
    else:
        return render_template('edit_pet_form.html',form=form) 