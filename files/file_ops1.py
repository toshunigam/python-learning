file = open("file_operation.txt", "w")
file.write("This file is use for handling file operation")
file.write("it allow us to wrtie it into a perticular file")
file.close()

file_append = open("file_operation_append.txt", "a")
file_append.write("Hello there!! \n")
file_append.write("This will append the file. \n")
file_append.close()