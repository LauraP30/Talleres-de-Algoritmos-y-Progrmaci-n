Algoritmo Inicio_Materia_Algoritmos
	Escribir "Digite las 3 notas de los parciales"
	Leer N1, N2, N3
	Escribir "Digite la nota del examen final"
	Leer Ef
	Escribir "Digite la nota del trabajo final"
	Leer Tf
	Np<- (N1+N2+N3)/3
	Nf<- (Np*0.55)+(Ef*0.3)+(Tf*0.15)
	Escribir "La nota final es " Nf
FinAlgoritmo
