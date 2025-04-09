from homeric_greek.declinables.gender import Gender

class Noun:
    def __init__(self,
                 stem: str,
                 gender: str):
        self._stem = stem
        self._gender = Gender[gender]

    def __repr__(self) -> str:
        return ('Noun('
                + f'stem={self._stem!r},'
                + f' gender={self._gender!r}'
                + ')')

    @property
    def stem(self) -> str:
        return self._stem
    
    @property
    def gender(self) -> Gender:
        return self._gender
