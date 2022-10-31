import webbrowser

from requests import Session, Response

API = '2fb834eb-389d-46e2-9dee-f7eadf7937b1'  # Вбей сюда свой токен


def get_actor_id():
    with Session() as session:
        session.headers.update({'accept': 'application/json', 'X-API-KEY': API})
        response = session.get(
            url='https://kinopoiskapiunofficial.tech/api/v1/persons',
            params={
                'name': input('Input actor name: ').encode(),
                'page': 1
            }
        )
        i_need_this_dict = response.json()
        new_dict = i_need_this_dict['items']
        super_dict = new_dict[0]
        # webbrowser.open(super_dict['posterUrl'])
        print(super_dict)
        get_films_by_actor_id(str(super_dict['kinopoiskId']))
        return print(response.status_code)


def get_films_by_actor_id(actor_id: str):
    with Session() as session:
        session.headers.update({'accept': 'application/json', 'X-API-KEY': API})
        response: Response = session.get(
            url='https://kinopoiskapiunofficial.tech/api/v1/staff/' + actor_id
        )
        print(response.json())
        for films in response.json()['films']:
            if films['nameRu'] is None:
                print('id:', films['filmId'], ' название:', films['nameEn'])
            else:
                print('id:', films['filmId'], ' название:', films['nameRu'])


def get_film_id(filmId):
    with Session() as session:
        session.headers.update({'accept': 'application/json', 'X-API-KEY': API})
        response: Response = session.get(
            url='https://kinopoiskapiunofficial.tech/api/v2.2/films/' + str(filmId)
        )
        return response.json()


get_actor_id()
# get_film_id(str(input(507)))
# get_films_by_actor_id(input('Введи ид актера '))
