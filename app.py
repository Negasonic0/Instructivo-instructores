from flask import Flask, render_template, redirect, url_for, request, flash, jsonify, session

app = Flask(__name__)
app.secret_key = 'clave-secreta'  # Necesaria para sesiones y flash

# Ruta principal
@app.route('/', methods=['GET', 'POST'])
def Main():
    return render_template('main.html')