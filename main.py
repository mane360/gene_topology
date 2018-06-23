from lib import *
from sys import argv


def main(seed_filename, data_filename, test=False):
    seed_file = read(seed_filename, False)
    data_file = read(data_filename)

    seed = get_seed_list(seed_file)
    
    networks = find_networks(data_file)
        
    seeded_networks = filter_by_seed(networks, seed)
    
    results = get_data_for_seeded_networks(seeded_networks, data_file, test)
    
    return results


if __name__ == "__main__":
    data_filename_arg = argv[1]
    seed_filename_arg = argv[2]

    main(seed_filename_arg, data_filename_arg)
