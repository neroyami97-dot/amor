from flask import Flask, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

# Configuración personalizada de la relación
DATOS_PAREJA = {
    "titulo": "¡Felices 8 Meses, Mi Amor! ❤️",
    "fecha_inicio": "2026-03-16 00:00:00",  # Formato: AAAA-MM-DD HH:MM:SS
    "mensaje_principal": (
        "Han pasado 8 meses desde aquel 16 de marzo en que empezamos esta historia. "
        "Gracias por cada risa, cada abrazo y por hacer que cada día contigo valga la pena."
    ),
    "razones": [
        "Tu sonrisa ilumina hasta mis días más cansados.",
        "La paz y alegría que siento cada vez que estoy contigo.",
        "Cómo nos entendemos incluso sin decir una sola palabra.",
        "Todos los recuerdos que hemos construido en estos 8 meses y los que faltan."
    ],
    "carta_secreta": (
        "Si pudiera volver al 16 de marzo, te volvería a elegir mil veces más. "
        "Eres lo mejor que me ha pasado este año. ¡Por muchos meses y años más juntos! Te amo 💖"
    )
}

@app.route("/")
def inicio():
    return render_template("index.html", datos=DATOS_PAREJA)

@app.route("/api/tiempo")
def obtener_tiempo():
    inicio_dt = datetime.strptime(DATOS_PAREJA["fecha_inicio"], "%Y-%m-%d %H:%M:%S")
    ahora = datetime.now()
    diferencia = ahora - inicio_dt

    dias = diferencia.days
    segundos_restantes = diferencia.seconds
    horas = segundos_restantes // 3600
    minutos = (segundos_restantes % 3600) // 60
    segundos = segundos_restantes % 60

    return jsonify({
        "dias": dias,
        "horas": horas,
        "minutos": minutos,
        "segundos": segundos
    })

if __name__ == "__main__":
    print("💖 Servidor iniciado! Abre tu navegador en: http://127.0.0.1:5000")
    app.run(debug=True)