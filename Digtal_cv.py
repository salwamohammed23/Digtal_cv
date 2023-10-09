from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets/Salwa ML.pdf"
profile_pic = current_dir / "assets" / "300846713_5028669960567203_6940056269635120261_n.jpg"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Salwa Mohammed"
PAGE_ICON = ":wave:"
NAME = "Salwa Mohammed"
DESCRIPTION = """
ML engineer, image processing , Comuter vision.
"""
EMAIL = "salwa.studies@gmail.com"
SOCIAL_MEDIA = {
  
    "LinkedIn": "https://www.linkedin.com/in/salwa-muhammed-53b873246/",
    "GitHub": "https://github.com/salwamohammed23",
   
}
#PROJECTS = {}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ Training AI atZewail City of Science and Technology
- ✔️  Internship Trainee at WorldQuant University
- ✔️ teacher of Mathematics

"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas,TensorFlow, Keras,streamlit ), SQL.
- Write paper in Latic

- 📊 Data Visulization:Plotly, Statistics.
- 📚 Modeling: ML models, DL models.
- 🗄️ Databases: MongoDB, MySQL.
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("Mathematics Teacher")




# --- Education ---
st.write('\n')
st.subheader("Educationy")
st.write("---")

# --- Edu 1
st.write("M.Sc. degree in ‘pure Mathematics’.2017, Faculty of Science, South Valley University.")
# --- Edu 2
st.write("Bachelor Degree in Science (Mathematics) 2008, Al-Azhar University / Faculty of Science.")
# --- Edu 3
st.write("Professional Diploma in Software Engineering with Distinction, Cairo University with Honors.")
if st.button('Show'):

  # Example 2: Display an image from a local file
  image_file = 'assets/28461194_2024634324216872_2091704565_o.jpg'
  image_file2 = 'assets/28504645_2024633124216992_1882864731_o.jpg'
  image_file3 = 'assets/383389482_6258938180873702_6150650001186814059_n.jpg'
  image_file4 = 'assets/383783213_6258938014207052_5695492704011137997_n.jpg'
  
  #st.image(image_file, caption='Local Image')
  st.image(image_file,  width=300, caption='Resized Image')
  
  # Example 3: Display an image with custom dimensions
  #st.image('path/to/image.jpg', width=300, caption='Resized Image')
  st.image(image_file3, width=300, caption='Resized Image')
  st.image(image_file4, width=300, caption='Resized Image')
  st.image(image_file2, width=300, caption='Resized Image')
  
  
