# !/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Yeray Otero Mato'


# Definición tipos
tipos = {
    1 : "Planta",
    2 : "Fuego",
    3 : "Agua",
    4 : "Normal"
}

# Definición Pokémons
charmander = {
    "nombre" : "Charmander",
    "tipo" : tipos.get(2),
    "nivel" : 20, # Range(1, 99)
    "max_vitalidad" : 100,
    "vitalidad_actual" : 100,
    "ataques" : [
        {
        "nombre" : "Arañazo",
        "tipo" : tipos.get(4),
        "poder" : 5,
        "movimientos_maximos" : 15,
        "movimientos_restantes" : 15
    },
        {
        "nombre" : "Ascuas",
        "tipo" : tipos.get(2),
        "poder" : 15,
        "movimientos_maximos" : 10,
        "movimientos_restantes" : 10
    },
        {
        "nombre" : "Colmillo ígneo",
        "tipo" : tipos.get(2),
        "poder" : 20,
        "movimientos_maximos" : 7,
        "movimientos_restantes" : 7
    },
        {
        "nombre" : "Cuchillada",
        "tipo" : tipos.get(4),
        "poder" : 30,
        "movimientos_maximos" : 5,
        "movimientos_restantes" : 5
    }
    ]
}

bulbasur = {
    "nombre" : "Bulbasur",
    "tipo" : tipos.get(1),
    "nivel" : 20, # Range(1, 99)
    "max_vitalidad" : 100,
    "vitalidad_actual" : 100,
    "ataques" : [
        {
        "nombre" : "Placaje",
        "tipo" : tipos.get(4),
        "poder" : 5,
        "movimientos_maximos" : 15,
        "movimientos_restantes" : 15
    },
        {
        "nombre" : "Látigo cepa",
        "tipo" : tipos.get(1),
        "poder" : 15,
        "movimientos_maximos" : 10,
        "movimientos_restantes" : 10
    },
        {
        "nombre" : "Corte",
        "tipo" : tipos.get(4),
        "poder" : 20,
        "movimientos_maximos" : 7,
        "movimientos_restantes" : 7
    },
        {
        "nombre" : "Hoja afilada",
        "tipo" : tipos.get(1),
        "poder" : 30,
        "movimientos_maximos" : 5,
        "movimientos_restantes" : 5
    }
    ]
}