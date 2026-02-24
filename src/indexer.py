class Indexer:
        def __init__(self):
                        self.inverted_index = {}
        self.total_docs = 0
        self.doc_lengths = {}

        def add_document(self, doc_id, text):
                        self.total_docs += 1
                        text = text.lower()
                        words = text.split()
                        self.doc_lengths[doc_id] = len(words)