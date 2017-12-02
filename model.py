"""Models and database functions for HikeTrail project."""
from flask_sqlalchemy import SQLAlchemy
import datetime

# This is the connection to the PostgreSQL database; we're getting
# this through the Flask-SQLAlchemy helper library. On this, we can
# find the `session` object, where we do most of our interactions
# (like committing, etc.)

db = SQLAlchemy()


#####################################################################
# Model definitions

class User(db.Model):
    """User of hike-search website."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    user_name = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(64), nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User user_name=%s email=%s>" % (self.user_name,
                                                 self.email)


class Review(db.Model):
    """Review of a hiking trail by a user."""

    __tablename__ = "reviews"

    review_id = db.Column(db.Integer,
                          autoincrement=True,
                          primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    trail_id = db.Column(db.Integer, db.ForeignKey('hiketrails.trail_id'))
    comment_title = db.Column(db.Text, nullable=True)
    comment_description = db.Column(db.Text, nullable=True)
    score = db.Column(db.Integer, nullable=True)

    # Define relationship to user
    user = db.relationship("User",
                           backref=db.backref("reviews", order_by=review_id))

    # Define relationship to hiketrails
    hiketrail = db.relationship("HikeTrail",
                                backref=db.backref("reviews",
                                                   order_by=review_id))

    def __repr__(self):
        """Provide helpful representation when printed."""

        s = "<Rating review_id=%s trail_id=%s user_id=%s>"
        return s % (self.review_id, self.trail_id, self.user_id)


class Search(db.Model):
    """Search table for saved searches by users."""

    __tablename__ = "searches"

    search_id = db.Column(db.Integer, autoincrement=True,
                          primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    city = db.Column(db.String(20), nullable=True)
    state = db.Column(db.String(20), nullable=True)
    lat_value = db.Column(db.Float, nullable=True)
    long_value = db.Column(db.Float, nullable=True)
    searched_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    radius = db.Column(db.Integer, nullable=False)

    user = db.relationship("User",
                           backref=db.backref("searches", order_by=search_id))

    def __repr__(self):
        """Provide helpful representation when printed."""

        s = "<Comment search_id=%s user_id=%s>"
        return s % (self.search_id, self.user_id)


class HikeTrail(db.Model):
    """Table of hiketrails for ratings / comments"""

    __tablename__ = "hiketrails"
    # trail_id not auto-incremented, because the PK value will be taken from
    # the API unique_id
    trail_id = db.Column(db.Integer, primary_key=True)
    trail_name = db.Column(db.String(200), nullable=False)
    trail_description = db.Column(db.Text, nullable=True)
    trail_directions = db.Column(db.Text, nullable=True)
    trail_length = db.Column(db.Integer)

    def __repr__(self):
        """Provide helpful representation when printed."""

        s = "<Comment trail_id=%s trail_name=%s>"
        return s % (self.trail_id, self.trail_name)


#####################################################################
# Helper functions

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///searchtrails'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will
    # leave you in a state of being able to work with the database
    # directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."
