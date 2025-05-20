#!/usr/bin/env python3

import argparse
import os
import random
import sys

def mostrar_banner():
    banner = r"""


   ███████  ██████  ██████   ██████  ███████ ██      ██ ███████ ████████ 
   ██      ██    ██ ██   ██ ██       ██      ██      ██ ██         ██    
   █████   ██    ██ ██████  ██   ███ █████   ██      ██ ███████    ██    
   ██      ██    ██ ██   ██ ██    ██ ██      ██      ██      ██    ██    
   ██       ██████  ██   ██  ██████  ███████ ███████ ██ ███████    ██    
                                                                      
                                                                     
                [ ForgeList | Wordlist Combiner  ]    
    """
    print(banner)

def combinar_wordlists(files, output_path, output_name, randomize):
    palabras = []

    for file in files:
        try:
            with open(file, 'r', encoding='utf-8', errors='ignore') as f:
                palabras.extend(f.read().splitlines())
        except FileNotFoundError:
            print(f"❌ Archivo no encontrado: {file}")
            sys.exit(1)

    palabras = list(set(palabras))

    if randomize:
        random.shuffle(palabras)
    else:
        palabras.sort()

    salida_completa = os.path.join(output_path, output_name)
    try:
        with open(salida_completa, 'w', encoding='utf-8') as f:
            for palabra in palabras:
                f.write(palabra + '\n')
        print(f"\n✅ Wordlists combinadas guardadas en: {salida_completa}")
    except Exception as e:
        print(f"❌ Error al escribir el archivo: {e}")
        sys.exit(1)

def main():
    mostrar_banner()

    parser = argparse.ArgumentParser(
        description="🧩 ForgeList - Fusiona múltiples archivos .txt en uno solo para fuerza bruta, OSINT o testing."
    )
    parser.add_argument(
        "files",
        metavar="archivo",
        type=str,
        nargs="+",
        help="Archivos .txt a combinar"
    )
    parser.add_argument(
        "-r", "--random",
        action="store_true",
        help="Mezclar las líneas de forma aleatoria"
    )
    parser.add_argument(
        "-o", "--output",
        default=".",
        help="Ruta de salida del archivo combinado (por defecto: carpeta actual)"
    )
    parser.add_argument(
        "-n", "--name",
        default="combined_wordlist.txt",
        help="Nombre del archivo final (por defecto: combined_wordlist.txt)"
    )

    args = parser.parse_args()
    combinar_wordlists(args.files, args.output, args.name, args.random)

if __name__ == "__main__":
    main()
