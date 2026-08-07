ids = []
nombres = []
tipos = []
valores = []
categorias = []
estados = []
fechas = []
origenes = []
descripciones = []
#-----------------------------------------#
#--|menu_principal_aterrizador_de_datos|--#
#-----------------------------------------#
while True:
    print("menu principal aterrizador de datos")
    print("1) registrar dato")
    print("2) editar dato")
    print("3) eliminar dato")
    print("4) buscar dato")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #--------------------#
    #--|registrar_dato|--#
    #--------------------#
    if opcion == "1":
        if len(ids) == 0:
            id_dato = 1
        else:
            id_dato = ids[-1] + 1
        nombre = input("nombre del dato: ")
        tipo = input("tipo de dato (texto, entero, decimal o booleano): ")
        valor = input("valor: ")
        categoria = input("categoría: ")
        fecha = input("fecha de recepción: ")
        origen = input("origen: ")
        descripcion = input("descripción: ")
        estado = "inválido"
        if tipo.lower() == "texto":
            estado = "válido"
        elif tipo.lower() == "entero":
            try:
                int(valor)
                estado = "válido"
            except ValueError:
                estado = "inválido"
        elif tipo.lower() == "decimal":
            try:
                float(valor)
                estado = "válido"
            except ValueError:
                estado = "inválido"
        elif tipo.lower() == "booleano":
            if valor.lower() == "true" or valor.lower() == "false":
                estado = "válido"
            else:
                estado = "inválido"
        else:
            print("tipo de dato no reconocido.")
            estado = "inválido"
        ids.append(id_dato)
        nombres.append(nombre)
        tipos.append(tipo)
        valores.append(valor)
        categorias.append(categoria)
        estados.append(estado)
        fechas.append(fecha)
        origenes.append(origen)
        descripciones.append(descripcion)
        print("dato procesado correctamente.")
        print("id:", id_dato)
        print("estado:", estado)
    #-----------------#
    #--|editar_dato|--#
    #-----------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen datos registrados.")
        else:
            print("editar dato")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {tipos[i]} | {estados[i]}")
            id_buscar = int(input("ingrese la id del dato: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print("id:", ids[posicion])
                print("nombre:", nombres[posicion])
                print("tipo:", tipos[posicion])
                print("valor:", valores[posicion])
                nombres[posicion] = input("nuevo nombre: ")
                tipos[posicion] = input(
                    "nuevo tipo (texto, entero, decimal o booleano): "
                )
                valores[posicion] = input("nuevo valor: ")
                categorias[posicion] = input("nueva categoría: ")
                fechas[posicion] = input("nueva fecha: ")
                origenes[posicion] = input("nuevo origen: ")
                descripciones[posicion] = input("nueva descripción: ")
                estados[posicion] = "inválido"
                if tipos[posicion].lower() == "texto":
                    estados[posicion] = "válido"
                elif tipos[posicion].lower() == "entero":
                    try:
                        int(valores[posicion])
                        estados[posicion] = "válido"
                    except ValueError:
                        estados[posicion] = "inválido"
                elif tipos[posicion].lower() == "decimal":
                    try:
                        float(valores[posicion])
                        estados[posicion] = "válido"
                    except ValueError:
                        estados[posicion] = "inválido"
                elif tipos[posicion].lower() == "booleano":
                    if valores[posicion].lower() == "true" or valores[posicion].lower() == "false":
                        estados[posicion] = "válido"
                print("dato actualizado correctamente.")
                print("nuevo estado:", estados[posicion])
            else:
                print("id no encontrada.")
    #-------------------#
    #--|eliminar_dato|--#
    #-------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen datos registrados.")
        else:
            print("eliminar dato")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {estados[i]}")
            id_buscar = int(input("ingrese la id del dato: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("id:", ids[posicion])
                print("nombre:", nombres[posicion])
                print("valor:", valores[posicion])
                confirmacion = input(
                    "¿desea eliminar este dato? (s/n): "
                )
                if confirmacion.upper() == "S":
                    ids.pop(posicion)
                    nombres.pop(posicion)
                    tipos.pop(posicion)
                    valores.pop(posicion)
                    categorias.pop(posicion)
                    estados.pop(posicion)
                    fechas.pop(posicion)
                    origenes.pop(posicion)
                    descripciones.pop(posicion)
                    print("dato eliminado correctamente.")
                else:
                    print("el dato no fue eliminado.")
            else:
                print("id no encontrada.")
    #-----------------#
    #--|buscar_dato|--#
    #-----------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen datos registrados.")
        else:
            print("buscar dato")
            id_buscar = int(input("ingrese la id del dato: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("id:", ids[posicion])
                print("nombre:", nombres[posicion])
                print("tipo:", tipos[posicion])
                print("valor:", valores[posicion])
                print("categoría:", categorias[posicion])
                print("estado:", estados[posicion])
                print("fecha:", fechas[posicion])
                print("origen:", origenes[posicion])
                print("descripción:", descripciones[posicion])
            else:
                print("id no encontrada.")
    #--------------------#
    #--|lista_de_datos|--#
    #--------------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen datos registrados.")
        else:
            validos = 0
            invalidos = 0
            textos = 0
            enteros = 0
            decimales = 0
            booleanos = 0
            print("lista de datos")
            for i in range(len(ids)):
                print(
                    f"{ids[i]} | {nombres[i]} | "
                    f"{tipos[i]} | {valores[i]} | {estados[i]}"
                )
                if estados[i].lower() == "válido":
                    validos += 1
                elif estados[i].lower() == "inválido":
                    invalidos += 1
                if tipos[i].lower() == "texto":
                    textos += 1
                elif tipos[i].lower() == "entero":
                    enteros += 1
                elif tipos[i].lower() == "decimal":
                    decimales += 1
                elif tipos[i].lower() == "booleano":
                    booleanos += 1
            print("estadísticas aterrizador de datos")
            print("cantidad de datos:", len(ids))
            print("válidos:", validos)
            print("inválidos:", invalidos)
            print("texto:", textos)
            print("entero:", enteros)
            print("decimal:", decimales)
            print("booleano:", booleanos)
            print("aterrizador de datos")
            nombre_buscar = input(
                "ingrese el nombre del dato para procesarlo: "
            )
            encontrado = False
            for i in range(len(nombres)):
                if nombres[i].lower() == nombre_buscar.lower():
                    encontrado = True
                    print("dato procesado")
                    print("nombre:", nombres[i])
                    print("tipo esperado:", tipos[i])
                    print("valor:", valores[i])
                    print("resultado:", estados[i])
                    if estados[i].lower() == "válido":
                        print("el dato fue aceptado correctamente.")
                    else:
                        print("el dato presenta un formato incorrecto.")
                    break
            if encontrado == False:
                print("dato no encontrado.")
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el aterrizador de datos.")
        break
    else:
        print("opción no válida.")