from flask import render_template
from app.dashboard import bp
from app.models import Recipe
from flask_login import login_required


@bp.route('/')
@login_required
def home():
    recipes = Recipe.query.all()
    return render_template('dashboard/index.html', recipes=recipes)


@bp.route('/recipes/<int:recipe_id>')
@login_required
def recipe_detail(recipe_id):
    return render_template('dashboard/recipe_detail.html')