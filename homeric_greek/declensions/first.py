from enum import StrEnum

class MasculineSingular(StrEnum):
    NOMINATIVE = 'ς'
    GENITIVE = 'ο'
    DATIVE = 'ι'
    ACCUSATIVE = 'ν'
    VOCATIVE = ''

class FeminineSingular(StrEnum):
    NOMINATIVE = ''
    GENITIVE = 'ης'
    DATIVE = 'ι'
    ACCUSATIVE = 'ν'
    VOCATIVE = ''

# Both masculine and feminine endings are the same for dual and plural
class Dual(StrEnum):
    NOMINATIVE = ''
    GENITIVE = 'ιιν'
    DATIVE = 'ιιν'
    ACCUSATIVE = ''
    VOCATIVE = ''

class Plural(StrEnum):
    NOMINATIVE = 'ι'
    GENITIVE = 'ων'
    DATIVE = ('ισι', 'ις')
    ACCUSATIVE = 'νς'
    VOCATIVE = 'ι'
