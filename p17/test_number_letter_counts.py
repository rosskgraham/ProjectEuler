from p17.main import number_letter_counts

def test_number_letter_counts():
    assert number_letter_counts(1) == 3
    assert number_letter_counts(2) == 3
    assert number_letter_counts(3) == 5
    assert number_letter_counts(4) == 4
    assert number_letter_counts(5) == 4
    assert sum([number_letter_counts(num) for num in range(1,6)]) == 19
    assert number_letter_counts(342) == 23
    assert number_letter_counts(115) == 20