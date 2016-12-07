import Levenshtein_search
from .index import Index

class LevenshteinIndex(Index):
    def __init__(self):
        self.index_key = Levenshtein_search.populate_wordset(-1, [])

        self.docs = []

    def index(self, doc):
        Levenshtein_search.add_string(self.index_key, doc)

    def unindex(self, doc):
        Levenshtein_search.remove_string(self.index_key, doc)

    def initSearch(self):
        pass

    def search(self, doc, threshold=0):
        results = Levenshtein_search.lookup(self.index_key, doc, threshold)
        
        return [doc for doc, _, _ in results]

    def __del__(self):
        Levenshtein_search.clear_wordset(self.index_key)
    
        

        

        
        