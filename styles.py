import streamlit as st


def aplicar_estilos():
    st.markdown("""
    <style>
    /* ============================================================
       BASE – Desktop-first, luego responsive
       ============================================================ */

    /* --- TIPOGRAFÍA GLOBAL --- */
    .stMarkdown p, .stMarkdown li, .stMarkdown td, .stMarkdown th {
        font-size: 17px !important;
        line-height: 1.7 !important;
    }
    .stMarkdown h1 { font-size: 26px !important; }
    .stMarkdown h2 { font-size: 22px !important; }
    .stMarkdown h3 { font-size: 19px !important; }

    /* --- HEADER AZUL / ROJO (countdown) --- */
    .header-azul {
        background: linear-gradient(135deg, #6C63FF, #3b71ca);
        padding: 15px; border-radius: 15px 15px 0 0;
        color: white; text-align: center;
    }
    .titulo-header { font-size: 20px; font-weight: bold; margin-bottom: 5px; }
    .info-header   { font-size: 14px; opacity: 0.9; }
    .header-rojo {
        background: linear-gradient(135deg, #e74c3c, #cc0000);
        padding: 10px; color: white;
        display: flex; justify-content: space-around;
        border-radius: 0 0 15px 15px;
    }
    .timer-item { font-size: 16px; font-weight: bold; }

    /* --- BARRA DE NAVEGACIÓN 🏠 / N / A / G / D --- */
    [data-testid="stHorizontalBlock"] {
        display: flex !important; flex-direction: row !important;
        flex-wrap: nowrap !important; gap: 4px !important;
    }
    [data-testid="stHorizontalBlock"] > div {
        flex: 1 1 0% !important; min-width: 0 !important;
    }
    [data-testid="stHorizontalBlock"] button {
        width: 100% !important;
        min-height: 70px !important;
        font-size: 22px !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        background-color: #1a1a2e !important;
        color: white !important;
        border: none !important;
    }

    /* --- BOTONES DE LISTA DE CLASES --- */
    .cat-container div.stButton > button {
        min-height: 85px !important; border-radius: 12px !important;
        margin-bottom: 10px !important; width: 100% !important;
        font-size: 22px !important; text-align: left !important;
        padding-left: 20px !important; border: 1px solid #e0e0e0 !important;
        box-shadow: 0px 2px 4px rgba(0,0,0,0.05) !important;
    }

    /* --- BOTÓN PDF --- */
    .pdf-btn div.stButton > button {
        background: linear-gradient(135deg, #6C63FF, #4a0e8f) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        min-height: 65px !important;
        font-size: 18px !important;
        font-weight: bold !important;
    }

    /* --- BOTÓN FLOTANTE HOME --- */
    .fab-home {
        position: fixed !important; bottom: 25px !important; right: 25px !important;
        background: linear-gradient(135deg, #6C63FF, #0f3460) !important;
        color: white !important; border: none !important; border-radius: 50px !important;
        padding: 14px 20px !important; font-size: 20px !important; font-weight: bold !important;
        cursor: pointer !important; box-shadow: 0 4px 15px rgba(0,0,0,0.3) !important;
        z-index: 9999 !important; display: flex !important; align-items: center !important;
        gap: 8px !important; text-decoration: none !important;
        transition: transform 0.2s, box-shadow 0.2s !important;
    }
    .fab-home:hover {
        transform: scale(1.05) !important;
        box-shadow: 0 6px 20px rgba(0,0,0,0.4) !important;
    }
    .fab-container div.stButton > button {
        position: fixed !important; bottom: 25px !important; right: 25px !important;
        background: linear-gradient(135deg, #6C63FF, #0f3460) !important;
        color: white !important; border: none !important; border-radius: 50px !important;
        padding: 14px 24px !important; font-size: 18px !important; font-weight: bold !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.35) !important; z-index: 9999 !important;
        min-height: unset !important; width: auto !important;
    }

    /* --- CRONÓMETRO --- */
    .crono-digital {
        font-family: 'Courier New', monospace;
        font-size: 35px; font-weight: bold;
        color: #6C63FF; text-align: center;
        width: 100%; display: block;
    }

    /* ============================================================
       RESPONSIVE – Pantallas ≤ 768 px (móviles)
       ============================================================ */
    @media (max-width: 768px) {
        /* Tipografía más compacta */
        .stMarkdown p, .stMarkdown li, .stMarkdown td, .stMarkdown th {
            font-size: 15px !important;
            line-height: 1.6 !important;
        }
        .stMarkdown h1 { font-size: 22px !important; }
        .stMarkdown h2 { font-size: 19px !important; }
        .stMarkdown h3 { font-size: 17px !important; }

        /* Header más compacto */
        .header-azul { padding: 10px; border-radius: 12px 12px 0 0; }
        .titulo-header { font-size: 16px; }
        .info-header   { font-size: 12px; }
        .header-rojo   { padding: 8px; border-radius: 0 0 12px 12px; }
        .timer-item    { font-size: 14px; }

        /* Navegación: botones más pequeños */
        [data-testid="stHorizontalBlock"] { gap: 3px !important; }
        [data-testid="stHorizontalBlock"] button {
            min-height: 44px !important;
            font-size: 15px !important;
            border-radius: 8px !important;
            padding: 4px 2px !important;
        }

        /* Botones de subcategoría y lista */
        .cat-container div.stButton > button {
            min-height: 60px !important;
            font-size: 16px !important;
            padding-left: 12px !important;
        }

        /* Botón PDF */
        .pdf-btn div.stButton > button {
            min-height: 50px !important;
            font-size: 15px !important;
        }

        /* Cronómetro */
        .crono-digital { font-size: 26px; }

        /* FAB más pequeño */
        .fab-home, .fab-container div.stButton > button {
            bottom: 16px !important; right: 16px !important;
            padding: 10px 16px !important; font-size: 16px !important;
        }

        /* Bienvenida hero */
        .bienvenida-hero { padding: 30px 16px !important; border-radius: 16px !important; }
        .bienvenida-dragon { font-size: 64px !important; }
        .bienvenida-titulo { font-size: 24px !important; letter-spacing: 1px !important; }
        .bienvenida-lema   { font-size: 16px !important; }
        .bienvenida-sub    { font-size: 15px !important; }

        /* Tarjetas de eje */
        .card-eje { padding: 14px !important; font-size: 14px !important; border-radius: 12px !important; }

        /* Sección título */
        .seccion-titulo { font-size: 18px !important; }

        /* Pills */
        .pill { font-size: 13px !important; padding: 5px 12px !important; }

        /* PDF cards */
        .pdf-card {
            padding: 14px 12px !important;
            border-radius: 12px !important;
            gap: 10px !important;
            flex-direction: column !important;
            text-align: center !important;
        }
        .pdf-icon { font-size: 28px !important; }
        .pdf-nombre { font-size: 14px !important; }
        .pdf-desc { font-size: 12px !important; }

        /* Proximamente card */
        .prox-card { padding: 30px 16px !important; border-radius: 16px !important; }
        .prox-icon { font-size: 50px !important; }
        .prox-codigo { font-size: 22px !important; }
        .prox-titulo { font-size: 15px !important; }
        .prox-badge  { font-size: 13px !important; padding: 6px 16px !important; }

        /* Matplotlib / imágenes responsive */
        .stImage, .stPlotlyChart, [data-testid="stImage"] {
            max-width: 100% !important;
            overflow-x: auto !important;
        }
        .stImage img, [data-testid="stImage"] img {
            max-width: 100% !important;
            height: auto !important;
        }

        /* Tablas responsive */
        .stMarkdown table { font-size: 13px !important; display: block; overflow-x: auto; }

        /* Ocultar sidebar por defecto en móvil (Streamlit ya lo hace,
           pero aseguramos que el botón sea visible) */
        [data-testid="stSidebar"] { min-width: 0 !important; }

        /* Contenido principal sin padding excesivo */
        .stMainBlockContainer, .block-container {
            padding-left: 1rem !important;
            padding-right: 1rem !important;
        }
    }

    /* ============================================================
       RESPONSIVE – Pantallas ≤ 480 px (móviles pequeños)
       ============================================================ */
    @media (max-width: 480px) {
        .stMarkdown p, .stMarkdown li { font-size: 14px !important; }
        .stMarkdown h1 { font-size: 20px !important; }
        .stMarkdown h2 { font-size: 18px !important; }
        .stMarkdown h3 { font-size: 16px !important; }

        .titulo-header { font-size: 14px !important; }
        .bienvenida-dragon { font-size: 50px !important; }
        .bienvenida-titulo { font-size: 20px !important; }
        .crono-digital { font-size: 22px !important; }

        [data-testid="stHorizontalBlock"] button {
            min-height: 40px !important;
            font-size: 13px !important;
        }

        .stMainBlockContainer, .block-container {
            padding-left: 0.5rem !important;
            padding-right: 0.5rem !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)


def css_boton_subcat(key, color_hex):
    """Inyecta CSS justo antes del botón usando su key como selector aria-label."""
    st.markdown(f"""
    <style>
    button[kind="secondary"][data-testid="baseButton-secondary"]:has(+ *),
    div.stButton:has(> button[aria-label="{key}"]) > button,
    div.stButton > button[title="{key}"] {{
        background-color: {color_hex} !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        min-height: 75px !important;
        font-size: 17px !important;
        font-weight: bold !important;
        width: 100% !important;
        margin-bottom: 10px !important;
    }}
    </style>
    """, unsafe_allow_html=True)
