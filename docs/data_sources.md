# About Dataset
Dataset was selected and downloaded from Kaggle.
Data Integration was done to Postgres using **Airbyte** in a separate process.


# Context
These files contain metadata for all 45,000 movies listed in the Full MovieLens Dataset.
The dataset consists of movies released on or before July 2017.
Data points include cast, crew, plot keywords, budget, revenue, posters, release dates, languages, production companies, countries, TMDB vote counts and vote averages.

This dataset also has files containing 26 million ratings from 270,000 users for all 45,000 movies.
Ratings are on a scale of 1-5 and have been obtained from the official GroupLens website.


# Content
This dataset consists of the following files:
- movies_metadata.csv: The main Movies Metadata file. Contains information on 45,000 movies featured in the Full MovieLens dataset. Features include posters, backdrops, budget, revenue, release dates, languages, production countries and companies.
- keywords.csv: Contains the movie plot keywords for our MovieLens movies. Available in the form of a stringified JSON Object.
- credits.csv: Consists of Cast and Crew Information for all our movies. Available in the form of a stringified JSON Object.
- links.csv: The file that contains the TMDB and IMDB IDs of all the movies featured in the Full MovieLens dataset.
- links_small.csv: Contains the TMDB and IMDB IDs of a small subset of 9,000 movies of the Full Dataset.
- ratings_small.csv: The subset of 100,000 ratings from 700 users on 9,000 movies.

The Full MovieLens Dataset consisting of 26 million ratings and 750,000 tag applications from 270,000 users on all the 45,000 movies in this dataset can be accessed here: https://grouplens.org/datasets/movielens/latest/


# Source Schema
Query for schema:
```sql
select
    table_schema
    , table_name
    , column_name
    , data_type
    , character_maximum_length
    , column_default
    , is_nullable
FROM 
   information_schema.columns
WHERE 
   table_name = '<table_name>';
```

## Credits
```
table_schema|table_name|column_name            |data_type               |character_maximum_length|column_default|is_nullable|
------------+----------+-----------------------+------------------------+------------------------+--------------+-----------+
srcdata     |credits   |id                     |text                    |                        |              |YES        |
srcdata     |credits   |cast                   |text                    |                        |              |YES        |
srcdata     |credits   |crew                   |text                    |                        |              |YES        |
srcdata     |credits   |_airbyte_ab_id         |character varying       |                        |              |YES        |
srcdata     |credits   |_airbyte_emitted_at    |timestamp with time zone|                        |              |YES        |
srcdata     |credits   |_airbyte_normalized_at |timestamp with time zone|                        |              |YES        |
srcdata     |credits   |_airbyte_credits_hashid|text                    |                        |              |YES        |
```

## Keywords
```
table_schema|table_name|column_name             |data_type               |character_maximum_length|column_default|is_nullable|
------------+----------+------------------------+------------------------+------------------------+--------------+-----------+
srcdata     |keywords  |id                      |text                    |                        |              |YES        |
srcdata     |keywords  |keywords                |text                    |                        |              |YES        |
srcdata     |keywords  |_airbyte_ab_id          |character varying       |                        |              |YES        |
srcdata     |keywords  |_airbyte_emitted_at     |timestamp with time zone|                        |              |YES        |
srcdata     |keywords  |_airbyte_normalized_at  |timestamp with time zone|                        |              |YES        |
srcdata     |keywords  |_airbyte_keywords_hashid|text                    |                        |              |YES        |
```

## Links
```
table_schema|table_name|column_name           |data_type               |character_maximum_length|column_default|is_nullable|
------------+----------+----------------------+------------------------+------------------------+--------------+-----------+
srcdata     |links     |movieid               |text                    |                        |              |YES        |
srcdata     |links     |imdbid                |text                    |                        |              |YES        |
srcdata     |links     |tmdbid                |text                    |                        |              |YES        |
srcdata     |links     |_airbyte_ab_id        |character varying       |                        |              |YES        |
srcdata     |links     |_airbyte_emitted_at   |timestamp with time zone|                        |              |YES        |
srcdata     |links     |_airbyte_normalized_at|timestamp with time zone|                        |              |YES        |
srcdata     |links     |_airbyte_links_hashid |text                    |                        |              |YES        |
```

