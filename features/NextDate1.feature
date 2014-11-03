Feature: NextDay
	Como usuario del sistema
	Quiero obtener la fecha siguiente a hoy 
	Para estar ubicado

Scenario: La fecha es mes "10", dia "18" y year "2012"
	Given: la fecha dada es mes "10", dia "18" y year "2012"
	When: realizo el calculo
	Then: el resultado es "(10, 19, 2012)"