Algoritmo Inicio_Vehiculos
	Escribir "Digite la distancia en km entre los dos vehiculos"
	Leer d
	Escribir "Digite las velocidades en km/h de los dos vehiculos"
	Leer v1, v2
	Dv<-v2-v1
	T<-d/Dv
	Min<-T*60
	Escribir "El tiempo en que alcanzara al otro vehiculo es de " Min "min"
FinAlgoritmo
