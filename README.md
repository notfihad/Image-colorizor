# AI-Powered Image Colorization: Pix2Pix and DeOldify  

This repository combines two advanced deep learning approaches to colorize black-and-white images:  
1. **Pix2Pix** - A conditional Generative Adversarial Network (cGAN) trained on a paired dataset for supervised image-to-image translation.  
2. **DeOldify** - A GAN-based architecture optimized for colorization using user-provided prompts for context-aware outputs.  
---

## Features  
### Pix2Pix Implementation  
- **Fine-tuned on the Image-Colorization dataset from Hugging Face.**  
- **Black-and-white to color transformation** using paired input-output images.  
- Model trained using a supervised learning approach.  
- Training checkpoint stored in Google Drive for easy access.  

### DeOldify Integration  
- **Context-aware colorization** using FastAI and GANs.  
- Accepts **user-provided text prompts** to guide the colorization process.  
- Fully integrated with an external **model server hosted on Google Colab** for remote processing.
---

## System Architecture  

### 1. **Backend**  
- Built using **FastAPI** for serving the models.  
- Supports image upload, colorization requests, and result downloads.  

### 2. **Frontend**  
- Developed with **Streamlit** for an interactive, user-friendly UI.  
- Allows users to upload black-and-white images and text prompts.  

### 4. **Cloud Deployment**  
- **Model Server:** Google Colab with an **ngrok** tunnel for secure external access.  

---

## Setup and Usage  

### Prerequisites  
- Python 3.8+  
- Virtual environment (recommended)  
- Access to **Google Colab** for DeOldify model server.  
- GPU-enabled machine for Pix2Pix training and inference (optional).  

### Running the Application  

Set up the **Google Colab** notebook:  
- Load the DeOldify model.  
- Enable **ngrok** for tunneling the server.  
- Copy the `ngrok` URL to the frontend configuration.  
---

## Pix2Pix: Training and Evaluation  

### Dataset Preparation  
1. Download the **Image-Colorization** dataset from Hugging Face.  
2. Preprocess paired images for training.  

### Training  
1. Upload training dataset to the project directory.  
2. Run the training script:  
   ```bash  
   python train_pix2pix.py --data_path ./data  
   ```  
3. Save the model checkpoint to Google Drive:  
   ```bash  
   python save_checkpoint.py --drive_path ./drive/MyDrive/checkpoints  
   ```  

### Evaluation  
1. Test on custom black-and-white images:  
   ```bash  
   python evaluate_pix2pix.py --image_path ./input/image.jpg  
   ```  

---


## Future Work  
- Incorporating **image context understanding** for improved Pix2Pix outputs.  
- Adding support for **other GAN-based architectures** for comparison.  
- Optimizing deployment pipelines for large-scale use.  

---

## Acknowledgments  
- [Pix2Pix (Isola et al., 2017)](https://arxiv.org/abs/1611.07004)  
- [DeOldify](https://github.com/jantic/DeOldify)  
- [Hugging Face Datasets](https://huggingface.co/datasets)  

---
**Contributions welcome!** 🚀
