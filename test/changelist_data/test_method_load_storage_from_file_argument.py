""" Testing Main Package Method
"""
from changelist_data import load_storage_from_file_arguments


def test_load_storage_from_file_arguments_default_arguments_any_environment():
    load_storage_from_file_arguments()
