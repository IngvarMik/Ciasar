"""коди Цезаря"""
alphabet = ["а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о","п","р","с","т","у",
            "ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"] # список алфавит

phraze = str(input()) # запрос фразы 
result = "" # переменная результат 

for item in phraze: # цикл делаем - 
    """item.lower -это чтобы при запросе если будут большие буквы в тексте , то lower сделает их маленькими"""
    current_index = alphabet.index(item.lower())
     # связываем алфавит и индекс - в списке каждый элемент имеет индекс 
    if current_index + 3 > len(alphabet):
        new_index = current_index + 3 - len(alphabet) # это если буква "я" , то чтоб уйти в начало списка 
        # по индексу иначе он не найдет буквы на замену - закольцовываем индексы алфавита
    else:     
        new_index = current_index + 3 # а это добавление к индексу 3 , 
    """работаем с индексами списка - т.е к индексу буквы из списка 
    добавляем 3 - таким образом подменяем букву - пример буква "а" плюс три это буква "г" """
    result += alphabet[new_index]

print(result)
