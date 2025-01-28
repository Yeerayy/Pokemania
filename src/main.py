# !/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Yeray Otero Mato'


# Librerías importadas
import juego
import pokemons
from random import randint
from time import sleep

# Programa principal
print("\nVamos a tener una lucha Pokémon!")

print("\nSeleccione el pokémon con el que desea combatir:\n1) Charmander\n2) Bulbasur\n3) Squirtle")
while True:
    opcion = int(input(">"))
    if opcion == 1:
        pokemon_jugador = pokemons.charmander
        pokemon_ia = pokemons.squirtle
        pokemon_jugador["max_vitalidad"] = pokemon_jugador["nivel"] * 2
        pokemon_jugador["vitalidad_actual"] = pokemon_jugador.get("max_vitalidad")
        pokemon_ia["max_vitalidad"] = pokemon_ia["nivel"] * 2
        pokemon_ia["vitalidad_actual"] = pokemon_ia.get("max_vitalidad")
        print(f"\nHas escogido a Charmander!\n(Nivel {pokemon_jugador.get("nivel")})")
        sleep(2)
        print(f"Tu rival será Squirtle.\n(Nivel {pokemon_ia.get("nivel")})")
        sleep(2)
        break
    elif opcion == 2:
        pokemon_jugador = pokemons.bulbasur
        pokemon_ia = pokemons.charmander
        pokemon_jugador["max_vitalidad"] = pokemon_jugador["nivel"] * 2
        pokemon_jugador["vitalidad_actual"] = pokemon_jugador.get("max_vitalidad")
        pokemon_ia["max_vitalidad"] = pokemon_ia["nivel"] * 2
        pokemon_ia["vitalidad_actual"] = pokemon_ia.get("max_vitalidad")
        print(f"\nHas escogido a Bulbasur!\n(Nivel {pokemon_jugador.get("nivel")})")
        sleep(2)
        print(f"Tu rival será Charmander.\n(Nivel {pokemon_ia.get("nivel")})")
        sleep(2)
        break
    elif opcion == 3:
        pokemon_jugador = pokemons.squirtle
        pokemon_ia = pokemons.bulbasur
        pokemon_jugador["max_vitalidad"] = pokemon_jugador["nivel"] * 2
        pokemon_jugador["vitalidad_actual"] = pokemon_jugador.get("max_vitalidad")
        pokemon_ia["max_vitalidad"] = pokemon_ia["nivel"] * 2
        pokemon_ia["vitalidad_actual"] = pokemon_ia.get("max_vitalidad")
        print(f"\nHas escogido a Squirtle!\n(Nivel {pokemon_jugador.get("nivel")})")
        sleep(2)
        print(f"Tu rival será Bulbasur.\n(Nivel {pokemon_ia.get("nivel")})")
        sleep(2)
        break
    else:
        print("\nOpción inválida. Inténtelo otra vez.")

