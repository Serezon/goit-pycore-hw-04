def get_cats_info(path):
    def line_to_cat(line):
        [id, name, age] = line.strip().split(',')
        return {'id': id, 'name': name, 'age': age}

    try:
        with open(path, 'r', encoding='utf-8') as file:
            return list(map(line_to_cat, file))
        
    except FileNotFoundError:
        print('File not found')
    except ZeroDivisionError:
        print('Empty file')
    except:
        print('Invalid data in file')

print(get_cats_info('task2/cats.txt'))