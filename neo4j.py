# neo4j.py
# Algoritmos y Estructura de Datos - Seccion 10
# Christopher Sandoval 13660
# Maria Fernanda Estrada 14198
# Ana Lucia Diaz
# Alejandro Vasquez
# Hoja de trabajo 10 - 2 de junio del 2017





# Importando neo4j
from py2neo import Graph, authenticate, Node, Relationship
authenticate("localhost:7474", "neo4j", "123456")
graph = Graph()

#graph.delete_all()
loop = True

# Mostrar el menu hasta que se desea salir
while(loop):
    opcion = input("\nMenu:\n 1. Ingresar Doctor\n 2. Ingresar Paciente\n 3. Registrar Visita\n 4. Buscar doctores por especialidad\n 5. Registrar pacientes conocidos\n 6. Registrar doctores conocidos\n 7. Buscar doctor por conocidos\n 8. Salir\n")

	# Para ingresar un doctor
    if(opcion == 1):
        sNombre = raw_input("Ingrese el nombre: ")
        sEspecialidad = raw_input("Ingrese la especialidad: ")
        sColegiado = raw_input("Ingrese el numero de colegiado: ")
        sTelefono = raw_input("Ingrese el numero de telefono: ")
        doc = Node("Doctor", nombre=sNombre, especialidad=sEspecialidad, colegiado=sColegiado, telefono=sTelefono)
        graph.create(doc)
	
	# Para ingresar un paciente
    elif(opcion == 2):
        sNombre = raw_input("Ingrese el nombre: ")
        sTelefono = raw_input("Ingrese el numero de telefono: ")
        p = Node("Paciente", nombre=sNombre, telefono=sNombre)
        graph.create(p)
	
	# Para registrar una visita
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
	
	# Para buscar doctores por especialidad
    elif(opcion == 4):
        sEspecialidad = raw_input("Ingrese la especialidad: ")
        docs = graph.find("Doctor", "especialidad", sEspecialidad)
        for doc in docs:
            print(doc.properties["nombre"])
	
	# Para registrar pacientes conocidos
    elif(opcion == 5):
        sNombre = raw_input("Ingrese el numero del primer paciente: ")
        p = graph.find_one("Paciente", "nombre", sNombre)
        sNombre = raw_input("Ingrese el numero del segundo paciente: ")
        p2 = graph.find_one("Paciente", "nombre", sNombre)
        conoce = Relationship(p, "KNOWS", p2)
        graph.create(conoce)
		
	# Para registrar doctores conocidos
    elif(opcion == 6):
        sNombre = raw_input("Ingrese el numero del primer doctor: ")
        doc = graph.find_one("Doctor", "nombre", sNombre)
        sNombre = raw_input("Ingrese el numero del segundo doctor: ")
        doc2 = graph.find_one("Doctor", "nombre", sNombre)
        conoce = Relationship(doc, "KNOWS", doc2)
        graph.create(conoce)
	
	# Para buscar doctor por conocidos
    elif(opcion == 7):
        sNombre = raw_input("Ingrese el nombre del paciente que realizara la busqueda: ")
        p = graph.find_one("Paciente", "nombre", sNombre)
        sEspecialidad = raw_input("Ingrese la especialidad del doctor que desea: ")
        for rel in graph.match(start_node=p, rel_type="KNOWS"):
            print(rel.hydrate(graph.))
        #conocidos = graph.match(start_node=p, rel_type="KNOWS", bidirectional=True)
        #for p2 in conocidos:
        #    docs = graph.match(start_node=p2.end_node, rel_type="VISITS", bidirectional=True)
        #    for doc in docs:
        #        if(doc.end_node.properties("especialidad") == sEspecialidad):
        #            print(doc.properties("nombre"))
        ##    conocidos2 = graph.match(start_node=p2, rel_type="KNOWS", bidirectional=True)
        #    for p3 in conocidos2:
        #        docs2 = graph.match(start_node=p3, rel_type="VISITS", bidirectional=True)
        #        for doc2 in docs2:
        #            if(doc2.properties("especialidad") == sEspecialidad):
        #                print(doc2.properties("nombre"))
	
	# Para salir del programa
    elif(opcion == 8):
        loop = False
