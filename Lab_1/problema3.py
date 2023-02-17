def main():
    usuarios = [
        {"id": 0, "nombre": "Pepito"},
        {"id": 1, "nombre": "Mafalda"},
        {"id": 2, "nombre": "Pedrito"},
        {"id": 3, "nombre": "Pablito"},
        {"id": 4, "nombre": "Gustavito"},
        {"id": 5, "nombre": "Claudita"},
        {"id": 6, "nombre": "Marcita"},
        {"id": 7, "nombre": "Estelita"},
        {"id": 8, "nombre": "Fulanita"},
        {"id": 9, "nombre": "Menganita"}]

    Relacion_amistad = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3),
                        (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

    general = []
    conections = len(usuarios)
    amounConections = 0
    for i in range(len(usuarios)):
        local = []
        for j in range(len(Relacion_amistad)):
            if usuarios[i]["id"] == Relacion_amistad[j][0]:
                local.append(Relacion_amistad[j][1])
                amounConections += 1
            elif usuarios[i]["id"] == Relacion_amistad[j][1]:
                local.append(Relacion_amistad[j][0])
                amounConections += 1
        general.append(local)
    # print(general)
    # print(conections)

    for i in range(len(general)):
        for j in range(len(general[i])):
            for user in range(len(usuarios)):
                if general[i][j] == usuarios[user]["id"]:
                    general[i][j] = usuarios[user]["nombre"]

    for i in range(len(usuarios)):
        for j in range(len(general)):
            usuarios[i]["amigos"] = general[i]

    # [nombre["nombre"] for nombre in range (len(usuarios)) for key, value in usuarios[nombre].items() for y in range (len(Relacion_amistad)) for k in range (len(Relacion_amistad[y])) if Relacion_amistad[y][1] == usuarios[i]["id"]]
    # print(usuarios)

    # Average conections
    average = amounConections // conections
    print(f"promedio de amistades: {average}")
    # Amount Conections
    print(
        f"Cantidad de conexiones entre personas en total: {amounConections} (tambien se consideran conexiones bilaterales)")
    # Mayor numero de amigos
    print(f"\n\nPersonas con mayor cantidad de amigos\n")
    for i in range(len(usuarios)):
        for j in range(len(general)):
            if len(general[j]) > average and j == usuarios[i]["id"]:
                print(usuarios[i]["nombre"])


if __name__ == "__main__":
    main()
