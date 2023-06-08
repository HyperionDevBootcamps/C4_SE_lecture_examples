import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.cal_obj = Calculator() # Arrange

    def test_can_calculator_add_one_to_one_and_give_two(self):
        result = self.cal_obj.add(1,1) # Act
        self.assertEqual(result, 2) # Assert

    def test_can_calculator_add_two_to_one_and_give_three(self):
        result = self.cal_obj.add(2,1) # Act
        self.assertEqual(result, 3) # Assert

    def test_can_calculator_add_three_to_one_and_give_four(self):
        result = self.cal_obj.add(3,1) # Act
        self.assertEqual(result, 4) # Assert

    def test_can_calculator_add_one_to_two_and_give_three(self):
        result = self.cal_obj.add(1,2) # Act
        self.assertEqual(result, 3) # Assert

    def test_can_calculator_add_one_to_three_and_give_four(self):
        result = self.cal_obj.add(1,3) # Act
        self.assertEqual(result, 4) # Assert

    def test_result_does_return_if_first_number_is_string_number(self):
        result = self.cal_obj.add("1",3) # Act
        self.assertEqual(result, 4) # Assert
        
    def test_result_does_return_if_second_number_is_string_number(self):
        result = self.cal_obj.add(1,"3") # Act
        self.assertEqual(result, 4) # Assert
        
    def test_result_does_return_erre_if_first_number_is_invalid_string_number(self):
        result = self.cal_obj.add("asd",3) # Act
        self.assertEqual(result, "Invalid types") # Assert

    
    # Multiply
    def test_can_calculator_multiply_one_with_one_and_give_one(self):
        result = self.cal_obj.multiply(1,1) # Act
        self.assertEqual(result, 1) # Assert

    def test_can_calculator_multiply_one_with_two_and_give_two(self):
        result = self.cal_obj.multiply(1,2) # Act
        self.assertEqual(result, 2) # Assert

    def test_can_calculator_multiply_two_with_one_and_give_two(self):
        result = self.cal_obj.multiply(2,1) # Act
        self.assertEqual(result, 2) # Assert

    
    # def test_can_calculator_multiply_string_two_with_five_and_throw_type_error(self):
    #     with self.assertRaises(TypeError): # Assert
    #         result = self.cal_obj.multiply("2",5) # Act




if __name__ == "__main__":
    unittest.main()