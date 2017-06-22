


class Dict(dict):

	def __init__(self, **kw):
		super().__init__(**kw)

	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError :
			raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

	def __setattr__(self, key, value):
		self[key] = value

import unittest

class TestDict(unittest.TestCase):

	def setUp(self): #setUp 和 tearDown 方法分别会在每个测试方法前后执行一次
		print("setUp")

	def tearDown(self):
		print("tearDown")

	def test_init(self):
		d = Dict(a=1, b = 'test')
		self.assertEqual(d.a, 1)
		self.assertEqual(d.b, 'test')
		self.assertTrue(isinstance(d, dict))

	def test_key(self):
		d = Dict()
		d["key"] = 'value'
		self.assertEqual(d.key, 'value')

	def test_attr(self):
		d = Dict()
		d.key = 'value'
		self.assertTrue('key' in d)
		self.assertEqual(d['key'], 'value')

if __name__ == '__main__':
	unittest.main()



