# you'll need to install sklearn as its not a dependency of ell
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import json


class VectorStore:
    def __init__(self, vectorizer, tfidf_matrix, documents, thePassedDict=None):
        self.vectorizer = vectorizer
        self.tfidf_matrix = tfidf_matrix
        self.documents = documents
        self.thedict = thePassedDict

    @classmethod
    def from_documents(cls, documents):
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(documents)
        return cls(vectorizer, tfidf_matrix, documents)
    
    @classmethod
    def from_dict_inmemory(cls, data_dict):
        documents = list(data_dict.keys())
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(documents)
        return cls(vectorizer, tfidf_matrix, documents, data_dict)  # Pass the original dict
    
    @classmethod
    def from_dict_json(cls, jsonstring : str):
        data_dict = json.load(jsonstring)
        return cls.from_dict_inmemory(data_dict)
    
    @classmethod
    def from_dict_json_file(cls, filepath : str):
        with open(filepath, "r") as f:
            data_dict = json.load(f)
        return cls.from_dict_inmemory(data_dict)


    def search_strings(self, query: str, k: int = 2) -> list[dict]:
        query_vector = self.vectorizer.transform([query])
        similarities = cosine_similarity(query_vector, self.tfidf_matrix).flatten()
        top_k_indices = np.argsort(similarities)[-k:][::-1]
        return [
            {"document": self.documents[i], "relevan": float(similarities[i])}
            for i in top_k_indices
        ]


    def search_dict(self, query: str, k: int = 2) -> list[dict]:
        query_vector = self.vectorizer.transform([query])
        similarities = cosine_similarity(query_vector, self.tfidf_matrix).flatten()
        top_k_indices = np.argsort(similarities)[-k:][::-1]
        return [
            {"document": self.documents[i], "Value": self.thedict[self.documents[i]], "relevan": float(similarities[i])}
            for i in top_k_indices
        ]


if __name__ == "__main__":

    vector_store = VectorStore.from_dict_json_file("test.json")
    query = "Null Reference Exception: The object \"uber\" of type int returned null"
    context = vector_store.search(query)
    print(context)

