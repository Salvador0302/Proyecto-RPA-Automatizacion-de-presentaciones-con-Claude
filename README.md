# Proyecto RPA - Automatización de Presentaciones con Claude

Este proyecto automatiza la creación de presentaciones PowerPoint utilizando la API de Claude AI. Convierte archivos LaTeX y texto plano a presentaciones profesionales.

## 📋 Estructura del Proyecto

```
Proyecto-RPA-Automatizacion-de-presentaciones-con-Claude/
├─ README.md
├─ .gitignore
├─ requirements.txt
├─ scripts/
│  ├─ latex_to_pptx.py      # Conversor de LaTeX a PowerPoint
│  └─ text_to_pptx.py        # Conversor de texto a PowerPoint
├─ claude/
│  └─ claude_integration.py  # Integración con Claude API
├─ examples/
│  ├─ presentation.tex       # Ejemplo de presentación en LaTeX
│  └─ presentation.pdf       # PDF generado (después de compilar)
└─ LICENSE
```

## 🚀 Características

- ✨ **Generación automática** de presentaciones usando Claude AI
- 📄 **Conversión de LaTeX** (Beamer) a PowerPoint
- 📝 **Conversión de texto plano** a PowerPoint
- 🎨 **Formato profesional** automático
- 🤖 **Mejora de contenido** con IA

## 📦 Instalación

1. Clona el repositorio:
```bash
git clone https://github.com/Salvador0302/Proyecto-RPA-Automatizacion-de-presentaciones-con-Claude.git
cd Proyecto-RPA-Automatizacion-de-presentaciones-con-Claude
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Configura tu API key de Claude:
Crea un archivo `.env` en la raíz del proyecto:
```
ANTHROPIC_API_KEY=tu_api_key_aquí
```

## 💻 Uso

### Generar presentación con Claude AI

```python
from claude.claude_integration import ClaudeIntegration

claude = ClaudeIntegration()
content = claude.generate_presentation_content(
    topic="Inteligencia Artificial",
    num_slides=5,
    style="professional"
)
claude.save_to_file(content, "mi_presentacion.txt")
```

### Convertir texto a PowerPoint

```python
from scripts.text_to_pptx import TextToPptxConverter

converter = TextToPptxConverter()
converter.convert("entrada.txt", "salida.pptx")
```

### Convertir LaTeX a PowerPoint

```python
from scripts.latex_to_pptx import LatexToPptxConverter

converter = LatexToPptxConverter()
converter.convert("presentation.tex", "presentation.pptx")
```

## 📚 Ejemplos

El directorio `examples/` contiene:
- `presentation.tex`: Ejemplo de presentación en LaTeX Beamer
- Archivos generados por los scripts de conversión

## 🛠️ Tecnologías

- **Python 3.7+**
- **python-pptx**: Creación de archivos PowerPoint
- **anthropic**: API de Claude AI
- **python-dotenv**: Gestión de variables de entorno

## 📝 Formato de Entrada

### Formato de Texto
```
# Título Principal
Subtítulo
----
# Diapositiva 2
- Punto 1
- Punto 2
----
# Conclusión
Texto final
```

### LaTeX Beamer
```latex
\begin{frame}{Título}
    \begin{itemize}
        \item Punto 1
        \item Punto 2
    \end{itemize}
\end{frame}
```

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:
1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👤 Autor

**Salvador0302**

## 🙏 Agradecimientos

- Claude AI de Anthropic por la generación de contenido
- python-pptx por la manipulación de PowerPoint
- La comunidad de código abierto

---

⭐ Si este proyecto te resulta útil, considera darle una estrella en GitHub!
