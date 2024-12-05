import streamlit as st
import replicate
import requests

import os
from dotenv import load_dotenv
load_dotenv()
REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")

st.set_page_config(page_title="Generate Akash!", page_icon=":camera:")
st.title("Generate Akash!")

default_prompt = "Generate a picture of Miguel"

prompt = st.text_area("Complete your image generation prompt:", 
                      value=default_prompt, 
                      height=150)

generate_button = st.button("Generate")
image_placeholder = st.empty()

if generate_button:
    with st.spinner('Generating...'):
        try:
            akash = replicate.Client(REPLICATE_API_TOKEN)
            output = akash.run(
                "akashbachhar/miguel:20fede861f2e8d578bb6add6cdca9b6ca143b7e54c8205a74b14411476d390fa",
                input={
                    "model": "dev",
                    "prompt": prompt,
                    "go_fast": False,
                    "lora_scale": 1,
                    "megapixels": "1",
                    "num_outputs": 1,
                    "aspect_ratio": "1:1",
                    "output_format": "webp",
                    "guidance_scale": 3,
                    "output_quality": 80,
                    "prompt_strength": 0.8,
                    "extra_lora_scale": 1,
                    "num_inference_steps": 28
                }
            )
            
            image_url = output[0]
            image_response = requests.get(image_url)
            image_placeholder.image(image_response.content, caption="Generated Image", use_container_width=True)
        
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

st.markdown("---")
st.markdown("""
<div style="text-align: left;">
    Made by <a href="https://www.instagram.com/conjugatesky/" target="_blank" style="text-decoration: none; color: inherit;">Akash</a>
</div>
""", unsafe_allow_html=True)