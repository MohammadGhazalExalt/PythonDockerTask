import unittest

from api import Disk_stats, Mem_stats, Cpu_stats

class ActivityTests(unittest.TestCase):
	def test_cpu_to_json(self):
		tmp = Cpu_stats(10.23, "2020-11-23 03:00:01")
		self.assertEqual(
				tmp.to_json(), "{\"idle\": 10.23, \"timestamp\": \"2020-11-23 03:00:01\"}"
			)

	def test_disk_to_json(self):
		tmp = Disk_stats(123456, 654321, "2020-11-23 03:00:01")
		self.assertEqual(
				tmp.to_json(), "{\"used\": 123456, \"free\": 654321, \"timestamp\": \"2020-11-23 03:00:01\"}"
			)

	def test_mem_to_json(self):
		tmp = Mem_stats(123456, 654321, "2020-11-23 03:00:01")
		self.assertEqual(
				tmp.to_json(), "{\"used\": 123456, \"free\": 654321, \"timestamp\": \"2020-11-23 03:00:01\"}"
			)
if __name__ == "__main__":
	unittest.main()