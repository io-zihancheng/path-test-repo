import unittest

from opc_github_probe_20261011 import probe_label


class ProbeLabelTest(unittest.TestCase):
    def test_returns_exact_value(self):
        self.assertEqual(probe_label(), "opc-v062-github-download-ticker-20261011")

    def test_is_repeatable(self):
        self.assertEqual(probe_label(), probe_label())


if __name__ == "__main__":
    unittest.main()
