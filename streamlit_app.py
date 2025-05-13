import streamlit as st

# Judul aplikasi
st.markdown("""
    <h1 style='text-align: center; color: #5EFF33; animation: fadeIn 2s ease-in;'>🔊 Kalkulator Kebisingan</h1>
    <style>
        @keyframes fadeIn {
            0% {opacity: 0;}
            100% {opacity: 1;}
        }
        h1 {
            animation: fadeIn 2s ease-in;
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar menu
menu = st.sidebar.selectbox(
    "Pilih Menu",
    [
        "Beranda",
        "Kalkulator Kebisingan Umum",
        "Kalkulator Kebisingan Sekolah",
        "Kalkulator Kebisingan Rumah",
        "Tentang",
    ],
)

if menu == "Beranda":
    st.subheader("Selamat Datang di Kalkulator Kebisingan")
    st.write(
        """
        Aplikasi ini digunakan untuk mengevaluasi apakah tingkat kebisingan memenuhi standar SNI di berbagai lingkungan:
        - **Umum / Lingkungan Kerja**: Maks. 85 dB
        - **Sekolah**: Maks. 45 dB
        - **Rumah**: Maks. 55 dB
        """
    )
    st.image("https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExYTdndHhjOGo3eHpjbGxxMGp1cm0wamU2MG4xbXV6bjdha3JtMXplZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/5mYcsVrgxtxt7QUc55/giphy.gif", use_container_width=True)


elif menu == "Kalkulator Kebisingan Umum":
    st.subheader("Kalkulator Kebisingan Lingkungan Kerja / Umum")

    noise_level = st.number_input("Masukkan Tingkat Kebisingan (dalam dB)", min_value=0.0, max_value=150.0, value=0.0)
    SNI_LIMIT = 85.0

    if noise_level > 0.0:
        if noise_level <= SNI_LIMIT:
            st.success(f"{noise_level} dB ✅ MEMENUHI standar SNI lingkungan kerja (≤ {SNI_LIMIT} dB).")
            st.info("**Keterangan:** Tingkat kebisingan dalam batas aman. Risiko terhadap gangguan pendengaran rendah.")
        else:
            st.error(f"{noise_level} dB ❌ TIDAK MEMENUHI standar SNI lingkungan kerja (> {SNI_LIMIT} dB).")
            st.warning("**Dampak Potensial:** Dapat menyebabkan gangguan pendengaran, stres, kelelahan, dan menurunkan produktivitas kerja bila terpapar dalam waktu lama.")
    else:
        st.info("Silakan masukkan nilai tingkat kebisingan terlebih dahulu.")

elif menu == "Kalkulator Kebisingan Sekolah":
    st.subheader("Kalkulator Kebisingan Lingkungan Sekolah")

    noise_level = st.number_input("Masukkan Tingkat Kebisingan (dalam dB)", min_value=0.0, max_value=150.0, value=0.0)
    SNI_LIMIT = 45.0
    if noise_level > 0.0:
        if noise_level <= SNI_LIMIT:
            st.success(f"{noise_level} dB ✅ MEMENUHI standar SNI lingkungan sekolah (≤ {SNI_LIMIT} dB).")
            st.info("**Keterangan:** Kebisingan dalam batas wajar untuk proses belajar. Konsentrasi siswa tetap terjaga.")
        else:
            st.error(f"{noise_level} dB ❌ TIDAK MEMENUHI standar SNI lingkungan sekolah (> {SNI_LIMIT} dB).")
            st.warning("**Dampak Potensial:** Dapat mengganggu konsentrasi, menurunkan performa belajar, dan menambah stres bagi siswa dan guru.")
    else:
        st.info("Silakan masukkan nilai tingkat kebisingan terlebih dahulu.")

elif menu == "Kalkulator Kebisingan Rumah":
    st.subheader("Kalkulator Kebisingan Lingkungan Rumah")

    noise_level = st.number_input("Masukkan Tingkat Kebisingan (dalam dB)", min_value=0.0, max_value=150.0, value=0.0)
    SNI_LIMIT = 55.0

    if noise_level > 0.0:
        if noise_level <= SNI_LIMIT:
            st.success(f"{noise_level} dB ✅ MEMENUHI standar SNI lingkungan rumah (≤ {SNI_LIMIT} dB).")
            st.info("**Keterangan:** Suasana rumah dalam batas kebisingan yang nyaman dan aman untuk istirahat.")
        else:
            st.error(f"{noise_level} dB ❌ TIDAK MEMENUHI standar SNI lingkungan rumah (> {SNI_LIMIT} dB).")
            st.warning("**Dampak Potensial:** Dapat menyebabkan gangguan tidur, tekanan darah meningkat, stres psikologis, dan penurunan kualitas hidup.")
    else:
        st.info("SIlakan masukkan nilai tingkat kebisingan terlebih dahulu")

elif menu == "Tentang":
    st.subheader("Tentang Aplikasi")
    st.write(
        """
        Aplikasi ini membantu mengevaluasi tingkat kebisingan di berbagai lingkungan berdasarkan Standar Nasional Indonesia (SNI).

        **Referensi Standar:**
        - **Lingkungan Kerja / Umum**: SNI 7231:2009 - Metoda Pengukuran Intensitas Kebisingan di Tempat Kerja
        - **Lingkungan Sekolah**: SNI 03-6386-2000 - Spesifikasi Tingkat Bunyi dan Waktu Dengung dalam Bangunan Gedung dan Perumahan
        - **Lingkungan Rumah**: SNI 8427:2017 - Pengukuran Tingkat Kebisingan Lingkungan

        Tugas Akhir Mata Kuliah Logika dan Pemrograman Komputer  
        1F Pengolahan Limbah Industri - Politeknik AKA Bogor

        _Dikembangkan dengan Python & Streamlit._
        """
    )
