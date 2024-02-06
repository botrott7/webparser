def filter_bitcoin_list():
    try:
        filename = "lst.txt"

        with open(filename, 'r', encoding='utf-8') as file:
            content = file.readlines()

        new_filename = "filtered_bitcoin_list.txt"
        new_file = open(new_filename, 'w', encoding='utf-8')

        for line in content:
            currency_code = line.split()[0]
            new_file.write(currency_code + "\n")

        new_file.close()

        print("Файл успешно создан!")

    except FileNotFoundError:
        print("Ошибка: Файл не найден")


filter_bitcoin_list()
