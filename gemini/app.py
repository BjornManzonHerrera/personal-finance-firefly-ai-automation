from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # File validation
        # Save uploaded file
        # Process through OCR
        # Analyze with AI
        # Extract financial data
        # Create Firefly III transaction
        return jsonify({'status': 'success'})
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
