import re
import csv


def remove_duplicates(list_: list) -> list:
    k = 0
    while k < len(list_) - 1:
        for list1, list2 in zip(list_[k], list_[k + 1]):
            if list1 == list2:
                new_list = []
                for i in range(len(list_[k])):
                    if list_[k][i] == list_[k+1][i]:
                        new_list.append(list_[k][i])

                    elif list_[k][i] == '':
                        new_list.append(list_[k+1][i])

                    else:
                        new_list.append(list_[k][i])

                list_.remove(list_[k + 1])
                list_.remove(list_[k])
                list_.append(new_list)
            break
        k += 1
    return list_


def format_phone_numbers(text: str) -> str:
    pattern = r"(\+7|8)\s?\(?(\d{3})\)?-?\s?(\d{3})-?(\d{2})-?(\d{2})\s?(\(?(доб\.\s?\d{4})\)?)?"
    substitution = r"+7(\2)-\3-\4-\5 \7"
    edited_text = re.sub(pattern, substitution, text)
    return edited_text


def convert_to_string(text: list) -> str:
    result = ''
    for row in text:
        result += ', '.join(row)
        result += '\n'
    print(result)
    return result


def convert_for_csv(text: str) -> list:
    result_text = []
    for line in text.split('\n'):
        result_text.append(line.split(', '))
    result_text.remove([''])
    print(result_text)
    return result_text


def main():
    with open("phonebook_raw.csv", encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    for index, person in enumerate(contacts_list[1:]):
        result = ' '.join(person[:3]).split()
        if len(result) == 2:
            result.append('')
        contacts_list[index + 1][:3] = result[:3]
    sorted_list = sorted(contacts_list, key=lambda x: x[0:2])

    # step 1 remove duplicates
    result = remove_duplicates(sorted_list)
    # step 2 convert to string
    result = convert_to_string(result)
    # step 3 format phone numbers to the template
    result = format_phone_numbers(result)
    # step 4 convert to list for writing csv file
    result = convert_for_csv(result)

    # код для записи файла в формате CSV
    with open("phonebook.csv", "w", encoding="utf-8", newline='') as f:
        datawriter = csv.writer(f, delimiter=',')
        # Вместо contacts_list подставьте свой список
        datawriter.writerows(result)


if __name__ == '__main__':
    main()
