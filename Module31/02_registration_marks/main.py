import re
text = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

private_cars = re.findall(r'\b[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,}\w+', text)
taxi = re.findall(r'\b[АВЕКМНОРСТУХ]{2}\d{4,}\w+', text)
print(private_cars)
print(taxi)
