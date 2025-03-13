# patch_setupmodule.py
import unittest
from unittest.mock import MagicMock, patch


def setUpModule():
    """モジュールレベルのセットアップ"""
    global patcher
    patcher = patch.dict('sys.modules', {'fake_module': MagicMock()})
    patcher.start()

    # `setUpModule()` 内で `fake_module` をインポート
    global fake_module
    import fake_module


def tearDownModule():
    """モジュールレベルのクリーンアップ"""
    global patcher
    patcher.stop()


class TestFakeModule(unittest.TestCase):
    """fake_module のモックをテストする"""

    def test_fake_module_mocked(self):
        """fake_module がパッチされていることを確認"""
        global fake_module
        self.assertIsInstance(fake_module, MagicMock)
