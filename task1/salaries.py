def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            salaries = [int(line.strip().split(',')[1]) for line in file]

        total = sum(salaries)
        average = total / len(salaries)
        return (total, average)

    except FileNotFoundError:
        print('File not found')
    except ZeroDivisionError:
        print('Empty file')
    except:
        print('Invalid data in file')

print(total_salary('task1/salaries.txt'))