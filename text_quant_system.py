# HYBRID SYSTEM ////

# Import libraries
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import RegexpTokenizer
from sklearn import preprocessing
from scipy.sparse import hstack

# LOAD DATASET ////

# Reading data once again to reset changes
df = pd.read_csv(r"/kaggle/input/movies-on-netflix-prime-video-hulu-and-disney/MoviesOnStreamingPlatforms_updated.csv")
df = df.iloc[:, 1:]

# Finding missing values in all columns
missing_values = pd.DataFrame(df.isnull().sum())
missing_values = missing_values.rename(columns={0: "missing_count"})
missing_values["missing_%"] = (missing_values.missing_count / len(df.ID)) * 100

# Dropping values with missing % >50%
df.drop(['Rotten Tomatoes', 'Age'], axis=1, inplace=True)

# Dropping NaN values from the following columns
df.dropna(subset=['IMDb', 'Directors', 'Genres', 'Country', 'Language', 'Runtime'], inplace=True)
df.reset_index(inplace=True, drop=True)

# Convert to object type
df.ID = df.ID.astype('object')
df.Year = df.Year.astype('object')


# PREPROCESSING //// 
def preprocess(df):
    """Conducts preprocessing process detailed above over the input DataFrame"""

    # Store all object columns in a list
    objects = list(df.select_dtypes(include=['object']).columns)

    # Removing ID and Title column
    objects.remove("Title")
    objects.remove('ID')

    # Joining all text/object columns delimited by comma
    df['all_text'] = df[objects].apply(lambda x: ",".join(x.dropna().astype(str)), axis=1)

    # Create tokenizer to remove unwanted elements from data (symbols, numbers...)
    token = RegexpTokenizer(r'[a-zA-Z]+')

    # Convert TfidfVector from text
    cv = TfidfVectorizer(lowercase=True, stop_words='english', ngram_range=(1, 1), tokenizer=token.tokenize)
    text_counts = cv.fit_transform(df['all_text'])

    # Select quantitative variables and scale them
    num_df = df.select_dtypes(include=['float64', 'int64'])
    scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
    scaled_num_df = pd.DataFrame(scaler.fit_transform(num_df))
    scaled_num_df.columns = num_df.columns

    # Add quantitative variables to the TF-IDF vector
    IMDb = scaled_num_df.IMDb.values[:, None]
    X_train_dtm = hstack((text_counts, IMDb))
    netflix = scaled_num_df.Netflix.values[:, None]
    X_train_dtm = hstack((X_train_dtm, netflix))
    hulu = scaled_num_df.Hulu.values[:, None]
    X_train_dtm = hstack((X_train_dtm, hulu))
    prime = scaled_num_df["Prime Video"].values[:, None]
    X_train_dtm = hstack((X_train_dtm, prime))
    disney = scaled_num_df["Disney+"].values[:, None]
    X_train_dtm = hstack((X_train_dtm, disney))
    runtime = scaled_num_df['Runtime'].values[:, None]
    X_train_dtm = hstack((X_train_dtm, runtime))

    return X_train_dtm


# Preprocessing data
mat = preprocess(df)


# RECOMMENDATIONS
def give_recommendation(title, sig=cos_sim):
    """Takes a movie title and similarity score and returns a top 10 list of recommended movies from the dataset"""

    # Get index corresponding to the original title
    idx = indices[title]

    # Get the pairwise similarity scores
    sig_scores = [*enumerate(sig[idx])]

    # Sort the movies
    sig_scores = sorted(sig_scores, key=lambda x: x[1], reverse=True)

    # Scores of the 10 most similar movies
    sig_scores = sig_scores[1:11]

    # Movie indices
    movie_indices = [i[0] for i in sig_scores]

    # Top 10 similar movies
    return df['Title'].iloc[movie_indices]


# Compute the sigmoid kernel
sig2 = cosine_similarity(mat, mat)

# Reverse mapping of indices and movie titles
indices = pd.Series(df.index, index=df['Title']).drop_duplicates()

# Getting a recommendation
give_recommendation("The Matrix", sig=sig2)
