""" Testing Main Package Method
"""
from changelist_data import generate_changelists_from_storage_file_arguments


def test_generate_changelists_from_storage_file_arguments_default_arguments_any_environment():
    generate_changelists_from_storage_file_arguments()