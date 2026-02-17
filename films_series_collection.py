import random
from faker import Faker
from datetime import datetime

fake = Faker()


class Movies:
    
   def __init__(self, title, year, genre, views):
        self.title = title
        self.year = year
        self.genre = genre
        self.views = views
   
   def play(self, step=1):
       self.views += step
       return self.views 
    
   def __str__(self):
       return f"{self.title} ({self.year})"
   
class Series(Movies):
   
   def __init__(self, episode, season, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.episode = episode
       self.season = season     
    
   def __str__(self):
       return f"{self.title} S{self.season}E{self.episode}"  

def create_content(movie_titles, series_titles, genres):
    content = []
    
    for movie_title in movie_titles:

        movies = Movies(
            title=movie_title, 
            year=fake.year(), 
            genre=random.choice(genres), 
            views=fake.random_int(min=0, max=100))
        content.append(movies)

    for series_title in series_titles:  

        series = Series(
            title=series_title, 
            year=fake.year(), 
            genre=random.choice(genres), 
            episode=f"{random.randint(1, 20):02}",
            season=f"{random.randint(1, 10):02}",
            views=fake.random_int(min=0, max=100))
        content.append(series)
    
    return content

def get_movies(content):

    by_movies = [item for item in content if type(item) is Movies]
    return sorted(by_movies, key=lambda item: item.title)

def get_series(content):
    
    by_series = [item for item in content if type(item) is Series]
    return sorted(by_series, key=lambda item: item.title)

def generate_views(content):

    item_of_content = random.choice(content)
    number_of_views = random.randint(1, 100)
    
    for i in range(number_of_views):
        item_of_content.play()

def run_generate_views(content):
    for i in range(10):
        generate_views(content)
    
def top_titles(content, content_type, amount):
    
    if content_type == Movies:
        filtered_top_titles = get_movies(content)
    
    elif content_type == Series:
        filtered_top_titles = get_series(content)

    else:
        filtered_top_titles = content

    by_views = sorted(filtered_top_titles, key=lambda item: item.views, reverse=True)
    filtered_top_titles = by_views[:amount]

    for item in filtered_top_titles:
        print(f"{item}")

def search(content, title):
    search_result = [item for item in content if title.lower() in item.title.lower()]
    
    if search_result:
        for item in search_result:
            print(f"Tytuł {item} znajduje się w bibliotece")
    else:
        print(f"Niestety tytułu {title} nie ma w bibliotece")

        
if __name__ == '__main__':

    movie_titles = [
        "Dzień świra", 
        "Chłopaki nie płaczą", 
        "Pianista", 
        "Bogowie", 
        "Zimna wojna", 
        "Boże Ciało", 
        "Katyń", 
        "Killer", 
        "Psy", 
        "Wołyń"
        ]

    series_titles = [
        "Wataha",
        "1670",
        "Ranczo",
        "Ślepnąc od świateł",
        "Wielka woda",
        "Kruk",
        "Belfer",
        "Król",
        "Odwróceni",
        "Rojst"
        ]

    genres = [
        "Dramat",
        "Komedia",
        "Kryminał",
        "Sci-Fi",
        "Thriller",
        "Horror",
        "Dokumentalny",
        "Akcja",
        "Fantasy",
        "Historyczny"
        ]
    
    content = create_content(movie_titles, series_titles, genres)

    print("Biblioteka filmów:")   
    for item in get_movies(content):
        print(item)
    print()

    run_generate_views(content)

    print(f"Najpopularniejsze filmy i seriale dnia {datetime.now().strftime('%d.%m.%Y')}:")
    top_titles(content, None, 3)
    print()

    print("Wyszukiwanie tytułów w bibliotece:")
    search(content, "'Oczy'")
