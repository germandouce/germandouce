# 👋 Hola, soy Germán

Esta repo ahora está pensada como **portada/showcase** para mostrar tu perfil técnico de forma rápida.

## 🚀 Qué muestra esta portada

- Tu resumen profesional.
- Lenguajes y herramientas que manejas.
- Proyectos destacados.
- Formas de contacto.

## 🧰 Stack (ejemplo)

`Python` · `JavaScript` · `TypeScript` · `SQL` · `Git` · `Docker`

## 📌 Proyectos destacados (ejemplo)

- **API de Inventario** — FastAPI + PostgreSQL + Docker
- **Dashboard de métricas** — React + TypeScript + Charts
- **Automatizaciones internas** — Python + GitHub Actions

## 🛠️ Generador de portada por CLI

También dejé un pequeño generador en Python para crear una bio corta en Markdown desde terminal.

```bash
python3 src/main.py \
  --name "Germán" \
  --role "Backend Developer" \
  --skills "Python,FastAPI,PostgreSQL,Docker"
```

Ejemplo de salida:

```markdown
# 👋 Hola, soy Germán

**Backend Developer**

## 🧰 Stack
- Python
- FastAPI
- PostgreSQL
- Docker
```

## ✅ Tests

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
```
