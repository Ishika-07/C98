def swapFileData():

    file_1 = input("Enter the name of your first file: ")
    file_2 = input("Enter the name of your second file: ")

    with open(file_1, 'r') as a:
        data_a = a.read()

    with open(file_2, 'r') as b:
        data_b = b.read()

    with open(file_1, 'w') as write_a:
        write_a.write(data_b)

    with open(file_2, 'w') as write_b:
        write_b.write(data_a)

swapFileData()