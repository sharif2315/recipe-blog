from enum import Enum
from datetime import datetime as dt, timezone as tz
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login


class User(UserMixin, db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(
        sa.String(64), index=True, unique=True
    )
    email: so.Mapped[str] = so.mapped_column(
        sa.String(120), index=True, unique=True
    )
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    recipes: so.WriteOnlyMapped['Recipe'] = so.relationship(back_populates='author')

    def __repr__(self):
        return '<User {}'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class RecipeDifficulty(str, Enum):
    BEGINNER = 'Beginner'
    INTERMEDIATE = 'Intermediate'
    ADVANCED = 'Advanced'

# TODO:
# create models for:
# Ingredient -> name, order/rank -> 1 to many
# PreperationStep -> name, description, order/rank -> 1 to many

class Recipe(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    title: so.Mapped[str] = so.mapped_column(sa.String(60))
    description: so.Mapped[str] = so.mapped_column(sa.String(140))
    duration: so.Mapped[float] = so.mapped_column(sa.Numeric(precision=10, scale=1))
    difficulty: so.Mapped[str] = so.mapped_column(sa.Enum(RecipeDifficulty), nullable=True)
    servings_text: so.Mapped[str] = so.mapped_column(sa.String(60))
    timestamp: so.Mapped[dt] = so.mapped_column(
        index=True, default=lambda:dt.now(tz.utc)
    )
    user_id: so.Mapped[int] = so.mapped_column(
        sa.ForeignKey(User.id), index=True
    )
    author: so.Mapped[User] = so.relationship(back_populates='recipes')

    def _repr__(self):
        return '<Post {}'.format(self.body)


@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))