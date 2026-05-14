from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")



def generate_feedback(score, skill_gap):

    prompt = f'''

    Candidate ATS Score: {score}

    Matched Skills:
    {skill_gap.get("matched_skills", [])}

    Missing Skills:
    {skill_gap.get("missing_skills", [])}

    Generate professional ATS feedback in exactly 2 lines.
    '''

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content.strip()