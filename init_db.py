from project import create_app, db

# Crée l'application Flask et active le contexte
app = create_app()

with app.app_context():
    db.create_all()
    print("Base de données initialisée avec succès.")
