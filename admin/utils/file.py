def file_get_contents(path):
    return ''.join(open(path, 'r').readlines()).rstrip
