try:
	from run import app
	import unittest
except Exception as e:
	print('missing modules {}'.format(e))


class ApiTest(unittest.TestCase):

	# check for response 200
	def test_index(self):
		tester = app_client(self)
		response = tester.get('/foo')

		statuscode = response.status_code
		self.assertEqual(statuscode, 200)

if __name__ == '__main__':
	unittest.main()