import kagglehub
import pandas as pd
from pathlib import Path
import sys
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from scipy.sparse import hstack

anime_title = sys.argv[1]

# 読み込み
src_dir_path = Path(kagglehub.dataset_download("CooperUnion/anime-recommendations-database"))
anime_file = "anime.csv"

# 欠損データ削除
anime = pd.read_csv(src_dir_path / anime_file).dropna()

# 辞書化
indices = pd.Series(anime.index, index=anime["name"]).drop_duplicates()
matches = [n for n in indices.index if anime_title.lower() in n.lower()]
if not matches:
    print(f"{anime_title} not found")
    sys.exit()
anime_file = matches[0]

# 計算対象をベクトル化
genre_tfdif = TfidfVectorizer(stop_words="english")
genre_matrix = genre_tfdif.fit_transform(anime["genre"])

name_tfdif = TfidfVectorizer(stop_words="english")
name_matrix = name_tfdif.fit_transform(anime["name"])

# ベクトルを結合
combined_matrix = hstack([genre_matrix, name_matrix])

# コサイン類似度の計算
cosine_sim = linear_kernel(combined_matrix, combined_matrix)

# アニメ番号と類似度のペアを作る
idx = indices[anime_title]
sim_scores = list(enumerate(cosine_sim[idx]))

# 類似度でソートし、自分を除く10件を選ぶ
sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

# アニメのインデックスだけを抽出
anime_indices = [i[0] for i in sim_scores]

# 類似度の高い順に並べたアニメのindexでそのデータを抽出し、列を選択
similar_animes = anime.iloc[anime_indices][["name", "genre", "rating"]]
similar_animes = similar_animes[~similar_animes["name"].str.contains(anime_title, case=False)][1:11]
print(similar_animes)