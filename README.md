# React Tutorial project

The data folder contains an example dataset from [The Movie Database](https://www.themoviedb.org).


## Image URLs

To build an image URL, you will need 3 pieces of data. 
The base_url, size and file_path. Simply combine them all and you will have a fully qualified URL. Here’s an example URL:

    https://image.tmdb.org/t/p/w500/8uO0gUM8aNqYLs1OsTBQiXu0fEv.jpg

### Base URL:

    http://image.tmdb.org/t/p/
    https://image.tmdb.org/t/p/
    
### Sizes:

    [
        "w92",
        "w154",
        "w185",
        "w342",
        "w500",
        "w780",
        "original"
    ],

## Update dataset:

Create a `.env` file in the root folder with the following content:

    TMDB_KEY=<your api key>
    
Install the python dependencies

    pip install -r requirements.txt
    
Run the scrape script
  
    python scrape.py
    
