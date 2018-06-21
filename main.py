INDEX_G1 = 1
INDEX_G2 = 3
INDEX_SCORE = 5
INDEX_EXTRA_DATA = 6

def fill_networks(seed, filename):
    f = open(filename)
    for line in f:
        list_line = line.split("\t")
        g1 = list_line[INDEX_G1]
        g2 = list_line[INDEX_G2]
        score = list_line[INDEX_SCORE]
        extra = list_line[INDEX_EXTRA_DATA:]
        
        print("g1: %s, g2: %s, score: %s, extra: %s" % (g1, g2, score, extra))
        break
    
    f.close()

fill_networks(1, "test_data")