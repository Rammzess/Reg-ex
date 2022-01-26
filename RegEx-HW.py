from pprint import pprint
import csv
import re

# читаем адресную книгу в формате CSV в список contacts_list
with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)


# TODO 1: выполните пункты 1-3 ДЗ
if __name__ == '__main__':
  # Паттерны для обычных номеров  
  phone_pattern1 = r"\+?(7|8)?\s*\((\d+)\)\s*(\d+)[\s-]*(\d+)[\s-]*(\d+)"
  phone_pattern2 = (
    r"\+?(7|8)?\s*(495)[\s*-]*(\d{1,3})[\s*-]*(\d{1,2})[\s*-]*(\d{1,2})"
  )
  replace_num = r"+\1(\2)\3-\4-\5"
  
  # Паттерн для доб. номера
  dop_pattern = r"\(?([а-я]+.)\s(\d+)\)?"
  replace_dop = r"\1\2"
  
  for x in range(len(contacts_list)):
    contacts_list[x][5] = re.sub(
      phone_pattern1, replace_num, contacts_list[x][5]
      )
    contacts_list[x][5] = re.sub(
      phone_pattern2, replace_num, contacts_list[x][5]
      )
    contacts_list[x][5] = re.sub(
      dop_pattern, replace_dop, contacts_list[x][5]
      )

  # Разделение ФИО
  for contact in contacts_list:
    result1 = re.split(r"[\s,]", contact[0])
    result2 = re.split(r"[\s]", contact[1])
    if len(result1) > 1:
      contact[0:3] = result1[0:3]
    if contact[0] == 'Наркаев':
      contacts_list[3][1:3] = result2[0:2]

  # Заполнение пустых строк и удаление лишних
  contacts_list[2][4] = contacts_list[4][4]
  contacts_list[7][6] = contacts_list[8][5]
  contacts_list.pop(8)
  contacts_list.pop(4)

  pprint(contacts_list)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
  with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list)