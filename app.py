import streamlit as st
from pathlib import Path
from mono_b64 import MONO_DATA_URI
from ejercicios_python import EJERCICIOS
from github import Github
import base64

st.set_page_config(page_title="Ferrán's Library", page_icon="🐒", layout="centered")

if "seccion" not in st.session_state:
    st.session_state.seccion = "portada"

# ─── GITHUB UPLOAD CONFIG ────────────────────────────────────────────────────
GITHUB_TOKEN = st.secrets.get("GITHUB_TOKEN")
REPO_NAME = "johnbij/ferran"
BRANCH = "main"

def upload_to_github(file_uploaded, folder="uploads"):
    """Sube archivos al repositorio de GitHub"""
    if not GITHUB_TOKEN:
        st.error("❌ Token de GitHub no configurado")
        return False
    
    try:
        g = Github(GITHUB_TOKEN)
        repo = g.get_repo(REPO_NAME)
        
        content = file_uploaded.read()
        file_path = f"{folder}/{file_uploaded.name}"
        
        repo.create_file(
            path=file_path,
            message=f"Upload: {file_uploaded.name}",
            content=content,
            branch=BRANCH
        )
        
        st.success(f"✅ {file_uploaded.name} subido correctamente!")
        return True
    
    except Exception as e:
        st.error(f"❌ Error al subir: {str(e)}")
        return False

