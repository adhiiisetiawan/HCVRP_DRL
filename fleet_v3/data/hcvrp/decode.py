import pickle

# Specify the path to your pickle file
pickle_file_path = 'hcvrp_v3_40_seed24610.pkl'

# Load data from the pickle file
with open(pickle_file_path, 'rb') as f:
    loaded_data = pickle.load(f)

print(f"Total instance: {len(loaded_data)}")
print(f"Get 1st instance: {loaded_data[0]}")
print("")
print(f"Depot coordinate location 1st instance: {loaded_data[0][0]}")
print("")
print(f"Coordinate of customer 1st instance: {loaded_data[0][1]}")
print(f"Total number of customer: {len(loaded_data[0][1])}")
print("")
print(f"Demand of customer: {loaded_data[0][2]}")
print(f"Total Demand of customer: {len(loaded_data[0][2])}")
print("")
print(f"Capicity of 3 vehicle: {loaded_data[0][3]}")
# import pprint

# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(loaded_data)