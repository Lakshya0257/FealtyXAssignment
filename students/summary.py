import requests

def generate_student_summary(student):
    headers = {
        "Content-Type": "application/json",
    }
    prompt = f"Summarize the following student profile:\n\nID: {student['id']}\nName: {student['name']}\nAge: {student['age']}\nEmail: {student['email']}"
    response = requests.post('http://127.0.0.1:11434/api/generate', json={'prompt': prompt, 'model': "llama3.1:latest"}, headers=headers)
    
    if response.status_code == 200:
        try:
            return response.json().get('generated_text', '')
        except (KeyError, json.JSONDecodeError):
            return response.text
    else:
        return f"Error generating summary: {response.status_code} - {response.text}"
