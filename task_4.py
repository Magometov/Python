import os

result_dict = {
    100: 0,
    1000: 0,
    10000: 0,
    100000: 0
}


def size_file(file_name: str) -> None:
    if os.path.exists(file_name):
        for root, dirs, files in os.walk(file_name):
            for file in files:
                ext = os.stat(os.path.join(root, file)).st_size
                if ext < 100:
                    result_dict[100] += 1
                elif 100 < ext < 1000:
                    result_dict[1000] += 1
                elif 1000 < ext < 10000:
                    result_dict[10000] += 1
                else:
                    result_dict[100000] += 1

    print(result_dict)


size_file('C:\\Users\\Анзор\\Desktop\\Python')
