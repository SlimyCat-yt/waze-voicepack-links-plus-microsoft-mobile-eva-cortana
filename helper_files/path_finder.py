"""Compatibility wrapper: load the filename => waze path mapping from JSON.

The canonical data is stored in `helper_files/waze_filename_paths.json` so other tools
or non-Python environments can consume it easily. This module keeps the same
`filenames_and_paths` variable for backwards compatibility with existing imports.
"""

import json
import os

_here = os.path.dirname(__file__)
_json_path = os.path.join(_here, "waze_filename_paths.json")

try:
    with open(_json_path, "r", encoding="utf-8") as _f:
        filenames_and_paths = json.load(_f)
except Exception:
    # fall back to an empty dict so imports don't break
    filenames_and_paths = {}
