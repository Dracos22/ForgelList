# USAGE
```
python3 Forgelist.py  --help
```


```

   ███████  ██████  ██████   ██████  ███████ ██      ██ ███████ ████████ 
   ██      ██    ██ ██   ██ ██       ██      ██      ██ ██         ██    
   █████   ██    ██ ██████  ██   ███ █████   ██      ██ ███████    ██    
   ██      ██    ██ ██   ██ ██    ██ ██      ██      ██      ██    ██    
   ██       ██████  ██   ██  ██████  ███████ ███████ ██ ███████    ██    
                                                                      
                                                                     
                [ ForgeList | Wordlist Combiner  ]    
    
usage: Forgelist.py [-h] [-r] [-o OUTPUT] [-n NAME] archivo [archivo ...]

🧩 ForgeList - Fusiona múltiples archivos .txt en uno solo para fuerza bruta, OSINT o testing.

positional arguments:
  archivo              Archivos .txt a combinar

options:
  -h, --help           show this help message and exit
  -r, --random         Mezclar las líneas de forma aleatoria
  -o, --output OUTPUT  Ruta de salida del archivo combinado (por defecto: carpeta actual)
  -n, --name NAME      Nombre del archivo final (por defecto: combined_wordlist.txt)
```

```
python3 Forgelist.py  file1.txt file2.txt -r -o /ruta/ -n File_name.txt
```
