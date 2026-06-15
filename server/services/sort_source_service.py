from typing import List
from sentence_transformers import SentenceTransformer
import numpy as np


class SortSourceService:
    def __init__(self):
        self.embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

    def sort_sources(self, query: str, search_results: List[dict]):
        relevance_docs = []
        query_embedding = self.embedding_model.encode(query)

        # Calculate similarity for each result
        for result in search_results:
            content = result.get("content", "")
            if content:  # Only embed if content exists
                content_embedding = self.embedding_model.encode(content)
                similarity = np.dot(query_embedding, content_embedding) / (
                    np.linalg.norm(query_embedding) * np.linalg.norm(content_embedding)
                )
                result["relevance_score"] = float(similarity)
            else:
                result["relevance_score"] = 0.0

            if (
                similarity > 0.3
            ):  # Only consider results with a relevance score above 0.3
                relevance_docs.append(result)

        # Sort by relevance score (highest first)
        sorted_results = sorted(
            relevance_docs, key=lambda x: x.get("relevance_score", 0), reverse=True
        )
        return sorted_results
