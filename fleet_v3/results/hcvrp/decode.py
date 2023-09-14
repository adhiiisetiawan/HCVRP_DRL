import pickle

# Specify the path to your pickle file
pickle_file_path = 'hcvrp_40_seed24610/hcvrp_40_seed24610-hcvrp40_rollout_v100_20230911T095007_epoch-99-greedy-t1-0-1280.pkl'

# Load data from the pickle file
with open(pickle_file_path, 'rb') as f:
    loaded_data = pickle.load(f)

print(f"Total instance: {len(loaded_data[0])}")
print("")
print(f"Get 1st instance: {loaded_data[0][0]}")
print("")
print(f"Cost: {loaded_data[0][0][0]}")
print("")
print(f"Get tour in 1st instance: {loaded_data[0][0][1]}")
print("")
print(f"Vehicle tour in each customer: {loaded_data[0][0][2]}")
print("")
print(f"Duration: {loaded_data[0][0][3]}")
print(f"Length tour in 1st instance: {len(loaded_data[0][0][1])}")
print(f"Max number tour in 1st instance: {max(loaded_data[0][0][1])}")
# import pprint

# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(loaded_data)