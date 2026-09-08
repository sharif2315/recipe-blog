from flask import render_template, flash, redirect
from app.main import bp
from app.auth.forms import LoginForm
from app.models import Recipe


# a simple page that says hello
@bp.route('/')
def home():
    recipes = Recipe.query.all()
    return render_template('index.html', recipes=recipes)

@bp.route('/recipes')
def recipes_list():
    recipes = Recipe.query.all()
    return render_template('recipes_list.html', recipes=recipes)

@bp.route('/recipes/<int:recipe_id>')
def recipe_detail(recipe_id):
    # TODO: use post_id to fetch post from db
    return render_template('recipe_detail.html')
