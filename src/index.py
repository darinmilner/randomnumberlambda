import json
import random

def lambda_handler(event, context):
    # Generate a random number between 1 and 10
    random_number = random.randint(1, 10)

    # Chinese character and pronunciation for the number
    chinese_numbers = {
        1: ("一", "yī"),
        2: ("二", "èr"),
        3: ("三", "sān"),
        4: ("四", "sì"),
        5: ("五", "wǔ"),
        6: ("六", "liù"),
        7: ("七", "qī"),
        8: ("八", "bā"),
        9: ("九", "jiǔ"),
        10: ("十", "shí"),
        # Add more numbers as needed
    }

    # Thai equivalent for the number
    thai_numbers = {
        1: "หนึ่ง",
        2: "สอง",
        3: "สาม",
        4: "สี่",
        5: "ห้า",
        6: "หก",
        7: "เจ็ด",
        8: "แปด",
        9: "เก้า",
        10: "สิบ",
        # Add more numbers as needed
    }

    # Malay equivalent for the number
    malay_numbers = {
        1: "satu",
        2: "dua",
        3: "tiga",
        4: "empat",
        5: "lima",
        6: "enam",
        7: "tujuh",
        8: "lapan",
        9: "sembilan",
        10: "sepuluh",
        # Add more numbers as needed
    }

    # Get the Chinese character and pronunciation
    chinese_char, chinese_pronunciation = chinese_numbers.get(random_number, ("未知", "wèi zhī"))

    # Get the Thai equivalent
    thai_equivalent = thai_numbers.get(random_number, "ไม่ทราบ")

    # Get the Malay equivalent
    malay_equivalent = malay_numbers.get(random_number, "tidak diketahui")

    # Prepare the response
    response = {
        "random_number": random_number,
        "chinese": {
            "character": chinese_char,
            "pronunciation": chinese_pronunciation
        },
        "thai": thai_equivalent,
        "malay": malay_equivalent
    }

    return {
        'statusCode': 200,
        'body': json.dumps(response, ensure_ascii=False)
    }


lambda_handler({}, {})