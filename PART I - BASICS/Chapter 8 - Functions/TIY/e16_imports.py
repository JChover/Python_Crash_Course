# 8-16 Imports
"""To use the print_models function from the printing_functions.py file,
we can import it into our main program file using different approaches."""
# import module_name
import e16_printing_functions

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

e16_printing_functions.print_models(unprinted_designs, completed_models)
e16_printing_functions.show_completed_models(completed_models)

#from module_name import function_name
from e16_printing_functions import print_models, show_completed_models

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

#from module_name import function_name as fn
from e16_printing_functions import print_models as pm
from e16_printing_functions import show_completed_models as scm

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

pm(unprinted_designs, completed_models)
scm(completed_models)

#import module_name as mn
import e16_printing_functions as pf

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)

#import module name import *
from e16_printing_functions import *

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
