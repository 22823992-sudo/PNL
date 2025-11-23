import os
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma


# Rutas
PERSIST_DIR = "db_psico"
NUEVOS_DOCS_DIR = "nuevos_documentos"


def cargar_y_procesar_pdfs(folder_path):
    """Carga y procesa PDFs con validación robusta"""
    
    # 1. Verificar que la carpeta existe
    if not os.path.exists(folder_path):
        print(f"❌ ERROR: La carpeta '{folder_path}' no existe.")
        print(f"   📁 Crea la carpeta con: mkdir {folder_path}")
        return []
    
    # 2. Verificar que es un directorio
    if not os.path.isdir(folder_path):
        print(f"❌ ERROR: '{folder_path}' no es una carpeta.")
        return []
    
    # 3. Listar todos los archivos
    archivos = os.listdir(folder_path)
    print(f"📂 Archivos encontrados en '{folder_path}': {archivos}")
    
    # 4. Filtrar solo PDFs
    pdfs = [f for f in archivos if f.lower().endswith(".pdf")]
    print(f"📄 PDFs detectados: {pdfs}")
    
    if not pdfs:
        print(f"⚠️ No se encontraron archivos PDF en '{folder_path}'")
        return []
    
    # 5. Procesar cada PDF
    docs = []
    for file_name in pdfs:
        file_path = os.path.join(folder_path, file_name)
        print(f"   ⏳ Procesando: {file_name}...")
        
        try:
            loader = PyMuPDFLoader(file_path)
            loaded_docs = loader.load()
            
            # Limpiar contenido
            for d in loaded_docs:
                d.page_content = (
                    d.page_content.replace("\x0c", "")
                                  .replace("  ", " ")
                                  .strip()
                )
                d.metadata["source"] = file_name
            
            docs += loaded_docs
            print(f"   ✅ {file_name}: {len(loaded_docs)} páginas cargadas")
            
        except Exception as e:
            print(f"   ❌ Error al procesar {file_name}: {e}")
    
    return docs


def chunkear_documentos(docs):
    """Divide documentos en fragmentos"""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=700,
        chunk_overlap=150,
        separators=["\n\n", "\n", ".", " "]
    )
    return splitter.split_documents(docs)


# ====================
# EJECUCIÓN PRINCIPAL
# ====================

print("=" * 60)
print("🔄 AGREGANDO NUEVOS DOCUMENTOS A LA BASE DE DATOS")
print("=" * 60)

# 1. Cargar documentos
print("\n📄 Cargando nuevos documentos...")
docs = cargar_y_procesar_pdfs(NUEVOS_DOCS_DIR)

if not docs:
    print("\n⚠️ No hay documentos nuevos que cargar.")
    print("\n💡 SOLUCIONES:")
    print(f"   1. Verifica que existe la carpeta: {NUEVOS_DOCS_DIR}")
    print(f"   2. Coloca archivos PDF dentro de: {NUEVOS_DOCS_DIR}")
    print(f"   3. Verifica los permisos de lectura")
    exit()

print(f"\n✅ Total de páginas cargadas: {len(docs)}")

# 2. Dividir en chunks
print("\n✂️ Dividiendo en chunks...")
chunks = chunkear_documentos(docs)
print(f"✅ Se crearon {len(chunks)} fragmentos")

# 3. Verificar que existe la BD
if not os.path.exists(PERSIST_DIR):
    print(f"\n❌ ERROR: La base de datos '{PERSIST_DIR}' no existe.")
    print("   Primero debes crear la BD ejecutando: python indexacion.py")
    exit()

# 4. Cargar embeddings
print("\n🧠 Cargando modelo de embeddings...")
embeddings = HuggingFaceEmbeddings(
    model_name='sentence-transformers/all-MiniLM-L12-v2'
)

# 5. Cargar BD existente
print(f"\n📦 Cargando base de datos desde '{PERSIST_DIR}'...")
vectorstore = Chroma(
    embedding_function=embeddings,
    persist_directory=PERSIST_DIR
)

# 6. Agregar en lotes
BATCH_SIZE = 5000
total_chunks = len(chunks)

print(f"\n➕ Agregando {total_chunks} chunks en lotes de {BATCH_SIZE}...")

for i in range(0, total_chunks, BATCH_SIZE):
    batch = chunks[i:i+BATCH_SIZE]
    lote_num = i//BATCH_SIZE + 1
    chunks_hasta = min(i+BATCH_SIZE, total_chunks)
    
    print(f"   📦 Lote {lote_num}: chunks {i+1} a {chunks_hasta}")
    vectorstore.add_documents(batch)

vectorstore.persist()

print("\n" + "=" * 60)
print("✅ DOCUMENTOS AÑADIDOS CORRECTAMENTE")
print("=" * 60)
print(f"📊 Total agregado: {total_chunks} chunks")
print(f"📁 Base de datos: {PERSIST_DIR}")
print("\n💡 Ahora puedes reiniciar la app de Streamlit")