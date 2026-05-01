from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-secret-rural-2024'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reciclaje_quimico.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class ReporteResiduo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tipo_quimico = db.Column(db.String(100), nullable=False)
    cantidad = db.Column(db.Float, nullable=False)
    impacto_co2 = db.Column(db.Float)

@app.route('/')
def index():
    reportes = ReporteResiduo.query.all()
    total_co2 = sum(r.impacto_co2 for r in reportes) if reportes else 0
    total_residuos = sum(r.cantidad for r in reportes) if reportes else 0
    return render_template('index.html', reportes=reportes, total_co2=total_co2, total_residuos=total_residuos)

@app.route('/agregar', methods=['POST'])
def agregar_reporte():
    tipo = request.form.get('tipo_quimico')
    cant = float(request.form.get('cantidad'))
    impacto = cant * 0.5 
    nuevo = ReporteResiduo(tipo_quimico=tipo, cantidad=cant, impacto_co2=impacto)
    db.session.add(nuevo)
    db.session.commit()
    return redirect(url_for('index'))

# RUTA DE EDICIÓN (FUNDAMENTAL PARA EL BOTÓN)
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def edit_reporte(id):
    reporte = ReporteResiduo.query.get_or_404(id)
    if request.method == 'POST':
        reporte.tipo_quimico = request.form.get('tipo_quimico')
        reporte.cantidad = float(request.form.get('cantidad'))
        reporte.impacto_co2 = reporte.cantidad * 0.5
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', reporte=reporte)

@app.route('/eliminar/<int:id>')
def eliminar_reporte(id):
    reporte = ReporteResiduo.query.get_or_404(id)
    db.session.delete(reporte)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)