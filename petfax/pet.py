from flask import ( Blueprint, render_template )
import json
bp = Blueprint(
    'pet',
    __name__,
    url_prefix="/pets"
)

@bp.route('/')
def index():
    return render_template('index.html',pets=pets)

@bp.route('/<int:pet_id>')
def show_pet(pet_id):
    pet = pets[pet_id-1]
    return render_template('show.html',pet=pet)

@bp.route('/new')
def new_pet():
    return render_template('new.html')
pets = json.load(open('pets.json'))