import menu
import controlador

menu_principal = menu.Menu()
op = None
entrada = controlador.cargar_datos('respuestas')
entrada = controlador.eliminar_columnas(entrada, [0,1,2])
agiles,no_agiles = controlador.separar_datos(entrada,'agiles')
estiman,no_estiman = controlador.separar_datos(agiles,'estiman')

while not op:
	menu_principal.limpiar()
	opcion = menu_principal.seleccionar()
	if opcion == 1:
		controlador.graficar(Agilidad=[agiles,no_agiles],Estimacion=[estiman,no_estiman])
	
	
	op = input()	
		
	