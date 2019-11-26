"""Case-study #4 Парсинг web-страниц
Разработчики:
Иванов А.С., Петров П.С., Сидоров C.H.

"""
import urllib.request

url = 'http://www.nfl.com/player/brycepetty/2552369/profile'
f = urllib.request.urlopen(url)
s = f.read()
text = str(s)
print(text)
part_name = text.find("player-name")
name = text[text.find('>', part_name) + 1:text.find('&', part_name)]
part_stat = text.find('TOTAL')
stat = text[text.find('>', part_stat) + 1:text.find('</tr>', part_stat)].replace('t','').replace('n','')
stat = stat.replace('\\','').replace('<d>','').split('</d>')
print(name)
print(stat)
ATT = float(stat[1])
COMP = float(stat[0])
YDS = float((stat[3]).replace(',',''))
TD = float(stat[5])
INT = float(stat[6])
PR = ((ATT + COMP + YDS + TD + INT)/6) * 100
print(PR)
# Файл input.txt
