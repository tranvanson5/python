import json

from src.user.DetectFace import write_person_json
from src.utils.HandlingXlsxFile import read_excel
from src.MainWidows import MainWindows

def get_list_employees():
    employees = read_excel(r'C:\Users\drive\Desktop\FaceAttendance\assets\information\DanhSachNhanVien.xlsx')

    try:
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(employees, f, indent=4)
        print("Employees data saved successfully!")
    except IOError as e:
        print("Error saving data:", e)


def main():
    write_person_json(None)
    get_list_employees()
    MainWindows()
if __name__ == '__main__':
    main()