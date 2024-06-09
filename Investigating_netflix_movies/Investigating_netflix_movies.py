import pandas as pd
import matplotlib.pyplot as plt

netflix_df = pd.read_csv("netflix_data.csv")

after_nineteens = netflix_df.loc[(netflix_df["release_year"] > 1989) & (netflix_df["type"]=="Movie") & (netflix_df["release_year"] < 2000)]
plt.hist(after_nineteens["duration"])
plt.title('Distribution of Movie Durations in the 1990s')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.show()

duration = 100

action_movies_1990s = movies_1990s[movies_1990s["genre"] == "Action"]

short_movie_count = 0

for label, row in action_movies_1990s.iterrows() :
    if row["duration"] < 90 :
        short_movie_count = short_movie_count + 1
    else:
        short_movie_count = short_movie_count

print(short_movie_count)

