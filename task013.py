# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

from itertools import count
import os
os.system('cls')

str1 = '''Один из наиболее известных русских писателей и мыслителей, 
            один из величайших писателей-романистов мира. Участник обороны Севастополя. 
            Просветитель, публицист, религиозный мыслитель, его авторитетное мнение 
            послужило причиной возникновения нового религиозно-нравственного течения - толстовства. 
            За свои взгляды был отлучён от РПЦ. Член-корреспондент Императорской Академии наук, 
            почётный академик по разряду изящной словесности. Был номинирован на 
            Нобелевскую премию по литературе. Впоследствии отказался от дальнейших номинаций. 
            Классик мировой литературы.'''
str2 = 'из'


print('Количество вхождений второй строки в первую: ',
      str1.count(str2), '\n')