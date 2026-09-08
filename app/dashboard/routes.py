from flask import render_template
from app.dashboard import bp
from app.models import Recipe

@bp.route('/')
def home():
    recipes = Recipe.query.all()
    return render_template('dashboard/index.html', recipes=recipes)

@bp.route('/recipes/<int:recipe_id>')
def recipe_detail(recipe_id):
    return render_template('dashboard/recipe_detail.html')