from google import genai

client = genai.Client(api_key="AIzaSyCf-7v_0mTRrXK6bwRMAQdj9e4WoUiEKqg")

def generate_feedback(score, skill_gap):

    prompt = f'''

    Candidate ATS Score: {score}

    Matched Skills:
    {skill_gap.get("matched_skills", [])}

    Missing Skills:
    {skill_gap.get("missing_skills", [])}

    Generate professional ATS feedback in exactly 2 lines.
    '''

    # response = model.generate_content(prompt)
    response = client.interactions.create(
    model="gemini-3-flash-preview", 
    input=prompt)
    return response.text.strip()
