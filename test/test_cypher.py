import assert_functions as test
import sub_cypher as cy


def test_all_pairs():
    test.print_bar()
    test.print_info("BEGIN all_pairs")
    test.assert_equals_bool("all_pairs1", False, cy.all_pairs(None))
    test.assert_equals_bool("all_pairs2", False, cy.all_pairs([['a', 'b'], None, ['c', 'd']]))
    test.assert_equals_bool("all_pairs3", True, cy.all_pairs([[]]))
    test.assert_equals_bool("all_pairs4", True, cy.all_pairs([['a', 'b']]))
    test.assert_equals_bool("all_pairs5", False, cy.all_pairs([['a', 'b'], ['a']]))
    test.print_info("END all_pairs")
    test.print_bar()


test_all_pairs()


def test_get_column():
    test.print_bar()
    test.print_info("BEGIN get_column")
    test.assert_equals_arr("get_columns1", [], cy.get_column([[]], 0))
    test.assert_equals_arr("get_columns2", [], cy.get_column([[]], 1))
    test.assert_equals_arr("get_columns3", ['a'], cy.get_column([['a', 'b']], 0))
    test.assert_equals_arr("get_columns4", ['b'], cy.get_column([['a', 'b']], 1))
    test.assert_equals_arr("get_columns5", ['a', 'c'], cy.get_column([['a', 'b'], ['c', 'd']], 0))
    test.assert_equals_arr("get_columns6", ['b', 'd'], cy.get_column([['a', 'b'], ['c', 'd']], 1))
    test.print_info("END get_columns")
    test.print_bar()


test_get_column()


def test_contains_in_suffix():
    test.print_bar()
    test.print_info("BEGIN contains_in_suffix")
    test.assert_equals_arr("contains_in_suffix1", False, cy.contains_in_suffix([], 12, 'a'))
    test.assert_equals_arr("contains_in_suffix2", False, cy.contains_in_suffix(['a'], 2, 'a'))
    test.assert_equals_arr("contains_in_suffix3", False, cy.contains_in_suffix(['a', 'b'], 1, 'a'))
    test.assert_equals_arr("contains_in_suffix4", True, cy.contains_in_suffix(['a', 'b'], 1, 'b'))
    test.print_info("END contains_in_suffix")
    test.print_bar()


test_contains_in_suffix()


def test_unique():
    test.print_bar()
    test.print_info("BEGIN unique")
    test.assert_equals_arr("unique1", True, cy.unique(['']))
    test.assert_equals_arr("unique2", True, cy.unique(['a']))
    test.assert_equals_arr("unique3", False, cy.unique(['a', 'a']))
    test.assert_equals_arr("unique4", True, cy.unique(['a', 'b', 'c', 'd', 'e', 'f']))
    test.assert_equals_arr("unique5", False, cy.unique(list("abcad")))
    test.print_info("END unique")
    test.print_bar()


test_unique()


def test_is_valid():
    test.print_bar()
    test.print_info("BEGIN is_valid")
    test.assert_equals_bool("is_valid1", False, cy.is_valid(None))
    test.assert_equals_bool("is_valid2", True, cy.is_valid([[]]))
    test.assert_equals_bool("is_valid3", False, cy.is_valid([[None]]))
    test.assert_equals_bool("is_valid4", True, cy.is_valid([['a', 'b']]))
    test.assert_equals_bool("is_valid5", False, cy.is_valid([['a']]))
    test.assert_equals_bool("is_valid6", False, cy.is_valid([['a', 'b'], ['a', 'c']]))
    test.assert_equals_bool("is_valid7", False, cy.is_valid([['a', 'b'], ['c', 'b']]))
    test.assert_equals_bool("is_valid8", True, cy.is_valid([['a', 'b'], ['c', 'd']]))
    test.print_info("END unique")
    test.print_bar()


test_is_valid()


def test_invert():
    test.print_bar()
    test.print_info("BEGIN invert")
    test.assert_equals_arr_twod("invert1", [[]], cy.invert([[]]))
    test.assert_equals_arr_twod("invert2", [['b', 'a']], cy.invert([['a', 'b']]))
    test.assert_equals_arr_twod("invert3", [['b', 'a'], ['d', 'c']], cy.invert([['a', 'b'], ['c', 'd']]))
    test.print_info("END invert")
    test.print_bar()


test_invert()


def test_create_key():
    test.print_bar()
    test.print_info("BEGIN create_key")
    test.assert_equals_arr_twod("create_key1", [[]], cy.create_key("", "anything"))
    test.assert_equals_arr_twod("create_key2", [[]], cy.create_key("anything", ""))
    test.assert_equals_arr_twod("create_key3", [['a', 'b']], cy.create_key("a", "bc"))
    test.assert_equals_arr_twod("create_key4", [['a', 'c']], cy.create_key("ab", "c"))
    test.assert_equals_arr_twod("create_key5", [['a', 'c'], ['b', 'd']], cy.create_key("ab", "cd"))
    test.print_info("END create_key")
    test.print_bar()


test_create_key()


def test_encode_char():
    test.print_bar()
    test.print_info("BEGIN test_encode_char")
    test.assert_equals_int("encode_char1", -1, cy.encode_char([[]], 'a'))
    test.assert_equals_int("encode_char2", 'b', cy.encode_char([['a', 'b']], 'a'))
    test.assert_equals_int("encode_char3", 'd', cy.encode_char([['a', 'b'], ['c', 'd']], 'c'))
    test.assert_equals_int("encode_char4", -1, cy.encode_char([['a', 'b'], ['c', 'd']], 'x'))
    test.print_info("END test_encode_char")
    test.print_bar()


test_encode_char()


def test_encode_text():
    test.print_bar()
    test.print_info("BEGIN encode_text")
    test.assert_equals_str("encode_text1", "", cy.encode_text([[]], ""))
    test.assert_equals_str("encode_text2", None, cy.encode_text([['a', 'b']], "aca"))
    test.assert_equals_str("encode_text3", "bddb", cy.encode_text([['a', 'b'], ['c', 'd']], "acca"))
    test.print_info("END encode_text")
    test.print_bar()


test_encode_text()


def test_decode_text():
    test.print_bar()
    test.print_info("BEGIN decode_text")
    test.assert_equals_str("decode_text1", "", cy.decode_text([[]], ""))
    test.assert_equals_str("decode_text2", "acca", cy.decode_text([['a', 'b'], ['c', 'd']], "bddb"))
    test.print_info("END decode_text")
    test.print_bar()


test_decode_text()
