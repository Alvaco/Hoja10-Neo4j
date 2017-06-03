from py2neo import Graph, authenticate, Node, Relationship
authenticate("localhost:7474", "neo4j", "123456")
graph = Graph()

loop = True

while(loop):
    opcion = input("\nMenu:\n 1. Ingresar Doctor\n 2. Ingresar Paciente\n 3. Registrar Visita\n 4. Buscar doctores por especialidad\n 5. Registrar pacientes conocidos\n 6. Registrar doctores conocidos\n 7. Buscar doctores de pacientes conocidos\n 8. Referir a otro doctor\n 9. Salir\n")

    if(opcion == 1):
        sNombre = raw_input("Ingrese el nombre: ")
        sEspecialidad = raw_input("Ingrese la especialidad: ")
        sColegiado = raw_input("Ingrese el numero de colegiado: ")
        sTelefono = raw_input("Ingrese el numero de telefono: ")
        doc = Node("Doctor", nombre=sNombre, especialidad=sEspecialidad, colegiado=sColegiado, telefono=sTelefono)
        graph.create(doc)
    elif(opcion == 2):
        sNombre = raw_input("Ingrese el nombre: ")
        sTelefono = raw_input("Ingrese el numero de telefono: ")
        p = Node("Paciente", nombre=sNombre, telefono=sNombre)
        graph.create(p)
    elif(opcion == 3):
        sNombre = raw_input("Ingrese el nombre del paciente: ")
        p = graph.find_one("Paciente", "nombre", sNombre)
        sNombre = raw_input("Ingrese el nombre del doctor: ")
        doc = graph.find_one("Doctor", "nombre", sNombre)
        sFecha = raw_input("Ingrese la fecha de la visita: ")
        visita = Relationship(p, "VISITS", doc, fecha=sFecha)
        sNombre = raw_input("Ingrese el nombre de la medicina: ")
        sDesdeFecha = raw_input("Ingrese el dia que inicia el tratamiento: ")
        sHastaFecha = raw_input("Ingrese el dia que finaliza el tratamiento: ")
        sDosis = raw_input("Ingrese la dosis: ")
        paracetamol = Node("Medicina", nombre=sNombre, desdeFecha=sDesdeFecha, hastaFecha=sHastaFecha, dosis=sDosis)
        graph.create(paracetamol)
        toma = Relationship(p, "TAKES", paracetamol)
        prescribe = Relationship(doc, "PRESCRIBES", paracetamol)
        graph.create(visita)
        graph.create(toma)
        graph.create(prescribe)
    elif(opcion == 4):
        sEspecialidad = raw_input("Ingrese la especialidad: ")
        docs = graph.find("Doctor", "especialidad", sEspecialidad)
        for doc in docs:
            print(doc.properties["nombre"])
    elif(opcion == 5):
        sNombre = raw_input("Ingrese el numero del primer paciente: ")
        p = graph.find_one("Paciente", "nombre", sNombre)
        sNombre = raw_input("Ingrese el numero del segundo paciente: ")
        p2 = graph.find_one("Paciente", "nombre", sNombre)
        conoce = Relationship(p, "KNOWS", p2)
        graph.create(conoce)
    elif(opcion == 6):
        sNombre = raw_input("Ingrese el numero del primer doctor: ")
        doc = graph.find_one("Doctor", "nombre", sNombre)
        sNombre = raw_input("Ingrese el numero del segundo doctor: ")
        doc2 = graph.find_one("Doctor", "nombre", sNombre)
        conoce = Relationship(doc, "KNOWS", doc2)
        graph.create(conoce)
    elif(opcion == 7):
        sNombre = raw_input("Ingrese el nombre del paciente que realizara la busqueda: ")
        p = graph.find_one("Paciente", "nombre", sNombre)
        sEspecialidad = raw_input("Ingrese la especialidad del doctor que desea: ")
        conocidos = graph.match(start_node=p, rel_type="KNOWS", bidirectional=True)
        listaDocs = [""]
        for p2 in conocidos:
            docs = graph.match(start_node=p2.end_node(), rel_type="VISITS")
            for doc in docs:
                if(doc.end_node().properties["especialidad"] == sEspecialidad and doc.end_node().properties["nombre"] not in listaDocs):
                    
                    listaDocs.insert(0, doc.end_node().properties["nombre"])
            conocidos2 = graph.match(start_node=p2.end_node(), rel_type="KNOWS", bidirectional=True)
            for p3 in conocidos2:
                docs2 = graph.match(start_node=p3.end_node(), rel_type="VISITS")
                for doc2 in docs2:
                    if(doc2.end_node().properties["especialidad"] == sEspecialidad and doc2.end_node().properties["nombre"] not in listaDocs):
                        listaDocs.insert(0, doc2.end_node().properties["nombre"])
        if(len(listaDocs) > 0):
            print "\nDoctores encontrados:"
            for p in listaDocs: print p
        else:
            print "No se encontro ningun doctor que cumpliera con los requesitos."
    elif(opcion == 8):
        sNombre = raw_input("Ingrese el nombre del doctor que realizara la busqueda: ")
        doc = graph.find_one("Doctor", "nombre", sNombre)
        sEspecialidad = raw_input("Ingrese la especialidad del doctor que desea: ")
        conocidos = graph.match(start_node=doc, rel_type="KNOWS", bidirectional=True)
        listaDocs = [""]
        for doc2 in conocidos:
            if(doc2.end_node().properties["especialidad"] == sEspecialidad and doc2.end_node().properties["nombre"] not in listaDocs):
                listaDocs.insert(0, doc2.end_node().properties["nombre"])

            conocidos2 = graph.match(start_node=doc2.end_node(), rel_type="KNOWS", bidirectional=True)
            for doc3 in conocidos2:
                if(doc3.end_node().properties["especialidad"] == sEspecialidad and doc3.end_node().properties["nombre"] not in listaDocs):
                    listaDocs.insert(0, doc3.end_node().properties["nombre"])
        if(len(listaDocs) > 0):
            print "\nDoctores encontrados:"
            for p in listaDocs: print p
        else:
            print "No se encontro ningun doctor que cumpliera con los requesitos."
    elif(opcion == 9):
        loop = False
