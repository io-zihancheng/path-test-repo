import unittest

from opc_delivery_probe_20261017_smoke import delivery_probe


class DeliveryProbeTest(unittest.TestCase):
    def test_returns_exact_value(self):
        self.assertEqual(delivery_probe(), "opc-delivery-check-20261017-smoke")

    def test_repeated_calls_are_consistent(self):
        self.assertEqual(delivery_probe(), delivery_probe())


if __name__ == "__main__":
    unittest.main()
