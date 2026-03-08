import io
import os
import streamlit as st
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload

from mono_b64 import MONO_DATA_URI
from styles import apply_styles
from utils import download_button
from ejercicios_python import EJERCICIOS

# Tamaño máximo permitido: 250 MB
MAX_UPLOAD_BYTES = 250 * 1024 * 1024

DRIVE_SCOPES = ["https://www.googleapis.com/auth/drive"]

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(page_title="Ferran", page_icon="📚", layout="wide")
apply_styles()

# ── Session state ─────────────────────────────────────────────────────────────
if "seccion" not in st.session_state:
    st.session_state.seccion = None

# ── Helper: sanitize filename ────────────────────────────────────────────────
def sanitize_filename(name: str) -> str:
    """Devuelve solo el nombre base del archivo eliminando separadores de ruta."""
    return os.path.basename(name).replace("..", "").strip()

# ── Helper: build Google Drive service ───────────────────────────────────────
def _get_drive_service():
    """Crea y devuelve un cliente autenticado de Google Drive usando la cuenta de servicio."""
    info = dict(st.secrets["google"])
    creds = service_account.Credentials.from_service_account_info(info, scopes=DRIVE_SCOPES)
    return build("drive", "v3", credentials=creds)

# ── Helper: subir archivo a Google Drive ─────────────────────────────────────
def upload_to_drive(file_bytes: bytes, file_name: str, mime_type: str = "application/octet-stream") -> str | None:
    """Sube un archivo a la carpeta de Google Drive indicada en secrets.toml.

    Devuelve el enlace al archivo recién subido, o None si hubo error.
    """
    safe_name = sanitize_filename(file_name)
    if not safe_name:
        st.error("❌ Nombre de archivo inválido.")
        return None
    try:
        folder_id = st.secrets["folders"]["uploads_folder_id"]
        service = _get_drive_service()
        file_metadata = {"name": safe_name, "parents": [folder_id]}
        resumable = len(file_bytes) > 5 * 1024 * 1024
        media = MediaIoBaseUpload(io.BytesIO(file_bytes), mimetype=mime_type, resumable=resumable)
        uploaded = (
            service.files()
            .create(body=file_metadata, media_body=media, fields="id, webViewLink, name")
            .execute()
        )
        return uploaded.get("webViewLink")
    except KeyError:
        st.error("❌ Secrets no configurados correctamente (sección [google] o [folders]).")
        return None
    except Exception as exc:
        st.error(f"❌ Error al subir a Google Drive: {exc}")
        return None

# ── Helper: listar archivos recientes de Google Drive ────────────────────────
def list_recent_uploads():
    """Devuelve la lista de archivos recientes en la carpeta de Google Drive.

    Cada elemento es un dict con 'name', 'id' y 'webViewLink'.
    """
    try:
        folder_id = st.secrets["folders"]["uploads_folder_id"]
        service = _get_drive_service()
        query = f"'{folder_id}' in parents and trashed = false"
        result = (
            service.files()
            .list(
                q=query,
                fields="files(id, name, webViewLink, modifiedTime)",
                orderBy="modifiedTime desc",
                pageSize=20,
            )
            .execute()
        )
        return result.get("files", [])
    except KeyError:
        st.warning("⚠️ Secrets no configurados correctamente (sección [google] o [folders]).")
        return []
    except Exception as exc:
        st.error(f"❌ Error al listar archivos de Google Drive: {exc}")
        return []

# ──────────────────────────────────────────────────────────────────────────────
# INTERFAZ PRINCIPAL
# ──────────────────────────────────────────────────────────────────────────────

# Imagen de Fido Dido
st.image(MONO_DATA_URI, use_column_width=True)
st.title("📚 Ferran — Recursos Académicos")
st.markdown("---")

# ── Sección de UPLOAD ─────────────────────────────────────────────────────────
st.subheader("⬆️ Subir archivo a Google Drive")
uploaded_file = st.file_uploader(
    "Selecciona un archivo para subir a la carpeta compartida de Google Drive",
    type=None,
    help="Máximo 250 MB por archivo",
)

if uploaded_file is not None:
    file_size_mb = uploaded_file.size / (1024 * 1024)
    if uploaded_file.size > MAX_UPLOAD_BYTES:
        st.error(f"❌ Archivo demasiado grande ({file_size_mb:.1f} MB). Máximo: 250 MB")
    else:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"📄 {uploaded_file.name} ({file_size_mb:.1f} MB)")
        with col2:
            if st.button("📤 Subir"):
                with st.spinner("Subiendo a Google Drive…"):
                    file_bytes = uploaded_file.read()
                    mime_type = uploaded_file.type or "application/octet-stream"
                    link = upload_to_drive(file_bytes, uploaded_file.name, mime_type)
                if link:
                    st.success(f"✅ '{uploaded_file.name}' subido correctamente.")
                    st.markdown(f"🔗 [Abrir archivo en Google Drive]({link})")

st.markdown("---")

# ── Secciones principales ────────────────────────────────────────────────────
st.subheader("📂 Secciones")
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("📘 ICS111\nAdm. Empresas", key="ics111"):
        st.session_state.seccion = "ics111"

with col2:
    if st.button("📗 ICS161\nIntro. Economía", key="ics161"):
        st.session_state.seccion = "ics161"

with col3:
    if st.button("📐 MATE10\nÁlgebra", key="mate10"):
        st.session_state.seccion = "mate10"

with col4:
    if st.button("🐍 Ejercicios\nPython", key="python"):
        st.session_state.seccion = "python"

# Renderizar sección seleccionada
PDF_PATHS = {
    "ics111": ("pdfs/ics111_administracion_empresas.pdf", "ICS111 - Administración de Empresas"),
    "ics161": ("pdfs/ics161_introduccion_economia.pdf", "ICS161 - Introducción a la Economía"),
    "mate10": ("pdfs/mate10_algebra_geometria.pdf", "MATE10 - Álgebra y Geometría"),
}

if st.session_state.seccion in PDF_PATHS:
    path, title = PDF_PATHS[st.session_state.seccion]
    st.markdown(f"### {title}")
    download_button(path, title)

elif st.session_state.seccion == "python":
    st.markdown("### 🐍 Ejercicios Python")
    for categoria in EJERCICIOS:
        with st.expander(f"{categoria['icono']} {categoria['categoria']}"):
            for ej in categoria["ejercicios"]:
                st.markdown(f"**{ej['titulo']}**")
                st.info(ej["enunciado"])
                if ej.get("ejemplo"):
                    st.code(ej["ejemplo"], language="text")
                st.code(ej["codigo"], language="python")
                st.markdown("---")

st.markdown("---")

# ── Sección: Archivos recientes en Google Drive ───────────────────────────────
if st.button("🗂️ Ver Archivos Recientes en Drive", key="recientes"):
    st.session_state.seccion = "recientes"

if st.session_state.seccion == "recientes":
    st.subheader("📥 Archivos subidos recientemente a Google Drive")
    with st.spinner("Cargando lista de archivos…"):
        archivos = list_recent_uploads()
    if archivos:
        for archivo in archivos:
            col_a, col_b = st.columns([3, 1])
            with col_a:
                st.markdown(f"📄 **{archivo['name']}**")
            with col_b:
                link = archivo.get("webViewLink", "#")
                st.markdown(f"[🔗 Abrir]({link})")
    else:
        st.info("📭 No hay archivos en la carpeta de Google Drive todavía.")
