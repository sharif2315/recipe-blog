from flask import render_template
from app.dashboard import bp


@bp.route('/')
def home():
    return render_template('dashboard/index.html')

@bp.route('/recipes/<int:recipe_id>')
def recipe_detail(recipe_id):
    return render_template('dashboard/recipe_detail.html')