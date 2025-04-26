# Contributing to http-scanner

Thank you for considering contributing to http-scanner! 🚀

## How to Contribute

1. Fork the repo
2. Create a new branch (`git checkout -b feature-branch`)
3. Make your changes
4. Write tests if applicable
5. Ensure all code passes `black` and `flake8`
6. Open a Pull Request

## Development Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install -e .
pip install -r requirements.txt
pip install black flake8 pytest
```

## Testing

Run all tests using:

```bash
pytest
```

## Code Style

Format code with:

```bash
black src tests
```

Check linting with:

```bash
flake8 src tests
```

---
Happy scanning! 🛰️
