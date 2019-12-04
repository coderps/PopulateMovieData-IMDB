# PopulateMovieData-IMDB

This is a simple code to print the details of the top 250 movies available on IMDB servers

## Installation

```bash
pip install IMDbPY
```

## Usage

Sample Code:
```python
from imdb import IMDb

# create an instance of the IMDb class
ia = IMDb()

# get a movie and print its director(s)
the_matrix = ia.get_movie('0133093')
for director in the_matrix['directors']:
    print(director['name'])

# show all information that are currently available for a movie
print(sorted(the_matrix.keys()))

# show all information sets that can be fetched for a movie
print(ia.get_movie_infoset())

# update a Movie object with more information
ia.update(the_matrix, ['technical'])
# show which keys were added by the information set
print(the_matrix.infoset2keys['technical'])
# print one of the new keys
print(the_matrix.get('tech'))
```

For complete documentation, visit this [page](https://imdbpy.readthedocs.io/en/latest/)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
