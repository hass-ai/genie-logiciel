import unittest
from robot import parse_robot_command


class RobotTest(unittest.TestCase):

    def test_avancer(self):
        res = parse_robot_command("0X123")
        self.assertEqual(res[0].code, "moveForward")

    def test_reculer(self):
        res = parse_robot_command("0X789")
        self.assertEqual(res[0].code, "moveBackward")

    def test_stop(self):
        res = parse_robot_command("0XABC")
        self.assertEqual(res[0].code, "stop")

    def test_plusieurs_commandes(self):
        res = parse_robot_command("0X123,0X789,0XABC")
        self.assertEqual(res[0].code, "moveForward")
        self.assertEqual(res[1].code, "moveBackward")
        self.assertEqual(res[2].code, "stop")

    def test_compression(self):
        res = parse_robot_command("0X123:3,0XABC")
        self.assertEqual(res[0].code, "moveForward")
        self.assertEqual(res[1].code, "moveForward")
        self.assertEqual(res[2].code, "moveForward")
        self.assertEqual(res[3].code, "stop")

if __name__ == "__main__":
    unittest.main()
