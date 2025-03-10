#!/usr/bin/python
#-*- coding: utf-8 -*-
#Autor: Luis Angel Ramirez Mendoza
#______________________________________________________________________________________________________________________

from flask import Flask, request, render_template, redirect, url_for, make_response

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Simulación de una base de datos de usuarios
users = {
    'admin': 'password123',
    'user': 'user123'
}

# Simulación de una base de datos de comentarios
comments = []

# Plantilla base con Bootstrap
base_template = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CTF de Robo de Cookies</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            padding: 20px;
            background-color: #f8f9fa;
        }
        .navbar {
            margin-bottom: 20px;
        }
        .footer {
            margin-top: 20px;
            text-align: center;
            font-size: 0.9em;
            color: #6c757d;
        }
    </style>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <a class="navbar-brand" href="/">CTF de Robo de Cookies</a>
        <div class="collapse navbar-collapse">
            <ul class="navbar-nav ml-auto">
                <li class="nav-item">
                    <a class="nav-link" href="/login">Iniciar Sesión</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/comments">Comentarios</a>
                </li>
            </ul>
        </div>
    </nav>
    <div class="container">
        {% block content %}{% endblock %}
    </div>
    <footer class="footer">
        <p>© 2024 CTF de Robo de Cookies. Todos los derechos reservados.</p>
    </footer>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in users and users[username] == password:
            resp = make_response(redirect(url_for('profile')))
            resp.set_cookie('auth', 'true')
            return resp
        else:
            return render_template('login.html', error="Credenciales incorrectas. Inténtalo de nuevo.")
    return render_template('login.html')

@app.route('/profile')
def profile():
    auth = request.cookies.get('auth')
    if auth == 'true':
        return render_template('profile.html')
    else:
        return redirect(url_for('login'))

@app.route('/comments', methods=['GET', 'POST'])
def comments_route():
    if request.method == 'POST':
        comment = request.form.get('comment')
        comments.append(comment)
        return redirect(url_for('comments_route'))
    
    return f"""
    <title>CTF de Robo de Cookies</title>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <a class="navbar-brand" href="/">CTF de Robo de Cookies</a>
        <div class="collapse navbar-collapse">
            <ul class="navbar-nav ml-auto">
                <li class="nav-item">
                    <a class="nav-link" href="/login">Iniciar Sesión</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="/comments">Comentarios</a>
                </li>
            </ul>
        </div>
    </nav>
    <style>
        body {{
            padding: 20px;
            background-color: #f8f9fa;
        }}
        .navbar {{
            margin-bottom: 20px;
        
        }}
        .footer {{
            margin-top: 20px;
            text-align: center;
            font-size: 0.9em;
            color: #6c757d;
        }}
    </style>

    <h1>Comentarios</h1>
    <form method="POST">
    <div class="form-group">
        <label for="comment">Comentario:</label>
        <input type="text" class="form-control" id="comment" name="comment" required>
    </div>
    <button type="submit" value="Publicar" class="btn btn-primary">Publicar</button>
</form>
    <hr>
    <h2>Comentarios Publicados:</h2>
    {"<br>".join(comments)}
    <footer class="footer">
        <p>© 2024 CTF de Robo de Cookies. Todos los derechos reservados.</p>
    </footer>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    """
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)