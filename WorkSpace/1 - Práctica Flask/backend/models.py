import sqlite3


def init_db():
    connection = sqlite3.connect('backend/peliculas.db')
    cursor = connection.cursor()

    # TABLA DE CONTACTOS / USUARIOS
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            subject TEXT,
            message TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """

    )

    # TABLA DE PELÍCULAS
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            director TEXT NOT NULL,
            year INTEGER NOT NULL,
            genre TEXT NOT NULL,
            description TEXT NOT NULL,
            rating DEFAULT 0.0,
            poster_url TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        
        )
    """

    )
    connection.commit()
    connection.close()


def add_movies():
    connection = sqlite3.connect('backend/peliculas.db')
    cursor = connection.cursor()

    movies = [
        (
             "The Shawshank Redemption",
             "Frank Darabont",
             1994,
             "Drama",
             "The Shawshank Redemption is a 1994 American prison drama film based on a Stephen King novella, starring Tim Robbins as banker Andy Dufresne and Morgan Freeman as his friend Red. Andy is wrongly convicted of murdering his wife and serves a life sentence at Shawshank Prison, where he endures brutality while using his financial skills to assist the corrupt warden. Over two decades, he and Red form a deep friendship, and Andy eventually orchestrates a daring escape and exposes the prison's corruption ",
             9.2,
             "https://image.tmdb.org/t/p/original/j8IMbiv2LN0pSptfVgoVUkhWbPE.jpg"   
        ), (
         "Django Unchined",
         "Quentin Tarantino",
         2012,
         "Action",
         "Django is a free and open-source Python project with an active community that reviews and maintains the software. A not-for-profit organization called the Django Software Foundation promotes and supports the use and maintenance of Django",
         9.6,
         "https://wiki.tarantino.info/images/Djangounchainedposter3.jpg" 
        )
    ]

    cursor.executemany(
        '''
            INSERT INTO movies (title, director, year, genre, description, rating, poster_url)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', movies
    )


    connection.commit()
    connection.close()

    print("Películas añadidas por primera vez")


def save_contact(name, email, subject, message):
    connection = sqlite3.connect('backend/peliculas.db')
    cursor = connection.cursor()

    if not subject():
        subject = ""

    cursor.execute(
        '''
            INSERT INTO contacts (name, email, subject, message)
            VALUES (?, ?, ?, ?)
        ''', (name, email, subject, message)
    )
    
    connection.commit()
    connection.close()


def get_movies():
    connection = sqlite3.connect('backend/peliculas.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()


    cursor.execute('SELECT * FROM movies ORDER BY created_at DESC')
    movies = cursor.fetchall()
    
    connection.commit()
    connection.close()
    return movies


def get_movie_by_id(movie_id: int):
    connection = sqlite3.connect('backend/peliculas.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM movies WHERE id = ?', (movie_id))
    movie = cursor.fetchone()

    connection.commit()
    connection.close()
    return movie

def cualquier_funcion():
    connection = sqlite3.connect('backend/peliculas.db')
    cursor = connection.cursor()


      #codigo 
    
    connection.commit()
    connection.close()

# Esto es como poner psvm en java
if __name__ == '__main__':
    print("")