def file_get_contents_inline(path):
    return ''.join(open(path, 'r').readlines()).rstrip().replace("\n", "").replace("\r", "")

def config_settings(path):
    return "--- \"{}\"".format(file_get_contents_inline(path).replace('"', r'\"'))
