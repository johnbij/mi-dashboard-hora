import streamlit as st
from pathlib import Path
from mono_b64 import MONO_DATA_URI

st.set_page_config(page_title="Ferrán", page_icon="🐒", layout="centered")

if "seccion" not in st.session_state:
    st.session_state.seccion = "portada"

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap');
* { font-family: 'Inter', sans-serif; }
.stApp { background: #f5f5f0; }

.hero {
    background: linear-gradient(160deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%);
    border-radius: 24px;
    padding: 36px 24px 28px 24px;
    text-align: center;
    color: white;
    margin-bottom: 0;
    box-shadow: 0 8px 32px rgba(0,0,0,0.25);
}
.hero-titulo {
    font-size: 52px; font-weight: 900; letter-spacing: 6px;
    margin: 10px 0 4px 0; text-shadow: 0 2px 8px rgba(0,0,0,0.4);
}
.hero-sub { font-size: 13px; opacity: 0.7; letter-spacing: 2px; margin-bottom: 6px; font-weight: 600; text-transform: uppercase; }
.hero-lema { font-size: 13px; color: #f0c040; font-style: italic; font-weight: bold; }
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
    border-radius: 16px; padding: 24px; color: white; text-align: center; margin-bottom: 20px;
}
.seccion-titulo-txt { font-size: 26px; font-weight: 900; letter-spacing: 2px; }
.seccion-sub { font-size: 13px; opacity: 0.8; margin-top: 4px; }
</style>
""", unsafe_allow_html=True)

RAMOS = {
    "matematica": {
        "nombre": "Matemática", "emoji": "📐",
        "desc": "Álgebra y Geometría · MATE-10",
        "color": "#c0392b", "color2": "#922b21",
        "pdfs": [{"archivo": "mate10_algebra_geometria.pdf",
                  "nombre": "Programa Álgebra y Geometría",
                  "desc": "MATE-10 · Programa oficial USM", "icono": "📐"}],
    },
    "administracion": {
        "nombre": "Administración", "emoji": "🏢",
        "desc": "Administración de Empresas · ICS-111",
        "color": "#1a5276", "color2": "#154360",
        "pdfs": [{"archivo": "ics111_administracion_empresas.pdf",
                  "nombre": "Programa Administración de Empresas",
                  "desc": "ICS-111 · Programa oficial USM", "icono": "🏢"}],
    },
    "economia": {
        "nombre": "Economía", "emoji": "📊",
        "desc": "Introducción a la Economía · ICS161",
        "color": "#117a65", "color2": "#0e6655",
        "pdfs": [{"archivo": "ics161_introduccion_economia.pdf",
                  "nombre": "Programa Introducción a la Economía",
                  "desc": "ICS161 · Programa oficial USM", "icono": "📊"}],
    },
    "python": {
        "nombre": "Python", "emoji": "🐍",
        "desc": "Próximamente · Guías y ejercicios",
        "color": "#6c3483", "color2": "#5b2c6f",
        "pdfs": [],
    },
}

def render_portada():
    st.markdown(f"""
    <div class="hero">
        <img src="{MONO_DATA_URI}" width="150" height="200"
             style="display:block;margin:0 auto 10px auto;" alt="Ferrán"/>
        <div class="hero-titulo">FERRÁN</div>
        <div class="hero-sub">Repositorio de recursos universitarios</div>
        <div class="hero-lema">"El conocimiento es el único recurso que crece al compartirse"</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="seccion-titulo-bar">📚 Selecciona tu ramo</div>', unsafe_allow_html=True)

    ramos_lista = list(RAMOS.items())
    col1, col2 = st.columns(2)
    with col1:
        k, d = ramos_lista[0]
        if st.button(f"{d['emoji']} {d['nombre']}\n{d['desc']}", key=f"b_{k}", use_container_width=True):
            st.session_state.seccion = k; st.rerun()
    with col2:
        k, d = ramos_lista[1]
        if st.button(f"{d['emoji']} {d['nombre']}\n{d['desc']}", key=f"b_{k}", use_container_width=True):
            st.session_state.seccion = k; st.rerun()

    col3, col4 = st.columns(2)
    with col3:
        k, d = ramos_lista[2]
        if st.button(f"{d['emoji']} {d['nombre']}\n{d['desc']}", key=f"b_{k}", use_container_width=True):
            st.session_state.seccion = k; st.rerun()
    with col4:
        k, d = ramos_lista[3]
        if st.button(f"{d['emoji']} {d['nombre']}\n{d['desc']}", key=f"b_{k}", use_container_width=True):
            st.session_state.seccion = k; st.rerun()

    st.markdown('<div style="text-align:center;margin-top:28px;color:#bbb;font-size:12px;">Ferrán · USM · 2026 🐒</div>', unsafe_allow_html=True)


def render_seccion(key_r):
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
    pdfs = data_r.get("pdfs", [])

    if not pdfs:
        st.markdown("""<div style="background:#f9f9f9;border-radius:14px;padding:30px;text-align:center;color:#aaa;">
            <div style="font-size:40px;">🚧</div>
            <div style="font-size:16px;font-weight:700;margin-top:8px;">Próximamente</div>
            <div style="font-size:13px;margin-top:4px;">Los recursos de este ramo estarán disponibles pronto.</div>
        </div>""", unsafe_allow_html=True)
        return

    for m in pdfs:
        pdf_path = pdf_dir / m["archivo"]
        st.markdown(f"""<div class="pdf-card">
            <div class="pdf-icon">{m['icono']}</div>
            <div><div class="pdf-nombre">{m['nombre']}</div><div class="pdf-desc">{m['desc']}</div></div>
        </div>""", unsafe_allow_html=True)
        if pdf_path.exists():
            with open(pdf_path, "rb") as f:
                st.download_button(f"⬇️ Descargar {m['nombre']}", data=f,
                    file_name=m["archivo"], mime="application/pdf",
                    key=f"dl_{m['archivo']}", use_container_width=True)
        else:
            st.warning(f"No encontrado: {m['archivo']}")

    st.markdown('<div style="text-align:center;margin-top:20px;color:#ccc;font-size:11px;">Ferrán · USM · 2026 🐒</div>', unsafe_allow_html=True)


s = st.session_state.seccion
if s == "portada":
    render_portada()
elif s in RAMOS:
    render_seccion(s)
else:
    st.session_state.seccion = "portada"; st.rerun()
