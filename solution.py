"""Case-study #4 Парсинг web-страниц
Разработчики:
Силкачев В.В. 35%, Попов К.М. 45%, Винников А.А. 35%

"""
import urllib.request

with open('output.txt', "w") as f:
    pass

with open('input.txt', 'r') as inp_file:
    lst_file = inp_file.readlines()
for url in lst_file:

    f = urllib.request.urlopen(url)
    s = f.read()
    text = str(s)
    part_name = text.find("player-name")
    name = text[text.find('>', part_name) + 1:text.find('&', part_name)]
    part_stat = text.find('TOTAL')
    stat = text[text.find('>', part_stat) + 1:text.find('</tr>', part_stat)].replace('t','').replace('n','')
    stat = stat.replace('\\','').replace('<d>','').split('</d>')
    ATT = int((stat[1]).replace(',',''))
    COMP = int((stat[0]).replace(',',''))
    YDS = int((stat[3]).replace(',',''))
    TD = int((stat[5]).replace(',',''))
    INT = int((stat[6]).replace(',',''))
    a = (COMP/ATT) / 6
    b = (YDS/ATT - 3) * .25
    c = (TD/ATT) * 20
    d = (2.375 - (INT/ATT * 25))
    PR = ((a + b + c + d)/6) * 100
    PR = ('{0:.2f}'.format(PR))
    with open('output.txt', "a") as f:
        f.write(name + ' ' + str(COMP) + ' ' + str(ATT) + ' ' + str(YDS) + ' ' + str(TD) + ' ' + str(INT) + ' ' + PR + '\n')

