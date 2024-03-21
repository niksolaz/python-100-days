from PIL import Image
import os

def convert_images_to_webp(source_folder):
    # Estensioni dei file da convertire
    extensions = ('.png', '.jpeg', '.jpg', '.tiff')
    
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.endswith(extensions):
                # Percorso completo del file
                full_path = os.path.join(root, file)
                # Nome del file senza estensione
                filename_without_extension = os.path.splitext(full_path)[0]
                # Percorso del nuovo file con estensione .webp
                new_file_path = filename_without_extension + '.webp'
                
                try:
                    # Apertura e conversione dell'immagine
                    with Image.open(full_path) as img:
                        img.convert('RGB').save(new_file_path, 'webp')
                    print(f'Convertito: {full_path} a {new_file_path}')
                except Exception as e:
                    print(f'Errore nella conversione di {full_path}: {e}')

# Percorso della cartella contenente le immagini da convertire
source_folder = input("inserisci il percorso della cartella contenente le immagini da convertire: ")
convert_images_to_webp(source_folder)
