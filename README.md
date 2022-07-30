# How to use imdb-api ?
### Let's start by importing the library and instantiating the IMDb class :
	from imdb-api import IMDb
	
	imdb = IMDb()

## getFeatures(movie_name or imdb_id):
### Return basic features in a dictionnary such as title, release year, director...

	input : imdb.getFeatures("Se7en")
	
	output : {'title': 'Se7en',
	'release_year': 1995,
	'imdb_id': 'tt0114369',
	'director': 'David Fincher',
	'creator': 'Andrew Kevin Walker',
	'main_actors': ['Morgan Freeman', 'Brad Pitt', 'Kevin Spacey'], 
	'countries': ['United States'],
	'languages': ['English'],
	'companies': ['Cecchi Gori Pictures', 'Juno Pix', 'New Line Cinema'],
	'genre': ['Crime', 'Drama', 'Mystery'],
	'type': 'Movie',
	'runtime': '2h07',
	'release_date': '1996-01-31', 
	'description': 'Two detectives, a rookie and a veteran, hunt a serial killer who uses the seven deadly sins as his motives.', 
	'content_rating': '12',
	'rating': 8.6,
	'rating_count': 1608215,
	'reviews_count': 1800	}
	

## getMedia(movie_name or imdb_id):
### Return media-type features such as URLs of the poster, the trailer,...

	input : imdb.getMedia("Se7en")
	
	output : {'title': 'Se7en',
	'release_year': 1995,
	'imdb_id': 'tt0114369',
	'poster_url': 'https://m.media-amazon.com/images/M/MV5BMmJlNmU0MjMtYmVkZS00ZDdiLTljZjQtYTA2YWRjYTI1OWYxXkEyXkFqcGdeQXVyMTgxOTIzNzk@._V1_.jpg', 
	'trailer_url': 'https://www.imdb.com/video/imdb/vi2508831257',
	'trailer_download_url': 'https://imdb-video.media-imdb.com/vi2508831257/1434659607842-pgv4ql-1540843135385.mp4?Expires=1659301640&Signature=LY82oBZ4CAc9XJciLFFDFmdG2aT-4412qMVYZOoHuiTsocFa8pzlhfOVh1YJmq7-ocUCiU5z5bdkZLsHVA0im93DJ5yoJCREDOZn7Lc0itqW9YosWrygqED9VlwOYP2TjEbYBRQ~CgiQ4LBDESuhB856h4fWV349-gPusvQoiqZtXz~daqsnOhpjeG7LfDPVIl7sqyzSnuJzNYPwj4NDU-1zpLnSS-hf4RWdiJqLTD2RA404GsIp1b47IWNcCALwu~dGn1YLGS6I~5cHJbn5xRdglc6R-s8Mgl2sITqTKv~6gnzxzO9Ilm33j7LmupoqxpFjAxa3jamL9sm4y6~Vew__&Key-Pair-Id=APKAIFLZBVQZ24NQH3KA',
	'trailer_thumbnail_url': 'https://m.media-amazon.com/images/M/MV5BZmMxNmJiYzctNGRkZC00YzcxLTgyNjMtMmIxZWVlNDA4ZWRjXkEyXkFqcGdeQXRodW1ibmFpbC1pbml0aWFsaXplcg@@._V1_.jpg'}
	
## getCast(movie_name or imdb_id):
Return a list which each object is a dictionary with a key "actor" and a key "character" and an optional key "id" (name_id = False by default).

Note that you can set a limit with the argument limit (limit = 5), or no limit at all with the argument all = True.

The uncredited actors are by default unshown : use the argument uncredited = True for adding them to the cast list.

	input : imdb.getCast("Se7en", limit = 5, uncredited = False, all = False, name_id = True):
	
	output : [{'id': 'nm0000151', 'actor': 'Morgan Freeman', 'character': 'Somerset'}, 
	{'id': 'nm0001825', 'actor': 'Andrew Kevin Walker', 'character': 'Dead Man at 1st Crime Scene (as Andy Walker)'}, 
	{'id': 'nm0669254', 'actor': 'Daniel Zacapa', 'character': 'Detective Taylor at First Murder'}, 
	{'id': 'nm0000093', 'actor': 'Brad Pitt', 'character': 'Mills'}, 
	{'id': 'nm0000569', 'actor': 'Gwyneth Paltrow', 'character': 'Tracy'}]
	
	
