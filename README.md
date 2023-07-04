## Update (2022/07/04)
The `requests` library does not work anymore with [https://imdb.com](https://www.imdb.com/), a new version using the `selenium` library has been added.

You can install the API with pip and replace the content of `__init__.py` by the content of the file `imdb-api_selenium_version.py`. 

# Installation
## Windows
	python -m pip install imdb-page-api
## Linux
	pip install imdb-page-api

# How to use imdb-api ?
Let's start by importing the library and instantiating the IMDb class :

	from imdb_api import IMDb 
	
	imdb = IMDb()


An imdb id of a title is the id starting by *tt*... For example, Se7en (1995) is referenced to the IMDb page https://www.imdb.com/title/tt0114369/. The imdb id of Se7en (1995) is ***tt0114369***.

When a function is loaded, both ***imdb id*** and ***title*** can be typed in the input. 

For example, `getFeatures("Se7en")` and `getFeatures("tt0114369")` will give the same results. Note that `getFeatures("Se7en")` will take more time because the program need to load the search page.

## Main functions
### getFeatures(imdb_id, seconds = False, InList = False, name_id = False):
Return basic features in a dictionnary such as title, release year, director...

`seconds = True` --> return the runtime in seconds

`InList = True` --> return director / creator in lists where each person if an item of the list

`name_id = True` --> return director / creator / main actors in lists where each person is a dictionary of the list including their imdb id (e.g. Brad Pitt : url = https://www.imdb.com/name/nm0000093/, id = nm0000093) and their name. Dictionary keys are director / creator / actor.

	input : imdb.getFeatures("Se7en", seoncds = False, InList = False, name_id = False)
	
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
	

### getMedia(imdb_id):
Return media-type features such as URLs of the poster, the trailer,...

	input : imdb.getMedia("Se7en")
	
	output : {'title': 'Se7en',
	'release_year': 1995,
	'imdb_id': 'tt0114369',
	'poster_url': 'https://m.media-amazon.com/images/M/MV5BMmJlNmU0MjMtYmVkZS00ZDdiLTljZjQtYTA2YWRjYTI1OWYxXkEyXkFqcGdeQXVyMTgxOTIzNzk@._V1_.jpg', 
	'trailer_url': 'https://www.imdb.com/video/imdb/vi2508831257',
	'trailer_download_url': 'https://imdb-video.media-imdb.com/vi2508831257/1434659607842-pgv4ql-1540843135385.mp4?Expires=1659301640&Signature=LY82oBZ4CAc9XJciLFFDFmdG2aT-4412qMVYZOoHuiTsocFa8pzlhfOVh1YJmq7-ocUCiU5z5bdkZLsHVA0im93DJ5yoJCREDOZn7Lc0itqW9YosWrygqED9VlwOYP2TjEbYBRQ~CgiQ4LBDESuhB856h4fWV349-gPusvQoiqZtXz~daqsnOhpjeG7LfDPVIl7sqyzSnuJzNYPwj4NDU-1zpLnSS-hf4RWdiJqLTD2RA404GsIp1b47IWNcCALwu~dGn1YLGS6I~5cHJbn5xRdglc6R-s8Mgl2sITqTKv~6gnzxzO9Ilm33j7LmupoqxpFjAxa3jamL9sm4y6~Vew__&Key-Pair-Id=APKAIFLZBVQZ24NQH3KA',
	'trailer_thumbnail_url': 'https://m.media-amazon.com/images/M/MV5BZmMxNmJiYzctNGRkZC00YzcxLTgyNjMtMmIxZWVlNDA4ZWRjXkEyXkFqcGdeQXRodW1ibmFpbC1pbml0aWFsaXplcg@@._V1_.jpg'}
	
### getCast(imdb_id, limit = 15, uncredited = False, all = False, name_id = False):
Return a list which each object is a dictionary with a key ***actor*** and a key ***character*** and an optional key ***id*** (name_id = False by default).

`limit = 15` --> limit the number of actors to 15 in the list

`all = True` --> the limit is ignored and all the credited actors are added to the list

`uncredited = True` --> add the uncredited actors in the credits to the list

`name_id = True` --> add the key ***id*** to each actors


	input : imdb.getCast("Se7en", limit = 5, uncredited = False, all = False, name_id = True):
	
	output : [{'id': 'nm0000151', 'actor': 'Morgan Freeman', 'character': 'Somerset'}, 
	{'id': 'nm0001825', 'actor': 'Andrew Kevin Walker', 'character': 'Dead Man at 1st Crime Scene (as Andy Walker)'}, 
	{'id': 'nm0669254', 'actor': 'Daniel Zacapa', 'character': 'Detective Taylor at First Murder'}, 
	{'id': 'nm0000093', 'actor': 'Brad Pitt', 'character': 'Mills'}, 
	{'id': 'nm0000569', 'actor': 'Gwyneth Paltrow', 'character': 'Tracy'}]
	

### getFeaturesWithCast(imdb_id, seconds = False, InList = False, limit = 15, uncredited = False, all = False, name_id = False):
Return a dictionary including basic features of `getFeatures` and the cast of `getCast`. The cast can be retrieved with the key ***cast***.

### getAllFeatures(imdb_id, seconds = False, InList = False, name_id = False):
Return all features in a dictionnary including those in getFeatures, getMedia + keywords, filming location and other working title.

Please, note that returning this list does not take more time than getFeatures because all these features are loaded in the main imdb page of the title.

`seconds = True`, `name_id = True` --> see above in `getFeatures`

`InList = True` --> return director / creator / filming locations / other working titles in lists


	input : 
	
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
	'rating_count': 1608851,
	'reviews_count': 1800,
	'keywords': ['serial killer', 'detective', 'serial murder', 'seven deadly sins', 'murder']
	'filming_location': 'Pacific Electric Building, Los Angeles, California, USA',
	'aka': 'Se7en',
	'poster_url': 'https://m.media-amazon.com/images/M/MV5BMmJlNmU0MjMtYmVkZS00ZDdiLTljZjQtYTA2YWRjYTI1OWYxXkEyXkFqcGdeQXVyMTgxOTIzNzk@._V1_.jpg',
	'trailer_url': 'https://www.imdb.com/video/imdb/vi2508831257',
	'trailer_download_url': 'https://imdb-video.media-imdb.com/vi2508831257/1434659607842-pgv4ql-1540843135385.mp4?Expires=1659430658&Signature=nf0wlhRH9so6py9ScVndH80DDadzpBU0bcmOCm6ZX2mAB7zxPx7lInq61Vj-GzmzC-OiC9jyhe6G~aWO40AqTOcEbhqr1-rqHVaqrcKSYTzKFQwTUDqwr6OMk9JLp0znTjTRsFAIQoUBjkY2~hn5jx0lN3pREgStHHfN11V-GNtZhZuaXheAn9RtDdtgf2MpC5vKMJcH0kLqRsXQ4yj2plZxKoMT1~Q0q4S3M0C2Rt~YAJmOfvnSYFs7DlTzeoXmNke7yZP42KebMO3xFZnJJaHg7ZSisrPEI~x0XJtC9MtOoAkiNYpl0pq7Ekmi2st60ZYvBs46aPo8hajM3NghsA__&Key-Pair-Id=APKAIFLZBVQZ24NQH3KA',
	'trailer_thumbnail_url': 'https://m.media-amazon.com/images/M/MV5BZmMxNmJiYzctNGRkZC00YzcxLTgyNjMtMmIxZWVlNDA4ZWRjXkEyXkFqcGdeQXRodW1ibmFpbC1pbml0aWFsaXplcg@@._V1_.jpg'}
	
### getAll(imdb_id, seconds = False, InList = False, limit = 15, uncredited = False, all = False, name_id = False):
Return all possible features in a dictionary including those in `getAllFeatures` and `getCast`.

Please, note that returning this list does take more time than `getAllFeatures` because the cast is on a different web page.

## Other functions & examples

For the examples, **search/imdb_id** = ***'Se7en'***

`getIdFromSearch(search)` --> 'tt0114369'

`getTitle(imdb_id)` --> 'Se7en'

`getReleaseYear(imdb_id)` --> 1995

`getDirector(imdb_id, InList = False, name_id = False)` --> 'David Fincher'

`getCreator(imdb_id, InList = False, name_id = False)` --> 'Andrew Kevin Walker'

`getMainActors(imdb_id, InList = True, name_id = False)` --> ['Morgan Freeman', 'Brad Pitt', 'Kevin Spacey']

`getCountries(imdb_id)` --> ['United States']

`getLanguages(imdb_id)` --> ['English']

`getCompanies(imdb_id)` --> ['Cecchi Gori Pictures', 'Juno Pix', 'New Line Cinema']

`getGenres(imdb_id)` --> ['Crime', 'Drama', 'Mystery']

`getType(imdb_id)` --> 'Movie'

`getRuntime(imdb_id, seconds = False)` --> '2h07'

`getReleaseDate(imdb_id)` --> '1996-01-31'

`getDescription(imdb_id)` --> 'Two detectives, a rookie and a veteran, hunt a serial killer who uses the seven deadly sins as his motives.'

`getContentRating(imdb_id)` --> '12'

`getRating(imdb_id)` --> 8.6

`getRatingCount(imdb_id)` --> 1608851

`getReviewsCount(imdb_id)` --> 1800

`getPosterURL(imdb_id)` --> 'h<span>ttps://</span>m.media-amazon.com/images/M/MV5BMmJlNmU0MjMtYmVkZS00ZDdiLTljZjQtYTA2YWRjYTI1OWYxXkEyXkFqcGdeQXVyMTgxOTIzNzk@.\_V1\_.jpg'

`getTrailerURL(imdb_id)` --> h<span>ttps://www</span>.imdb.com/video/imdb/vi2508831257'

`getTrailerDownloadURL(imdb_id)` --> 'h<span>ttps://</span>imdb-video.media-imdb.com/vi2508831257/1434659607842-pgv4ql-1540843135385.mp4?Expires=1659434493&Signature=SIEnPOL-... '

`getTrailerThumbnailURL(imdb_id)` --> 'h<span>ttps://</span>m.media-amazon.com/images/M/MV5BZmMxNmJiYzctNGRkZC00YzcxLTgyNjMtMmIxZWVlNDA4ZWRjXkEyXkFqcGdeQXRodW1ibmFpbC1pbml0aWFsaXplcg@@.\_V1\_.jpg'

`getKeywords(imdb_id, InList = True)` --> ['serial killer', 'detective', 'serial murder', 'seven deadly sins', 'murder']

`getAka(imdb_id, InList = False)` --> 'Se7en'

`getFilmingLocation(imdb_id, InList = False)` --> 'Pacific Electric Building, Los Angeles, California, USA'


 
