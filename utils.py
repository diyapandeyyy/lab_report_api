import re

def extract_lab_tests(text):
    lab_tests = []
    lines = text.split('\n')

    for line in lines:
        if re.search(r'\d', line):
            match = re.match(r"([A-Za-z\s]+)\s+([\d.]+)\s*([a-zA-Z%/]+)?\s*(\d+\.?\d*)\s*-\s*(\d+\.?\d*)", line)
            if match:
                name = match.group(1).strip()
                value = float(match.group(2))
                unit = match.group(3) or ""
                low = float(match.group(4))
                high = float(match.group(5))
                out_of_range = value < low or value > high

                lab_tests.append({
                    "lab_test_name": name,
                    "value": str(value),
                    "unit": unit,
                    "bio_reference_range": f"{low} - {high}",
                    "lab_test_out_of_range": out_of_range
                })

    return lab_tests
