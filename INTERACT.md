# GEMINI - Financial AI OCR Project

## Project Overview

**GEMINI** (Generate Expense Management Intelligence Natively, Independently) is a privacy-focused, self-hosted solution for automatically processing financial documents through AI-powered OCR and natural language understanding. The system allows users to photograph receipts, invoices, and financial documents, which are then processed locally to extract and categorize financial data for automatic entry into Firefly III.

## Architecture

### Core Components

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Web Frontend  │───▶│  Flask Backend  │───▶│   Firefly III   │
│   (HTML/JS)     │    │   (Python)      │    │     (API)       │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                              │
                              ▼
                    ┌─────────────────┐    ┌─────────────────┐
                    │  Tesseract OCR  │    │ Ollama + LLaVA  │
                    │   (Text Extract)│    │ (AI Processing) │
                    └─────────────────┘    └─────────────────┘
```

### Technology Stack

- **Frontend**: HTML5, JavaScript, CSS3 (responsive web interface)
- **Backend**: Flask (Python web framework)
- **OCR Engine**: Tesseract OCR (local text extraction)
- **AI Model**: Ollama with LLaVA (local multimodal AI)
- **Financial API**: Firefly III REST API
- **Platform**: Windows (self-hosted)
- **Storage**: Local filesystem (no cloud dependencies)

## Prerequisites

### System Requirements

- **OS**: Windows 10/11
- **RAM**: Minimum 8GB (16GB recommended for LLaVA)
- **Storage**: 10GB free space (for models and processing)
- **Python**: 3.8+ with pip
- **Network**: Local network access to Firefly III instance

### Required Software

1. **Firefly III** (running locally or on network)
2. **Ollama** (Windows version)
3. **Tesseract OCR** (Windows binaries)
4. **Python 3.8+** with pip

## Installation Guide

### 1. Install Tesseract OCR

```bash
# Download from: https://github.com/UB-Mannheim/tesseract/wiki
# Install to default location: C:\Program Files\Tesseract-OCR
# Add to PATH environment variable
```

### 2. Install Ollama and LLaVA

```bash
# Download Ollama for Windows from: https://ollama.ai
# Install Ollama
ollama pull llava:7b-v1.6

# Verify installation
ollama list
```

### 3. Setup Python Environment

```bash
# Create virtual environment
python -m venv gemini-env
gemini-env\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 4. Configure Environment

Create `.env` file:
```env
# Firefly III Configuration
FIREFLY_URL=http://localhost:8080
FIREFLY_TOKEN=your_personal_access_token_here

# Tesseract Configuration
TESSERACT_PATH=C:\Program Files\Tesseract-OCR\tesseract.exe

# Ollama Configuration
OLLAMA_URL=http://localhost:11434
OLLAMA_MODEL=llava:7b-v1.6

# Application Configuration
FLASK_ENV=development
FLASK_DEBUG=True
UPLOAD_FOLDER=./uploads
MAX_FILE_SIZE=16777216  # 16MB
```

## Project Structure

```
gemini/
├── app.py                 # Flask application entry point
├── requirements.txt       # Python dependencies
├── .env                  # Environment configuration
├── README.md             # Project documentation
├── GEMINI.md             # This development file
├── static/               # Static web assets
│   ├── css/
│   │   └── styles.css    # Application styles
│   ├── js/
│   │   └── app.js        # Frontend JavaScript
│   └── uploads/          # Temporary file storage
├── templates/            # Jinja2 templates
│   ├── index.html        # Main interface
│   ├── upload.html       # File upload page
│   └── results.html      # Processing results
├── src/                  # Core application modules
│   ├── __init__.py
│   ├── ocr_processor.py  # Tesseract OCR integration
│   ├── ai_processor.py   # Ollama/LLaVA integration
│   ├── firefly_client.py # Firefly III API client
│   ├── data_models.py    # Data structures
│   └── utils.py          # Utility functions
├── config/               # Configuration files
│   ├── prompts.py        # AI prompt templates
│   └── categories.py     # Expense categorization rules
└── tests/                # Unit and integration tests
    ├── test_ocr.py
    ├── test_ai.py
    └── test_firefly.py
```

## Key Components

### 1. OCR Processor (`src/ocr_processor.py`)

