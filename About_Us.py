import streamlit as st



def about_page():
    # Title + Hero Section
    st.set_page_config(page_title="EduShield | ℹ️ About US", page_icon="images/Edushield_Icon1.png", layout="wide")
    
    st.title("ℹ️ About US")
    st.caption("'Everything you need to know about EduShield'")
    st.divider()

    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("images/EduShield_Logo7.png", caption="EduShield", width=180)  # You can replace with your logo
    with col2:
        st.markdown(
            """
            EduShield is a **Secure Academic Management System** designed to provide institutions 
            with a safe, reliable, and user-friendly platform for managing academic records.  

            Our goal is to ensure that students, lecturers, and administrators can seamlessly access academic data 
            while maintaining the highest standards of **security and privacy**.
            """
        )

    st.markdown("---")

    # Mission
    st.header("🎯 Our Mission")
    st.info(
        """
        To create a **secure, efficient, and transparent academic management system** that empowers institutions 
        to protect sensitive data, enhance student performance, and streamline academic operations.
        """
    )

    st.markdown("---")

    # Who We Serve
    st.header("👥 Who We Serve")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("🎓 Students")
        st.markdown("Access **attendance, results, GPA predictions, and exam eligibility** in one place.")

    with col2:
        st.subheader("👨‍🏫 Lecturers")
        st.markdown("Easily **manage courses, upload resources, and monitor student performance.**")

    with col3:
        st.subheader("🏛️ Administrators")
        st.markdown("Control **system settings, allocate courses, and ensure institutional compliance.**")

    st.markdown("---")

    # Why Choose EduShield
    st.header("🔒 Why Choose EduShield?")
    col1, col2 = st.columns(2)

    with col1:
        st.success("✅ **Data Security** – Role-based access control")
        st.success("✅ **Transparency** – Real-time academic progress tracking")
        st.success("✅ **Efficiency** – Automated GPA prediction and attendance monitoring")

    with col2:
        st.success("✅ **Scalability** – Grows with institutions of any size")
        st.success("✅ **Reliability** – Modern, stable, and high-performance system")
        st.success("✅ **User-Friendly** – Simple and intuitive for all roles")

    st.markdown("---")

    # Core Values
    st.header("🌟 Core Values")
    st.markdown(
        """
        - **Integrity** 🕊️ – Protecting academic data with honesty and transparency  
        - **Innovation** 💡 – Leveraging technology to transform education  
        - **Collaboration** 🤝 – Bridging the gap between students, lecturers, and admins  
        - **Excellence** 🏆 – Empowering institutions and students to achieve more  
        """
    )

    st.markdown("---")

    # Vision
    st.header("📌 Our Vision")
    st.info(
        "To become a **trusted global platform** that redefines how academic institutions handle and secure sensitive data "
        "while promoting **academic excellence** everywhere."
    )

    st.markdown("---")

    # Contact Section
    st.header("📞 Contact & Support")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("📧 **Email**: support@edushield.com")
        st.markdown("🌐 **Website**: www.edushield.com")
    with col2:
        st.markdown("📍 **Headquarters**: Lagos, Nigeria")
        st.markdown("☎️ **Phone**: +234 800 123 4567")

    # Footer
    st.markdown("---")
    st.caption("© 2025 EduShield | All Rights Reserved | Privacy Policy | Terms of Service")



about_page()