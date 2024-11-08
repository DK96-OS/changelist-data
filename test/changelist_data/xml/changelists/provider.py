""" Test Data Provider for Changelists XML Inputs.
"""


def get_no_changelist_xml() -> str:
    return """<?xml version="1.0" encoding="UTF-8"?>
<changelists></changelists>"""


def get_simple_changelist_xml() -> str:
    return """<?xml version="1.0" encoding="UTF-8"?>
<changelists>
<list id="9f60fda2f83a47c88" name="Simple" comment="Main Program Files">
  <change beforePath="/main.py" beforeDir="false"  afterPath="/main.py" afterDir="false" />
</list>
</changelists>"""


def get_multi_changelist_xml() -> str:
    return """<?xml version="1.0" encoding="UTF-8"?>
<changelists>
<list default="true" id="af84ea1b9f3a2835e933" name="Main" comment="Main Program Files">
  <change beforePath="/history.py" beforeDir="false" />
  <change beforePath="/main.py" beforeDir="false" />
</list>
<list id="9f60fda24c8f83a47c88" name="Test" comment="Test Files">
  <change afterPath="/test/test_file.py" afterDir="false" />
</list>
</changelists>"""


def get_invalid_component_xml() -> str:
    return """<?xml version="1.0" encoding="UTF-8"?>
<changelists>
<lisat id="af84ea1b9f3a2835e933" name="Main" comment="Main Files">
  <change beforePath="/main.py" beforeDir="false" />
</lisat>
</changelists>"""
