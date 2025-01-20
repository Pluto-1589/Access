from unittest import TestCase
import task_6

# You'll probably want to write at least two tests for each of the functions,
# one passing a valid and one passing an invalid value to confirm that each
# individual function works on its own.

# Here' we've already provided a few examples. You should be able to fill
# in the empty strings by yourself by studying the task description:

IPv4_OCTET = "255"
IPv4_OCTET_INVALID = "256"

IPv4 = "127.0.0.1"                 # fill this in yourself
IPv4_INVALID = "300.0.0.1"         # fill this in yourself

IPv6_HEXTET = "fff"
IPv6_HEXTET_INVALID = "hello!!!"  # fill this in yourself

IPv6 = "2001:0db8:85a3:0000:0000:8a2e:0370:7334"
# fill this in yourself
IPv6_INVALID = "2001:0db8:85a3:0:0000:8a2e:0370:7334:1234"

IP = "192.168.1.1"
IP_INVALID = "A string that is not a valid IP"


class TasksTestSuite(TestCase):

    # we already provide 2 tests for the first two examples (valid/invalid octet)
    def test_ipv4_octet_valid(self):
        actual = task_6.is_valid_IPv4_octet(IPv4_OCTET)
        self.assertEqual(actual, True)

    def test_ipv4_octet_invalid(self):
        actual = task_6.is_valid_IPv4_octet(IPv4_OCTET_INVALID)
        self.assertEqual(actual, False)

    # write more test cases, one for each of the examples above!
    def test_ipv4_invalid(self):
        actual = task_6.is_valid_IPv4(IPv4_INVALID)
        self.assertEqual(actual, False)

    def test_ipv4_invalid(self):
        actual = task_6.is_valid_IPv4(IPv4_INVALID)
        self.assertEqual(actual, False)

    def test_ipv6_hextet_valid(self):
        actual = task_6.is_valid_IPv6_hextet(IPv6_HEXTET)
        self.assertEqual(actual, True)

    def test_ipv6_hextet_invalid(self):
        actual = task_6.is_valid_IPv6_hextet(IPv6_HEXTET_INVALID)
        self.assertEqual(actual, False)

    def test_ipv4_invalid(self):
        actual = task_6.is_valid_IPv6(IPv6_HEXTET_INVALID)
        self.assertEqual(actual, False)

    def test_ipv6_invalid(self):
        actual = task_6.is_valid_IPv6(IPv6_HEXTET_INVALID)
        self.assertEqual(actual, False)
