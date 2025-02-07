import json
from unittest.mock import patch
from src.index import lambda_handler # Import the Lambda function code

# Test case for a known number (7)
@patch('random.randint')
def test_lambda_handler_known_number(mock_randint):
    # Mock the random number generation to always return 7
    mock_randint.return_value = 7

    # Call the Lambda handler
    result = lambda_handler({}, {})

    # Parse the response body
    response_body = json.loads(result['body'])

    # Expected response for the number 7
    expected_response = {
        "random_number": 7,
        "chinese": {
            "character": "七",
            "pronunciation": "qī"
        },
        "thai": "เจ็ด",
        "malay": "tujuh"
    }

    # Assert the response matches the expected output
    assert result['statusCode'] == 200
    assert response_body == expected_response

# Test case for an unknown number (11)
@patch('random.randint')
def test_lambda_handler_unknown_number(mock_randint):
    # Mock the random number generation to return a number not in the dictionaries (e.g., 11)
    mock_randint.return_value = 11

    # Call the Lambda handler
    result = lambda_handler({}, {})

    # Parse the response body
    response_body = json.loads(result['body'])

    # Expected response for an unknown number
    expected_response = {
        "random_number": 11,
        "chinese": {
            "character": "未知",
            "pronunciation": "wèi zhī"
        },
        "thai": "ไม่ทราบ",
        "malay": "tidak diketahui"
    }

    # Assert the response matches the expected output
    assert result['statusCode'] == 200
    assert response_body == expected_response