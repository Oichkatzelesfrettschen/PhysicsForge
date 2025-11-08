# PhysicsForge GitHub Pages Site

This directory contains the web-native version of the PhysicsForge document, automatically deployed to GitHub Pages.

## Structure

```
site/
├── index.html           # Main landing page with KaTeX math rendering
├── assets/
│   ├── css/
│   │   └── typography.css   # STIX Two Text fonts + styling
│   └── fonts/              # (Optional) Self-hosted fonts
├── figs/                    # Auto-generated SVG figures (gitignored)
└── pdf/                     # Built PDF (gitignored)
```

## Features

- **Math Rendering**: KaTeX for fast, high-quality math typesetting
- **Typography**: STIX Two Text fonts (CDN or self-hosted)
- **Figures**: SVG with embedded WOFF2 fonts (text remains selectable)
- **Dark Mode**: Automatic via `prefers-color-scheme`
- **Responsive**: Mobile-friendly layout

## Local Development

```bash
# Build PDF and generate SVG figures
make web

# Serve locally
make serve
# Visit http://localhost:8000
```

## Deployment

Automated via GitHub Actions (`.github/workflows/build.yml`):
1. **PDF Build**: LuaLaTeX compilation via `xu-cheng/latex-action@v4`
2. **Figure Generation**: XeLaTeX → XDV → SVG with `dvisvgm --font-format=woff2`
3. **Pages Deploy**: Official `deploy-pages@v4` action

## Font Embedding

SVG figures use **XDV → SVG** workflow (not PDF → SVG) to preserve:
- Selectable text (not converted to paths)
- Embedded WOFF2 webfonts
- Crisp rendering at all zoom levels

See ChatGPT's research summary in project root for technical details.
