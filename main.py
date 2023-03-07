from app.models.posts.post_model import Genre, PostGenres, Post
from app.models.basemodel import db_connection, db 
from app.queries.genres import create_genre, delete_genre, get_genres
from app.queries.posts import create_post, get_all_films, get_film_by_id
from app.schemas.posts import PostCreateSchema
from app.routes.posts import router

from fastapi import FastAPI

@db
def create_tables():
    db_connection.create_tables([Genre, Post, PostGenres])

create_tables()

app = FastAPI()

app.include_router(router)






# create_genre('Detektivy')
# create_genre('Ujasy')
# delete_genre('Detektivy')
# print(get_genres())
# create_post('Hodiachie mertvesy',
#             'Serial pro zombi!',
#             '2003',
#             'USA',
#             ['Detektivy', 'Ujasy'])


# create_post('Sherlok Holms',
#             'Serial pro detektiva!',
#             '2005',
#             'USA',
#             ['Detektivy'])
# # print(get_all_films())
# print(get_film_by_id(2))
# from datetime import date
# create_post(PostCreateSchema(title='Batman', description='Mysh', year=date(2015, 1, 1), country='USA', genre=['Detektivy', 'Ujasy']))