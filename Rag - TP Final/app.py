import os
from langchain_community.document_loaders import PyMuPDFLoader

NUEVOS_DOCS_DIR = "nuevos_documentos"

print("=" * 60)
print("🔍 TEST DE LECTURA DE PDFs")
print("=" * 60)

# 1. Verificar carpeta
print(f"\n📁 Verificando carpeta: {NUEVOS_DOCS_DIR}")
if not os.path.exists(NUEVOS_DOCS_DIR):
    print("❌ La carpeta no existe")
    exit()

print("✅ Carpeta existe")

# 2. Listar archivos
archivos = os.listdir(NUEVOS_DOCS_DIR)
print(f"\n📂 Total de archivos: {len(archivos)}")

# 3. Filtrar PDFs
pdfs = [f for f in archivos if f.lower().endswith(".pdf")]
print(f"📄 PDFs encontrados: {len(pdfs)}")

if not pdfs:
    print("❌ No hay PDFs")
    exit()

# 4. Mostrar lista de PDFs
print("\n📋 Lista de PDFs:")
for i, pdf in enumerate(pdfs, 1):
    file_path = os.path.join(NUEVOS_DOCS_DIR, pdf)
    tamaño = os.path.getsize(file_path) / (1024 * 1024)  # MB
    print(f"   {i}. {pdf} ({tamaño:.2f} MB)")

# 5. Probar cargar el PRIMER PDF
print(f"\n⏳ Probando cargar el primer PDF: {pdfs[0]}...")
try:
    file_path = os.path.join(NUEVOS_DOCS_DIR, pdfs[0])
    loader = PyMuPDFLoader(file_path)
    docs = loader.load()
    
    print(f"✅ ¡ÉXITO! Se cargaron {len(docs)} páginas")
    print(f"📝 Primeros 200 caracteres de la página 1:")
    print("-" * 60)
    print(docs[0].page_content[:200])
    print("-" * 60)
    
except Exception as e:
    print(f"❌ ERROR al cargar: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 60)
print("✅ TEST COMPLETADO")
print("=" * 60)