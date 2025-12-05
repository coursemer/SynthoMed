from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
    db.create_all()
    
    # Create default users if they don't exist
    if not User.query.filter_by(username='admin').first():
        admin = User(username='admin', email='admin@synthomed.com', role='admin')
        admin.set_password('admin123')
        db.session.add(admin)
        
    if not User.query.filter_by(username='doctor').first():
        doctor = User(username='doctor', email='doctor@synthomed.com', role='doctor')
        doctor.set_password('doctor123')
        db.session.add(doctor)
        
    if not User.query.filter_by(username='researcher').first():
        researcher = User(username='researcher', email='researcher@synthomed.com', role='researcher')
        researcher.set_password('researcher123')
        db.session.add(researcher)
        
    db.session.commit()
    print("Database initialized with default users.")
