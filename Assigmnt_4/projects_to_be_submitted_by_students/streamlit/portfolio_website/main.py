import streamlit as st

# Page Configuration
st.set_page_config(page_title="My Portfolio", page_icon="💼", layout="centered")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects", "Contact"])

# Home Page
if page == "Home":
    st.title("👩‍💻 Welcome to My Portfolio!")
    st.write("Hello! I'm **Sidra farooq**, a passionate Web Developer specializing in **Next.js, Tailwind CSS, and TypeScript**.")
    st.write("I love building modern, responsive websites and exploring new technologies.")
    
    # Skills Section
    st.subheader("🔧 Skills")
    st.write("✅ HTML, CSS, Tailwind CSS")  
    st.write("✅ JavaScript, TypeScript")  
    st.write("✅ React.js, Next.js")  
    st.write("✅ UI/UX Design")

# Projects Page
elif page == "Projects":
    st.title("🚀 My Projects")
    project_data = {
        "🌸 chairs website": "An e-commerce website for buying chairs, built with Next.js and Tailwind CSS.",
        "📚 Books API": "A RESTful API for managing books, using Next.js API routes.",
        "🛍️ Skincare Brand": "A brand website designed in Figma and built using Next.js.",
        "🛒 Marketplace": "A fully functional marketplace for online shopping, built with Next.js and Tailwind CSS.",
        "📄 Resume Builder": "A dynamic resume builder that generates a unique resume URL,and download resume in PDF form, built with HTML, CSS and JavaScript."
    }

    for project, desc in project_data.items():
        st.subheader(project)
        st.write(desc)
        st.markdown("---")

# Contact Page
elif page == "Contact":
    st.title("📞 Contact Me")
    st.write("I'd love to connect with you! Reach out via:")
    st.write("𝕏 Twitter: https://x.com/sidrafarooq752")  
    st.write("🖥️ Github: https://github.com/sidrafarooqq")  
    st.write("💼 LinkedIn: https://www.linkedin.com/in/sidra-farooq-1415282b6/")  

# Footer
st.markdown("---")
st.write("Made with ❤️ using Streamlit")