# ─── ESTILOS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap');
* { font-family: 'Inter', sans-serif; }
.stApp { background: #f5f5f0; }

.hero {
    background: linear-gradient(160deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%);
    border-radius: 24px; padding: 0 0 28px 0;
    text-align: center; color: white; margin-bottom: 0;
    box-shadow: 0 8px 32px rgba(0,0,0,0.25);
    overflow: hidden;
}
.hero-titulo { font-size: 80px; font-weight: 900; letter-spacing: 6px; margin: 0 0 6px 0; line-height: 1; }
.hero-sub { font-size: 13px; opacity: 0.7; letter-spacing: 2px; margin-bottom: 6px; font-weight: 600; text-transform: uppercase; padding: 0 24px; }
.hero-lema { font-size: 13px; color: #f0c040; font-style: italic; font-weight: bold; padding: 0 24px 4px 24px; }

.seccion-titulo-bar {
    font-size: 17px; font-weight: 800; color: #1a1a2e;
    border-left: 5px solid #f0c040; padding-left: 12px; margin: 22px 0 14px 0;
}
.pdf-card {
    background: white; border-radius: 14px; padding: 18px 20px;
    margin-bottom: 12px; box-shadow: 0 2px 10px rgba(0,0,0,0.07);
    display: flex; align-items: center; gap: 14px;
}
.pdf-icon { font-size: 32px; }
.pdf-nombre { font-size: 15px; font-weight: 700; color: #1a1a2e; margin-bottom: 3px; }
.pdf-desc { font-size: 12px; color: #777; }
.pdf-placeholder {
    background: #fafafa; border: 2px dashed #ddd;
    border-radius: 14px; padding: 18px 20px; margin-bottom: 12px;
    display: flex; align-items: center; gap: 14px;
}

/* Botones portada */
div[data-testid="stHorizontalBlock"]:nth-of-type(1) div[data-testid="column"]:nth-child(1) button {
    background: linear-gradient(135deg, #c0392b, #922b21) !important;
    color: white !important; border: none !important; border-radius: 16px !important;
    min-height: 100px !important; font-size: 15px !important; font-weight: 800 !important;
    box-shadow: 0 4px 14px rgba(0,0,0,0.2) !important;
}
div[data-testid="stHorizontalBlock"]:nth-of-type(1) div[data-testid="column"]:nth-child(2) button {
    background: linear-gradient(135deg, #1a5276, #154360) !important;
    color: white !important; border: none !important; border-radius: 16px !important;
    min-height: 100px !important; font-size: 15px !important; font-weight: 800 !important;
    box-shadow: 0 4px 14px rgba(0,0,0,0.2) !important;
}
div[data-testid="stHorizontalBlock"]:nth-of-type(2) div[data-testid="column"]:nth-child(1) button {
    background: linear-gradient(135deg, #117a65, #0e6655) !important;
    color: white !important; border: none !important; border-radius: 16px !important;
    min-height: 100px !important; font-size: 15px !important; font-weight: 800 !important;
    box-shadow: 0 4px 14px rgba(0,0,0,0.2) !important;
}
div[data-testid="stHorizontalBlock"]:nth-of-type(2) div[data-testid="column"]:nth-child(2) button {
    background: linear-gradient(135deg, #6c3483, #5b2c6f) !important;
    color: white !important; border: none !important; border-radius: 16px !important;
    min-height: 100px !important; font-size: 15px !important; font-weight: 800 !important;
    box-shadow: 0 4px 14px rgba(0,0,0,0.2) !important;
}

.seccion-header {
    border-radius: 16px; padding: 24px; color: white;
    text-align: center; margin-bottom: 20px;
}
.seccion-titulo-txt { font-size: 26px; font-weight: 900; letter-spacing: 2px; }
.seccion-sub { font-size: 13px; opacity: 0.8; margin-top: 4px; }

/* Ejercicio */
.ej-titulo-bar {
    background: linear-gradient(135deg, #6c3483, #5b2c6f);
    border-radius: 12px 12px 0 0;
    padding: 12px 16px;
    color: white;
    font-size: 15px;
    font-weight: 800;
    margin-bottom: 0;
}
.ej-link-ext {
    font-size: 11px; color: #f0c040; font-weight: 600;
    text-decoration: none; float: right; margin-top: 2px;
}
.ej-body {
    background: white;
    border-radius: 0 0 12px 12px;
    padding: 16px 18px 12px 18px;
    margin-bottom: 6px;
    border: 1px solid #e8e0f0;
    border-top: none;
}
.ej-enunciado {
    font-size: 15px; color: #222; line-height: 1.7; margin-bottom: 12px;
}
.ej-io-label {
    font-size: 11px; font-weight: 700; color: #999;
    text-transform: uppercase; letter-spacing: 1px; margin-bottom: 4px;
}
.ej-io {
    background: #f4f4f4; border-radius: 8px; padding: 10px 14px;
    font-family: monospace; font-size: 13px; color: #333;
    white-space: pre; margin-bottom: 0;
}
.cat-label {
    font-size: 14px; font-weight: 800; color: #6c3483;
    border-left: 4px solid #6c3483; padding-left: 10px;
    margin: 26px 0 12px 0;
}
/* Separador entre ejercicios */
.ej-sep { height: 16px; }
</style>
""", unsafe_allow_html=True)

# ─── CONFIG RAMOS ────────────────────────────────────────────────────────────
RAMOS = {
    "matematica": {
        "nombre": "Matemática", "emoji": "📐",
        "desc": "Álgebra y Geometría · MATE-10",
        "color": "#c0392b", "color2": "#922b21",
        "pdfs": [
            {"archivo": "mate10_algebra_geometria.pdf",
             "nombre": "Programa Álgebra y Geometría",
             "desc": "MATE-10 · Programa oficial USM",
             "icono": "📐", "placeholder": False},
        ],
    },
    "administracion": {
        "nombre": "Administración", "emoji": "🏢",
        "desc": "Administración de Empresas · ICS-111",
        "color": "#1a5276", "color2": "#154360",
        "pdfs": [
            {"archivo": "ics111_administracion_empresas.pdf",
             "nombre": "Programa Administración de Empresas",
             "desc": "ICS-111 · Programa oficial USM",
             "icono": "🏢", "placeholder": False},
        ],
    },
    "economia": {
        "nombre": "Economía", "emoji": "📊",
        "desc": "Introducción a la Economía · ICS161",
        "color": "#117a65", "color2": "#0e6655",
        "pdfs": [
            {"archivo": "ics161_introduccion_economia.pdf",
             "nombre": "Programa Introducción a la Economía",
             "desc": "ICS161 · Programa oficial USM",
             "icono": "📊", "placeholder": False},
            {"archivo": "Mankiw-Principios de Economia 6taED.pdf",
             "nombre": "Principios de Economía — Mankiw",
             "desc": "Mankiw, G. (2012) · 6ª Ed. · Texto guía del ramo",
             "icono": "📗", "placeholder": False},
        ],
    },
    "python": {
        "nombre": "Python", "emoji": "🐍",
        "desc": "Ejercicios resueltos · Python 3",
        "color": "#6c3483", "color2": "#5b2c6f",
        "pdfs": [],
    },
}

# ─── PORTADA ─────────────────────────────────────────────────────────────────
def render_portada():
    st.markdown(f"""
    <div class="hero">
        <div style="text-align:center; line-height:0; margin-bottom:-10px;">
            <img src="{MONO_DATA_URI}"
                 style="width:100%; max-width:320px; display:block; margin:0 auto;"/>
        </div>
        <div class="hero-titulo">Ferrán</div>
        <div class="hero-sub">Mis apuntes de la U</div>
        <div class="hero-lema">"El conocimiento es poder"</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="seccion-titulo-bar">📚 Selecciona tu ramo</div>',
                unsafe_allow_html=True)

    rl = list(RAMOS.items())
    c1, c2 = st.columns(2)
    with c1:
        k, d = rl[0]
        if st.button(f"{d['emoji']} {d['nombre']}\n{d['desc']}", key=f"b_{k}", use_container_width=True):
            st.session_state.seccion = k; st.rerun()
    with c2:
        k, d = rl[1]
        if st.button(f"{d['emoji']} {d['nombre']}\n{d['desc']}", key=f"b_{k}", use_container_width=True):
            st.session_state.seccion = k; st.rerun()
    c3, c4 = st.columns(2)
    with c3:
        k, d = rl[2]
        if st.button(f"{d['emoji']} {d['nombre']}\n{d['desc']}", key=f"b_{k}", use_container_width=True):
            st.session_state.seccion = k; st.rerun()
    with c4:
        k, d = rl[3]
        if st.button(f"{d['emoji']} {d['nombre']}\n{d['desc']}", key=f"b_{k}", use_container_width=True):
            st.session_state.seccion = k; st.rerun()

    st.markdown('<div style="text-align:center;margin-top:28px;color:#bbb;font-size:12px;">Ferrán · USM · 2026 🐒</div>',
                unsafe_allow_html=True)


# ─── SECCIÓN PDF ────────────────────────────────────────────────────────────��
def render_seccion_pdf(key_r):
    data_r = RAMOS[key_r]
    color, color2 = data_r["color"], data_r["color2"]
    pdf_dir = Path(__file__).parent / "pdfs"

    st.markdown(f"""
    <div class="seccion-header" style="background:linear-gradient(135deg,{color},{color2});">
        <div style="font-size:40px;">{data_r['emoji']}</div>
        <div class="seccion-titulo-txt">{data_r['nombre'].upper()}</div>
        <div class="seccion-sub">{data_r['desc']}</div>
    </div>""", unsafe_allow_html=True)

    if st.button("← Volver al inicio", key="btn_volver"):
        st.session_state.seccion = "portada"; st.rerun()
    st.write("")

    for m in data_r.get("pdfs", []):
        pdf_path = pdf_dir / m["archivo"]
        if m.get("placeholder"):
            st.markdown(f"""
            <div class="pdf-placeholder">
                <div class="pdf-icon">{m['icono']}</div>
                <div>
                    <div class="pdf-nombre">{m['nombre']}</div>
                    <div class="pdf-desc">{m['desc']}</div>
                    <div style="font-size:11px;color:#e67e22;font-weight:700;margin-top:4px;">
                        ⏳ Agregar PDF a /pdfs/{m['archivo']}
                    </div>
                </div>
            </div>""", unsafe_allow_html=True)
            st.button(f"⬇️ Descargar {m['nombre']}", key=f"dl_{m['archivo']}",
                      use_container_width=True, disabled=True)
        else:
            st.markdown(f"""
            <div class="pdf-card">
                <div class="pdf-icon">{m['icono']}</div>
                <div>
                    <div class="pdf-nombre">{m['nombre']}</div>
                    <div class="pdf-desc">{m['desc']}</div>
                </div>
            </div>""", unsafe_allow_html=True)
            if pdf_path.exists():
                with open(pdf_path, "rb") as f:
                    st.download_button(f"⬇️ Descargar {m['nombre']}", data=f,
                        file_name=m["archivo"], mime="application/pdf",
                        key=f"dl_{m['archivo']}", use_container_width=True)
            else:
                st.warning(f"No encontrado: {m['archivo']}")

    st.markdown('<div style="text-align:center;margin-top:20px;color:#ccc;font-size:11px;">Ferrán · USM · 2026 🐒</div>',
                unsafe_allow_html=True)


# ─── SECCIÓN PYTHON ───────────────────────────────────────────────────────────
def render_python():
    st.markdown("""
    <div class="seccion-header" style="background:linear-gradient(135deg,#6c3483,#5b2c6f);">
        <div style="font-size:40px;">🐍</div>
        <div class="seccion-titulo-txt">PYTHON</div>
        <div class="seccion-sub">Ejercicios resueltos · Python 3 · progra.usm.cl</div>
    </div>""", unsafe_allow_html=True)

    if st.button("← Volver al inicio", key="btn_volver"):
        st.session_state.seccion = "portada"; st.rerun()

    st.info("💡 Ejercicios en **Python 3** basados en la ayudantía oficial USM. "
            "El título de cada ejercicio enlaza al enunciado original.")

    for cat in EJERCICIOS:
        st.markdown(f'<div class="cat-label">{cat["icono"]} {cat["categoria"]}</div>',
                    unsafe_allow_html=True)

        for ej in cat["ejercicios"]:
            # ── Cabecera con título + link externo ──
            st.markdown(f"""
            <div class="ej-titulo-bar">
                🔹 <a href="{ej['url']}" target="_blank"
                   style="color:white;text-decoration:none;">{ej['titulo']}</a>
                <a href="{ej['url']}" target="_blank" class="ej-link-ext">
                    enunciado original ↗
                </a>
            </div>""", unsafe_allow_html=True)

            # ── Cuerpo: enunciado + ejemplo — HTML nativo pero simple ──
            st.markdown(f"""
            <div class="ej-body">
                <div class="ej-enunciado">{ej['enunciado'].replace(chr(10), '<br>')}</div>
                <div class="ej-io-label">📟 Ejemplo de ejecución</div>
                <div class="ej-io">{ej['ejemplo']}</div>
            </div>
            <div class="ej-sep"></div>
            """, unsafe_allow_html=True)

            # ── Código en expander nativo de Streamlit ──
            with st.expander(f"💻 Ver código Python 3"):
                st.code(ej["codigo"].strip(), language="python")

            st.markdown("---")

    st.markdown('<div style="text-align:center;margin-top:8px;color:#ccc;font-size:11px;">Ferrán · USM · 2026 🐒</div>',
                unsafe_allow_html=True)


# ─── SECCIÓN UPLOAD ───────────────────────────────────────────────────────────
def render_upload():
    st.markdown("""
    <div class="seccion-header" style="background:linear-gradient(135deg,#e74c3c,#c0392b);">
        <div style="font-size:40px;">📤</div>
        <div class="seccion-titulo-txt">CARGAR ARCHIVOS</div>
        <div class="seccion-sub">Sube tus archivos al repositorio</div>
    </div>""", unsafe_allow_html=True)

    if st.button("← Volver al inicio", key="btn_volver_upload"):
        st.session_state.seccion = "portada"; st.rerun()
    
    st.write("")
    
    uploaded_files = st.file_uploader(
        "Selecciona los archivos que deseas subir:",
        accept_multiple_files=True,
        type=["pdf", "py", "txt", "xlsx", "csv", "json"]
    )
    
    if uploaded_files:
        for file in uploaded_files:
            col1, col2 = st.columns([0.8, 0.2])
            with col1:
                st.write(f"📄 {file.name} ({file.size} bytes)")
            with col2:
                if st.button("Subir", key=f"upload_{file.name}"):
                    upload_to_github(file)

    st.markdown('<div style="text-align:center;margin-top:20px;color:#ccc;font-size:11px;">Ferrán · USM · 2026 🐒</div>',
                unsafe_allow_html=True)


# ─── ROUTER ───────────────────────────────────────────────────────────────────
s = st.session_state.seccion
if s == "portada":
    render_portada()
elif s == "python":
    render_python()
elif s == "upload":
    render_upload()
elif s in RAMOS:
    render_seccion_pdf(s)
else:
    st.session_state.seccion = "portada"; st.rerun()
   
