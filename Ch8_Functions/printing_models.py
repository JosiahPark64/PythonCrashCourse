import printing_functions as pf
#start with designs that need to be printed
unprinted_designs_original = ['phone case', 'robot pendant', 'dodecahedron']
completed_models_original = []

#to pass a COPY of a list to a function, use slice notation
pf.print_models(unprinted_designs_original[:], completed_models_original)
pf.show_completed_models(completed_models_original)