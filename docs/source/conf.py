# pylint: disable=invalid-name, redefined-builtin, wrong-import-position
import sys
from pathlib import Path
repo_relative_path = Path('../..')
repo_abs_path = repo_relative_path.resolve()
sys.path.insert(0, f'{repo_abs_path}')
from ifrs16 import __version__  # noqa


project = 'ifrs16'
copyright = '2023, Bradley Smith'
author = 'Bradley Smith'
version = __version__

extensions = [
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.extlinks',
    'sphinx.ext.autosectionlabel',
    'sphinx_copybutton',
]

templates_path = ['_templates']

exclude_patterns = []


html_theme = 'press'

html_static_path = ['_static']

copybutton_selector = 'div.highlight pre, pre.literal-block'

wheel_url = (
    'https://github.com/bradley-smith-gpa/ifrs16/releases/latest/'
    f'download/ifrs16-{version}-py3-none-any.whl'
)

rst_epilog = f"""
.. |wheel_url| replace:: {wheel_url}
"""

autosectionlabel_prefix_document = True
