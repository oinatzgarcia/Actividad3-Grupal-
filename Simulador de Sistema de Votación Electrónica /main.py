import os
import socket
import sys
import hashlib
import rsa


def main():
    # Solicita al votante que introduzca su nombre y dirección IP.
    name = input("Introduzca su nombre: ")
    ip = socket.gethostbyname(socket.gethostname())

    # Genera un par de claves pública/privada para el votante.
    public_key, private_key = rsa.newkeys(2048)

    # Envia la clave pública al servidor.
    public_key_bytes = public_key.save_pkcs1(format="PEM")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(("localhost", 8000))
    server_socket.sendall(public_key_bytes)
    server_socket.close()

    # Presenta al votante una lista de candidatos.
    candidates = ["Candidato 1", "Candidato 2", "Candidato 3"]
    for candidate in candidates:
        print(f"{candidate}")

    # El votante selecciona sus candidatos.
    votes = []
    for i in range(len(candidates)):
        vote = input(f"¿Quiere votar por {candidates[i]}? (S/N): ")
        if vote == "S":
            votes.append(i)

    # Encripta los votos utilizando la clave pública del servidor.
    encrypted_votes = []
    for vote in votes:
        encrypted_vote = public_key.encrypt(vote.encode())
        encrypted_votes.append(encrypted_vote)

    # Envia los votos encriptados al servidor.
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(("localhost", 8000))
    server_socket.sendall(encrypted_votes)
    server_socket.close()

    # Recibe un mensaje de confirmación del servidor.
    confirmation = server_socket.
