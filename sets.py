#Eliminar elementos repetidos de una lista
# [1 , 1 , 2, 2, 4 ] -> [1, 2, 4]

def remove_duplicate(some_list):
    without_duplicates = []
    for element in some_list:
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates


def remove_duplicate_using_sets(some_list):
    return list(set(some_list))


def run():
    random_list = [1, 1, 2, 2, 4]
    print(remove_duplicate(random_list))
    print(remove_duplicate_using_sets(random_list))

if __name__ == '__main__':
    run() 