# Changelist Data
Data Management for Changelists CLI Tools.

## Usage Scenarios
This package is designed for the purpose of serving other changelist packages, and reducing code duplication.

### Storage Scenarios
There are two storage options for Changelists.
- The first is the `.idea/workspace.xml` file associated with popular IDEs.
- The second is a dedicated `.changelists/data.xml` file managed by changelist-data on behalf of other changelist tools.

Each changelist tool must be compatible with both storage options. The goal of this package is to provide access to both storage options, and support the file reading and writing needs of all changelist tools.

#### Changelist Tools
The Data Storage needs of the Changelist Tools:
- Changelist Init
    - Create New Changelists File
    - Find Existing Storage File
    - Update Existing Storage File (with git status info)
- ChangeList Sort
    - Find Existing Storage File
    - Load Existing Storage File
    - Update Existing Storage File
- ChangeList FOCI
    - Find Existing Storage File
    - Read Existing Storage File

### Data Structures
`class FileChange` : Individual Files
- before_path: str | None = None
- before_dir: bool | None = None
- after_path: str | None = None
- after_dir: bool | None = None

`class Changelist` : Lists of Files
- id: str
- name: str
- changes: list[FileChange] = field(default_factory=lambda: [])
- comment: str = ""
- is_default: bool = False

## Package Structure
Call the public methods of the appropriate package for the level of detail required.
- `changelist_data/` contains high level methods with default options for accessing storage files
- `changelist_data/storage/` contains storage option specific methods for read-only and writable access.
- `changelist_data/xml/` contains some simple xml modules, and two subpackages.
- `changelist_data/xml/changelists/` changelists data xml management.
- `changelist_data/xml/workspace/` workspace xml management.

### Changelist Data Storage Access Methods
The highest level package should contain the highest level methods and modules.

#### High Level Default Methods
- `read_default() -> list[Changelist]`
- `load_default() -> ChangelistDataStorage`
- `write_tree(ChangelistDataStorage, Path) -> bool`

**Storage File Management**:
- Find Existing Storage File and Read or Load it (Default is Changelists data xml)
- Search for Storage File via Argument (workspace file argument backwards compatibility)
- Create Changelists Data File if not exists

**Read-Only Changelist Requirements**:
- Find and Read the Workspace File into a List of Changelist data objects
- Find and Read the Changelists Data File into a List of Changelist data objects

**Loading Changelist Data Tree Structures**: 
- Existing File is Loaded into one of the two Tree classes
- Tree classes handle updates to the storage data file

### Storage Package
This package contains modules for both workspace and changelist storage options.
Each option provides a reader and a tree loader.

- `read_changelists_storage(Path) -> list[Changelist]`
- `read_workspace_storage(Path) -> list[Changelist]`
- `load_changelists_tree(Path) -> ChangelistsTree`
- `load_workspace_tree(Path) -> WorkspaceTree`

#### File Validation Module
This module determines if a storage option is already in use (one of those files exists).
- Check if `.idea/workspace.xml` exists
- Check if `.changelists/data.xml` exists
- Check given workspace_xml or data_xml file argument exists
- Validate the Input File, prevent loading any file over 32MB

#### XML Changelists Package
This package provides all the methods one may need for processing Changelists XML.
- `read_xml(changelists_xml: str) -> list[Changelist]`
- `load_tree(changelists_xml: str) -> ChangelistsTree`
- `new_tree() -> ChangelistsTree`

The `new_tree` method is a shortcut for creating a Changelists XML Tree.
This is to be used when initializing changelist workflows for the first time in a project.

#### XML Workspace Reader
This package provides methods for processing Workspace XML.
- `read_xml(workspace_xml: str) -> list[Changelist]`
- `load_tree(workspace_xml: str) -> WorkspaceTree`
