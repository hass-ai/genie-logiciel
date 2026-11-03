import unittest
from robot import parse_robot_command

class RobotTest(unittest.TestCase):
    def test_avancer(self):
        self.assertEqual(parse_robot_command("0X123"), ["moveForward"])

    def test_reculer(self):
        self.assertEqual(parse_robot_command("0X789"), ["moveBackward"])

    def test_stop(self):
        self.assertEqual(parse_robot_command("0XABC"), ["stop"])

    def test_plusieurs_commandes(self):
        res = parse_robot_command("0X123,0X789,0XABC")
        self.assertEqual(res, ["moveForward", "moveBackward", "stop"])

    def test_compression(self):
        res = parse_robot_command("0X123:3,0XABC")
        self.assertEqual(res, ["moveForward", "moveForward", "moveForward", "stop"])

if __name__ == "__main__":
    unittest.main()
