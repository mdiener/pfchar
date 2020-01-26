import json

from flask import render_template, request, session, url_for, redirect, abort, flash
from pfchar.database.user import User, new_user
from pfchar.database.character import Character, new_char
from pfchar.database.exceptions import CharacterReadError, DatabaseError


class Views(object):
    def index(self):
        return render_template('index.html')

    def character(self, charid):
        if not session.get('loggedin', False):
            flash('Please log in to get your character.')
            session['login_forward'] = 'character'

            return redirect(url_for('login'))

        try:
            char = Character(charid, session.get('uid'))
        except CharacterReadError as e:
            flash('Could not retrieve the character.', 'error')
            return redirect(url_for('characters'))

        return render_template('character.html', char=str(char))

    def characters(self):
        if not session.get('loggedin', False):
            flash('Please log in to access your characters.')
            session['login_forward'] = 'characters'

            return redirect(url_for('login'))

        try:
            user = User(uid=session.get('uid'))
            chars = user.characters
        except DatabaseError as e:
            flash('Something went wrong when trying to get your characters. Please try again or contact an administrator if the problem persists.', 'error')
            return redirect(url_for('index'))

        return render_template('characters.html', characters=json.dumps(chars))

    def contact(self):
        return render_template('contact.html')

    def logout(self):
        if not session.get('loggedin', False):
            flash('You are not logged in and have been returned to the home page.')
            return redirect(url_for('index'))

        session.pop('loggedin', None)
        session.pop('uid', None)

        return redirect(url_for('index'))

    def login(self):
        if session.get('loggedin', False):
            return redirect(url_for('index'))

        if request.method == 'GET':
            return render_template('login.html')

        if request.method == 'POST':
            email = request.form.get('email', default=None)
            password = request.form.get('password', default=None)

            user = User(email=email)
            try:
                user.check_password(password)
            except UserPasswordError as e:
                abort(401)

            session['loggedin'] = True
            session['uid'] = user.uid

            login_forward = session.pop('login_forward', None)
            if login_forward is not None:
                return redirect(url_for(login_forward))

            return redirect(url_for('index'))

    def signup(self):
        if session.get('loggedin', False):
            return redirect(url_for('index'))

        if request.method == 'GET':
            return render_template('signup.html')

        if request.method == 'POST':
            email = request.form.get('email', default=None)
            password = request.form.get('password', default=None)
            repeat_password = request.form.get('repeat_password', default=None)

            if password != repeat_password:
                flash('Please make sure both passwords are the same.')
                return render_template('signup.html', email=email, password=password, repeat_password=repeat_password)

            try:
                user = new_user(email, password)
            except DatabaseError as e:
                flash('Something went wrong when trying to create your user. Please try again or contact an administrator if the problem persists.', 'error')
                return redirect(url_for('index'))

            session['loggedin'] = True
            session['uid'] = user.uid

            return redirect(url_for('index'))
