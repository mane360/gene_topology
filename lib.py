INDEX_G1 = 1
INDEX_G2 = 3
INDEX_SCORE = 5
INDEX_EXTRA_DATA = 6


def read(filename, skip_header=True):
    f = open(filename)

    if skip_header:
        f.readline()

    return f


def get_seed_list(seed_file):
    seed = []

    for line in seed_file:
        seed.append(line.strip())

    return seed


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

                if g1_index != -1 and g2_index != -1:
                    break

            # if new network
            if g1_index == -1 and g2_index == -1:
                networks.append({g1, g2})

            elif g1_index != -1 and g2_index != -1:
                # if 2 different current networks, union those networks
                if g1_index != g2_index:
                    networks[g1_index].update(networks[g2_index])
                    del networks[g2_index]
                # otherwise ignore - they are already recorded

            # if 1 current network
            elif g1_index != -1:
                g1_network.add(g2)
            elif g2_index != -1:
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


def get_data_for_seeded_networks(seeded_networks, f, test):
    f.seek(0)
    f.readline()  # skip header
    results = []

    # open the output files for writing
    out_files = [open("output/gene_topology_output_network_" + str(index), "w")
                 for index in range(len(seeded_networks))]

    for line in f:
        list_line = line.split("\t")
        g1 = list_line[INDEX_G1]
        g2 = list_line[INDEX_G2]
        score = list_line[INDEX_SCORE]
        extra = list_line[INDEX_EXTRA_DATA:]

        if relevant_score(score):
            for index, seeded_network in enumerate(seeded_networks):
                if g1 in seeded_network:  # g2 must also be in the network
                    row = [g1, g2, score]
                    row.extend(extra)
                    results.append(row)

                    if not test:
                        out_files[index].write("\t".join(row) + "\n")

                    break

    for out_file in out_files:
        out_file.close()

    return results
