# Data Knowledge Center
![Build Status](https://img.shields.io/badge/Made%20with-Sphinx-1f425f.svg)

![Build Status](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Build Status](https://img.shields.io/badge/HTML-239120?style=for-the-badge&logo=html5&logoColor=white)
![Build Status](https://img.shields.io/badge/GitLab-330F63?style=for-the-badge&logo=gitlab&logoColor=white)
![Build Status](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)

## Description

The **Data Knowledge Center** is a documentation website generated using **Sphinx**. It is designed to host project documentation and includes a built-in tutorial for learning Sphinx commands and reStructuredText (RST) syntax.

The site is configured for automatic deployment via **GitLab Pages**, providing a centralized hub for team knowledge and project specifications.

---

## 🛠 Main Commands to Remember

| Action | Command |
| --- | --- |
| **Install environment** | `make dev-install` |
| **Local live preview** | `make livehtml` |
| **Build HTML locally** | `make html` |
| **Build PDF (LaTeX)** | `make pdf_build` |
| **Build PDF (SimplePDF)** | `make simplepdf_build` |
| **Clean build artifacts** | `make clean` |

---

## 📥 Installation & Setup

### Pre-requirements

To use this template, you must have the following installed on your computer:

* [Python](https://www.python.org/) (>= 3.12) 
* [uv](https://www.google.com/search?q=https://astral.sh/uv/) (Package manager) 


### Project Installation

1. **Clone the repository**: `git clone <repository_url>` 
2. **Initialize the environment**:

```bash
make dev-install
```

---

## 🚀 Usage

### Local Development

You can automatically build and preview changes in real-time using `sphinx-autobuild`:

```bash
make livehtml
```

The documentation will be available locally (typically at `http://127.0.0.1:8001`).

### Building PDFs

The project supports two methods for PDF generation. Both commands require prerequisite tools to work smoothly.

#### 1. LaTeX (High Quality & Customizable)
This process uses the `xelatex` engine and relies on specific fonts (like DejaVu Sans) defined in the corporate theme.
* **For Ubuntu/Debian users**, you can install all necessary dependencies automatically using:
  ```bash
  make latex_setup
  ```
  *(This runs `apt install` for `texlive-xetex`, `texlive-fonts-recommended` (which provides the DejaVu font), `latexmk`, and `fonts-liberation`)*

* **For other operating systems (macOS, Windows, Fedora)**, ensure you manually install a full TeX distribution (like TeX Live, MiKTeX, or MacTeX) that includes:
  - `xelatex` and `latexmk` engines
  - The `texlive-fonts-recommended` package (critical for the DejaVu Sans font)

Once the prerequisites are met, build the PDF with:
```bash
make pdf_build
```

#### 2. SimplePDF
A lighter alternative using the Python `sphinx-simplepdf` library. No local LaTeX installation is required.
```bash
make simplepdf_build
```


### CI/CD Deployment

This project is pre-configured for **GitLab Pages**. Every push to the `main` branch triggers the GitLab CI pipeline:

* **Build**: Compiles RST files into HTML using `uv`.
* **Deploy**: Publishes the `public` folder to the GitLab Pages URL.
* **Azure (Optional)**: Manual deployment to Azure Static Web Apps is also supported.

---

## 📂 Project Structure

```text
knowledge_center/
    ├── conf.py              # Sphinx configuration (extensions, themes, LaTeX)
    ├── index.rst            # Root documentation file
    ├── Makefile             # Automation commands
    ├── pyproject.toml       # Python dependencies and project metadata
    ├── docs/                # Documentation source files
    └── sphinx_quickstart/   # Basic Sphinx tutorial
    ├── .gitlab/             # Issue and Merge Request templates
    └── .github/             # GitHub Actions workflows
```

## 🎨 Customizing the Graphic Chart

To personalize the documentation and make it match your organization's branding (especially for PDF / LaTeX generation), follow these steps:

### 1. Update Graphics & Logos
The images used for the PDF generation are stored in the `_static/pdf/` directory. Simply replace the following files with your own while keeping the same dimensions/formats for best results:
* `logo.png`: Main logo used on the cover and headers.
* `background.png`: Background image for the cover page.
* `page-background.pdf`: Background watermark used across all PDF pages.

### 2. Update Colors & Fonts
To modify the corporate color palette and styling for the LaTeX PDFs, open `conf.py` and locate the `latex_elements` dictionary. You can define your own HEX colors in the preamble under the `%%% --- Palette corporate ---` section:

```latex
\definecolor{CorpPrimary}{HTML}{E2001A}
\definecolor{CorpBlack}{HTML}{000000}
\definecolor{CorpGrey}{HTML}{666666}
```

You can also adjust the HTML theme settings directly inside the `html_theme_options` variable in `conf.py`.

---

## 🤝 Contributing

The project includes standard templates for structured collaboration:

* **Issue Templates**: Bug reports, Task tracking, Workshop minutes (CR), and Project Committee prep.
* **Merge Requests**: A standardized `MR.md` template including walkthroughs and visual sequence diagrams.


### Code Quality

Before committing, run pre-commit hooks to ensure code consistency:

```bash
make pc
```

This runs `ruff` for linting/formatting and checks for common file issues

---

## 📜 License

{% if cookiecutter.open_source_license == 'MIT' -%}
This project is licensed under the terms of the MIT License.
{% elif cookiecutter.open_source_license == 'BSD-3-Clause' -%}
This project is licensed under the terms of the BSD 3-Clause License.
{% elif cookiecutter.open_source_license == 'No license file' -%}
**Proprietary License**. Copyright © {% now 'utc', '%Y' %} {{ cookiecutter.author_name }}. All rights reserved.    
Permission to use is granted only to authorized clients.
{% else -%}
This project is licensed under the terms of the {{ cookiecutter.open_source_license }} license.
{% endif -%}
