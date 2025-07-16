# Flask App Project

This repository contains multiple Flask applications and related resources, organized into different folders for various phases and examples. Below is an overview of the project structure and the purpose of each file and folder.

## Project Structure

```
flask_app/
├── app.py
├── app2.py
├── flask_using_jinja/
│   ├── app.py
│   └── templates/
│       ├── base.html
│       └── profile.html
├── know.txt
├── phase-3/
│   ├── app.py
│   ├── forms.py
│   └── templates/
│       ├── base.html
│       ├── register.html
│       ├── success.html
│       └── thankyou.html
├── phase-4-Advance/
├── phase2/
│   ├── app.py
│   └── templates/
│       ├── login.html
│       └── welcome.html
├── templates/
│   ├── home.html
│   └── welcome.html
├── testing/
│   ├── app.py
│   └── templates/
│       ├── about.html
│       ├── contact.html
│       ├── index.html
│       └── thankyou.html
├── venv/
└── ...
```

## Folder and File Descriptions

- **app.py, app2.py**: Standalone Flask application scripts for different demos or experiments.

- **flask_using_jinja/**: Contains a Flask app demonstrating Jinja templating.
  - `app.py`: Main Flask app for this example.
  - `templates/`: Jinja2 HTML templates for the app.
    - `base.html`, `profile.html`: Template files.

- **know.txt**: Likely a notes or knowledge file (custom content).

- **phase-3/**: Contains a more advanced Flask app with forms and templates.
  - `app.py`: Main application script.
  - `forms.py`: WTForms or Flask-WTF form definitions.
  - `templates/`: HTML templates for registration, success, and thank you pages.

- **phase-4-Advance/**: Placeholder for further advanced phase (currently empty or not listed in detail).

- **phase2/**: Contains another phase of the Flask app.
  - `app.py`: Main application script.
  - `templates/`: HTML templates for login and welcome pages.

- **templates/**: Shared or global templates for the project.
  - `home.html`, `welcome.html`: HTML template files.

- **testing/**: Contains a Flask app for testing purposes.
  - `app.py`: Main application script for testing.
  - `templates/`: HTML templates for about, contact, index, and thank you pages.

- **venv/**: Python virtual environment directory. Contains all installed dependencies and should not be modified directly.

## How to Run

1. **Set up the virtual environment** (if not already):
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # or
   source venv/bin/activate  # On Unix/Mac
   ```
2. **Install dependencies** (if requirements.txt is available):
   ```bash
   pip install -r requirements.txt
   ```
3. **Run a Flask app**:
   ```bash
   python app.py
   # or for a specific phase:
   python phase-3/app.py
   ```

## Notes
- Each subfolder may represent a different phase or example of using Flask.
- The `venv/` folder is for local development and should not be committed to version control.
- Template files are used for rendering HTML pages with Flask and Jinja2.

---

Feel free to explore each folder for more details on the specific Flask app implementations. 