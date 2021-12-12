# File I/O

FILE_NAME = "test.txt"

# file_obj=open(FILE_NAME, mode='w', encoding='utf-8')
# file_obj.write("TEST\n")
# file_obj.write("TEST\n")
# file_obj.write("TEST\n")
# file_obj.write("오늘은 수요일입니다~\n")
# file_obj.close()


# file_obj=open(FILE_NAME, mode='r', encoding='utf-8')
# data=file_obj.read()
# file_obj.close()
with open(FILE_NAME, mode='r', encoding='utf-8') as file_obj:
    data = file_obj.read("TEST\n")
    print(f"Read File Data => {data}")
