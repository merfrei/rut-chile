import pytest
from rut_chile import rut_chile


class TestIsValidRutTests:

    @pytest.mark.parametrize("test_input, expected", [
        (None, False),
        ("", False),
        (" ", False),
        ("k", False),
        ("1", False),
        ("*", False),
        ("1-", False),
        (".-", False),
        ("1.", False),
        ("1.11", False),
        ("1.111K", False),
        (".1", False),
        ("123.K", False),
        ("123.12-K", False)
    ])
    def test_invalid_argument(self, test_input, expected):
        with pytest.raises(ValueError) as error:   
            rut_chile.is_valid_rut(test_input)  
        assert type(error.value) is ValueError

    @pytest.mark.parametrize("test_input, expected", [
        ("9868503-1", False),
        ("21518268-2", False),
        ("17175325-3", False),
        ("20930576-4", False),
        ("13402128-5", False),
        ("20737522-6", False),
        ("6842256-7", False),
        ("14983005-8", False),
        ("20247667-9", False),
        ("17832479-k", False),
        ("12667869-0", False)
    ])
    def test_invalid_rut(self, test_input, expected):
        assert rut_chile.is_valid_rut(test_input) == expected

    @pytest.mark.parametrize("test_input, expected", [
        ("00", True),
        ("0-0", True),
        ("1-9", True),
        ("98685030", True),
        ("9868503-0", True),
        ("9.868.503-0", True),
        ("21518268-1", True),
        ("17175325-2", True),
        ("20930576-3", True),
        ("13402128-4", True),
        ("20737522-5", True),
        ("6842256-6", True),
        ("14983005-7", True),
        ("20247667-8", True),
        ("17832479-9", True),
        ("12667869-k", True),
        ("12667869-K", True),
        ("12.667.869-K", True),
        ("12.667.869-k", True)
    ])
    def test_valid_rut(self, test_input, expected):
        assert rut_chile.is_valid_rut(test_input) == expected


class TestGetVerificationDigit:
    @pytest.mark.parametrize("test_input", [
        (None),
        (""),
        (" "),
        ("k"),
        ("1k"),
        ("*"),
        ("1-"),
        (".-"),
        ("12312-K"),
        ("12.312-K"),
    ])
    def test_invalid_argument(self, test_input):
        with pytest.raises(ValueError) as error:   
            rut_chile.get_verification_digit(test_input)  
        assert type(error.value) is ValueError

    @pytest.mark.parametrize("test_input, upper, expected", [
        ("0", False, "0"),
        ("1", False, "9"),
        ("9868503", False, "0"),
        ("21518268", False, "1"),
        ("17175325", False, "2"),
        ("20930576", False, "3"),
        ("13402128", False, "4"),
        ("20737522", False, "5"),
        ("6842256", False, "6"),
        ("14983005", False, "7"),
        ("20247667", False, "8"),
        ("17832479", False, "9"),
        ("12667869", False, "k"),
        ("12667869", True, "K")
    ])
    def test_valid_rut(self, test_input, upper, expected):
        assert rut_chile.get_verification_digit(test_input, upper) == expected


class TestFormatRut:
    @pytest.mark.parametrize("test_input", [
        (None),
        (""),
        (" "),
        ("k"),
        ("ab"),
        ("*"),
        ("1-"),
        (".-"),
        ("1."),
        ("1.11")
    ])
    def test_invalid_argument(self, test_input):
        with pytest.raises(ValueError) as error:
            rut_chile.format_rut(test_input)
        assert type(error.value) is ValueError

    @pytest.mark.parametrize("test_input, with_dots, upper, expected", [
        ("12", False, False, "1-2"),
        ("123", False, False, "12-3"),
        ("1234", False, False, "123-4"),
        ("12345", False, False, "1234-5"),
        ("12345", True, False, "1.234-5"),
        ("123456", True, False, "12.345-6"),
        ("1234567", True, False, "123.456-7"),
        ("12345678", True, False, "1.234.567-8"),
        ("123456789", True, False, "12.345.678-9"),
        ("123456789k", True, False, "123.456.789-k"),
        ("123456789k", True, True, "123.456.789-K"),
    ])
    def test_valid_rut(self, test_input, with_dots, upper, expected):
        assert rut_chile.format_rut(test_input, with_dots, upper) == expected
