from generator import Generator
from LinkList import LinkList
from datetime import datetime

gen = Generator()

# генерация новых объектов
timer_start = datetime.utcnow()
gen_10000 = gen.generate_10000()
timer_stop = datetime.utcnow() - timer_start
print("Генерация 10 000 элементов:\n" + str(timer_stop))

# Таймер для добавления элементов в конец массива
timer_start = datetime.utcnow()

# s_list = StandardList2()/
s_list = LinkList()
for gpu in gen_10000:
    s_list.add(gpu)
timer_stop = datetime.utcnow() - timer_start
print("Добавление 10 000 элементов в конец массива:\n" + str(timer_stop) + "\tРазмер массива: " + str(s_list.size))

# Таймер для добавления элементов в начало массива
timer_start = datetime.utcnow()

# s_list = StandardList2()
s_list = LinkList()
for gpu in gen_10000:
    s_list.add(gpu, 0)

timer_stop = datetime.utcnow() - timer_start
print("Добавление 10 000 новых элементов в начало:\n" + str(timer_stop) + "\tРазмер массива: " + str(s_list.size))

# Таймер для замены элемента
timer_start = datetime.utcnow()

for gpu in gen_10000:
    s_list.insert(gpu, len(gen_10000) - 1)

timer_stop = datetime.utcnow() - timer_start
print("Последовательная замена последнего элемента 10 000 значений:\n" + str(timer_stop) + "\tРазмер массива: " +
      str(s_list.size))

# Таймер для поиска элемента
timer_start = datetime.utcnow()

res = s_list.find(gen_10000[0])

timer_stop = datetime.utcnow() - timer_start
print("Поиск первого элемента:\n" + str(timer_stop) + "\tРазмер массива: " + str(s_list.size))


# Таймер для поиска элемента
timer_start = datetime.utcnow()

timer_stop = datetime.utcnow() - timer_start
print("Поиск последнего элемента:\n" + str(timer_stop) + "\tРазмер массива: " + str(s_list.size))

# Таймер для поиска элемента по индексу
timer_start = datetime.utcnow()

timer_stop = datetime.utcnow() - timer_start
print("Поиск последнего элемента из 10 000 по индексу:\n" + str(timer_stop) + "\tРазмер массива: " + str(s_list.size))

# Таймер для удаления первых элементов
timer_start = datetime.utcnow()

for gpu in gen_10000:
    s_list.remove(gpu)

timer_stop = datetime.utcnow() - timer_start
print("Удаление 1-го элемента 10 000 раз:\n" + str(timer_stop) + "\tРазмер массива: " + str(s_list.size))

# Таймер для удаления последних элементов
timer_start = datetime.utcnow()

for gpu in reversed(gen_10000):
    s_list.remove(gpu)

timer_stop = datetime.utcnow() - timer_start
print("Удаление последнего элемента 10 000 раз:\n" + str(timer_stop) + "\tРазмер массива: " + str(s_list.size))
