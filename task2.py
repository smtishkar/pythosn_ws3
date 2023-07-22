attributes = ['fgdgd', '12435', '12.05', 'dFGdfgdf',
               'dssdg.dffd','-12']


for attr in attributes:
    if attr.lstrip('-').isdigit():
        res = abs(int(attr))
        print(res, type(res))
    elif attr.count('.')==1:
        if attr.replace('.','',1).isdigit():
            res = float(attr)
            print(res, type(res))

    elif attr != attr.lower():
        print(attr.lower())
    else:
        print(attr.upper())