🎙️ AI Podcast Generator (FREE & GPU BASED)
Transform any web article or blog post into an engaging podcast between two speakers using Groq for scripting and Kokoro for high-fidelity local speech synthesis.

Overview
AI Podcast Generator is an intelligent tool that converts written content into natural-sounding podcast dialogues. This custom version is optimized for NVIDIA RTX GPUs to ensure lightning-fast, cost-free audio generation.

Scrape: Extract clean content from any webpage using Firecrawl.

Generate: Create an engaging two-host script using Llama 3.3 via Groq.

Synthesize: Convert text to speech locally using the Kokoro-82M model.

Merge: Seamlessly combine audio segments into a complete .mp3 file.

Tech Stack (Custom Build)
Groq (Llama-3.3-70b): For near-instant, intelligent script generation.

Kokoro-82M: Local, high-quality text-to-speech (No API costs).

Firecrawl: Robust web scraping and content extraction.

PyTorch (CUDA): Optimized for NVIDIA RTX 3050 Ti for rapid audio rendering.

Streamlit: An intuitive and interactive web interface.

How It Works
Content Extraction: Firecrawl scrapes the provided URL and extracts clean, structured content.

Script Generation: Groq analyzes the content and creates a natural dialogue between Host 1 (Male) and Host 2 (Female).

Audio Synthesis: The script is processed locally on your GPU using Kokoro, ensuring privacy and speed.

Merging: All audio segments are combined into a single podcast file using FFmpeg.

Delivery: Listen to, download, and share your AI-generated podcast directly from the UI.

Installation & Setup
Prerequisites: Python 3.12+, FFmpeg, and eSpeak-ng.

Install System Dependencies:

FFmpeg: winget install ffmpeg

eSpeak-ng: Download MSI Installer (Required for Kokoro).

Set up the environment:

Bash
# Clone and enter directory
cd ai-podcast-generator

# Create virtual environment
python -m venv venv
.\venv\Scripts\activate  # Windows
Install Dependencies:

Bash
# Install core requirements
pip install -r requirements.txt

# Install GPU-optimized PyTorch (for RTX 3050 Ti)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
API Keys:
You will need keys for Firecrawl and Groq. This version does not require a paid MiniMax subscription.

Groq: console.groq.com

Firecrawl: firecrawl.dev

Usage
Running the Web Application
Bash
streamlit run app.py
Steps to Generate
Enter API Keys: Input your Firecrawl and Groq keys in the sidebar.

Provide URL: Enter the URL of the article you want to convert.

Generate: Click "Generate Podcast." (Note: The first run will download the 300MB Kokoro model weights).

Listen: Download the final .mp3 and enjoy!

Customization & Attribution
This project is a customized fork of the original AI Engineering Hub project.

Changes made in this version:

Swapped OpenRouter for Groq (Llama 3.3) for faster inference.

Replaced MiniMax with Kokoro for local, free, and private TTS.

Added CUDA/GPU support for RTX series laptops.

Fixed indentation and stability issues following a local environment rebuild.

Contribution
Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

Instructions for you:
Open your project folder.

Open README.md.

Select everything and paste the code above.

Save and then run your final git commands:

PowerShell
git add README.md
git commit -m "Update README to reflect custom Groq and Kokoro GPU build"
git push
