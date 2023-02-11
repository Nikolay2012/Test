import os

def search(file_name):
    path = __file__.split("/")
    for i in range(2):
        del path[-1]
    path = '/'.join(path)
    path = os.path.join(path, file_name)
    return path