```python
class TesseractOCR:
    def __init__(self, tesseract_path):
        self.tesseract_path = tesseract_path
    
    def extract_text(self, image_path):
        """Extract text from image using Tesseract"""
        # Image preprocessing
        # Text extraction
        # Confidence scoring
        return extracted_text, confidence_score
    
    def preprocess_image(self, image):
        """Optimize image for OCR"""
        # Noise reduction
        # Contrast enhancement
        # Rotation correction
        return processed_image
```

### 2. AI Processor (`src/ai_processor.py`)

```python
class LLaVAProcessor:
    def __init__(self, ollama_url, model_name):
        self.ollama_url = ollama_url
        self.model_name = model_name
    
    def analyze_receipt(self, image_path, ocr_text):
        """Analyze receipt using LLaVA multimodal AI"""
        # Combine image and OCR text
        # Generate structured prompt
        # Process with LLaVA
        # Parse response into structured data
        return financial_data
    
    def extract_financial_data(self, content):
        """Extract structured financial information"""
        # Amount detection
        # Vendor identification
        # Category classification
        # Date extraction
        return {
            'amount': float,
            'description': str,
            'vendor': str,
            'category': str,
            'date': datetime,
            'type': 'expense|income|transfer'
        }
```

### 3. Firefly III Client (`src/firefly_client.py`)

```python
class FireflyClient:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {'Authorization': f'Bearer {token}'}
    
    def create_transaction(self, transaction_data):
        """Create transaction in Firefly III"""
        # Validate transaction data
        # Format for Firefly III API
        # Submit via REST API
        return transaction_id
    
    def get_accounts(self):
        """Retrieve available accounts"""
        return accounts_list
    
    def get_categories(self):
        """Retrieve available categories"""
        return categories_list
```

### 4. Main Flask Application (`app.py`)

```python
from flask import Flask, request, render_template, jsonify
from src.ocr_processor import TesseractOCR
from src.ai_processor import LLaVAProcessor
from src.firefly_client import FireflyClient

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    # File validation
    # Save uploaded file
    # Process through OCR
    # Analyze with AI
    # Extract financial data
    # Create Firefly III transaction
    return jsonify(result)

@app.route('/api/accounts')
def get_accounts():
    return jsonify(firefly_client.get_accounts())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

## Development Phases

### Phase 1: Core Infrastructure (Week 1-2)

**Objectives**:
- Set up development environment
- Implement basic Flask application
- Configure Tesseract OCR integration
- Test Ollama/LLaVA connectivity

**Deliverables**:
- Working Flask server
- OCR text extraction from images
- Basic LLaVA prompt processing
- Simple web interface for file upload

**Tasks**:
1. Initialize Flask project structure
2. Create basic HTML upload interface
3. Implement file handling and validation
4. Integrate Tesseract OCR with image preprocessing
5. Set up Ollama communication layer
6. Create basic prompt templates for financial document analysis

### Phase 2: AI Processing Pipeline (Week 3-4)

**Objectives**:
- Develop intelligent financial data extraction
- Implement transaction categorization
- Create confidence scoring system
- Build data validation layer

**Deliverables**:
- Structured financial data extraction
- Category classification system
- Amount and date recognition
- Vendor identification

**Tasks**:
1. Design prompt engineering for financial document analysis
2. Implement multimodal processing (image + OCR text)
3. Create data validation and sanitization
4. Build confidence scoring for extracted data
5. Develop fallback mechanisms for low-confidence extractions
6. Test with various receipt/invoice formats

### Phase 3: Firefly III Integration (Week 5-6)

**Objectives**:
- Complete Firefly III API integration
- Implement transaction creation workflow
- Add account and category management
- Create error handling and retry logic

**Deliverables**:
- Full Firefly III API client
- Automated transaction creation
- Account mapping interface
- Error recovery system

**Tasks**:
1. Complete Firefly III REST API client
2. Implement transaction formatting and validation
3. Create account selection interface
4. Add category mapping and creation
5. Build error handling for API failures
6. Implement transaction review before submission

### Phase 4: User Experience & Polish (Week 7-8)

**Objectives**:
- Enhance user interface
- Add batch processing capabilities
- Implement logging and monitoring
- Create user configuration options

**Deliverables**:
- Polished web interface
- Batch upload functionality
- Configuration dashboard
- Processing history and logs

**Tasks**:
1. Enhance frontend with progress indicators
2. Add batch file processing
3. Create transaction review and editing interface
4. Implement user settings and preferences
5. Add processing history and audit trail
6. Create comprehensive error reporting

## API Specifications

### Internal API Endpoints

#### File Processing
```http
POST /api/process
Content-Type: multipart/form-data

