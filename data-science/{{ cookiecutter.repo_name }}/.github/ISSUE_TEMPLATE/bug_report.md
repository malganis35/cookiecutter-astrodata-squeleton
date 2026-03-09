name: Bug Report
description: Report unexpected behavior or an error.
labels: ["bug"]
body:
  - type: textarea
    id: description
    attributes:
      label: Bug Description
      description: A clear and concise summary of the issue.
    validations:
      required: true
  - type: textarea
    id: reproduction
    attributes:
      label: Steps to Reproduce
      description: |
        1. Uploaded specific file...
        2. Selected specific column...
        3. Clicked on...
        4. Error occurred.
    validations:
      required: true
  - type: textarea
    id: expected
    attributes:
      label: Expected Behavior
      description: What you should have seen happen.
  - type: textarea
    id: context
    attributes:
      label: Technical Context
      description: Python version, OS, Browser, etc.
  - type: input
    id: version
    attributes:
      label: Package Version
      placeholder: e.g., 0.1.0