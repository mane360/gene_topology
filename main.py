from lib import *
from sys import argv


def main(seed_filename, data_filename, distance=-1, test=False):
    print("Open the file")
    seed_file = read(seed_filename, False)
    data_file = read(data_filename)

    print("Make list of seed")
    seed = get_seed_list(seed_file)
    
    seeded_networks = set()
    
    if distance == -1:
    
        print("make list of networks")
        networks = find_networks(data_file)
        
        print("network doesnt contain aseed")
        seeded_networks = filter_by_seed(networks, seed)
        
        print("output")
        results = get_data_for_seeded_networks(seeded_networks, data_file, test)
        
    else:
        print("make list of networks to distance %s" % distance)
        seeded_networks = find_cropped_networks(data_file, seed, distance)

        print("output")
        results = get_data_for_seeded_networks_pairs(seeded_networks, data_file, test)
    
    print("Done")
    return results


if __name__ == "__main__":
    seed_filename = argv[1]
    data_filename = argv[2]
    distance = int(argv[3])
    main(seed_filename, data_filename, distance, False)
    
    