{
  "file": <image_file>,
  "account_id": "optional_account_id",
  "auto_submit": false
}

Response:
{
  "status": "success|error",
  "transaction_data": {
    "amount": 25.50,
    "description": "Grocery Store Purchase",
    "vendor": "SuperMart",
    "category": "Groceries",
    "date": "2025-09-01",
    "confidence": 0.95
  },
  "firefly_transaction_id": "123",
  "processing_time": 2.3
}
```

#### Account Management
```http
GET /api/accounts
Response: [{"id": "1", "name": "Checking", "type": "asset"}]

GET /api/categories  
Response: [{"id": "1", "name": "Groceries"}]
```

### Firefly III API Usage

```python
# Transaction creation format
transaction_payload = {
    "error_if_duplicate_hash": True,
    "apply_rules": True,
    "fire_webhooks": True,
    "group_title": None,
    "transactions": [{
        "type": "withdrawal",  # or "deposit", "transfer"
        "date": "2025-09-01T10:37:17+01:00",
        "amount": "25.50",
        "description": "Grocery Store Purchase",
        "source_id": "1",  # Asset account ID
        "destination_name": "SuperMart",
        "category_name": "Groceries",
        "tags": ["ai-processed", "receipt-scan"]
    }]
}
```

## Configuration

### AI Prompts (`config/prompts.py`)

```python
FINANCIAL_ANALYSIS_PROMPT = """
Analyze this financial document image and extracted text to identify:

1. Transaction Type: expense, income, or transfer
2. Amount: exact monetary value
3. Vendor/Payee: business or person name
4. Date: transaction date
5. Category: expense/income category
6. Description: brief transaction description

OCR Text: {ocr_text}

Respond in JSON format:
{
  "type": "expense|income|transfer",
  "amount": 0.00,
  "vendor": "string",
  "date": "YYYY-MM-DD",
  "category": "string", 
  "description": "string",
  "confidence": 0.0-1.0
}
"""
```

### Category Mapping (`config/categories.py`)

```python
CATEGORY_KEYWORDS = {
    "Groceries": ["supermarket", "grocery", "food", "walmart", "target"],
    "Restaurants": ["restaurant", "cafe", "bar", "pizza", "mcdonalds"],
    "Transportation": ["gas", "fuel", "uber", "taxi", "parking"],
    "Utilities": ["electric", "water", "internet", "phone", "cable"],
    "Healthcare": ["pharmacy", "doctor", "hospital", "medical", "cvs"]
}
```

## Security Considerations

### Privacy Features
- **Local Processing**: All OCR and AI processing happens locally
- **No Cloud Dependencies**: No external API calls for sensitive data
- **Encrypted Storage**: Option to encrypt uploaded files
- **Secure Deletion**: Automatic cleanup of processed images

### Security Measures
```python
# File validation
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf'}
MAX_FILE_SIZE = 16 * 1024 * 1024  # 16MB

# Input sanitization
def sanitize_input(data):
    # Remove potential injection attacks
    # Validate data types and ranges
    return clean_data

# Firefly III token protection
def mask_token(token):
    return f"{token[:8]}{'*' * 20}{token[-4:]}"
```

## Performance Optimization

### Image Processing
- **Preprocessing Pipeline**: Resize, denoise, enhance contrast
- **Format Optimization**: Convert to optimal format for OCR
- **Caching**: Cache processed results for duplicate uploads

### AI Processing
- **Model Warm-up**: Keep LLaVA model loaded in memory
- **Batch Processing**: Process multiple images efficiently
- **Fallback Strategy**: Use OCR-only mode if AI is unavailable

### Memory Management
```python
# Cleanup strategy
def cleanup_temp_files():
    # Remove files older than 1 hour
    # Clear processing cache
    # Free up memory resources
```

## Testing Strategy

### Unit Tests
- OCR accuracy testing with sample receipts
- AI prompt validation and response parsing
- Firefly III API integration testing
- File upload and validation testing

### Integration Tests
- End-to-end workflow testing
- Error handling and recovery
- Performance benchmarking
- Cross-browser compatibility

### Test Data
```
tests/
├── sample_receipts/
│   ├── grocery_receipt_01.jpg
│   ├── restaurant_bill_01.pdf
│   ├── gas_station_receipt_01.png
│   └── utility_bill_01.jpg
├── expected_outputs/
│   └── receipt_01_expected.json
└── mock_responses/
    └── firefly_api_responses.json
