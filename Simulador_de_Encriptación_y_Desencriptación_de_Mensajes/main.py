# Importing necessary modules
import os  # Module for operating system functionalities
import time  # Module for time-related functions
import pyfiglet  # Module for creating ASCII art from text
import random  # Module for creating random numbers
from simple_term_menu import TerminalMenu  # Module for creating terminal menus

# Function to read a file and return its content as text
def leer_archivo(camino):
    '''
    Reads a file specified by the user and returns its content as text.
    '''
    try:
        with open(camino, 'r') as file:
            texto = file.read()
        return texto
    except FileNotFoundError:
        print("Archivo no encontrado. Por favor, proporciona una ruta de archivo válida.")
        time.sleep(1.5)
        exit()

# Function to retrieve encryption/decryption key
def coger_clave():
    try:
        introducido = input("Introduzca la clave con la que encriptar/desencriptar: ")
        clave = int(introducido)
        return clave
    except ValueError:
        print("Valor inválido. Introduzca un valor válido.")
        time.sleep(1.5)
        exit()

# Function to transform text based on a numerical value
def transformar(texto, clave):
    '''
    Transforms the given text using the provided numerical key.
    '''
    texto_transformado = ""
    for caracter in texto:
        caracter_transformado = chr(ord(caracter) + clave)
        texto_transformado += caracter_transformado 
    print("El texto resultante es: \n", texto_transformado)

# Function displaying the main menu of the program
def main_menu():
    '''
    Displays the main menu and controls program flow based on user input.
    '''
    while True:
        os.system("clear")
        print(pyfiglet.figlet_format("Menu", font="big", justify="center"))
        time.sleep(0.5)
        # Options for all menus
        main_options = ["[1] Encriptar", "[2] Desencriptar", "[3] Salir"]
        encrypt_options = ["[1] Introducir Clave", "[2] Clave aleatoria", "[3] Salir"]
        entry_options = ["[1] Cargar archivo", "[2] Entrada manual", "[3] Salir"]
        terminal_menu = TerminalMenu(main_options)
        terminal_menu_entry_index = terminal_menu.show()
        clave = 1  # Default value for the key
        time.sleep(0.5)  # Adding delay for smoother transition
        if terminal_menu_entry_index == 0: 
            encrypt_menu = TerminalMenu(encrypt_options)
            encrypt_menu_entry_index = encrypt_menu.show()
            time.sleep(0.5)  # Adding delay for smoother transition
            if encrypt_menu_entry_index == 0: 
                clave = coger_clave()  # Retrieves key from user input
            if encrypt_menu_entry_index == 1: 
                clave = random.randint(-50, 50)  # Generates a random key
                print("La clave aleatoria es ", clave)
            if encrypt_menu_entry_index == 2:
                exit() 
        if terminal_menu_entry_index == 1: 
            clave = -1 * coger_clave()  # Inverts the key retrieved from user input
        if terminal_menu_entry_index == 2:
            exit()
        # Entry options display and selection
        entry_menu = TerminalMenu(entry_options)
        entry_menu_entry_index = entry_menu.show()
        time.sleep(0.5)  # Adding delay for smoother transition
        if entry_menu_entry_index == 0:
            camino = input("Introduce el nombre del archivo que contiene el texto a encriptar/desencriptar: ")
            texto = leer_archivo(camino)
            transformar(texto, clave)
            time.sleep(5)
            break
        if entry_menu_entry_index == 1:
            texto = input("Introduce el texto a encriptar/desencriptar: ")
            transformar(texto, clave)
            time.sleep(5)
            break
        if entry_menu_entry_index == 2:
            exit()

# Main function of the program
def main():
    '''
    Executes the main functionality of the program.
    '''
    os.system("clear")
    print(pyfiglet.figlet_format("Euneiz", font="big", justify="center"))
    time.sleep(1.5)
    os.system("clear")
    print(pyfiglet.figlet_format("Proyecto:\nSimulador de Encriptación y Desencriptación de Mensajes", font="big", justify="center", width=100))
    time.sleep(1.5)
    main_menu()

# Program execution
if __name__ == "__main__":
    main()
