import os
import streamlit as st
from github import Github, GithubException, UnknownObjectException

from mono_b64 import MONO_DATA_URI
from styles import apply_styles
from utils import download_button
from ejercicios_python import EJERCICIOS

# Maximum allowed upload size (10 MB)
MAX_UPLOAD_BYTES = 10 * 1024 * 1024

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(page_title="Ferran", page_icon="📚", layout="centered")
apply_styles()

# ── Session state ─────────────────────────────────────────────────────────────
if "seccion" not in st.session_state:
    st.session_state.seccion = None

# ── Helper: upload a file to GitHub ──────────────────────────────────────────
def sanitize_filename(name: str) -> str:
    """Devuelve solo el nombre base del archivo eliminando separadores de ruta."""
    return os.path.basename(name).replace("..", "").strip()


def upload_to_github(file_bytes: bytes, file_name: str) -> bool:
    """Sube un archivo a la carpeta 'recién subidos' del repositorio de GitHub.

    Devuelve True si el upload fue exitoso, False si ocurrió un error.
    """
    safe_name = sanitize_filename(file_name)
    if not safe_name:
        st.error("Nombre de archivo inválido.")
        return False
    try:
        token = st.secrets["github"]["token"]
        repo_name = st.secrets["github"]["repo"]
        g = Github(token)
        repo = g.get_repo(repo_name)
        path = f"recién subidos/{safe_name}"
        try:
            existing = repo.get_contents(path)
            repo.update_file(
                path=path,
                message=f"Actualizar {safe_name}",
                content=file_bytes,
                sha=existing.sha,
            )
        except UnknownObjectException:
            # File doesn't exist yet — create it
            repo.create_file(
                path=path,
                message=f"Agregar {safe_name}",
                content=file_bytes,
            )
        return True
    except GithubException as exc:
        st.error(f"Error de GitHub al subir '{safe_name}': {exc.data.get('message', exc)}")
        return False
    except Exception as exc:
        st.error(f"Error inesperado al subir el archivo: {exc}")
        return False


# ── Helper: list files in 'recién subidos' ────────────────────────────────────
def list_recent_uploads():
    """Obtiene la lista de archivos en la carpeta 'recién subidos' de GitHub."""
    try:
        token = st.secrets["github"]["token"]
        repo_name = st.secrets["github"]["repo"]
        g = Github(token)
        repo = g.get_repo(repo_name)
        contents = repo.get_contents("recién subidos")
        return contents if isinstance(contents, list) else [contents]
    except UnknownObjectException:
        # Folder does not exist yet — treat as empty
        return []
    except GithubException as exc:
        st.warning(f"No se pudo acceder a la carpeta 'recién subidos': {exc.data.get('message', exc)}")
        return []
    except Exception as exc:
        st.error(f"Error inesperado al acceder a los archivos: {exc}")
        return []


# ── 1. Imagen de Fido Dido ────────────────────────────────────────────────────
st.image(MONO_DATA_URI, use_column_width=True)

st.title("📚 Ferran — Recursos Académicos")
st.markdown("---")

# ── 2. Subir archivos a 'recién subidos' ──────────────────────────────────────
st.subheader("⬆️ Subir archivo al repositorio")
uploaded_file = st.file_uploader(
    "Selecciona un archivo para subir a la carpeta *recién subidos*",
    type=None,
    help="El archivo se guardará en la carpeta 'recién subidos' del repositorio de GitHub.",
)
if uploaded_file is not None:
    if uploaded_file.size > MAX_UPLOAD_BYTES:
        st.error(
            f"El archivo supera el tamaño máximo permitido "
            f"({MAX_UPLOAD_BYTES // (1024 * 1024)} MB)."
        )
    elif st.button("📤 Confirmar subida", key="btn_subir"):
        file_bytes = uploaded_file.read()
        if upload_to_github(file_bytes, uploaded_file.name):
            st.success(f"✅ '{uploaded_file.name}' subido correctamente.")

st.markdown("---")

# ── 3. Los 4 botones originales ───────────────────────────────────────────────
st.subheader("📂 Secciones")
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("📘 ICS111\nAdm. Empresas", key="btn_ics111"):
        st.session_state.seccion = "ics111"

with col2:
    if st.button("📗 ICS161\nIntro. Economía", key="btn_ics161"):
        st.session_state.seccion = "ics161"

with col3:
    if st.button("📐 MATE10\nÁlgebra", key="btn_mate10"):
        st.session_state.seccion = "mate10"

with col4:
    if st.button("🐍 Ejercicios\nPython", key="btn_python"):
        st.session_state.seccion = "python"

# ── Renderizar la sección seleccionada ────────────────────────────────────────
PDF_PATHS = {
    "ics111": ("pdfs/ics111_administracion_empresas.pdf", "ics111_administracion_empresas.pdf"),
    "ics161": ("pdfs/ics161_introduccion_economia.pdf", "ics161_introduccion_economia.pdf"),
    "mate10": ("pdfs/mate10_algebra_geometria.pdf", "mate10_algebra_geometria.pdf"),
}

if st.session_state.seccion in PDF_PATHS:
    path, name = PDF_PATHS[st.session_state.seccion]
    st.markdown(f"### {name}")
    download_button(path, name)

elif st.session_state.seccion == "python":
    st.markdown("### 🐍 Ejercicios Python")
    for categoria in EJERCICIOS:
        with st.expander(f"{categoria['icono']} {categoria['categoria']}"):
            for ej in categoria["ejercicios"]:
                st.markdown(f"**[{ej['titulo']}]({ej['url']})**")
                st.info(ej["enunciado"])
                if ej.get("ejemplo"):
                    st.code(ej["ejemplo"], language="text")
                st.code(ej["codigo"], language="python")
                st.markdown("---")

st.markdown("---")

# ── 4. Botón 'Ver Recién Subidos' ─────────────────────────────────────────────
if st.button("🗂️ Ver Recién Subidos", key="btn_recientes"):
    st.session_state.seccion = "recientes"

if st.session_state.seccion == "recientes":
    st.subheader("📥 Archivos subidos recientemente")
    archivos = list_recent_uploads()
    if archivos:
        for archivo in archivos:
            col_a, col_b = st.columns([3, 1])
            with col_a:
                st.markdown(f"📄 **{archivo.name}**")
            with col_b:
                st.download_button(
                    label="⬇️ Descargar",
                    data=archivo.decoded_content,
                    file_name=archivo.name,
                    key=f"dl_{archivo.sha}",
                )
    else:
        st.info("No hay archivos en la carpeta 'recién subidos' todavía.")
