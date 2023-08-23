import pickle

# Specify the path to your pickle file
pickle_file_path = 'hcvrp_v3_40.pkl'

# Load data from the pickle file
with open(pickle_file_path, 'rb') as f:
    loaded_data = pickle.load(f)

import pprint

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(loaded_data)