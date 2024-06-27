import json

def write_person_json(employee):
    try:
        with open('person.json', 'w', encoding='utf-8') as f:
            json.dump(employee, f, indent=4)
        print("Employee data saved successfully!")
    except IOError as e:
        print("Error saving data:", e)
