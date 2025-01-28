# !/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Yeray Otero Mato'


# Librerías importadas
import juego
import pokemons

# Programa principal
print("\nVamos a tener una lucha Pokémon!")

pokemon_atacado = pokemons.bulbasur
pokemon_atacante = pokemons.charmander

while pokemon_atacado.get("vitalidad_actual") > 0:
    
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
            print(f"Errorr: {e}")
            
    # Atacar
    if menu == 1:
        while True:
            print(
f"""\nEscoja uno de los cuatro ataques:

1. {pokemon_atacante.get("ataques")[0].get("nombre")}
2. {pokemon_atacante.get("ataques")[1].get("nombre")}
3. {pokemon_atacante.get("ataques")[2].get("nombre")}
4. {pokemon_atacante.get("ataques")[3].get("nombre")}""")

            ataque_control = True
            while ataque_control:
                try:
                    ataque = int(input(">"))
                    ataque_control = False
                except ValueError as e:
                    print(f"Error: {e}")
            if ataque == 1:
                comprobacion_ataque = juego.comprobacion_ataques(ataque, pokemon_atacante) # Diccionario que se pasará a juego.danho_ataque
                if comprobacion_ataque:
                    danho = juego.danho_ataque(pokemon_atacante, comprobacion_ataque, pokemon_atacado)
                    mostrar = juego.mostrar_tras_ataque(pokemon_atacado, danho)
                    if mostrar:
                        break
                else:
                    print("No quedan movimientos de este ataque!")
            elif ataque == 2:
                comprobacion_ataque = juego.comprobacion_ataques(ataque, pokemon_atacante) # Diccionario que se pasará a juego.danho_ataque
                if comprobacion_ataque:
                    danho = juego.danho_ataque(pokemon_atacante, comprobacion_ataque, pokemon_atacado)
                    mostrar = juego.mostrar_tras_ataque(pokemon_atacado, danho)
                    if mostrar:
                        break
                else:
                    print("No quedan movimientos de este ataque!")
            elif ataque == 3:
                comprobacion_ataque = juego.comprobacion_ataques(ataque, pokemon_atacante) # Diccionario que se pasará a juego.danho_ataque
                if comprobacion_ataque:
                    danho = juego.danho_ataque(pokemon_atacante, comprobacion_ataque, pokemon_atacado)
                    mostrar = juego.mostrar_tras_ataque(pokemon_atacado, danho)
                    if mostrar:
                        break
                else:
                    print("No quedan movimientos de este ataque!")
            elif ataque == 4:
                comprobacion_ataque = juego.comprobacion_ataques(ataque, pokemon_atacante) # Diccionario que se pasará a juego.danho_ataque
                if comprobacion_ataque:
                    danho = juego.danho_ataque(pokemon_atacante, comprobacion_ataque, pokemon_atacado)
                    mostrar = juego.mostrar_tras_ataque(pokemon_atacado, danho)
                    if mostrar:
                        break
                else:
                    print("No quedan movimientos de este ataque!")
            else:
                print("\nDebe elegir un número válido (entre 1 y 4).\n")
    
    # Revisar los ataques restantes (PP)
    elif menu == 2:
        print(f"""
1. {pokemon_atacante.get("ataques")[0].get("nombre")} - {pokemon_atacante.get("ataques")[0].get("movimientos_restantes")} PP restantes
2. {pokemon_atacante.get("ataques")[1].get("nombre")} - {pokemon_atacante.get("ataques")[1].get("movimientos_restantes")} PP restantes
3. {pokemon_atacante.get("ataques")[2].get("nombre")} - {pokemon_atacante.get("ataques")[2].get("movimientos_restantes")} PP restantes
4. {pokemon_atacante.get("ataques")[3].get("nombre")} - {pokemon_atacante.get("ataques")[3].get("movimientos_restantes")} PP restantes""")
    
    # Ver las estadísticas de los pokémon combatientes
    elif menu == 3:
        print(f"""\nA {pokemon_atacante.get("nombre")} le quedan {pokemon_atacante.get("vitalidad_actual")} puntos de vida.
Al contrincante {pokemon_atacado.get("nombre")} le quedan {pokemon_atacado.get("vitalidad_actual")} puntos de vida.""")
    
    # Ver las interacciones de los tipos (debilidades/fortalezas)
    elif menu == 4:
        print("") # Para que se vea mais bonito
        for key, value in juego.debilidades.items():
            print(f"{key} es débil contra: {value}")
    
    else:
        print("Debe elegir un número válido (entre 1 y 4).\n")