from unittest.mock import MagicMock, Mock, patch
import bmi_calc_json


TEST_JSON = [
    {"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
    { "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
    {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}
]

TEST_IN = [
    ['Gender', 'HeightCm', 'WeightKg'], 
    ['Male', '171', '96'], 
    ['Male', '161', '85'], 
    ['Female', '167', '82']
]

TEST_result = [
    ['Male', '171', '96', 'Moderately obese', 32.83061454806607, 'Medium risk'], 
    ['Male', '161', '85', 'Moderately obese', 32.79194475521777, 'Medium risk'], 
    ['Female', '167', '82', 'Overweight', 29.402273297715947, 'Enhanced risk']
]



@patch("json.load", MagicMock(return_value=TEST_JSON))
def test_read_json_content():
    result = bmi_calc_json.read_json_content()
    assert result == TEST_IN


def test_write_json():
    test_total_overweight = 1
    t_result = f'JSON file created successfully.. & Total Number of Overweighted person {test_total_overweight}'
    result  = bmi_calc_json.write_json(TEST_result)
    assert result == t_result