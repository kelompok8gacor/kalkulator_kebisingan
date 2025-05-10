import streamlit as st

# Judul aplikasi
st.title(":green[Kalkulator Kebisingan]")

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

elif menu == "Kalkulator Kebisingan Umum":
    st.subheader("Kalkulator Kebisingan Lingkungan Kerja / Umum")

    noise_level = st.number_input("Masukkan Tingkat Kebisingan (dalam dB)", min_value=0.0, max_value=150.0, value=70.0)
    SNI_LIMIT = 85.0

    if noise_level <= SNI_LIMIT:
        st.success(f"{noise_level} dB ✅ MEMENUHI standar SNI lingkungan kerja (≤ {SNI_LIMIT} dB).")
    else:
        st.error(f"{noise_level} dB ❌ TIDAK MEMENUHI standar SNI lingkungan kerja (> {SNI_LIMIT} dB).")

elif menu == "Kalkulator Kebisingan Sekolah":
    st.subheader("Kalkulator Kebisingan Lingkungan Sekolah")

    noise_level = st.number_input("Masukkan Tingkat Kebisingan di Sekolah (dalam dB)", min_value=0.0, max_value=150.0, value=40.0)
    SNI_LIMIT = 45.0

    if noise_level <= SNI_LIMIT:
        st.success(f"{noise_level} dB ✅ MEMENUHI standar SNI sekolah (≤ {SNI_LIMIT} dB).")
    else:
        st.error(f"{noise_level} dB ❌ TIDAK MEMENUHI standar SNI sekolah (> {SNI_LIMIT} dB).")

elif menu == "Kalkulator Kebisingan Rumah":
    st.subheader("Kalkulator Kebisingan Lingkungan Rumah")

    noise_level = st.number_input("Masukkan Tingkat Kebisingan di Rumah (dalam dB)", min_value=0.0, max_value=150.0, value=50.0)
    SNI_LIMIT = 55.0

    if noise_level <= SNI_LIMIT:
        st.success(f"{noise_level} dB ✅ MEMENUHI standar SNI rumah (≤ {SNI_LIMIT} dB).")
    else:
        st.error(f"{noise_level} dB ❌ TIDAK MEMENUHI standar SNI rumah (> {SNI_LIMIT} dB).")

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
