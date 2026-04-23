# VARIABLES WITH TYPE ANNOTATIONS
# USED TO PREDEFINE THE TYPE OF THE VARIABLE DATA

text: str = 'apple'                  # string
number: int = 10                    # integer
decimal: float = -10.123            # floating point
has_money: bool = True              # boolean
coordinates: tuple[float, float] = (2.5, 1.5)  # tuple of floats
names: list[str] = ['Agnetha', 'Björn', 'Benny', 'Anni-Frid']  # list of strings
unique: set[int] = {1, 2, 3, 4, 4, 5}    # set of ints (duplicates removed)
users: dict[str, int] = {'Bob': 1, 'James': 2} # dict: key=str, value=int