while pokemon_ia.get("vitalidad_actual") > 0: # Atacando
    if pokemon_jugador.get("vitalidad_actual") <= 0:
        break
    
    # Primer menú
    print(
f"""\nQué quieres hacer?

1. Atacar
2. Revisar ataques restantes (PP)
3. Ver la vida restante de los pokémons
4. Ver las interacciones de los tipos (debilidades/fortalezas)""")
    
    menu_control = True
    while menu_control:
        try:
            menu = int(input(">"))
            menu_control = False
        except ValueError as e:
            print(f"Error: {e}")
            
    # Atacar
    if menu == 1:
        while True:
            print(
f"""\nEscoja uno de los cuatro ataques:

1. {pokemon_jugador.get("ataques")[0].get("nombre")}
2. {pokemon_jugador.get("ataques")[1].get("nombre")}
3. {pokemon_jugador.get("ataques")[2].get("nombre")}
4. {pokemon_jugador.get("ataques")[3].get("nombre")}""")

            ataque_control = True
            while ataque_control:
                try:
                    ataque = int(input(">"))
                    ataque_control = False
                except ValueError as e:
                    print(f"Error: {e}")
            if ataque == 1:
                comprobacion_ataque = juego.comprobacion_ataques(ataque, pokemon_jugador) # Diccionario que se pasará a juego.danho_ataque
                if comprobacion_ataque:
                    danho = juego.danho_ataque(pokemon_jugador, comprobacion_ataque, pokemon_ia)
                    sleep(2)
                    print(f"\n{pokemon_jugador.get("nombre")} ha utilizado el ataque {pokemon_jugador.get("ataques")[0].get("nombre")}!")
                    sleep(1)
                    mostrar = juego.mostrar_tras_ataque(pokemon_ia, danho, pokemon_jugador)
                    if mostrar:
                        break
                else:
                    print("No quedan movimientos de este ataque!")
            elif ataque == 2:
                comprobacion_ataque = juego.comprobacion_ataques(ataque, pokemon_jugador) # Diccionario que se pasará a juego.danho_ataque
                if comprobacion_ataque:
                    danho = juego.danho_ataque(pokemon_jugador, comprobacion_ataque, pokemon_ia)
                    sleep(2)
                    print(f"\n{pokemon_jugador.get("nombre")} ha utilizado el ataque {pokemon_jugador.get("ataques")[1].get("nombre")}!")
                    sleep(1)
                    mostrar = juego.mostrar_tras_ataque(pokemon_ia, danho, pokemon_jugador)
                    if mostrar:
                        break
                else:
                    print("No quedan movimientos de este ataque!")
            elif ataque == 3:
                comprobacion_ataque = juego.comprobacion_ataques(ataque, pokemon_jugador) # Diccionario que se pasará a juego.danho_ataque
                if comprobacion_ataque:
                    danho = juego.danho_ataque(pokemon_jugador, comprobacion_ataque, pokemon_ia)
                    sleep(2)
                    print(f"\n{pokemon_jugador.get("nombre")} ha utilizado el ataque {pokemon_jugador.get("ataques")[2].get("nombre")}!")
                    sleep(1)
                    mostrar = juego.mostrar_tras_ataque(pokemon_ia, danho, pokemon_jugador)
                    if mostrar:
                        break
                else:
                    print("No quedan movimientos de este ataque!")
            elif ataque == 4:
                comprobacion_ataque = juego.comprobacion_ataques(ataque, pokemon_jugador) # Diccionario que se pasará a juego.danho_ataque
                if comprobacion_ataque:
                    danho = juego.danho_ataque(pokemon_jugador, comprobacion_ataque, pokemon_ia)
                    sleep(2)
                    print(f"\n{pokemon_jugador.get("nombre")} ha utilizado el ataque {pokemon_jugador.get("ataques")[3].get("nombre")}!")
                    sleep(1)
                    mostrar = juego.mostrar_tras_ataque(pokemon_ia, danho, pokemon_jugador)
                    if mostrar:
                        break
                else:
                    print("No quedan movimientos de este ataque!")
            else:
                print("\nDebe elegir un número válido (entre 1 y 4).\n")
                
        while pokemon_jugador.get("vitalidad_actual") > 0: # Ataca a IA
            if pokemon_ia.get("vitalidad_actual") <= 0:
                break
            ataque_ia = randint(1, 4)
            
            if ataque_ia == 1:
                comprobacion_ataque = juego.comprobacion_ataques(ataque, pokemon_ia) # Diccionario que se pasará a juego.danho_ataque
                if comprobacion_ataque:
                    danho = juego.danho_ataque(pokemon_ia, comprobacion_ataque, pokemon_jugador)
                    sleep(5)
                    print(f"\n{pokemon_ia.get("nombre")} ha utilizado el ataque {pokemon_ia.get("ataques")[0].get("nombre")}!")
                    sleep(2)
                    mostrar = juego.mostrar_tras_ataque(pokemon_jugador, danho, pokemon_ia)
                    if mostrar:
                        break
                else:
                    print("No quedan movimientos de este ataque!")
            elif ataque_ia == 2:
                comprobacion_ataque = juego.comprobacion_ataques(ataque, pokemon_ia) # Diccionario que se pasará a juego.danho_ataque
                if comprobacion_ataque:
                    danho = juego.danho_ataque(pokemon_ia, comprobacion_ataque, pokemon_jugador)
                    sleep(5)
                    print(f"\n{pokemon_ia.get("nombre")} ha utilizado el ataque {pokemon_ia.get("ataques")[1].get("nombre")}!")
                    sleep(2)
                    mostrar = juego.mostrar_tras_ataque(pokemon_jugador, danho, pokemon_ia)
                    if mostrar:
                        break
                else:
                    print("No quedan movimientos de este ataque!")
            elif ataque_ia == 3:
                comprobacion_ataque = juego.comprobacion_ataques(ataque, pokemon_ia) # Diccionario que se pasará a juego.danho_ataque
                if comprobacion_ataque:
                    danho = juego.danho_ataque(pokemon_ia, comprobacion_ataque, pokemon_jugador)
                    sleep(5)
                    print(f"\n{pokemon_ia.get("nombre")} ha utilizado el ataque {pokemon_ia.get("ataques")[2].get("nombre")}!")
                    sleep(2)
                    mostrar = juego.mostrar_tras_ataque(pokemon_jugador, danho, pokemon_ia)
                    if mostrar:
                        break
                else:
                    print("No quedan movimientos de este ataque!")
            elif ataque_ia == 4:
                comprobacion_ataque = juego.comprobacion_ataques(ataque, pokemon_ia) # Diccionario que se pasará a juego.danho_ataque
                if comprobacion_ataque:
                    danho = juego.danho_ataque(pokemon_ia, comprobacion_ataque, pokemon_jugador)
                    sleep(5)
                    print(f"\n{pokemon_ia.get("nombre")} ha utilizado el ataque {pokemon_ia.get("ataques")[3].get("nombre")}!")
                    sleep(2)
                    mostrar = juego.mostrar_tras_ataque(pokemon_jugador, danho, pokemon_ia)
                    if mostrar:
                        break
                else:
                    print("No quedan movimientos de este ataque!")
    
    # Revisar os ataques restantes (PP)
    elif menu == 2:
        print(f"""
1. {pokemon_jugador.get("ataques")[0].get("nombre")} - {pokemon_jugador.get("ataques")[0].get("movimientos_restantes")} PP restantes
2. {pokemon_jugador.get("ataques")[1].get("nombre")} - {pokemon_jugador.get("ataques")[1].get("movimientos_restantes")} PP restantes
3. {pokemon_jugador.get("ataques")[2].get("nombre")} - {pokemon_jugador.get("ataques")[2].get("movimientos_restantes")} PP restantes
4. {pokemon_jugador.get("ataques")[3].get("nombre")} - {pokemon_jugador.get("ataques")[3].get("movimientos_restantes")} PP restantes""")
    
    # Ver as estadísticas dos Pokémon combatintes
    elif menu == 3:
        print(f"""\nA {pokemon_jugador.get("nombre")}, de nivel {pokemon_jugador.get("nivel")}, le quedan {pokemon_jugador.get("vitalidad_actual")} puntos de vida.
Al contrincante {pokemon_ia.get("nombre")}, de nivel {pokemon_ia.get("nivel")}, le quedan {pokemon_ia.get("vitalidad_actual")} puntos de vida.""")
    
    # Ver as interaccións dos tipos (debilidades/fortalezas)
    elif menu == 4:
        print("") # Para que se vexa mais bonito
        for key, value in juego.debilidades.items():
            print(f"{key} es débil contra: {value}")
    
    else:
        print("\nDebe elegir un número válido (entre 1 y 4).")