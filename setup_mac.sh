#!/bin/bash
# Setup script for macOS

echo "🚀 Setting up RBI-RAG on macOS..."

# Check if Python 3.10+ is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.10 or higher."
    exit 1
fi

# Create virtual environment
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "✅ Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Install Playwright browser
echo "🎭 Installing Playwright browser..."
playwright install chromium

# Copy environment template
if [ ! -f .env ]; then
    echo "📝 Creating .env file from template..."
    cp .env.example .env
    echo "⚠️  Please add your GROQ_API_KEY to .env"
fi

echo "✨ Setup complete! Run 'python run.py' to start the app."
