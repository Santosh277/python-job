import re


def extract_experience(text):

    patterns = [

        r'(\d+(?:\.\d+)?)\+?\s*years?',
        r'(\d+(?:\.\d+)?)\+?\s*yrs?',
        r'experience of\s*(\d+(?:\.\d+)?)',
        r'minimum\s*(\d+(?:\.\d+)?)\s*years?',
        r'over\s*(\d+(?:\.\d+)?)\s*years?',
        r'(\d+(?:\.\d+)?)\s*-\s*\d+\s*years?',
        r'(\d+(?:\.\d+)?)\s*to\s*\d+\s*years?'
    ]

    years = []

    lower_text = text.lower()

    for pattern in patterns:

        matches = re.findall(pattern, lower_text)

        for match in matches:

            try:
                years.append(float(match))
            except:
                pass

    if len(years) == 0:
        return 0

    return max(years)