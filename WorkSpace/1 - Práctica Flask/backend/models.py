import sqlite3

# Base de datos SQL
def save_contact(name, email, subject, message):
    pass


def get_movies():
    return  [
        {'id' : 1,
            'title' : "The Shawshank Redemption",
            'director' : "Frank Darabont",
            'year' : 1994,
            'genre' : "Drama",
            'description' : "The Shawshank Redemption is a 1994 American prison drama film based on a Stephen King novella, starring Tim Robbins as banker Andy Dufresne and Morgan Freeman as his friend Red. Andy is wrongly convicted of murdering his wife and serves a life sentence at Shawshank Prison, where he endures brutality while using his financial skills to assist the corrupt warden. Over two decades, he and Red form a deep friendship, and Andy eventually orchestrates a daring escape and exposes the prison's corruption ",
            'rating' : 9.2,
            'poster_url' : "https://image.tmdb.org/t/p/original/j8IMbiv2LN0pSptfVgoVUkhWbPE.jpg"   
        },
        {'id' : 2,
        'title' : "Django Unchined",
        'director' : "Quentin Tarantino",
        'year' : 2012,
        'genre' : "Action",
        'description' : "Django is a free and open-source Python project with an active community that reviews and maintains the software. A not-for-profit organization called the Django Software Foundation promotes and supports the use and maintenance of Django",
        'rating' : 9.6,
        'poster_url' : "https://wiki.tarantino.info/images/Djangounchainedposter3.jpg" 
        },  
    ]

def init_db():
    connection = sqlite3.connect('peliculas.db')
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
            descriptionre TEXT NOT NULL,
            rating DEFAULT 0.0,
            poster_url TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        
        )
    """

    )


# Esto es como poner psvm en java
if __name__ == '__main__':
    print("")