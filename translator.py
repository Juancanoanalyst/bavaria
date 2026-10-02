from deep_translator import GoogleTranslator
import json

# Archivo
archivo = '/home/jpcano/Bavaria/parte 1/parte 1.ipynb'

# Leer notebook
with open(archivo, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

# Traducir
traductor = GoogleTranslator(source='es', target='en')
print("Traduciendo...")

for celda in notebook['cells']:
    if celda['cell_type'] == 'markdown':  # Solo celdas markdown
        texto_original = ''.join(celda['source'])
        
        # Traducir
        try:
            texto_traducido = traductor.translate(texto_original)
            # Agregar traducción debajo
            celda['source'] = [
                texto_original + '\n\n',
                '---\n\n',
                '**English:**\n\n',
                texto_traducido
            ]
            print("✅ Celda traducida")
        except:
            print("⚠️ Celda omitida (muy corta o vacía)")

# Guardar
salida = 'parte 1_bilingue.ipynb'
with open(salida, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, ensure_ascii=False, indent=2)

print(f"\n🎉 Listo! Archivo guardado: {salida}")