import unittest
from unittest.mock import patch
from io import StringIO
from your_module_name import math_quiznew  # replace 'your_module_name' with the actual module name


class TestMathQuiz(unittest.TestCase):
    @patch("builtins.input", side_effect=["5", "2", "8"])
    def test_math_quiz_correct_answer(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            math_quiznew()
        output = mock_stdout.getvalue().strip()
        self.assertIn("Correct! You earned a point.", output)

    @patch("builtins.input", side_effect=["5", "2", "7"])
    def test_math_quiz_wrong_answer(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            math_quiznew()
        output = mock_stdout.getvalue().strip()
        self.assertIn("Wrong answer. The correct answer is", output)

    @patch("builtins.input", side_effect=["abc", "5", "2"])
    def test_math_quiz_invalid_input(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            math_quiznew()
        output = mock_stdout.getvalue().strip()
        self.assertIn("Invalid input. Please enter a valid integer.", output)


if __name__ == "__main__":
    unittest.main()
