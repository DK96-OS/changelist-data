""" Test Data Provider
"""
import pytest

from changelist_data.changelist import Changelist
from changelist_data.file_change import FileChange

MODULE_SRC_PATH = '/module/src/main/java/module/Main.java'
MODULE_TEST_PATH = '/module/src/test/java/module/MainTest.java'
MODULE_DEBUG_PATH = '/module/src/debug/java/module/MainDebug.java'
ROOT_GRADLE_PATH = '/build.gradle'
ROOT_README_PATH = '/README.md'
GRADLE_PROPERTIES_PATH = '/gradle/wrapper/gradle-wrapper.properties'
APP_GRADLE_PATH = '/app/build.gradle'
GITHUB_WORKFLOW_PATH = '/.github/workflows/build_and_test.yml'
GITHUB_DEPENDABOT_PATH = '/.github/dependabot.yml'


def get_change_data(after_path: str) -> FileChange:
    return FileChange(
        after_path=after_path,
        after_dir=False,
    )


def get_module_src_change_data() -> FileChange:
    return get_change_data(MODULE_SRC_PATH)


def get_module_test_change_data() -> FileChange:
    return get_change_data(MODULE_TEST_PATH)


def get_module_debug_change_data() -> FileChange:
    return get_change_data(MODULE_DEBUG_PATH)


def get_root_gradle_build_change_data() -> FileChange:
    return get_change_data(ROOT_GRADLE_PATH)


def get_root_readme_change_data() -> FileChange:
    return get_change_data(ROOT_README_PATH)


def get_gradle_properties_change_data() -> FileChange:
    return get_change_data(GRADLE_PROPERTIES_PATH)


def get_app_gradle_build_change_data() -> FileChange:
    return get_change_data(APP_GRADLE_PATH)


def get_github_workflows_change_data() -> FileChange:
    return get_change_data(GITHUB_WORKFLOW_PATH)


def get_github_dependabot_change_data() -> FileChange:
    return get_change_data(GITHUB_DEPENDABOT_PATH)


@pytest.fixture()
def fc_all():
    return FileChange(
        before_path=MODULE_SRC_PATH,
        after_path=MODULE_SRC_PATH,
        before_dir=False,
        after_dir=False
    )


@pytest.fixture()
def fc_before():
    return FileChange(
        before_path=MODULE_SRC_PATH,
        before_dir=False,
    )


@pytest.fixture()
def fc_after():
    return FileChange(
        after_path=MODULE_SRC_PATH,
        after_dir=False
    )


def get_cl0():
    return Changelist(
        id="0",
        name="",
        changes=list(),
    )


def get_cl1():
    return Changelist(
        id="1212434",
        name="ChangeList",
        changes=[
            FileChange(
                after_path="/module/file.txt",
                after_dir=False,
            )
        ],
    )
