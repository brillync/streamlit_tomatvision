import streamlit as st
from login import login_page
from signup import signup_page
from index import camera_scan_page, gallery_and_details_page, homepage
from auth import get_db_connection



# Fungsi utama aplikasi
def main():
    # Periksa koneksi database dan tampilkan status
    if get_db_connection():
        st.sidebar.success("Koneksi ke database berhasil")
    else:
        st.sidebar.error("Gagal terhubung ke database")

    # Periksa status login
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False
    if "username" not in st.session_state:
        st.session_state["username"] = None

    # Jika pengguna belum login, tampilkan halaman login atau signup
    if not st.session_state["logged_in"]:
        page = st.sidebar.selectbox("Pilih Halaman", ["Login", "Signup"])
        if page == "Login":
            login_page()
        elif page == "Signup":
            signup_page()
    else:
        st.sidebar.write(f"Selamat datang, {st.session_state['username']}!")
        page = st.sidebar.selectbox("Pilih Halaman", ["Home", "Camera Scan", "Gallery & Photo Details"])
        if page == "Home":
            homepage()
        elif page == "Camera Scan":
            camera_scan_page()
        elif page == "Gallery & Photo Details":
            gallery_and_details_page()

        if st.sidebar.button("Logout"):
            st.session_state["logged_in"] = False
            st.session_state["username"] = None  # Reset username setelah logout
            st.experimental_rerun()  # Rerun aplikasi setelah logout

# Menyematkan CSS dari file styles.css
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Jalankan fungsi utama
if __name__ == "__main__":
    main()
