#Using prebuilt modules using import keyword
import math #imports the math library
import math as m #import library with an alias
from math import sqrt #import specific funtion from the library
                      #You can also import multiple functions at once (eg, sqrt, tan, cos)

print(math.sqrt(256)) #Using the sqrt function from the math library
print(m.sqrt(64)) #Using the alias to call the func in math library
print(sqrt(16)) #Using the imported function directly
