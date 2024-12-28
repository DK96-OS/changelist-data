""" Testing Arguments Module Methods in the Validation Package.
"""
import pytest

from changelist_data.validation.arguments import has_illegal_filesystem_chars, validate_string_argument


_PARAMS_CONTAINS_ILLEGAL_CHARS = [
    "example*file.txt",
    "example<file.txt",
    "example>file.txt",
    "example?file.txt",
    "example|file.txt",
    "example&file.txt",
    ";examplefile.txt",
    "\0examplefile.txt",
    "example\nfile.txt",
    "example\rfile.txt",
    "*a" * 10**2 + "*",
]

_PARAMS_ONLY_VALID_CHARS = [
    "examplefile.txt",
    "safefilename.txt",
    "/safefilename.txt",
    "asdf/safefilename.txt",
    "asdf/safefilenam",
]

_PARAMS_BLANK_SPACE_INPUTS = [
    "",
    " ",
    "  ",
    "\t",
    "    ",
]


@pytest.mark.parametrize("input_string", _PARAMS_CONTAINS_ILLEGAL_CHARS)
def test_has_illegal_filesystem_chars_contains_illegal_chars_returns_true(input_string):
    assert has_illegal_filesystem_chars(input_string)


@pytest.mark.parametrize("input_string", _PARAMS_ONLY_VALID_CHARS)
def test_has_illegal_filesystem_chars_only_valid_chars_returns_false(input_string):
    assert not has_illegal_filesystem_chars(input_string)


@pytest.mark.parametrize("input_string", _PARAMS_BLANK_SPACE_INPUTS)
def test_has_illegal_filesystem_chars_blank_space_combinations_returns_false(input_string):
    assert not has_illegal_filesystem_chars(input_string)


@pytest.mark.parametrize("input_string", _PARAMS_CONTAINS_ILLEGAL_CHARS)
def test_validate_string_argument_contains_illegal_chars_returns_false(input_string):
    assert not validate_string_argument(input_string)


@pytest.mark.parametrize("input_string", _PARAMS_CONTAINS_ILLEGAL_CHARS)
def test_validate_string_argument_contains_illegal_chars_do_not_filter_illegal_chars_returns_true(input_string):
    assert validate_string_argument(input_string, False)


@pytest.mark.parametrize("input_string", _PARAMS_ONLY_VALID_CHARS)
def test_validate_string_argument_only_valid_chars_returns_true(input_string):
    assert validate_string_argument(input_string)


@pytest.mark.parametrize("input_string", _PARAMS_ONLY_VALID_CHARS)
def test_validate_string_argument_only_valid_chars_do_not_filter_illegal_chars_returns_true(input_string):
    assert validate_string_argument(input_string, False)


@pytest.mark.parametrize("input_string", _PARAMS_BLANK_SPACE_INPUTS)
def test_validate_string_argument_blank_space_combinations_returns_false(input_string):
    assert not validate_string_argument(input_string)


@pytest.mark.parametrize("input_string", _PARAMS_BLANK_SPACE_INPUTS)
def test_validate_string_argument_blank_space_combinations_do_not_filter_illegal_chars_returns_false(input_string):
    assert not validate_string_argument(input_string, False)
