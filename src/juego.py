# !/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Yeray Otero Mato'


# Librerías importadas
from utils import is_dict
from pokemons import tipos
from random import randint
from time import sleep

# Debilidades. El tipo Normal no es debil ni fuerte contro nada
debilidades = {
    # Planta       Fuego
    tipos.get(1) : tipos.get(2),
    # Fuego        Agua
    tipos.get(2) : tipos.get(3),
    # Agua         Planta
    tipos.get(3) : tipos.get(1),
}

# Funciones
def danho_ataque(pokemon_atacante, ataque, pokemon_atacado):
    """Función que realiza un ataque de un pokémon a otro.

    Args:
        pokemon_atacante (dict): datos del pokémon atacante.
        ataque (dict): datos del ataque realizado.
        pokemon_atacado (dict): datos del pokémon que recibe el ataque.

    Raises:
        ValueError: si el pokémon atacante, el pokémon atacado o el ataque no son diccionarios.

    Returns:
        int or False: el daño aplicado o False si el ataque no supera los 0 de daño.
    """
    if not (is_dict(pokemon_atacante)) or not (is_dict(ataque)) or not (is_dict(pokemon_atacado)):
        raise ValueError("El dato introducido no fue el esperado.")
    
    tipo_ataque = ataque.get("tipo")
    tipo_defensor = pokemon_atacado.get("tipo")
    nivel_atacante = pokemon_atacante.get("nivel")
    
    if tipo_ataque == debilidades.get(tipo_defensor):
        poder_ataque = ataque.get("poder") * 2
    else:
        poder_ataque = ataque.get("poder")
    
    if tipo_ataque == pokemon_atacante.get("tipo"):
        poder_ataque *= 1.5 # STAB
    
    # Random
    aleatorizador = randint(-5, 5)
    poder_ataque += aleatorizador
    
    poder_ataque = max(poder_ataque, 0) # Devuelve o bien el `poder_ataque` si es mayor a 0 o `0` si el daño es negativo.
    
    danho_total = (((nivel_atacante * ((2/5) + 2)) * poder_ataque) / 50) + 2 # Fórmula sacada de internet.
    
    if danho_total > 0:
        pokemon_atacado["vitalidad_actual"] -= danho_total
        return danho_total # No hace falta devolver `pokemon_atacado["vitalidad_actual"]` ya que los diccionarios son mutables.
    else:
        return False # Devuelve False para poner por pantalla que el ataque ha fallado.

def comprobacion_ataques(ataque, pokemon_atacante):
    """Comprueba si quedan o no ataques restantes, devolviendo el dicccionario del ataque seleccionado y restando un movimiento.

    Args:
        ataque (int): número del ataque, introducido por el jugador.
        pokemon_atacante (dict): diccionario con la información del pokémon atacante.

    Returns:
        dict or False: dict si el ataque tiene movimientos (para pasárselo a danho_ataque) o False si no quedan movimientos en el ataque.
    """
    ataque -= 1 # El usuario introduce el ataque del 1 al 4 pero los índices son del 0 al 3.
    if pokemon_atacante.get("ataques")[ataque].get("movimientos_restantes") > 0:
        pokemon_atacante["ataques"][ataque]["movimientos_restantes"] -= 1 # Resto el movimiento de este turno. Si falla también se resta.
        return pokemon_atacante.get("ataques")[ataque]
    else:
        return False

def mostrar_tras_ataque(pokemon_atacado, daho, pokemon_atacando):
    if pokemon_atacado.get("vitalidad_actual") <= 0:
        sleep(2)
        print(f"\nSe ha inflingido un daño total de {daho:.2f} a {pokemon_atacado.get("nombre")}.")
        sleep(7)
        print(f"\n{pokemon_atacado.get("nombre")} ha caído debilitado!")
        sleep(3)
        print(f"\n{pokemon_atacando.get("nombre")} ha ganado el combate!")
        return True
    elif daho:
        sleep(2)
        print(f"\nSe ha inflingido un daño total de {daho:.2f} a {pokemon_atacado.get("nombre")}.")
        sleep(2)
        print(f"Su vitalidad restante es de {pokemon_atacado.get("vitalidad_actual"):.2f} puntos de vida.")
        sleep(3)
        return True
    else:
        sleep(2)
        print("\nEl ataque ha fallado!")
        sleep(2)
        return True