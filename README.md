# Text Generation Frontend (LSTM-style)

Minimal HTML/CSS/JS frontend + Python Flask backend.

## Features
- Frontend form for `prompt` + `length`
- `/generate` endpoint returns `generated_text`
- Pseudo-LSTM generation (random next words from base corpus)

## Setup
1. Create a venv:

   python -m venv venv
   .\\venv\\Scripts\\activate

2. Install dependencies:

   pip install -r requirements.txt

3. Run app:

   python app.py

4. Open in browser:

   http://127.0.0.1:5000

## Notes
- This implementation is frontend-focused and does not train an actual LSTM.
- It is intended for a demo that behaves like text generation in a prototype.
