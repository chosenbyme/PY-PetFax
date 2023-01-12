from flask import ( Blueprint, render_template )
bp = Blueprint(
    'fact',
    __name__,
    url_prefix="/fact"
)


@bp.route('/')
def show_fact():
    return render_template('fact.html')

@bp.route('/new')
def new_fact():
    return render_template('new.html')