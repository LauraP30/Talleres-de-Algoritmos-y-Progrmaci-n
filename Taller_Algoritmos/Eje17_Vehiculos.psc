Algoritmo Inicio_Vehiculos
	Escribir "Digite la distancia en km entre los vehiculos"
	Leer d
	Escribir "Digite las velocidades en km/h de los vehiculos"
	Leer v1, v2
	dv<-v2-v1
	t<-d/dv
	m<-t*60
	Escribir "El tiempo en que lo alcanzara es " m " min"
FinAlgoritmo
