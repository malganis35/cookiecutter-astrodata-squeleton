FROM python:{{ cookiecutter.python_version }}-slim

# Installer uv
RUN pip install uv

# Définir le dossier de travail
WORKDIR /app
ENV PYTHONPATH=/app/src

# Copier le fichier des dépendances
COPY pyproject.toml ./

# Compiler les dépendances en requirements.txt et les installer
RUN uv pip compile pyproject.toml > requirements.txt && \
    uv pip install --system -r requirements.txt && \
    rm requirements.txt

# Copier le reste de l'application
COPY . .

# Lancer l'API
CMD ["uvicorn", "{{ cookiecutter.package_name }}.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
