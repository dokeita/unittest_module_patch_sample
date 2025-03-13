import unittest
from unittest.mock import MagicMock, patch

# モジュールのトップレベルでパッチ適用（問題があるパターン）
patcher = patch.dict('sys.modules', {'fake_module': MagicMock()})
patcher.start()

# `fake_module` をインポート
import fake_module


def tearDownModule():
    """モジュールレベルのクリーンアップ"""
    global patcher
    patcher.stop()


class TestFakeModule(unittest.TestCase):
    """fake_module のモックをテストする"""

    def test_fake_module_mocked(self):
        """fake_module がパッチされていることを確認"""
        self.assertIsInstance(fake_module, MagicMock)
