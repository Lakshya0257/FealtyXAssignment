import requests
import json
def generate_student_summary(student):
    headers = {
        "Content-Type": "application/json",
    }
    prompt = f"Summarize the following student profile:\n\nID: {student['id']}\nName: {student['name']}\nAge: {student['age']}\nEmail: {student['email']}"
    response = requests.post('http://127.0.0.1:11434/api/generate', json={'prompt': prompt, 'model': "llama3.2"}, headers=headers)

    print(response)
    print(len(response.text))
    print(response.text[0])
    if response.ok:
        # Convert response to JSON
        # data = response.json()
        # # Filter to essential fields and combine to single line
        # final_response = {
        #     "model": data.get("model"),
        #     "created_at": data.get("created_at"),
        #     "response": data.get("response"),
        #     "done": data.get("done")
        # }
        # # Print or return as single-line JSON
        # print(json.dumps(final_response, separators=(',', ':')))
        return "Done"
    else:
        print("Error:", response.status_code, response.text)
        return f"Error generating summary: {response.status_code} - {response.text}"
    
    # if response.status_code == 200:
    #     try:
    #         return response.json().get('generated_text', '')
    #     except (KeyError, json.JSONDecodeError):
    #         return response.text
    # else:
    #     return f"Error generating summary: {response.status_code} - {response.text}"
