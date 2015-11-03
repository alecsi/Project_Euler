import pandigital

def solution():
    """i only bother searching for i = 2 as this gave a correct solution"""   
    x = {int(str(n*1)+str(n*2)) for n in range(0,9999) if (len(str(n*1)+str(n*2))==9 and pandigital.is_pandigital({n*1, n*2}))}

    return max(x) 
