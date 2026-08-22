from flask import render_template, flash, redirect
from app.main import bp
from app.auth.forms import LoginForm


# a simple page that says hello
@bp.route('/')
def home():
    return render_template('index.html')

@bp.route('/recipes')
def recipes_list():
    return render_template('recipes_list.html')

@bp.route('/recipes/<int:recipe_id>')
def recipe_detail(recipe_id):
    # TODO: use post_id to fetch post from db
    return render_template('recipe_detail.html')