```

## Deployment

### Local Development Setup

```bash
# 1. Clone repository
git clone <repository_url>
cd gemini

# 2. Setup environment
python -m venv gemini-env
gemini-env\Scripts\activate
pip install -r requirements.txt

# 3. Configure environment
copy .env.example .env
# Edit .env with your settings

# 4. Start services
ollama serve
python app.py

# 5. Access application
# Navigate to http://localhost:5000
```

### Production Deployment

```bash
# Use Waitress WSGI server for Windows
pip install waitress

# Production startup script
waitress-serve --host=0.0.0.0 --port=5000 app:app
```

## Monitoring and Maintenance

### Logging Configuration
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('gemini.log'),
        logging.StreamHandler()
    ]
)
```

### Health Checks
- Tesseract OCR availability
- Ollama service status
- Firefly III API connectivity
- Disk space monitoring
- Model performance metrics

### Backup Strategy
- Regular backup of configuration files
- Export processing logs
- Backup custom category mappings
- Document API token management

## Troubleshooting

### Common Issues

**OCR Not Working**:
- Verify Tesseract installation path
- Check image quality and format
- Ensure proper PATH environment variable

**LLaVA Model Issues**:
- Confirm Ollama service is running
- Verify model is downloaded: `ollama list`
- Check system memory availability

**Firefly III Connection**:
- Validate API token permissions
- Confirm Firefly III URL accessibility
- Check network connectivity

**File Upload Problems**:
- Verify file size limits
- Check file format restrictions
- Ensure upload directory permissions

## Future Enhancements

### Planned Features
- **Multi-language OCR**: Support for non-English receipts
- **Receipt Templates**: Custom parsing for specific vendors
- **Bulk Processing**: Batch upload and processing
- **Mobile App**: Companion mobile application
- **Advanced Categories**: Machine learning-based categorization
- **Data Export**: Backup and export capabilities

### Performance Improvements
- **Model Quantization**: Reduce LLaVA memory usage
- **GPU Acceleration**: CUDA support for faster processing
- **Parallel Processing**: Multi-threaded document processing
- **Smart Caching**: Intelligent result caching system

## Development Guidelines

### Code Standards
- **PEP 8**: Follow Python style guidelines
- **Type Hints**: Use type annotations throughout
- **Documentation**: Comprehensive docstrings
- **Error Handling**: Robust exception management

### Git Workflow
```bash
# Feature development
git checkout -b feature/new-feature
git commit -m "feat: add new feature"
git push origin feature/new-feature

# Bug fixes
git checkout -b fix/bug-description
git commit -m "fix: resolve bug description"
```

### Version Control
- **Semantic Versioning**: MAJOR.MINOR.PATCH
- **Changelog**: Maintain CHANGELOG.md
- **Release Tags**: Tag stable releases
- **Branch Protection**: Protect main branch

## Contributing

### Development Setup
1. Fork the repository
2. Create feature branch
3. Implement changes with tests
4. Submit pull request with description

### Code Review Checklist
- [ ] Functionality works as expected
- [ ] Unit tests pass
- [ ] Security considerations addressed
- [ ] Performance impact assessed
- [ ] Documentation updated
- [ ] Privacy implications reviewed

## License and Legal

### Privacy Commitment
- **Local Processing**: All sensitive data processed locally
- **No Telemetry**: No usage data collection
- **Open Source**: Transparent, auditable codebase
- **User Control**: Complete user control over data

### Dependencies Licenses
- Flask: BSD-3-Clause
- Tesseract: Apache License 2.0
- Ollama: MIT License
- Python libraries: Various open source licenses

---

## Quick Start Commands

```bash
# Full setup (run once)
git clone <repo>
cd gemini
python -m venv gemini-env
gemini-env\Scripts\activate
pip install -r requirements.txt
cp .env.example .env

# Daily development
gemini-env\Scripts\activate
ollama serve &
python app.py

# Access: http://localhost:5000
```

**Remember**: This is a privacy-focused solution. All processing happens locally on your machine, ensuring your financial data never leaves your control.