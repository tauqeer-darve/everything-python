text = 'apple'                  # str
number = 10                    # int
decimal = -10.123              # float
has_money = True               # bool
coordinates = (2.5, 1.5)       # tuple
names = ['Agnetha', 'Björn', 'Benny', 'Anni-Frid']  # list
unique = {1, 2, 3, 4, 4, 5}    # set (duplicates removed → {1,2,3,4,5})
users = {'Bob': 1, 'James': 2} # dict

# TYPE CONVERSIONS

# to string
num_str = str(number)          # str
dec_str = str(decimal)         # str

# to int
str_to_int = int("100")        # int
dec_to_int = int(decimal)      # int

# to float
int_to_float = float(number)   # float
str_to_float = float("10.5")   # float

# to bool
num_to_bool = bool(number)     # bool
empty_to_bool = bool("")       # bool

# to list
tuple_to_list = list(coordinates)  # list
set_to_list = list(unique)         # list

# to tuple
list_to_tuple = tuple(names)       # tuple

# to set (removes duplicates)
list_to_set = set([1, 2, 2, 3])    # set

# to dict
pairs = [('a', 1), ('b', 2)]       # list of tuples
list_to_dict = dict(pairs)         # dict