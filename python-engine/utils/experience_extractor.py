import re



def extract_experience(text):

    patterns = [
        r'(\d+)\+? years',
        r'(\d+)\+? yrs',
        r'experience of (\d+)'
    ]

    years = []

    for pattern in patterns:

        matches = re.findall(pattern, text.lower())

        for match in matches:
            years.append(int(match))

    if len(years) == 0:
        return 0

    return max(years)