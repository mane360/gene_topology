INDEX_G1 = 1  # type: int
INDEX_G2 = 3
INDEX_SCORE = 5
INDEX_EXTRA_DATA = 6


def relevant_score(score):
    return float(score) != 0


def find_networks(f):
    # initialise empty set of sets
    # each set represents a connected network
    networks = []

    for line in f:
        list_line = line.split("\t")
        g1 = list_line[INDEX_G1]
        g2 = list_line[INDEX_G2]
        score = list_line[INDEX_SCORE]

        # if the nodes are connected
        if relevant_score(score):

            g1_index = -1
            g2_index = -1
            g1_network = []
            g2_network = []
            for index, network in enumerate(networks):

                if g1 in network:
                    g1_index = index
                    g1_network = network
                if g2 in network:
                    g2_index = index
                    g2_network = network

                if g1_index > 0 and g2_index > 0:
                    break

            # if new network
            if g1_index < 0 and g2_index < 0:
                networks.append({g1, g2})

            # if 2 current networks, union
            elif g1_index > -1 and g2_index > -1:
                networks[g1_index].update(networks[g2_index])
                del networks[g2_index]

            # if 1 current network
            elif g1_index > -1:
                g1_network.add(g2)
            elif g2_index > -1:
                g2_network.add(g1)
            else:
                raise Exception()

    return networks


def filter_by_seed(networks, seed):
    seeded_networks = []
    for network in networks:
        # if there is a seed in the network
        if len(network.intersection(seed)) > 0:
            seeded_networks.append(network)
        # otherwise, ignore it

    return seeded_networks


def get_data_for_seeded_networks(seeded_networks, f):
    f.seek(0)
    f.readline()  # skip header
    results = []

    for line in f:
        list_line = line.split("\t")
        g1 = list_line[INDEX_G1]
        g2 = list_line[INDEX_G2]
        score = list_line[INDEX_SCORE]
        extra = list_line[INDEX_EXTRA_DATA:]

        if relevant_score(score):
            for seeded_network in seeded_networks:
                if g1 in seeded_network:  # g2 must also be in the network
                    row = [g1, g2, score]
                    row.extend(extra)
                    results.append(row)
                    break

    return results


def main(seed, filename):
    f = open(filename, "r")    
    f.readline()  # skip header
    
    networks = find_networks(f)
        
    seeded_networks = filter_by_seed(networks, seed)
    
    results = get_data_for_seeded_networks(seeded_networks, f)
    
    return results
    

# TESTS


def print_results(got, target):
    if got != target:
        print("FAIL!\ngot: %s\ntarget: %s\n" % (got, target))
    else:
        print("pass")


def test_readfile_and_output():
    got = main(["1"], "test_readfile_and_output")
    target = [["1", "2", "3", "4", "5", "6", "7", "8\n"]]
    print_results(got, target)


def test_two_rows_one_with_seed():
    got = main(["1"], "test_two_rows_one_with_seed")
    target = [["1", "2", "1.0", "0", "0", "0", "0", "0\n"]]
    print_results(got, target)


def test_two_rows_one_with_nonzero_score():
    got = main(["1", "4"], "test_two_rows_one_with_nonzero_score")
    target = [["1", "2", "1.0", "0", "0", "0", "0", "0\n"]]
    print_results(got, target)


def test_network_genes_removed_from_seed():
    got = main(["1"], "test_network_genes_removed_from_seed")
    target = [["1", "2", "1.0", "0", "0", "0", "0", "0\n"],
              ["4", "5", "1.0", "0", "0", "0", "0", "0\n"],
              ["2", "4", "1.0", "0", "0", "0", "0", "0\n"]]
    print_results(got, target)


def test_union():
    got = main(["1"], "test_union")
    target = [["1", "2", "1.0", "0", "0", "0", "0", "0\n"],
              ["4", "5", "1.0", "0", "0", "0", "0", "0\n"],
              ["2", "4", "1.0", "0", "0", "0", "0", "0\n"],
              ["5", "6", "1.0", "0", "0", "0", "0", "0\n"]]
    print_results(got, target)


def test_ignore_unseeded():
    got = main(["1"], "test_ignore_unseeded")
    target = [["1", "2", "1.0", "0", "0", "0", "0", "0\n"]]
    print_results(got, target)


def test_ignore_zero_conns_to_seed():
    got = main(["vps8"], "test_ignore_zero_conns_to_seed")
    target = [['vps8', 'ecm15', '0.1157', '7.554e-04', '0.7640', '1.0230', '0.8973', '0.0269\n']]
    print_results(got, target)


def test_include_negative_conns():
    got = main(["1"], "test_include_negative_conns")
    target = [["1", "2", "-1.0", "0", "0", "0", "0", "0\n"]]
    print_results(got, target)


test_readfile_and_output()
test_two_rows_one_with_seed()
test_two_rows_one_with_nonzero_score()
test_network_genes_removed_from_seed()
test_union()
test_ignore_unseeded()
test_ignore_zero_conns_to_seed()
test_include_negative_conns()
