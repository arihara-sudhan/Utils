import re
import json

def parse_text_file(file_path, encoding='utf-8'):
    data = []
    current_question = None
    current_answer = None
    
    with open(file_path, 'r', encoding=encoding) as file:
        lines = file.readlines()
        
        for line in lines:
            line = line.strip()
            
            match = re.match(r'^(\d+)\.', line)
            if match:
                # Save the previous question and answer
                if current_question and current_answer:
                    data.append({"question": current_question, "answer": current_answer})
                
                # Start a new question
                current_question = line[len(match.group(0)):].strip()
                current_answer = None
            elif current_question and line:
                if not current_answer:
                    current_answer = line.strip()
                else:
                    current_answer += " " + line.strip()
        
        # Save the last question and answer
        if current_question and current_answer:
            data.append({"question": current_question, "answer": current_answer})
            
    return data

def save_as_json(data, output_path):
    with open(output_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    input_file_path = "gkmain2.txt"
    output_file_path = "gkmain2.json"
    
    parsed_data = parse_text_file(input_file_path, encoding='utf-8')
    save_as_json(parsed_data, output_file_path)
    
    print("Conversion complete. JSON file saved as 'questions.json'.")
