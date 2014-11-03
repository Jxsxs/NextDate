# -*- coding: utf-8 -*-
from lettuce import step, world
import sys
sys.path.append('../')
from NextDate1 import NextDate1

@step(u'Given: la fecha dada es mes "([^"]*)", dia "([^"]*)" y year "([^"]*)"')
def given_la_group1_dada_es_mes_group2_dia_group3_y_year_group4(step,mes, dia, year):
   	world.par = [int(mes),int(dia),int(year)]
   	
@step(u'When: realizo el calculo')
def when_realizo_el_calculo(step):
    date = NextDate1(world.par)
    world.date = date.Date()

@step(u'Then: el resultado es "([^"]*)"')
def then_el_resultado_es_group1(step, fecha):
    assert world.date == fecha, 'Fecha calculada {0}, Fecha esperada {1}'.format(world.date,fecha)
