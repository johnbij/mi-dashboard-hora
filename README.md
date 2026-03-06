# 📚 Ferran — Guía de configuración

## ¿Tengo que configurar algo?

**Sí, solo un paso**: necesitas crear el archivo de secretos de Streamlit con tu
token de GitHub. La aplicación **no usa Supabase** — todo funciona directamente
con la API de GitHub.

---

## Pasos para poner en marcha la app

### 1. Crear un Token de GitHub

1. Inicia sesión en [github.com](https://github.com) con tu cuenta.
2. Ve a **Settings → Developer settings → Personal access tokens → Tokens (classic)**.
3. Haz clic en **"Generate new token (classic)"**.
4. Dale un nombre, por ejemplo `ferran-app`.
5. En **"Select scopes"** marca únicamente `repo` (acceso completo al repositorio).
6. Haz clic en **"Generate token"** y **copia el token** (empieza por `ghp_…`).
   > ⚠️ Solo lo verás una vez. Guárdalo antes de cerrar la página.

---

### 2. Crear el archivo de secretos

En la raíz del proyecto crea la carpeta `.streamlit` (si no existe) y dentro
crea el archivo `secrets.toml`:

```
ferran/
└── .streamlit/
    └── secrets.toml   ← créalo tú (no está en el repo por seguridad)
```

Contenido de `secrets.toml` (reemplaza el token con el tuyo):

```toml
[github]
token = "ghp_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
repo  = "johnbij/ferran"
```

> Puedes copiar la plantilla que ya está en `.streamlit/secrets.toml.example`.

---

### 3. Si despliegas en Streamlit Community Cloud

No uses `secrets.toml` — en su lugar:

1. Ve a tu app en [share.streamlit.io](https://share.streamlit.io).
2. Abre **"Settings" → "Secrets"**.
3. Pega exactamente el mismo contenido TOML:

```toml
[github]
token = "ghp_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
repo  = "johnbij/ferran"
```

4. Haz clic en **"Save"** y reinicia la app.

---

### 4. Verificar que funciona

- Abre la aplicación.
- Sube cualquier archivo con el componente **"Subir archivo al repositorio"**.
- Haz clic en **"📤 Confirmar subida"**.
- Deberías ver el mensaje ✅ y el archivo aparecerá en la carpeta
  `recién subidos/` de tu repositorio de GitHub.
- Usa el botón **"🗂️ Ver Recién Subidos"** para listar y descargar los archivos.

---

## ¿Por qué no Supabase?

La app usa la **API de GitHub** directamente (biblioteca `PyGithub`) para leer
y escribir archivos en el repositorio. No necesitas ninguna cuenta ni
configuración de Supabase.

---

## Requisitos

Las dependencias ya están en `requirements.txt`:

```
streamlit
matplotlib
pytz
streamlit-autorefresh
PyGithub>=1.58.0
```

Para instalarlas localmente:

```bash
pip install -r requirements.txt
```

Para ejecutar la app localmente:

```bash
streamlit run main.py
```
