# Contributing to api-practice

Thank you for your interest in contributing to this FastAPI-based project! Your help is appreciated. Please follow the guidelines below to ensure a smooth contribution process.

## Getting Started

1. **Fork the repository** and clone it to your local machine.
2. **Create a new branch** for your feature or bugfix:
   ```bash
   git checkout -b your-feature-name
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Coding Guidelines

- Follow PEP8 standards for Python code.
- Keep functions and endpoints clear and well-documented.
- For JavaScript, HTML, and CSS changes (in `static/`), ensure code is clean and organized.
- Add or update tests in the `tests/` directory as appropriate.

## Making Changes

- Update the documentation (`README.md`, etc.) if your changes require it.
- Ensure the app runs without errors:
  ```bash
  uvicorn main:app --reload
  ```
- Run tests to verify your change:
  ```bash
  pytest
  ```

## Submitting Changes

1. **Commit your changes** with a descriptive message:
   ```bash
   git add .
   git commit -m "Add new feature: description"
   ```
2. **Push to your fork** and submit a Pull Request (PR) to the `main` branch.
3. In your PR, describe what you changed and why. Reference any related issues.

## Code of Conduct

By participating, you agree to uphold a respectful and welcoming environment.

## Reporting Issues

Found a bug or have a feature request? Please open an issue with clear steps to reproduce or a detailed description of your suggestion.

## Need Help?

If you have questions, open an issue or contact the repository owner directly via GitHub.

---

Thank you for contributing!
