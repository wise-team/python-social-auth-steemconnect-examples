from flask import render_template, redirect, request, send_from_directory
from flask_login import login_required, logout_user
from example import app


@app.route('/')
def main():
    return render_template('home.html', STATIC_URL='/static/')


@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)


@app.route('/done/')
@login_required
def done():
    return render_template('home.html', STATIC_URL='/static/')


@app.route('/logout/')
@login_required
def logout():
    """Logout view"""
    logout_user()
    return redirect('/')