## Movies_metadata
```
table_schema|table_name     |column_name                    |data_type               |character_maximum_length|column_default|is_nullable|
------------+---------------+-------------------------------+------------------------+------------------------+--------------+-----------+
srcdata     |movies_metadata|id                             |text                    |                        |              |YES        |
srcdata     |movies_metadata|imdb_id                        |text                    |                        |              |YES        |
srcdata     |movies_metadata|title                          |text                    |                        |              |YES        |
srcdata     |movies_metadata|original_title                 |text                    |                        |              |YES        |
srcdata     |movies_metadata|runtime                        |text                    |                        |              |YES        |
srcdata     |movies_metadata|video                          |text                    |                        |              |YES        |
srcdata     |movies_metadata|poster_path                    |text                    |                        |              |YES        |
srcdata     |movies_metadata|spoken_languages               |text                    |                        |              |YES        |
srcdata     |movies_metadata|revenue                        |text                    |                        |              |YES        |
srcdata     |movies_metadata|release_date                   |text                    |                        |              |YES        |
srcdata     |movies_metadata|production_companies           |text                    |                        |              |YES        |
srcdata     |movies_metadata|genres                         |text                    |                        |              |YES        |
srcdata     |movies_metadata|popularity                     |text                    |                        |              |YES        |
srcdata     |movies_metadata|vote_average                   |text                    |                        |              |YES        |
srcdata     |movies_metadata|production_countries           |text                    |                        |              |YES        |
srcdata     |movies_metadata|belongs_to_collection          |text                    |                        |              |YES        |
srcdata     |movies_metadata|tagline                        |text                    |                        |              |YES        |
srcdata     |movies_metadata|adult                          |text                    |                        |              |YES        |
srcdata     |movies_metadata|vote_count                     |text                    |                        |              |YES        |
srcdata     |movies_metadata|budget                         |text                    |                        |              |YES        |
srcdata     |movies_metadata|status                         |text                    |                        |              |YES        |
srcdata     |movies_metadata|homepage                       |text                    |                        |              |YES        |
srcdata     |movies_metadata|overview                       |text                    |                        |              |YES        |
srcdata     |movies_metadata|original_language              |text                    |                        |              |YES        |
srcdata     |movies_metadata|_airbyte_ab_id                 |character varying       |                        |              |YES        |
srcdata     |movies_metadata|_airbyte_emitted_at            |timestamp with time zone|                        |              |YES        |
srcdata     |movies_metadata|_airbyte_normalized_at         |timestamp with time zone|                        |              |YES        |
srcdata     |movies_metadata|_airbyte_movies_metadata_hashid|text                    |                        |              |YES        |
```

## Ratings
```
table_schema|table_name|column_name        |data_type               |character_maximum_length|column_default|is_nullable|
------------+----------+-------------------+------------------------+------------------------+--------------+-----------+
srcdata     |ratings   |ratings_data       |jsonb                   |                        |              |YES        |
srcdata     |ratings   |_airbyte_emitted_at|timestamp with time zone|                        |              |YES        |
```
> Note: `Ratings` table's original data was compromised so just extracted the required metadata from backup and stored as JSON in single column


# Acknowledgements
This dataset is an ensemble of data collected from TMDB and GroupLens.
The Movie Details, Credits and Keywords have been collected from the TMDB Open API.
This product uses the TMDb API but is not endorsed or certified by TMDb.
Their API also provides access to data on many additional movies, actors and actresses, crew members, and TV shows.

You can try it for yourself here: https://www.themoviedb.org/documentation/api

The Movie Links and Ratings have been obtained from the Official GroupLens website. The files are a part of the dataset available here

## Inspiration
The notebooks for the original inspiration are are available as kernels with this dataset: [The Story of Film](https://www.kaggle.com/rounakbanik/the-story-of-film) and [Movie Recommender Systems](https://www.kaggle.com/rounakbanik/the-story-of-film)

Some of the things you can do with this dataset:
Predicting movie revenue and/or movie success based on a certain metric. What movies tend to get higher vote counts and vote averages on TMDB? Building Content Based and Collaborative Filtering Based Recommendation Engines.
