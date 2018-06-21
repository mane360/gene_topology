def fill_networks(seed, filename):
    f = open(filename)
    for line in f:
        list_line = line.split("\t")
        print(list_line)
        break
    f.close()

fill_networks(1, "test_data")