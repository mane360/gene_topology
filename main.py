from lib import *


def main(seed, filename, test):
    f = open(filename, "r")    
    f.readline()  # skip header
    
    networks = find_networks(f)
        
    seeded_networks = filter_by_seed(networks, seed)
    
    results = get_data_for_seeded_networks(seeded_networks, f, test)
    
    return results
