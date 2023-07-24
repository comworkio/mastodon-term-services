def file_get_contents(path, separator = ''):
    return separator.join(open(path, 'r').readlines())

def file_get_contents_inline(path):
    return file_get_contents(path).rstrip().replace("\n", "").replace("\r", "")

def format_html_settings(path):
    return "--- \"{}\"".format(file_get_contents_inline(path).replace('"', r'\"'))

def format_css_settings(path):
    return format_html_settings(path)

def format_md_settings(path):
    return "--- \"{}\"".format(file_get_contents(path, '\n'))
