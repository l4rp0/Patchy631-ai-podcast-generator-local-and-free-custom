
# 🎙️ AI Podcast Generator (Local & GPU Optimized)

![Python](https://img.shields.io/badge/python-3.12-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![GPU](https://img.shields.io/badge/RTX%203050%20Ti-Optimized-orange.svg)

A high-performance tool that transforms any web article or blog post into an engaging podcast conversation between two speakers. This custom build is optimized for **NVIDIA RTX GPUs** and uses **Local TTS** .

---

## 🌟 Key Features

- **Web Scraping**: Clean content extraction via **Firecrawl**.
- **Instant Scripting**: Llama 3.3 (via **Groq**) generates natural dialogue in seconds.
- **Local Voice**: **Kokoro-82M** integration for high-fidelity, offline speech synthesis.
- **GPU Accelerated**: Fully optimized for **NVIDIA CUDA** (tested on RTX 3050 Ti).
- **Zero Cost**: No per-character fees. Replaced cloud APIs (MiniMax) with local models.

---

## ⚙️ Installation & Setup

### 1. System Requirements
Before running the Python code, you must install these two system tools:
* **FFmpeg**: For merging audio clips. (`winget install ffmpeg`)
* **eSpeak-ng**: Required for Kokoro's phoneme processing. [Download MSI](https://github.com/espeak-ng/espeak-ng/releases)

### 2. Project Setup
```powershell
# Clone and enter directory
git clone [https://github.com/YOUR_USERNAME/ai-podcast-generator.git](https://github.com/YOUR_USERNAME/ai-podcast-generator.git)
cd ai-podcast-generator

# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install GPU-optimized PyTorch (for RTX 3050 Ti)
pip install torch torchvision torchaudio --index-url [https://download.pytorch.org/whl/cu121](https://download.pytorch.org/whl/cu121) --force-reinstall

```

---

## 🚀 Usage

### Running the Application

```bash
streamlit run app.py

```

### Step-by-Step Guide

1. **Enter API Keys**: Provide your **Firecrawl** and **Groq** keys in the left sidebar.
2. **Input URL**: Paste the link to the article or tutorial you want to convert.
3. **Generate**: Click **"Generate Podcast"**.
* *Note: On the first run, the app will download the 300MB Kokoro model weights automatically.*


4. **Download**: Once the "Merging segments" bar turns green, listen to the preview or download the full `.mp3` file.

---

## 🔧 Troubleshooting (Dev Notes)

* **Hash Mismatch**: If PyTorch fails to install, use `pip cache purge` and the `--no-cache-dir` flag.
* **WinError 2**: This means **FFmpeg** is not found. Restart your terminal after installation.
* **Memory**: Ensure your laptop is **plugged in** to utilize the full power of the RTX 3050 Ti.

---

## 🤝 Credits & Attribution

This project is a customized fork and optimization of the original "AI Podcast Generator" concept.

* **Original Architecture**: Inspired by the [AI Engineering Hub](https://github.com/patchy631/ai-engineering).
* **Local TTS Integration**: Modified to use **Kokoro-82M** for free, local voice generation.
* **GPU Optimization**: Reconfigured for **NVIDIA CUDA** execution on RTX series laptops.
* **Scripting Logic**: Transitioned from OpenRouter to **Groq** for high-speed inference.

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.
