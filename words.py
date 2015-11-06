def csv_to_list(csv_file):

    f = open(csv_file, 'r')
    g = f.read()
    g = g.replace('"','')
    result = g.split(',')

    return result
