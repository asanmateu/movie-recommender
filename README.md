# Movie Recommendations Algorithm

Notebook containing a detailed exploratory data analysis and a NLP vector based recommendations system with Python3 and Scikit-Learn using a Kaggle dataset containing movies hosted by Netflix, Hulu, Prime Video, and Disney+.

Dataset: https://www.kaggle.com/ruchi798/movies-on-netflix-prime-video-hulu-and-disney / Guidance by Avinash Navlani

# 1. Dataset Exploration

**Data Attributes**

1. ID: Unique identifier for each record
2. Title: Name of the movie
3. Year: Release year of the movie
4. Age: Target age group
5. IMDb: IMDB movie rating (/10)
6. Rotten Tomatoes: Rotten Tomatoes % rating
7. Netflix: Movie is found on netflix (1/0)
8. Hulu: Movie is found on Hulu (1/0)
9. Prime Video: Movie is found on Prime Video
10. Disney+: Movie is found on Disney+ (1/0)
11. Type: Movie or TV show
12. Directors: Name of director
13. Genres: Genre category
14. Country: Country of origin
15. Language: Original version language
16. Runtime: Duration of the movie

# 2. Handling Missing Values

1. Drop columns with >50% NaN values
2. Drop NaN rows
3. Reset index
4. Convert data types

# 3. Exploratory Data Analysis

**Statistical exploration includes:**

1. Distribution plots
2. Distribution of movies on each streaming platform
3. Movie distributions according to:
    * Genre
    * Country
    * Language
4. IMDb distribution on each platform
5. Runtime analysis per platform and age group

# 4. Recommendations Systems

1. Quantitatice system
2. Quant-text hybrid system

