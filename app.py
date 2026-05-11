import os
import tempfile
import streamlit as st
from pathlib import Path
from pydub import AudioSegment

from scraper import WebScraper
from script_generator import ScriptGenerator
from tts_converter import TTSConverter

# Page config
st.set_page_config(
    page_title="AI Podcast Generator",
    page_icon="🎙️",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 1rem;
        color: #ffffff;
    }
    .sub-header {
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="main-header">🎙️ AI Podcast Generator</div>', unsafe_allow_html=True)

st.markdown('<div class="sub-header">Transform any web article into an engaging podcast</div>', unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("⚙️ Configuration")
    
    st.subheader("API Keys")
    #minimax_key = st.text_input("Minimax API Key", type="password")
    firecrawl_key = st.text_input("Firecrawl API Key", type="password")
    groq_key = st.text_input("Groq API Key", type="password", help="Get yours at console.groq.com")
    
    st.divider()
    
    st.subheader("📝 Input")
    url = st.text_input("Article URL", placeholder="https://example.com/article")
    
    st.divider()
    
    generate_btn = st.button("🚀 Generate Podcast", type="primary", use_container_width=True)

# Main area
if generate_btn:
    # Set environment variables from sidebar input
    os.environ['FIRECRAWL_API_KEY'] = firecrawl_key
    os.environ['GROQ_API_KEY'] = groq_key
    #os.environ['MINIMAX_API_KEY'] = minimax_key (optional)
        
    progress_container = st.container()
        
    with progress_container:
        # Step 1: Scraping
        with st.status("🌐 Scraping content from URL...", expanded=True) as status:
            try:
                scraper = WebScraper()
                content = scraper.scrape(url)
                st.success(f"✅ Successfully scraped {len(content)} characters")
                status.update(label="✅ Content scraped successfully!", state="complete")
            except Exception as e:
                st.error(f"❌ Scraping failed: {str(e)}")
                st.stop()
        
        # Step 2: Script Generation
        with st.status("✍️ Generating podcast script...", expanded=True) as status:
            try:
                generator = ScriptGenerator()
                script = generator.generate(content)
                st.success("✅ Podcast script generated successfully")
                status.update(label="✅ Script generated successfully!", state="complete")
            except Exception as e:
                st.error(f"❌ Script generation failed: {str(e)}")
                st.stop()
        
        # Step 3: Audio Generation
        with st.status("🎙️ Converting script to audio...", expanded=True) as status:
            try:
                converter = TTSConverter()
                segments = converter._parse_script(script)
                total_segments = len(segments)
                
                st.info(f"Generating {total_segments} audio segments...")
                progress_bar = st.progress(0)
                
                audio_dir = tempfile.mkdtemp()
                audio_files = []
                
                for i, (speaker, text) in enumerate(segments, 1):
                    voice = speaker
                    audio_file = os.path.join(audio_dir, f"segment_{i:03d}.mp3")
                    converter._generate_and_save_speech(text, voice, audio_file)
                    
                    if os.path.exists(audio_file):
                        audio_files.append((speaker, audio_file))
                    
                    progress_bar.progress(i / total_segments)
                
                status.update(label="✅ Audio generated successfully!", state="complete")
                
            except Exception as e:
                st.error(f"❌ Audio generation failed: {str(e)}")
                st.stop()

        # Step 4: Merging
        with st.status("🔗 Merging segments...", expanded=True) as status:
            try:
                combined = AudioSegment.empty()
                for _, filepath in audio_files:
                    audio = AudioSegment.from_mp3(filepath)
                    combined += audio
                
                output_path = os.path.join(audio_dir, "full_podcast.mp3")
                combined.export(output_path, format="mp3")
                status.update(label="✅ Podcast ready!", state="complete")
            except Exception as e:
                st.error(f"❌ Merging failed: {str(e)}")
                st.stop()

    # Results Area
    st.divider()
    st.header("📊 Results")
    tab1, tab2 = st.tabs(["🎧 Podcast", "📝 Script"])
    
    with tab1:
        with open(output_path, "rb") as f:
            st.audio(f.read(), format="audio/mp3")
        with open(output_path, "rb") as f:
            st.download_button("📥 Download Podcast", f.read(), "podcast.mp3", "audio/mp3")
            
    with tab2:
        st.text_area("Script", script, height=400)

    st.balloons()
else:
    st.info("👈 Enter your API keys and a URL to get started!")