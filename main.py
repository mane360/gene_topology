INDEX_G1 = 1
INDEX_G2 = 3
INDEX_SCORE = 5
INDEX_EXTRA_DATA = 6

def fill_networks(seed, filename):
    f = open(filename)
    results = []       
    f.readline() # skip header
    
    
    # initialise empty set of sets
    # each set represents a connected network
    networks = set()    
    
    for line in f:
        list_line = line.split("\t")
        g1 = list_line[INDEX_G1]
        g2 = list_line[INDEX_G2]
        score = list_line[INDEX_SCORE]
        extra = list_line[INDEX_EXTRA_DATA:]
        
        if (g1 in seed or g2 in seed): # todo parse score
            networks.update(set([g1, g2]))
        
            row = [g1, g2, score]
            row.extend(extra)
            results.append(row)    
    
    f.close()
    return results

# TESTS

def test_readfile_and_output():
    got = fill_networks(["1"], "test_readfile_and_output")
    target = [["1", "2", "3", "4", "5", "6", "7", "8\n"]]
    if (got != target):
        print("FAIL!\ngot: %s\ntarget: %s\n" % (got, target))
    else:
        print("pass")
          
def test_two_rows_one_with_seed():
    got = fill_networks(["1"], "test_two_rows_one_with_seed")
    target = [["1", "2", "1.0", "0", "0", "0", "0", "0\n"]]
    if (got != target):
        print("FAIL!\ngot: %s\ntarget: %s\n" % (got, target))
    else:
        print("pass")


test_readfile_and_output()
test_two_rows_one_with_seed()