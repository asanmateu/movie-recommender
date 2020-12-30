# NUMERIC SYSTEM ////

# Import libraries
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn import preprocessing


# LOADING DATA & HANDLE MISSING VALUES ////

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

# Select the numerical variable
num_df = df.select_dtypes(include=['float64', 'int64'])

# Scaling the numerical variable using a min-max scaler to reduce model complexity and training time
scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
trans_df = pd.DataFrame((scaler.fit_transform(num_df)))
trans_df.columns = num_df.columns

# Compute cosine similarity
cos_sim = cosine_similarity(trans_df, trans_df)

# Reverse mapping of indices and movie titles
indices = pd.Series(df.index, index=df['Title']).drop_duplicates()


# RECOMMENDATION FUNCTION
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


give_recommendation("The Matrix", sig=cos_sim)
