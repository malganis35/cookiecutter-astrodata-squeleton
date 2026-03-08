name: Rapport de Bug
description: Signaler un comportement inattendu ou une erreur.
labels: ["bug"]
body:
  - type: textarea
    id: description
    attributes:
      label: Description du bug
      description: Un résumé clair et concis du problème.
    validations:
      required: true
  - type: textarea
    id: reproduction
    attributes:
      label: Étapes pour reproduire
      description: |
        1. Upload de tel fichier...
        2. Sélection de telle colonne...
        3. Clic sur ...
        4. Erreur constatée.
    validations:
      required: true
  - type: textarea
    id: expected
    attributes:
      label: Comportement attendu
      description: Ce que vous auriez dû voir.
  - type: textarea
    id: context
    attributes:
      label: Contexte technique
      description: Version Python, OS, Navigateur, etc.
  - type: input
    id: version
    attributes:
      label: Version du package
      placeholder: ex: 0.1.0
