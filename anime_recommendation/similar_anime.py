import kagglehub
import pandas as pd
from pathlib import Path
import sys
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

anime_title = sys.argv[1]

# 読み込み
src_dir_path = Path(kagglehub.dataset_download("CooperUnion/anime-recommendations-database"))
anime_file = "anime.csv"

# 欠損データ削除
anime = pd.read_csv(src_dir_path / anime_file).dropna()

# 辞書化
indices = pd.Series(anime.index, index=anime["name"]).drop_duplicates()
if anime_title not in indices:
    print(f"{anime_title} not found")
    sys.exit()

# 計算対象をベクトル化
tfidf = TfidfVectorizer(stop_words="english")
tfdif_matrix = tfidf.fit_transform(anime["genre"])

# コサイン類似度の計算
cosine_sim = linear_kernel(tfdif_matrix, tfdif_matrix)

# アニメ番号と類似度のペアを作る
idx = indices[anime_title]
sim_scores = list(enumerate(cosine_sim[idx]))

# 類似度でソートし、自分を除く10件を選ぶ
sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:11]

# アニメのインデックスだけを抽出
anime_indices = [i[0] for i in sim_scores]

# 類似度の高い順に並べたアニメのindexでそのデータを抽出し、列を選択
similar_animes = anime.iloc[anime_indices][["name", "genre", "rating"]]
print(similar_animes)