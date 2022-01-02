from m3u_parser import M3uParser
from tmdbv3api import TMDb, Movie
import time
import xbmcplugin


tmdb = TMDb()
tmdb.api_key = '3e24a03dcdc99659fb784adc4fbb4966'
tmdb.language = 'fr'
movie = Movie()

url = "/Users/carnicero/Downloads/test2.m3u"
useragent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
parser = M3uParser(timeout=5, useragent=useragent)
parser.parse_m3u(url)

elements = parser.get_list()
# elements.sort(key=itemgetter(0))

tic = time.perf_counter()
grouped_map = {}
for element in elements:
    search = movie.search(element["name"][5:])
    if len(search) > 0:
        id = search[0].id
    # for element in elements:
        if id in grouped_map:
            grouped_map[id].append(element)
        else:
            new_list = [element]
            grouped_map[id] = new_list
    else:
        print(f'Movie not found: {element["name"]}')
toc = time.perf_counter()
print(f'Time spent: {toc - tic}:0.4f')

for element in grouped_map.keys():
    print(f'Element: {element}, entries: {len(grouped_map[element])}')

