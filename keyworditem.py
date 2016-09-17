class KeywordItem(object):
    def __init__(self, text_id, text, connection_id):
        self.text_id = text_id
        self.text = text
        self.connection_id = connection_id
        self.synonyms = []

    def __hash__(self):
        return hash(self.connection_id)

    def __eq__(self, other):
        if self.connection_id == other.connection_id:
            if (not self.synonyms.__contains__(other)) and self.text != other.text:
                self.synonyms.append(other)
        return self.connection_id == other.connection_id

    def __str__(self):
        return self.text

    def __repr__(self):
        return self.text
