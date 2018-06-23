from main import main


def print_results(got, target):
    if got != target:
        print("FAIL!\ngot: %s\ntarget: %s\n" % (got, target))
    else:
        print("pass")


def run_test(filename, test=True):
    return main("tests/" + filename + "_SEED",
                "tests/" + filename, test)


def test_readfile_and_output():
    got = run_test("test_readfile_and_output")
    target = [["1", "2", "3", "4", "5", "6", "7", "8\n"]]
    print_results(got, target)


def test_two_rows_one_with_seed():
    got = run_test("test_two_rows_one_with_seed")
    target = [["1", "2", "1.0", "0", "0", "0", "0", "0\n"]]
    print_results(got, target)


def test_two_rows_one_with_nonzero_score():
    got = run_test("test_two_rows_one_with_nonzero_score")
    target = [["1", "2", "1.0", "0", "0", "0", "0", "0\n"]]
    print_results(got, target)


def test_network_genes_removed_from_seed():
    got = run_test("test_network_genes_removed_from_seed")
    target = [["1", "2", "1.0", "0", "0", "0", "0", "0\n"],
              ["4", "5", "1.0", "0", "0", "0", "0", "0\n"],
              ["2", "4", "1.0", "0", "0", "0", "0", "0\n"]]
    print_results(got, target)


def test_union():
    got = run_test("test_union")
    target = [["1", "2", "1.0", "0", "0", "0", "0", "0\n"],
              ["4", "5", "1.0", "0", "0", "0", "0", "0\n"],
              ["2", "4", "1.0", "0", "0", "0", "0", "0\n"],
              ["5", "6", "1.0", "0", "0", "0", "0", "0\n"]]
    print_results(got, target)


def test_ignore_unseeded():
    got = run_test("test_ignore_unseeded")
    target = [["1", "2", "1.0", "0", "0", "0", "0", "0\n"]]
    print_results(got, target)


def test_ignore_zero_conns_to_seed():
    got = run_test("test_ignore_zero_conns_to_seed")
    target = [['vps8', 'ecm15', '0.1157', '7.554e-04', '0.7640', '1.0230', '0.8973', '0.0269\n']]
    print_results(got, target)


def test_include_negative_conns():
    got = run_test("test_include_negative_conns")
    target = [["1", "2", "-1.0", "0", "0", "0", "0", "0\n"]]
    print_results(got, target)


def test_big():
    got = run_test("test_big")
    target = [['vps8', 'ecm15', '0.1157', '7.554e-04', '0.7640', '1.0230', '0.8973', '0.0269\n'],
              ['vps8', 'hta2', '0.0290', '2.500e-01', '0.7640', '1.0115', '0.8018', '0.0333\n'],
              ['vps8', 'pdr3', '-0.0278', '2.418e-01', '0.7640', '1.0365', '0.7641', '0.0307\n'],
              ['vps8', 'sla1', '-0.0554', '1.649e-01', '0.7640', '0.8322', '0.5804', '0.0564\n'],
              ['vps8', 'hir1', '0.0638', '4.134e-03', '0.7640', '0.9477', '0.7879', '0.0163\n'],
              ['fun14', 'nvj2', '-0.0236', '6.063e-02', '1.0445', '1.0205', '1.0423', '0.0104\n'],
              ['fun14', 'ypr092w', '-0.0123', '3.807e-01', '1.0445', '1.0010', '1.0332', '0.0300\n'],
              ['fun14', 'asr1', '0.0187', '3.651e-01', '1.0445', '1.0040', '1.0673', '0.0405\n'],
              ['fun14', 'syt1', '0.0082', '2.925e-01', '1.0445', '1.0150', '1.0684', '0.0096\n'],
              ['fun14', 'ypr096c', '-0.0215', '3.322e-01', '1.0445', '0.9720', '0.9938', '0.0420\n'],
              ['fun14', 'ypr097w', '0.0051', '3.658e-01', '1.0445', '1.0110', '1.0611', '0.0090\n'],
              ['fun14', 'ypr098c', '-0.0019', '4.572e-01', '1.0445', '1.0182', '1.0616', '0.0109\n'],
              ['fun14', 'vps8', '-0.0364', '5.572e-02', '1.0445', '1.0182', '1.0271', '0.0164\n'],
              ['fun14', 'ypr114w', '-0.0031', '4.758e-01', '1.0445', '1.0167', '1.0589', '0.0450\n'],
              ['ccr5', 'fun14', '0.0106', '3.469e-01', '0.4460', '0.9920', '0.4531', '0.0227']]
    print_results(got, target)


def test_new_conn_in_existing_network():
    got = run_test("test_new_conn_in_existing_network")
    target = [["1", "2", "1.0", "0", "0", "0", "0", "0\n"],
              ["2", "3", "1.0", "0", "0", "0", "0", "0\n"],
              ["1", "3", "1.0", "0", "0", "0", "0", "0\n"]]
    print_results(got, target)


def test_full():
    run_test("test_data", False)


test_readfile_and_output()
test_two_rows_one_with_seed()
test_two_rows_one_with_nonzero_score()
test_network_genes_removed_from_seed()
test_union()
test_ignore_unseeded()
test_ignore_zero_conns_to_seed()
test_include_negative_conns()
test_big()
test_new_conn_in_existing_network()
# test_full()
