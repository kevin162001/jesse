import streamlit as st

def app():
    st.title("Tentang Kami")

    st.header("Deskripsi Projek")
    st.markdown("""
        Pembuatan dashboard ini merupakan projek akhir dari Program DTS TSA 2023 yang dikerjakan oleh kelompok 4 (Kelas A).
        Projek ini disusun semata-mata untuk tujuan pendidikan dan pembelajaran.
    """)

    col_1, col_2, col_3 = st.columns(3)
    with col_1:
        st.header("Visi")
        st.markdown("""
        Menjadi penyedia solusi inovatif dalam mengatasi risiko banjir dan memberikan informasi yang akurat 
        untuk pengambilan keputusan di Kabupaten Cilacap.
        """)
    with col_2:
        st.header("Misi")
        st.markdown("""
        1. Mengumpulkan dan menganalisis data kejadian banjir serta curah hujan dengan akurat.
        2. Mengembangkan model prediksi banjir yang handal berdasarkan data historis.
        3. Menyediakan dashboard interaktif untuk memantau dan meramalkan risiko banjir.
        4. Menyebarkan informasi mengenai risiko banjir kepada masyarakat secara efektif.
        """)
    with col_3:
        st.header("Tujuan")
        st.markdown("""
        1. Menyediakan sumber informasi yang terpercaya terkait risiko banjir di Kabupaten Cilacap.
        2. Meningkatkan kewaspadaan dan kesiapsiagaan masyarakat terhadap potensi risiko banjir.
        3. Mendukung upaya mitigasi dan penanggulangan risiko banjir di tingkat lokal.
        """)