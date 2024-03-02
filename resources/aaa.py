import os

file_path = "/Users/max/PycharmProjects/qa_guru_10_10/demoqa_tests/resources/123.jpeg"

if os.path.exists(file_path):
    print("Файл существует.")
else:
    print("Файл не существует.")