from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/dashboard')
@login_required
def dashboard():
    if current_user.role == 'admin':
        return render_template('dashboard_admin.html')
    elif current_user.role == 'doctor':
        return render_template('dashboard_doctor.html')
    elif current_user.role == 'researcher':
        return render_template('dashboard_researcher.html')
    return "Unknown Role", 403
