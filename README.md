# Test Docling

A Python-based document processing application powered by the `docling` package, featuring a Gradio web interface for easy document conversion to markdown format.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Overview

Test Docling simplifies document processing by providing an intuitive web interface for uploading and converting documents to markdown format, with built-in timing and preview capabilities.

## Features

- 📤 **Document Upload**: Simple drag-and-drop document upload interface
- 🔄 **Format Conversion**: Automatic conversion to markdown using `docling`
- ⏱️ **Performance Metrics**: Real-time conversion time tracking
- 💾 **Auto-saving**: Automatic storage of converted files in `output` directory
- 👀 **Preview**: CLI preview of conversion results

## Prerequisites

- Python 3.10 or higher
- Poetry package manager

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/test-docling.git
   cd test-docling
   ```

2. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

## Usage

1. Start the application:
   ```bash
   poetry run python -m test_docling.app
   ```

2. Access the application:
   - Open your web browser
   - Navigate to the URL displayed in the terminal (typically `http://localhost:7860`)
   - Upload your document using the interface
   - View the conversion results and processing time

## Project Structure

```
test-docling/
├── test_docling/
│   ├── __init__.py
│   ├── app.py        # Main application with Gradio interface
│   └── utils.py      # Utility functions for document conversion
├── tests/
│   └── test_app.py   # Unit tests
├── output/           # Converted document storage
└── pyproject.toml    # Project dependencies and metadata
```

## Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create your feature branch:
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m 'Add some amazing feature'
   ```
4. Push to the branch:
   ```bash
   git push origin feature/amazing-feature
   ```
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [`docling`](https://github.com/docling/docling) package for document processing capabilities
- [Gradio](https://gradio.app/) team for the web interface framework
