from pathlib import Path
import pandas as pd

path = Path("C:/Users/kawah/.cache/kagglehub/datasets/CooperUnion/anime-recommendations-database/versions/1/anime.csv")
df = pd.read_csv(path).dropna()
# print(df.loc[:, ['rating']])

# print(df[(df['rating']>=9) & ("Slice of Life" in df['genre'])])
print(df[(df['genre'].str.contains("Slice of Life")) & (df['rating'] >= 9)])