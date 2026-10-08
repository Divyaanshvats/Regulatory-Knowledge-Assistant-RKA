import faiss
from models.embeddings import embed_text
from utils.document_loader import load_documents


def build_vector_store():

    docs = load_documents()

    texts = [doc.page_content for doc in docs]

    embeddings = embed_text(texts)

    dimension = len(embeddings[0])

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    return index, docs


def retrieve_context(query, index, docs, k=3):

    query_embedding = embed_text([query])

    distances, indices = index.search(query_embedding, k)

    results = []
    scores = []

    for i, idx in enumerate(indices[0]):
        results.append(docs[idx].page_content)
        scores.append(distances[0][i])

    return results, scores