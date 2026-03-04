import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Ferrán", page_icon="🐒", layout="centered")

# ─────────────────────────────────────────────────────────────────────────────
# ESTADOS
# ─────────────────────────────────────────────────────────────────────────────
if "seccion" not in st.session_state:
    st.session_state.seccion = "portada"

# ─────────────────────────────────────────────────────────────────────────────
# ESTILOS GLOBALES
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap');

* { font-family: 'Inter', sans-serif; }

.stApp { background: #f5f5f0; }

/* ── hero ── */
.hero {
    background: linear-gradient(160deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%);
    border-radius: 24px;
    padding: 40px 24px 32px 24px;
    text-align: center;
    color: white;
    margin-bottom: 0;
    box-shadow: 0 8px 32px rgba(0,0,0,0.25);
}
.hero-titulo {
    font-size: 52px;
    font-weight: 900;
    letter-spacing: 6px;
    margin-bottom: 6px;
    text-shadow: 0 2px 8px rgba(0,0,0,0.4);
}
.hero-sub {
    font-size: 15px;
    opacity: 0.75;
    letter-spacing: 1px;
    margin-bottom: 20px;
    font-weight: 600;
}
.hero-lema {
    font-size: 14px;
    color: #f0c040;
    font-style: italic;
    font-weight: bold;
    margin-bottom: 0;
}

/* ── tarjetas de ramo ── */
.ramo-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    margin-top: 20px;
    margin-bottom: 8px;
}

.ramo-card {
    border-radius: 18px;
    padding: 22px 16px 18px 16px;
    color: white;
    text-align: center;
    cursor: pointer;
    box-shadow: 0 4px 16px rgba(0,0,0,0.15);
    transition: transform 0.15s;
    text-decoration: none;
}
.ramo-card:hover { transform: translateY(-3px); }
.ramo-emoji { font-size: 36px; margin-bottom: 8px; }
.ramo-nombre { font-size: 17px; font-weight: 800; letter-spacing: 0.5px; }
.ramo-desc { font-size: 12px; opacity: 0.85; margin-top: 4px; }

/* ── sección PDF ── */
.seccion-header {
    border-radius: 16px;
    padding: 24px;
    color: white;
    text-align: center;
    margin-bottom: 20px;
}
.seccion-titulo-txt { font-size: 26px; font-weight: 900; letter-spacing: 2px; }
.seccion-sub { font-size: 13px; opacity: 0.8; margin-top: 4px; }

