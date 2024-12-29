""" Testing Main Package Method
"""
from changelist_data import read_storage_from_file_arguments


def test_read_storage_from_file_arguments_default_arguments_any_environment():
    read_storage_from_file_arguments()
