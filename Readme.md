# AI Directory Management System

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![PyQt](https://img.shields.io/badge/PyQt-5.15.7-green.svg)](https://www.riverbankcomputing.com/software/pyqt/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📖 Overview

The **AI Directory Management System** is an intelligent file organization tool that leverages artificial intelligence and machine learning to automatically categorize, organize, and manage your digital files. Built with Python and PyQt5, it provides an intuitive graphical interface for efficient file management with advanced features like duplicate detection and undo functionality.

## ✨ Key Features

### 🤖 AI-Powered Intelligence
- **Smart File Classification**: Automatically categorizes files based on content analysis and file extensions
- **Machine Learning Models**: Utilizes BERT, LSTM, and computer vision models for enhanced file understanding
- **Adaptive Learning**: Improves categorization accuracy over time

### 📁 Intelligent Organization
- **Automatic Categorization**: Sorts files into logical categories (Documents, Images, Videos, Audio, Code, etc.)
- **Smart Directory Structure**: Creates organized folder hierarchies automatically
- **Batch Processing**: Handle large numbers of files efficiently

### 🔍 Advanced File Management
- **Duplicate Detection**: Identifies and manages duplicate files to save storage space
- **File Type Recognition**: Advanced file type detection using magic numbers and content analysis
- **Metadata Extraction**: Extracts and organizes file metadata for better categorization

### 🛡️ Safety & Control
- **Undo Functionality**: Revert organization changes with a single click
- **Backup System**: Automatic backup creation before any file operations
- **Safe File Operations**: Prevents data loss with comprehensive error handling

### 🎨 User Experience
- **Drag & Drop Interface**: Intuitive file selection with drag and drop support
- **Modern GUI**: Clean, responsive PyQt5-based interface
- **Real-time Progress**: Visual feedback during file processing operations

## 🚀 Installation

### Prerequisites

- **Python**: 3.10 or higher
- **Operating System**: Windows 10/11, macOS 10.14+, or Linux
- **Memory**: Minimum 4GB RAM (8GB recommended)
- **Storage**: At least 1GB free space for models and dependencies

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/Shashanklko/AI-Directory-Management-System.git
   cd AI-Directory-Management-System
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirement.txt
   ```

3. **Run the application**
   ```bash
   python -m gui.main
   ```

### Alternative Installation Methods

#### Using the Executable (Windows)
Download the latest release from the [Releases](https://github.com/Shashanklko/AI-Directory-Management-System/releases) page and run `AI Directory Manager.exe`.

#### Using the Batch File
```bash
# Windows
run_ai_directory_manager.bat

# Build from source
build_simple.bat
```

## 📚 Usage Guide

### Basic File Organization

1. **Launch the Application**
   - Run `python -m gui.main` or use the executable
   - The main window will appear with a clean interface

2. **Select Source Directory**
   - Click "Choose Folder" or drag and drop a folder
   - The selected path will be displayed

3. **Organize Files**
   - Click "Organize Files" to start the process
   - Choose a destination directory (optional)
   - Monitor progress in real-time

4. **Undo Changes (if needed)**
   - Click "Undo Last Organization" to revert changes
   - Files will be restored to their original locations

### Advanced Features

#### Custom Categorization
The system automatically categorizes files into:
- **Documents**: PDF, DOCX, TXT, XLSX, PPTX
- **Images**: JPG, PNG, GIF, BMP, SVG
- **Videos**: MP4, AVI, MOV, MKV
- **Audio**: MP3, WAV, AAC, FLAC
- **Code Files**: PY, JS, HTML, CSS, Java, C++
- **Archives**: ZIP, RAR, TAR, 7Z
- **Executables**: EXE, MSI, BAT, SH

#### Duplicate Management
- Automatic duplicate detection using content hashing
- Options to keep, replace, or move duplicates
- Storage space optimization

## 🏗️ Project Architecture

```
AI-Directory-Management-System/
├── backend/                 # Core processing logic
│   ├── ai_categorization.py # AI/ML classification models
│   ├── duplicate_checker.py # Duplicate detection algorithms
│   ├── file_organizer.py    # Main file organization logic
│   └── utils.py            # Utility functions
├── gui/                     # User interface components
│   ├── main.py             # Main application entry point
│   ├── ui_main.py          # Primary UI components
│   ├── ui_logic.py         # UI business logic
│   └── styles.qss          # Qt stylesheet
├── dist/                    # Distribution files
├── requirement.txt          # Python dependencies
└── README.md               # This file
```

## 🔧 Configuration

### Environment Variables
```bash
# Set model cache directory
export MODEL_CACHE_DIR="/path/to/models"

# Enable debug logging
export DEBUG_MODE="true"

# Set maximum file size for processing (in MB)
export MAX_FILE_SIZE="1000"
```

### Custom Categories
Modify `backend/file_organizer.py` to add custom file categories:
```python
self.categories = {
    "Custom Category": [".custom", ".ext"],
    # ... existing categories
}
```

## 🧪 Testing

Run the test suite to ensure everything works correctly:
```bash
# Install test dependencies
pip install pytest pytest-qt

# Run tests
pytest test_undo.py
```

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit your changes**: `git commit -m 'Add amazing feature'`
4. **Push to the branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

### Development Setup
```bash
# Install development dependencies
pip install -r requirement.txt
pip install pytest pytest-qt flake8 mypy

# Run linting
flake8 .
mypy .

# Run tests
pytest
```

## 📋 Requirements

### Core Dependencies
- **PyQt5**: 5.15.7+ - GUI framework
- **PyTorch**: 1.11.0+ - Deep learning framework
- **scikit-learn**: 1.1.1+ - Machine learning utilities
- **Pandas**: 1.4.2+ - Data manipulation
- **NumPy**: 1.22.3+ - Numerical computing

### AI/ML Models
- **Transformers**: 4.19.2+ - BERT and LSTM support
- **TIMM**: 0.5.4+ - Image classification models
- **Pillow**: 9.1.0+ - Image processing

### Utilities
- **python-magic**: 0.4.27+ - Advanced file type detection
- **Logging**: 0.5.1.2+ - Application logging

## 🐛 Troubleshooting

### Common Issues

#### Import Errors
```bash
# Ensure all dependencies are installed
pip install -r requirement.txt --upgrade

# Check Python version
python --version  # Should be 3.10+
```

#### GUI Not Loading
```bash
# Install PyQt5 dependencies
pip install PyQt5-tools

# Check display settings (Linux)
export DISPLAY=:0
```

#### Memory Issues
- Reduce `MAX_FILE_SIZE` environment variable
- Process files in smaller batches
- Ensure sufficient RAM (8GB+ recommended)

### Performance Optimization
- Use SSD storage for better I/O performance
- Enable GPU acceleration for PyTorch (if available)
- Process files during low system usage periods

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **PyQt5 Community** for the excellent GUI framework
- **PyTorch Team** for the powerful deep learning library
- **Open Source Contributors** who made this project possible

## 📞 Support & Contact

- **GitHub**: [Shashanklko](https://github.com/Shashanklko)
- **Issues**: [Report bugs or request features](https://github.com/Shashanklko/AI-Directory-Management-System/issues)
- **Discussions**: [Join the community](https://github.com/Shashanklko/AI-Directory-Management-System/discussions)

## 🔄 Version History

- **v1.0.0** - Initial release with core file organization
- **v1.1.0** - Added AI-powered categorization
- **v1.2.0** - Enhanced duplicate detection and undo functionality
- **v1.3.0** - Improved GUI and performance optimizations

---

**⭐ Star this repository if you find it helpful!**

**Made with ❤️ by the AI Directory Management System Team**
