from google import genai
client = genai.Client(api_key="AIzaB7KXak")
def generate_feedback(score, skill_gap):

    prompt = f'''

    Candidate ATS Score: {score}

    Matched Skills:
    {skill_gap.get("matched_skills", [])}

    Missing Skills:
    {skill_gap.get("missing_skills", [])}

    Generate professional ATS feedback in exactly 2 lines.
    '''
    response = client.models.generate_content(
    model="gemini-2.5-flash", 
    contents=prompt)
    return response.text.strip()
