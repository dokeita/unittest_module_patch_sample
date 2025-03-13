# check_patch.py
import sys

import unittest
from unittest.mock import MagicMock

try:
    import fake_module  # `patcher.stop()` が機能していれば、ここで ImportError になるはず
    print("[ERROR] fake_module is still patched! patcher.stop() did not work.")
except ModuleNotFoundError:
    print(
        "[SUCCESS] fake_module is not available. patcher.stop() worked correctly."
    )


class TestFakeModule(unittest.TestCase):

    def test_fake_module_mocked(self):
        self.assertIsInstance(fake_module, MagicMock)

