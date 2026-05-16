import google.generativeai as genai

genai.configure(
    api_key="AIzaSyCf-7v_0mTRrXK6bwRMAQdj9e4WoUiEKqg"
)
model = genai.GenerativeModel("gemini-2.0-flash")


def generate_feedback(score, skill_gap):

    prompt = f'''

    Candidate ATS Score: {score}

    Matched Skills:
    {skill_gap.get("matched_skills", [])}

    Missing Skills:
    {skill_gap.get("missing_skills", [])}

    Generate professional ATS feedback in exactly 2 lines.
    '''

    response = model.generate_content(prompt)
    return response.text.strip()