# your code here
class Movie:
    def __init__(self, title: str, year: int, rating: float):
        self._title = title
        self._year = year
        self._rating = rating
    
    def get_title(self) -> str:
        return self._title
    
    def get_year(self) -> int:
        return self._year
    
    def get_rating(self) -> float:
        return self._rating
    
    def __eq__(self, other: object) -> bool:
        return self._rating == other.get_rating()
    
    def __lt__(self, other: object) -> bool:
        return (self._year, self._rating, self._title) < (other.get_year(), other.get_rating(), other.get_title())
    
    def __str__(self) -> str:
        return f'{self._title},{self._year},{self._rating}'

m1 = Movie('Whispers of the Cosmos', 1994, 9.2)
m2 = Movie('Echoes in the Rain', 1994, 9.3)
m3 = Movie('The Midnight Wanderer', 1995, 9.1)
m4 = Movie('Shattered Horizons', 1995, 9.0)
m5 = Movie('Fading Embers', 1996, 8.9)
m1_repeat = Movie('Whispers of the Cosmos', 1994, 9.2)

def merge(a, b):
    c = []
    while len(a) > 0 and len(b) > 0:
        c.append(a.pop(0) if a[0] < b[0] else b.pop(0))
    return c + a + b

def merge_sort(movie_list):
    if len(movie_list) <= 1:
        return movie_list
    else:
        mid = len(movie_list) // 2
        orig_left = movie_list[:mid]
        orig_right = movie_list[mid:]

        sorted_left = merge_sort(orig_left)
        sorted_right = merge_sort(orig_right)

        return merge(sorted_left, sorted_right)

movies = [m1, m2, m3, m4, m5]

# sorted = merge_sort(movies)
# print(sorted)

lst = []
with open('05_Others/S4 EOY Revision I - OOP with Sort & File/data_files/movies.txt', 'r') as f:
    line = f.readline()
    while line:
        data = line.strip().split(',')
        # print(f'{data[0]},{data[1]},{data[2]}')
        movie = Movie(data[0], int(data[1]), float(data[2]))
        lst.append(movie)
        line = f.readline()

lst = merge_sort(lst)
with open('05_Others/S4 EOY Revision I - OOP with Sort & File/data_files/movies_sorted.txt', 'w') as f:
    for movie in lst:
        f.write(f'{movie.get_title()},{movie.get_year()},{movie.get_rating()}\n')
