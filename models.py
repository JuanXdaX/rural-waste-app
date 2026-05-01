from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ReporteResiduo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo_quimico = db.Column(db.String(100), nullable=False)
    cantidad = db.Column(db.Float, nullable=False)
    impacto_co2 = db.Column(db.Float)