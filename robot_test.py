import unittest
from robot import parse_robot_command

class RobotTest(unittest.TestCase):
    def test_avancer(self):
        self.assertEqual(parse_robot_command("0X123"), ["moveForward"])

    def test_reculer(self):
        self.assertEqual(parse_robot_command("0X789"), ["moveBackward"])

if __name__ == "__main__":
    unittest.main()
