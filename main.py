INDEX_G1 = 1
INDEX_G2 = 3
INDEX_SCORE = 5
INDEX_EXTRA_DATA = 6

def fill_networks(seed, filename):
    f = open(filename, "r")    
    f.readline() # skip header
    
    # FIRST PASS - FIND ALL NETWORKS
    
    # initialise empty set of sets
    # each set represents a connected network
    networks = []   
    
    for line in f:
        list_line = line.split("\t")
        g1 = list_line[INDEX_G1]
        g2 = list_line[INDEX_G2]
        score = list_line[INDEX_SCORE]
        
        if (float(score) > 0): # if the nodes are connected
        
            found = False
            
            for network in networks:
                if (g1 in network or g2 in network):
                    found = True
                    network.add(g1)
                    network.add(g2)
                    break
            
            if (found == False):
                networks.append(set([g1, g2]))
        
    # REMOVE NETWORKS THAT DON'T HAVE A SEED
    
    seeded_networks = []
    for network in networks:
        if (len(network.intersection(seed)) > 0): # if there is a seed in the network
            seeded_networks.append(network)
        # otherwise, ignore it
    
    # SECOND PASS - GET DATA FOR SEEDED NETWORKS
    
    f.seek(0)
    results = []
    f.readline() # skip header
    
    for line in f:
        list_line = line.split("\t")
        g1 = list_line[INDEX_G1]
        g2 = list_line[INDEX_G2]
        score = list_line[INDEX_SCORE]
        extra = list_line[INDEX_EXTRA_DATA:]
        
        for network in networks:
            if (g1 in network): # g2 must also be in the network
                row = [g1, g2, score]
                row.extend(extra)
                results.append(row)
            break
    
    return results

# TESTS
    
def print_results(got, target):
    if (got != target):
        print("FAIL!\ngot: %s\ntarget: %s\n" % (got, target))
    else:
        print("pass")

def test_readfile_and_output():
    got = fill_networks(["1"], "test_readfile_and_output")
    target = [["1", "2", "3", "4", "5", "6", "7", "8\n"]]
    print_results(got, target)
          
def test_two_rows_one_with_seed():
    got = fill_networks(["1"], "test_two_rows_one_with_seed")
    target = [["1", "2", "1.0", "0", "0", "0", "0", "0\n"]]
    print_results(got, target)

def test_two_rows_one_with_nonzero_score():
    got = fill_networks(["1", "4"], "test_two_rows_one_with_nonzero_score")
    target = [["1", "2", "1.0", "0", "0", "0", "0", "0\n"]]
    print_results(got, target)

def test_network_genes_removed_from_seed():
    got = fill_networks(["1"], "test_network_genes_removed_from_seed")
    target = [["1", "2", "1.0", "0", "0", "0", "0", "0\n"],
              ["4", "5", "1.0", "0", "0", "0", "0", "0\n"],
              ["2", "4", "1.0", "0", "0", "0", "0", "0\n"]]
    print_results(got, target)

test_readfile_and_output()
test_two_rows_one_with_seed()
test_two_rows_one_with_nonzero_score()
test_network_genes_removed_from_seed()