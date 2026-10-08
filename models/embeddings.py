from sentence_transformers import SentenceTransformer
from config.config import EMBEDDING_MODEL

def load_embedding_model():

    model = SentenceTransformer(EMBEDDING_MODEL)

    return model


def embed_text(texts):

    model = load_embedding_model()

    embeddings = model.encode(texts)

    return embeddings