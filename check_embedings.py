import numpy as np
embeddings = np.load('embeddings.npy')
print(f"Tamaño del array de embeddings: {embeddings.shape}")
print(f"Primeros embeddings:\n{embeddings[:5]}")