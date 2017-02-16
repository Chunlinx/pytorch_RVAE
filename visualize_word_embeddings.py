from sklearn.decomposition import PCA
from utils import BatchLoader
import matplotlib.pyplot as plt
import numpy as np
import os

if not os.path.exists('data/word_embeddings.npy'):
    raise FileNotFoundError("word embdeddings file was't found")

batch_loader = BatchLoader()

pca = PCA(n_components=2)
word_embeddings = np.load('data/word_embeddings.npy')
word_embeddings_pca = pca.fit_transform(word_embeddings)

words = batch_loader.idx_to_word

fig, ax = plt.subplots()
fig.set_size_inches(150, 150)
x = word_embeddings_pca[:, 0]
y = word_embeddings_pca[:, 1]
ax.scatter(x, y)

for i, word in enumerate(words):
    ax.annotate(word, (x[i], y[i]))

fig.savefig('word_embedding.png', dpi=100)