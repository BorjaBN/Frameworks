from flask import Flask, render_template, abort


app = Flask(__name__, template_folder='..\\frontend\\templates', static_folder='..\\frontend\\static')

movie_list = [
   {
        'id' : 1,
        'title' : "The Shawshank Redemption",
        'director' : "Frank Darabont",
        'year' : 1994,
        'gender' : "Drama",
        'description' : "The Shawshank Redemption is a 1994 American prison drama film based on a Stephen King novella, starring Tim Robbins as banker Andy Dufresne and Morgan Freeman as his friend Red. Andy is wrongly convicted of murdering his wife and serves a life sentence at Shawshank Prison, where he endures brutality while using his financial skills to assist the corrupt warden. Over two decades, he and Red form a deep friendship, and Andy eventually orchestrates a daring escape and exposes the prison's corruption ",
        'rating' : 9.2,
        'poster_url' : "https://image.tmdb.org/t/p/original/j8IMbiv2LN0pSptfVgoVUkhWbPE.jpg"
    },
    {
        'id' : 2,
        'title' : "Django Unchined",
        'director' : "Quentin Tarantino",
        'year' : 2012,
        'gender' : "Action ",
        'description' : "Django is a free and open-source Python project with an active community that reviews and maintains the software. A not-for-profit organization called the Django Software Foundation promotes and supports the use and maintenance of Django",
        'rating' : 9.6,
        'poster_url' : "https://wiki.tarantino.info/images/Djangounchainedposter3.jpg"
    },
    
]

@app.route('/contact')
def contact():
  return render_template("contact.html")


def get_movie_by_id(movie_id: int):
    return next((m for m in movie_list if m["id"] == movie_id), None)

@app.route("/movie/<int:movie_id>")
def movie_detail(movie_id):
    movie_detail = get_movie_by_id(movie_id)
    if not movie_detail:
        return abort(404)
    return render_template("movie_detail.html", movie=movie_detail)
    

@app.route('/movies', endpoint='movies')
def movies():
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
    app.run(debug=True)  #Para eliminar warnings


