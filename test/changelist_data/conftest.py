"""
"""
import pytest

from changelist_data.changelist import Changelist
from changelist_data.file_change import FileChange


MODULE_SRC_PATH = '/module/src/main/java/module/Main.java'


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


@pytest.fixture()
def simple_cl():
    return Changelist(
        id="9f60fda2-421e-4a4b-bd0f-4c8f83a47c88",
        name="Simple",
        changes=[
            FileChange(before_path='/main.py',
                       before_dir=False,
                       after_path='/main.py',
                       after_dir=False)
        ],
        comment="Main Program Files",
    )


@pytest.fixture()
def simple_cl_list(simple_cl):
    return [simple_cl]


@pytest.fixture()
def multi_cl_list():
    return [
        Changelist(
            id="af84ea1b-1b24-407d-970f-9f3a2835e933",
            name="Main",
            changes=[
                FileChange(before_path='/history.py',
                           before_dir=False,
                           after_path=None,
                           after_dir=None),
                FileChange(before_path='/main.py',
                           before_dir=False,
                           after_path=None,
                           after_dir=None)
            ],
            comment="Main Program Files",
            is_default=True,
        ),
        Changelist(
            id="9f60fda2-421e-4a4b-bd0f-4c8f83a47c88",
            name="Test",
            changes=[
                FileChange(before_path=None,
                           before_dir=None,
                           after_path='/test/test_file.py',
                           after_dir=False)
            ],
            comment="Test Files",
        ),
    ]


@pytest.fixture()
def no_clm_workspace_xml() -> str:
    """Workspace XML with no ChangeListManager component.
    """
    return """<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="AutoImportSettings">
    <option name="autoReloadType" value="NONE" />
  </component>
</project>"""


@pytest.fixture()
def empty_workspace_xml() -> str:
    """Workspace XML with empty ChangeListManager component.
    """
    return """<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="AutoImportSettings">
    <option name="autoReloadType" value="NONE" />
  </component>
  <component name="ChangeListManager">
  </component>
</project>"""


@pytest.fixture()
def simple_workspace_xml() -> str:
    """Workspace XML with a Simple Changelist.
    """
    return """<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="AutoImportSettings">
    <option name="autoReloadType" value="NONE" />
  </component>
  <component name="ChangeListManager">
    <list id="9f60fda2-421e-4a4b-bd0f-4c8f83a47c88" name="Simple" comment="Main Program Files">
      <change beforePath="$PROJECT_DIR$/main.py" beforeDir="false" afterPath="$PROJECT_DIR$/main.py" afterDir="false" />
    </list>
  </component>
</project>"""


@pytest.fixture()
def multi_workspace_xml():
    """Workspace XML with Multiple Changelists.
    """
    return """<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="AutoImportSettings">
    <option name="autoReloadType" value="NONE" />
  </component>
  <component name="ChangeListManager">
    <list default="true" id="af84ea1b-1b24-407d-970f-9f3a2835e933" name="Main" comment="Main Program Files">
      <change beforePath="$PROJECT_DIR$/history.py" beforeDir="false" />
      <change beforePath="$PROJECT_DIR$/main.py" beforeDir="false" />
    </list>
    <list id="9f60fda2-421e-4a4b-bd0f-4c8f83a47c88" name="Test" comment="Test Files">
      <change afterPath="$PROJECT_DIR$/test/test_file.py" afterDir="false" />
    </list>
  </component>
</project>"""


@pytest.fixture()
def empty_changelists_xml() -> str:
    return """<?xml version="1.0" encoding="UTF-8"?>
<changelists></changelists>"""


@pytest.fixture()
def simple_changelists_xml() -> str:
    return """<?xml version="1.0" encoding="UTF-8"?>
<changelists>
<list id="9f60fda2-421e-4a4b-bd0f-4c8f83a47c88" name="Simple" comment="Main Program Files">
  <change beforePath="/main.py" beforeDir="false"  afterPath="/main.py" afterDir="false" />
</list>
</changelists>"""


@pytest.fixture()
def multi_changelists_xml() -> str:
    return """<?xml version="1.0" encoding="UTF-8"?>
<changelists>
<list default="true" id="af84ea1b-1b24-407d-970f-9f3a2835e933" name="Main" comment="Main Program Files">
  <change beforePath="/history.py" beforeDir="false" />
  <change beforePath="/main.py" beforeDir="false" />
</list>
<list id="9f60fda2-421e-4a4b-bd0f-4c8f83a47c88" name="Test" comment="Test Files">
  <change afterPath="/test/test_file.py" afterDir="false" />
</list>
</changelists>"""


@pytest.fixture()
def invalid_changelists_xml() -> str:
    return """<?xml version="1.0" encoding="UTF-8"?>
<changelists>
<lisat id="9f60fda2-421e-4a4b-bd0f-4c8f83a47c88" name="Main" comment="Main Files">
  <change beforePath="/main.py" beforeDir="false" />
</lisat>
</changelists>"""
