def csv_to_list(csv_file):

    f = open(csv_file, 'r')
    g = f.read()
    g = g.replace('"','')
    result = g.split(',')

    return result


def convert_to_list(file_name, seperator = ' '):

    f = open(file_name, 'r')
    g = f.read()
    g = g.replace('"','')
    result = g.split(seperator)

    return result
