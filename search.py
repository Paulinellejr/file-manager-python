import os


def search_files(path, filename):
    filename,_ = os.path.splitext(filename)
    result = {}
    total_file = 0

    for root, dirs, files in os.walk(path):
        for file in files:
            name,_= os.path.splitext(file)
            if filename.lower() in name.lower():
                if root not in  result:
                    result[root] = []
                result[root].append(file)
                total_file += 1
    return result, total_file
