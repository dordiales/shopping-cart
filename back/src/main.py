from pathlib import Path


def split_counted_by_line_break(text):
    content_with_not_new_lines= text.rstrip()
    content_divided_by_lines = content_with_not_new_lines.split("\n")
    return content_divided_by_lines


def split_by_vertical_bar(mylist):
    newlist = []
    for element in mylist:
        separar = element.split("|")
        newlist.append(separar)
    return newlist

def make_list_as_dict(mylist):
    final_list = []
    for item in mylist:
        dictonary_product = {}
        dictonary_product['product'] = item[0]
        dictonary_product['cuantity'] = int(item[1])
        dictonary_product['value'] = float(item[2])
        calculated_subtotal(dictonary_product)
        final_list.append(dictonary_product)
    return final_list

def calculated_subtotal(mydict):
    subtotal = (mydict['cuantity']) * \
                (mydict['value'])
    mydict['subtotal'] = subtotal
    return mydict['subtotal']

def sum_product(diccionario):
    total = 0.0
    for item in diccionario:
        total += item['subtotal']
    return total

def shopping_list_as_prepare_to_jsonify():
    print("hello!!")
    rute_one = Path.cwd() / 'data' / 'new-shopping-list.txt'
    read_content = rute_one.read_text()
    texto_dividido_en_lineas = split_counted_by_line_break(read_content)
    lista_de_carrito = split_by_vertical_bar(texto_dividido_en_lineas)
    lista_de_diccionarios = make_list_as_dict(lista_de_carrito)
    total_de_la_suma = sum_product(lista_de_diccionarios)

    """ for element in lista_de_diccionarios:
        cadena_texto = ("" + str(element['product']) + " - unids: " +

                        str(element['unidades']) + " - p/u: " +
                        str(element['p_unidad']) + " - total: " +
                        str(element['subtotal']))
        print(cadena_texto)

        print('---------------------')
        print('Total: ' + str(total_de_la_suma)) """
    return lista_de_diccionarios