class MySet:

    def __init__(self, list = []):
        self.dictionary = {}
        for value in list:
            self.dictionary[value] = True
    def __repr__(self):
        return f"MySet({self.dictionary})"
    
    def has(self, value):
        return value in self.dictionary
    
    def add(self, value):
        self.dictionary[value] = True
        return self
    
    def delete(self, value):
        self.dictionary.pop(value)
        return self
    
    def size(self):
        return len(self.dictionary)
    
    def move(self, value1, value2):
    # value2 is the key to be moved, value1 is the value where value2 will be next to
        value_to_move = self.dictionary.pop(value2)
        new_dict = {}
        for key, value in self.dictionary.items():
            new_dict[key] = value
            if key == value1:
                new_dict[value2] = value_to_move
        self.dictionary = new_dict
    def __str__(self):
        return f"MySet: {{{(','.join(map(str, self.dictionary.keys())))}}}"

    def clear(self):
        self.dictionary = {}