""" Test Data Provider for Workspace XML Inputs.
"""


def get_no_changelist_xml() -> str:
    return """<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="AutoImportSettings">
    <option name="autoReloadType" value="NONE" />
  </component>
</project>"""


def get_empty_changelist_xml() -> str:
    return """<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="AutoImportSettings">
    <option name="autoReloadType" value="NONE" />
  </component>
  <component name="ChangeListManager">
  </component>
</project>"""


def get_simple_changelist_xml() -> str:
    return """<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component name="AutoImportSettings">
    <option name="autoReloadType" value="NONE" />
  </component>
  <component name="ChangeListManager">
    <list id="9f60fda2-421e-4a4b-bd0f-4c8f83a47c88" name="Simple" comment="Main Program Files">
      <change beforePath="$PROJECT_DIR$/main.py" beforeDir="false"  afterPath="$PROJECT_DIR$/main.py" afterDir="false" />
    </list>
  </component>
</project>"""


def get_multi_changelist_xml() -> str:
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


def get_invalid_component_xml() -> str:
    return """<?xml version="1.0" encoding="UTF-8"?>
<project version="4">
  <component>
  </component>
  <component name="ChangeListManager">
    <list default="true" id="af84ea1b-1b24-407d-970f-9f3a2835e933" name="Main" comment="Main Files">
      <change beforePath="$PROJECT_DIR$/main.py" beforeDir="false" />
    </list>
  </component>
</project>"""