.pdf-card {
    background: white;
    border-radius: 14px;
    padding: 18px 20px;
    margin-bottom: 12px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.07);
    display: flex;
    align-items: center;
    gap: 14px;
}
.pdf-icon { font-size: 32px; }
.pdf-nombre { font-size: 15px; font-weight: 700; color: #1a1a2e; margin-bottom: 3px; }
.pdf-desc { font-size: 12px; color: #777; }

/* botón volver */
.stButton > button {
    font-weight: 700 !important;
    border-radius: 10px !important;
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# MONO FIDO DIDO SVG — rubio, polera negra, espalda ancha, calugas gigantes
# ─────────────────────────────────────────────────────────────────────────────
MONO_SVG = """
<svg viewBox="0 0 200 280" width="160" height="220" xmlns="http://www.w3.org/2000/svg">

  <!-- ====== CALUGAS (cadena con calugas enormes) ====== -->
  <!-- cadena izquierda -->
  <line x1="70" y1="165" x2="30" y2="230" stroke="#888" stroke-width="2.5"/>
  <!-- caluga izq 1 -->
  <ellipse cx="55" cy="183" rx="12" ry="9" fill="#FF3366" stroke="#cc0044" stroke-width="1.5"/>
  <text x="55" y="187" text-anchor="middle" font-size="8" fill="white" font-weight="bold">■</text>
  <!-- caluga izq 2 -->
  <ellipse cx="40" cy="208" rx="14" ry="10" fill="#FF6600" stroke="#cc4400" stroke-width="1.5"/>
  <text x="40" y="212" text-anchor="middle" font-size="9" fill="white" font-weight="bold">■</text>
  <!-- caluga izq 3 (enorme) -->
  <ellipse cx="28" cy="234" rx="16" ry="12" fill="#FFCC00" stroke="#cc9900" stroke-width="1.5"/>
  <text x="28" y="239" text-anchor="middle" font-size="10" fill="white" font-weight="bold">■</text>

  <!-- cadena derecha -->
  <line x1="130" y1="165" x2="170" y2="230" stroke="#888" stroke-width="2.5"/>
  <!-- caluga der 1 -->
  <ellipse cx="145" cy="183" rx="12" ry="9" fill="#9933FF" stroke="#6600cc" stroke-width="1.5"/>
  <text x="145" y="187" text-anchor="middle" font-size="8" fill="white" font-weight="bold">■</text>
  <!-- caluga der 2 -->
  <ellipse cx="158" cy="208" rx="14" ry="10" fill="#00CC99" stroke="#009966" stroke-width="1.5"/>
  <text x="158" y="212" text-anchor="middle" font-size="9" fill="white" font-weight="bold">■</text>
  <!-- caluga der 3 (enorme) -->
  <ellipse cx="170" cy="234" rx="16" ry="12" fill="#FF3366" stroke="#cc0044" stroke-width="1.5"/>
  <text x="170" y="239" text-anchor="middle" font-size="10" fill="white" font-weight="bold">■</text>

  <!-- ====== CUERPO ESPALDA ANCHA (polera negra) ====== -->
  <!-- torso trapezoidal — ancho arriba, más ancho aún -->
  <path d="M 55 140 Q 45 155 42 180 Q 60 190 100 191 Q 140 190 158 180 Q 155 155 145 140 Z"
        fill="#111" stroke="#333" stroke-width="1"/>
  <!-- hombros extra anchos -->
  <ellipse cx="52" cy="143" rx="16" ry="12" fill="#111"/>
  <ellipse cx="148" cy="143" rx="16" ry="12" fill="#111"/>

  <!-- ====== BRAZOS (flacos estilo cartoon) ====== -->
  <!-- brazo izquierdo -->
  <path d="M 42 148 Q 20 160 18 185 Q 20 190 28 188 Q 35 165 55 155" 
        fill="#c8a27a" stroke="#b08060" stroke-width="1.5"/>
  <!-- mano izq -->
  <circle cx="20" cy="187" r="7" fill="#c8a27a" stroke="#b08060" stroke-width="1"/>

  <!-- brazo derecho -->
  <path d="M 158 148 Q 180 160 182 185 Q 180 190 172 188 Q 165 165 145 155"
        fill="#c8a27a" stroke="#b08060" stroke-width="1.5"/>
  <!-- mano der -->
  <circle cx="180" cy="187" r="7" fill="#c8a27a" stroke="#b08060" stroke-width="1"/>

  <!-- ====== CUELLO ====== -->
  <rect x="88" y="112" width="24" height="32" rx="8" fill="#c8a27a" stroke="#b08060" stroke-width="1"/>

  <!-- ====== CARA (Fido Dido style — oval, línea de expresión mínima) ====== -->
  <ellipse cx="100" cy="88" rx="40" ry="44" fill="#d4a87a" stroke="#b08060" stroke-width="1.5"/>

  <!-- ====== PELO RUBIO ESTILO FIDO DIDO ====== -->
  <!-- mechones hacia arriba irregulares -->
  <path d="M 68 65 Q 65 35 75 20 Q 80 45 82 55" fill="#FFD700" stroke="#DAA520" stroke-width="1"/>
  <path d="M 80 58 Q 82 28 92 15 Q 95 38 96 55" fill="#FFD700" stroke="#DAA520" stroke-width="1"/>
  <path d="M 96 55 Q 100 22 108 12 Q 111 35 112 53" fill="#FFCC00" stroke="#DAA520" stroke-width="1"/>
  <path d="M 112 56 Q 116 30 124 18 Q 126 42 124 58" fill="#FFD700" stroke="#DAA520" stroke-width="1"/>
  <path d="M 124 60 Q 132 38 138 25 Q 136 50 132 64" fill="#FFD700" stroke="#DAA520" stroke-width="1"/>
  <!-- base del pelo -->
  <ellipse cx="100" cy="60" rx="38" ry="18" fill="#FFD700"/>

  <!-- ====== OREJAS ====== -->
  <circle cx="60" cy="90" r="11" fill="#c8a27a" stroke="#b08060" stroke-width="1.5"/>
  <circle cx="60" cy="90" r="6" fill="#e8b090"/>
  <circle cx="140" cy="90" r="11" fill="#c8a27a" stroke="#b08060" stroke-width="1.5"/>
  <circle cx="140" cy="90" r="6" fill="#e8b090"/>

  <!-- ====== OJOS (Fido Dido — puntos simples pero expresivos) ====== -->
  <!-- ojo izq -->
  <ellipse cx="85" cy="88" rx="7" ry="8" fill="white" stroke="#333" stroke-width="1"/>
  <circle cx="86" cy="89" r="4" fill="#222"/>
  <circle cx="87" cy="87" r="1.5" fill="white"/>
  <!-- ojo der -->
  <ellipse cx="115" cy="88" rx="7" ry="8" fill="white" stroke="#333" stroke-width="1"/>
  <circle cx="116" cy="89" r="4" fill="#222"/>
  <circle cx="117" cy="87" r="1.5" fill="white"/>

  <!-- ====== CEJAS (levantadas, estilo fresco) ====== -->
  <path d="M 79 79 Q 85 75 92 79" stroke="#8B6914" stroke-width="2.5" fill="none" stroke-linecap="round"/>
  <path d="M 108 79 Q 115 75 121 79" stroke="#8B6914" stroke-width="2.5" fill="none" stroke-linecap="round"/>

  <!-- ====== NARIZ (pequeña, cartoon) ====== -->
  <ellipse cx="100" cy="100" rx="5" ry="4" fill="#b08060"/>
  <ellipse cx="97" cy="102" rx="2" ry="1.5" fill="#8B6040"/>
  <ellipse cx="103" cy="102" rx="2" ry="1.5" fill="#8B6040"/>

  <!-- ====== BOCA (sonrisa relajada Fido Dido) ====== -->
  <path d="M 88 112 Q 100 121 112 112" stroke="#8B5E3C" stroke-width="2.5" fill="none" stroke-linecap="round"/>

  <!-- ====== PIERNAS (flacos jeans azul) ====== -->
  <rect x="82" y="185" width="18" height="55" rx="6" fill="#2255AA" stroke="#1a3d80" stroke-width="1"/>
  <rect x="100" y="185" width="18" height="55" rx="6" fill="#1a4499" stroke="#1a3d80" stroke-width="1"/>
  <!-- zapatillas -->
  <ellipse cx="91" cy="241" rx="13" ry="7" fill="#f0f0f0" stroke="#999" stroke-width="1"/>
  <ellipse cx="109" cy="241" rx="13" ry="7" fill="#f0f0f0" stroke="#999" stroke-width="1"/>

</svg>
"""

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURACIÓN DE RAMOS
# ─────────────────────────────────────────────────────────────────────────────
RAMOS = {
    "matematica": {
        "nombre": "Matemática",
        "emoji": "📐",
        "desc": "Álgebra y Geometría · MATE-10",
        "color": "#c0392b",
        "color2": "#922b21",
        "pdfs": [
            {
                "archivo": "mate10_algebra_geometria.pdf",
                "nombre": "Programa Álgebra y Geometría",
                "desc": "MATE-10 · Programa de asignatura oficial USM",
                "icono": "📐",
            },
        ],
    },
    "administracion": {
        "nombre": "Administración",
        "emoji": "🏢",
        "desc": "Administración de Empresas · ICS-111",
        "color": "#1a5276",
        "color2": "#154360",
        "pdfs": [
            {
                "archivo": "ics111_administracion_empresas.pdf",
                "nombre": "Programa Administración de Empresas",
                "desc": "ICS-111 · Programa de asignatura oficial USM",
                "icono": "🏢",
            },
        ],
    },
    "economia": {
        "nombre": "Economía",
        "emoji": "📊",
        "desc": "Introducción a la Economía · ICS161",
        "color": "#117a65",
        "color2": "#0e6655",
        "pdfs": [
            {
                "archivo": "ics161_introduccion_economia.pdf",
                "nombre": "Programa Introducción a la Economía",
                "desc": "ICS161 · Programa de asignatura oficial USM",
                "icono": "📊",
            },
        ],
    },
    "python": {
        "nombre": "Python",
        "emoji": "🐍",
        "desc": "Próximamente · Guías y ejercicios",
        "color": "#6c3483",
        "color2": "#5b2c6f",
        "pdfs": [],
    },
}

# ─────────────────────────────────────────────────────────────────────────────
# PORTADA
# ─────────────────────────────────────────────────────────────────────────────
def render_portada():
    # Hero con mono
    st.markdown(f"""
    <div class="hero">
        <div style="display:flex; justify-content:center; margin-bottom:12px;">
            {MONO_SVG}
        </div>
        <div class="hero-titulo">FERRÁN</div>
        <div class="hero-sub">REPOSITORIO DE RECURSOS UNIVERSITARIOS</div>
        <div class="hero-lema">"El conocimiento es el único recurso que crece al compartirse"</div>
    </div>
    """, unsafe_allow_html=True)

    # Tarjetas de ramos
    st.markdown("""
    <div style="margin-top:20px; margin-bottom:8px;">
        <div style="font-size:18px; font-weight:800; color:#1a1a2e;
                    border-left:5px solid #f0c040; padding-left:12px;">
            📚 Selecciona tu ramo
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Grid 2x2 con botones Streamlit (más confiables que links HTML)
    col1, col2 = st.columns(2)
    ramos_lista = list(RAMOS.items())

    for i, col in enumerate([col1, col2]):
        with col:
            key_r, data_r = ramos_lista[i]
            _render_ramo_btn(key_r, data_r, f"btn_ramo_{key_r}")

    col3, col4 = st.columns(2)
    for i, col in enumerate([col3, col4]):
        with col:
            key_r, data_r = ramos_lista[i + 2]
            _render_ramo_btn(key_r, data_r, f"btn_ramo_{key_r}")

    # Footer
    st.markdown("""
    <div style="text-align:center; margin-top:28px; color:#bbb; font-size:12px;">
        Ferrán · USM · 2026 🐒
    </div>
    """, unsafe_allow_html=True)


def _render_ramo_btn(key_r, data_r, btn_key):
    color = data_r["color"]
    color2 = data_r["color2"]
    st.markdown(f"""
    <style>
    div[data-testid="stButton"] #{btn_key} > button {{
        background: linear-gradient(135deg, {color}, {color2}) !important;
        color: white !important;
        border: none !important;
        border-radius: 16px !important;
        min-height: 100px !important;
        font-size: 15px !important;
        font-weight: 800 !important;
        width: 100% !important;
        margin-bottom: 10px !important;
        box-shadow: 0 4px 14px rgba(0,0,0,0.2) !important;
    }}
    </style>
    """, unsafe_allow_html=True)

    label = f"{data_r['emoji']} {data_r['nombre']}\n{data_r['desc']}"
    if st.button(label, key=btn_key, use_container_width=True):
        st.session_state.seccion = key_r
        st.rerun()


# ─────────────────────────────────────────────────────────────────────────────
# SECCIÓN DE RAMO (lista de PDFs)
# ─────────────────────────────────────────────────────────────────────────────
def render_seccion(key_r):
    data_r = RAMOS[key_r]
    color  = data_r["color"]
    pdf_dir = Path(__file__).parent / "pdfs"

    # Header de sección
    st.markdown(f"""
    <div class="seccion-header" style="background:linear-gradient(135deg,{color},{data_r['color2']});">
        <div style="font-size:40px;">{data_r['emoji']}</div>
        <div class="seccion-titulo-txt">{data_r['nombre'].upper()}</div>
        <div class="seccion-sub">{data_r['desc']}</div>
    </div>
    """, unsafe_allow_html=True)

    # Botón volver
    if st.button("← Volver al inicio", key="btn_volver"):
        st.session_state.seccion = "portada"
        st.rerun()

    st.write("")

    pdfs = data_r.get("pdfs", [])

    if not pdfs:
        st.markdown(f"""
        <div style="background:#f9f9f9; border-radius:14px; padding:30px;
                    text-align:center; color:#aaa;">
            <div style="font-size:40px;">🚧</div>
            <div style="font-size:16px; font-weight:700; margin-top:8px;">Próximamente</div>
            <div style="font-size:13px; margin-top:4px;">
                Los recursos de este ramo estarán disponibles pronto.
            </div>
        </div>
        """, unsafe_allow_html=True)
        return

    for pdf_meta in pdfs:
        pdf_path = pdf_dir / pdf_meta["archivo"]

        st.markdown(f"""
        <div class="pdf-card">
            <div class="pdf-icon">{pdf_meta['icono']}</div>
            <div>
                <div class="pdf-nombre">{pdf_meta['nombre']}</div>
                <div class="pdf-desc">{pdf_meta['desc']}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        if pdf_path.exists():
            with open(pdf_path, "rb") as f:
                st.download_button(
                    label=f"⬇️ Descargar {pdf_meta['nombre']}",
                    data=f,
                    file_name=pdf_meta["archivo"],
                    mime="application/pdf",
                    key=f"dl_{pdf_meta['archivo']}",
                    use_container_width=True,
                )
        else:
            st.warning(f"Archivo no encontrado: {pdf_meta['archivo']}")

    st.markdown("""
    <div style="text-align:center; margin-top:20px; color:#ccc; font-size:11px;">
        Ferrán · USM · 2026 🐒
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# ROUTER
# ─────────────────────────────────────────────────────────────────────────────
seccion = st.session_state.seccion

if seccion == "portada":
    render_portada()
elif seccion in RAMOS:
    render_seccion(seccion)
else:
    st.session_state.seccion = "portada"
    st.rerun()
