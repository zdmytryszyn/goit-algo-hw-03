# HOMEWORK - 3rd task
import re


def normalize_phone(phone_number: str) -> str:
    pattern = r"\d+"
    phone_number_raw_numbers = "".join(re.findall(pattern=pattern, string=phone_number))
    return "+" + phone_number_raw_numbers if phone_number_raw_numbers.startswith("38") else ("+38" +
                                                                                             phone_number_raw_numbers)

