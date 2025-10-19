from flask import Flask, render_template, abort, request, redirect, flash, url_for
from models import save_contact, get_movies, get_movie_by_id, init_db, add_movies, save_movies

app = Flask(__name__, template_folder='..\\frontend\\templates', static_folder='..\\frontend\\static')
app.config['SECRET_KEY'] = 'random-key'


@app.route('/new_movies', methods=['GET', 'POST'])
def new_movies():
    if request.method == 'POST':
      title = request.form.get('title')
      director = request.form.get('director')
      year_str = request.form.get('year')
      genre = request.form.get('genre')
      description = request.form.get('description')
      rating_str = request.form.get('rating')
      poster_url = request.form.get('poster_url')

      # CONVERSIÓN CRÍTICA DE TIPOS        Añadidido por problemas de conversion con real number a string o al reves, recomendado por gemini
      try:
        # La validación de vacío ('') se maneja aquí (int('') da ValueError)
        year = int(year_str)
        rating = float(rating_str)
      except (ValueError, TypeError):
        # Este mensaje se muestra si están vacíos o no son números
        flash("Error: El Año y la Calificación deben ser números válidos.", 'error')
        return redirect(url_for('new_movies'))

      if not title or not director or not  genre or not description or not  poster_url:
          flash("Por favor, rellena bien los campos") # Te muestra un cartelito arriba de la pantalla con el texto
          return redirect(url_for('new_movies'))

      save_movies(title, director, year, genre, description, rating, poster_url)
      flash('Gracias por tu mensaje - Te responderemos pronto', 'succes')
      return redirect(url_for('new_movies'))

    return render_template('new_movies.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
  if request.method == 'POST':
      name = request.form.get('name')
      email = request.form.get('email')
      subject = request.form.get('subject')
      message = request.form.get('message')

      if not name:
          flash("Por favor, rellena bien el nombre") # Te muestra un cartelito arriba de la pantalla con el texto
          return redirect(url_for('contact'))

      save_contact(name, email, subject, message)
      flash('Gracias por tu mensaje - Te responderemos pronto', 'succes')
      return redirect(url_for('contact'))

  return render_template("contact.html")




@app.route("/movie/<int:movie_id>")
def movie_detail(movie_id):
    movie_detail = get_movie_by_id(movie_id)
    if not movie_detail:
        return abort(404)
    return render_template("movie_detail.html", movie=movie_detail)
    

@app.route('/movies', endpoint='movies')
def movies():
    movie_list = get_movies()
    return render_template("movies.html",movies=movie_list)


@app.route('/about')
def about():
   return render_template("about.html")


@app.route('/')
def index():
   #return "<h1>Hello, world</h1>\n<h2>Segundo encabezado</h2>\nTexto normal"
    return render_template("index.html")




# Esto es como poner psvm en java
if __name__ == '__main__':
    init_db()

    movies = get_movies()
    if not movies or len(movies) == 0:
        add_movies()


    app.run(debug=True)  #Para eliminar warnings


