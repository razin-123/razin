import streamlit as st
from PIL import Image

#Set page configuration
st.set_page_config(
    page_title="1901002_Architecture Portfolio",
    layout="wide",
)

#Title
st.title("1901002_Architecture Portfolio")
st.write(
    """
    Welcome to portfolio. Explore one of my architecture projects, Forest Abode : Design of a Residence 
    """
)

#Sidebar for navigation
st.sidebar.title("Navigation")
sections = ["Home", "Concept", "Plans", "Elevations and Sections", "Exterior and Interior views"]
selected_section = st.sidebar.radio("Go to", sections)

#Display images in one or two columns
def display_image(image_path, caption, column_layout=1, image_path2=None, caption2=None):
    if column_layout == 1:
        #Single column layout
        st.image(Image.open(image_path), caption=caption, use_container_width=True)
    elif column_layout == 2:
        #Two column layout
        if image_path2 is None or caption2 is None:
            st.error("For two columns, you must provide both image_path2 and caption2.")
        else:
            col1, col2 = st.columns(2)
            with col1:
                st.image(Image.open(image_path), caption=caption, use_container_width=True)
            with col2:
                st.image(Image.open(image_path2), caption=caption2, use_container_width=True)

#Home
if selected_section == "Home":
    st.header("01_Forest Abode")
    st.subheader('''DESIGN STUDIO III
DURATION : 4 WEEKS \n
STUDIO TEACHERS : PATRICK D. ROZARIO, RAFIA RUKHSAT TOHFA, BRISHTI MAJUMDER \n
Site : SUNDARBANS, BAGERHAT, Bangladesh''')
    st.write(
        """Forest Abode is a residence located in Bagerhat, near the Sundarbans. The form is conceptualized through two interconnected volumes and courtyards, blending indoor and outdoor spaces. Sloped roofs, skylights, and strategic openings optimize natural light and airflow, addressing the tropical climate. Water bodies and indoor greenery create relaxing zones, while the foyer connects the formal living, guest bedroom, and dining areas, ensuring spatial continuity with views oriented toward the southern river. The design integrates design elements, such as facade extensions for storage, bamboo screens reflecting local architectural heritage. The family living area features double-height bamboo screens for shading, adding both verticality and openness. A sculptural staircase leads to two upper-level bedrooms with green terraces overlooking the forest and river. Emphasizing climate responsiveness, ergonomics, and cultural context, the design offers a comfortable, natural living experience.
        """
    )
    display_image("images/south elevation.png", "View from river", column_layout=1)

#Concept
elif selected_section == "Concept":
    st.header("Conceptual Development")
    st.write("The form is designed as two forms connected by a intermediate space, with angles creating views towards river and forest, oriented towards south for optimum windflow and daylighting.")
    display_image("images/concept.png", "Conceptual Development", column_layout=1)


#Plans
elif selected_section == "Plans":
    st.header("Plans")
    display_image("images/site plan.png", "Site Plan", column_layout=1)
    display_image("images/plan.png", "Ground Floor Plan", column_layout=1)

#Elevations and Sections
elif selected_section == "Elevations and Sections":
    st.header("Elevations and Sections")
    st.markdown("Elevations")
    display_image("images/elevation.png", "Elevation", column_layout=1)
    st.markdown("Sections")
    display_image("images/section.png", "Section", column_layout=1)

#Exterior and Interior views
elif selected_section == "Exterior and Interior views":
    st.header("Exterior and Interior views")
    st.markdown("Exterior views")
    display_image(
    "images/east courtyard.png", "East courtyard", 
    column_layout=2, 
    image_path2="images/west courtyard.png", caption2="West courtyard"
)
    st.markdown("Interior views")
    display_image(
    "images/dining.png", "Dining", 
    column_layout=2, 
    image_path2="images/living.png", caption2="Living"
)
#Footer
st.markdown("---")
st.write("© 2024 Razin Sachi - All Rights Reserved.")
