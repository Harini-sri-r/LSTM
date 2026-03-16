from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Simple pseudo LSTM-like generator: expand prompt by choosing words from a mini-sentence bank
base_sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "A bright future starts with one single step.",
    "In a world of code, any idea can become real.",
    "Every design begins with a line of text.",
    "Learning algorithms empowers creative projects."
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json or {}
    prompt = data.get('prompt', '').strip()
    length = int(data.get('length', 20))

    if not prompt:
        return jsonify({'error': 'Prompt is required'}), 400

    # Build a pool using words from prompt + base text
    words = []
    for sentence in base_sentences:
        words.extend(sentence.strip('.!?').split())
    words.extend(prompt.split())

    # Build simple bigram transitions for smoother output
    transitions = {}
    all_source_texts = list(base_sentences)
    if prompt:
        all_source_texts.append(prompt)

    for source in all_source_texts:
        tokens = source.strip('.!?').split()
        for i in range(len(tokens) - 1):
            key = tokens[i].lower()
            transitions.setdefault(key, []).append(tokens[i + 1])

    generated = prompt.strip()
    last = generated.split()[-1] if generated.split() else ''

    if not last and words:
        last = random.choice(words)

    for i in range(length):
        # Prefer bigram transition candidates and avoid immediate repeated word
        candidates = []
        key = last.lower() if last else ''
        if key and key in transitions:
            candidates = [w for w in transitions[key] if w.lower() != last.lower()]

        if not candidates:
            candidates = [w for w in words if w.lower() != last.lower()]

        if not candidates:
            candidates = words

        next_word = random.choice(candidates)
        generated += ' ' + next_word
        last = next_word

    # Cap the length and add punctuation
    generated = generated.strip()
    if not generated.endswith(('.', '?', '!')):
        generated += '.'

    return jsonify({'generated_text': generated})

if __name__ == '__main__':
    app.run(debug=True)
