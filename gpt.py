import openai

openai.api_key = 'your_api_key'

def generate_cover_letter(resume, job_description, additional_context=None):
    prompt = f'Generate a cover letter based on the following resume and job description:\n\nResume:\n{resume}\n\nJob Description:\n{job_description}'

    if additional_context:
        prompt += f'\n\nAdditional Context:\n{additional_context}'

    response = openai.Completion.create(
        engine='text-davinci-002',
        prompt=prompt,
        max_tokens=400,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response.choices[0].text.strip()