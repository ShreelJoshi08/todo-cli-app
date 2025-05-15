# Notes API

A simple Flask-based Notes API.

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the app:
   ```
   python app.py
   ```

## Endpoints

- `GET /notes` - List all notes
- `GET /notes/<id>` - Get a note by ID
- `POST /notes` - Create a new note (`{"title": "...", "content": "..."}`)
- `PUT /notes/<id>` - Update a note
- `DELETE /notes/<id>` - Delete a note