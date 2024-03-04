import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='white')

#Bagaimana hubungan temperatur feeling (yang dirasakan manusia) dan temperatur aktual mempengaruhi jumlah peminjaman sepeda?
def atemp_temp_totalbike_df(hour_bike):
    plt.figure(figsize=(8, 5))
    sns.scatterplot(data=hour_bike, x='atemp', y='cnt', hue='temp', palette='YlGnBu')
    plt.xlabel('Temperatur Feeling')
    plt.ylabel('Jumlah Sewa Sepeda')
    plt.title('Korelasi Temperatur Feeling dengan Jumlah Sewa Sepeda')

    # Menyimpan visualisasi sebagai file gambar
    plt.savefig('scatterplot.png')
    # Menampilkan gambar di dashboard Streamlit
    st.image('scatterplot.png')

    with st.expander("Lihat Penjelasan"):
        st.write(
            """Berdasarkan hasil analisis di atas, dapat diketahui bahwa terdapat korelasi atau hubungan positif temperatur feeling (yang dirasakan manusia) dan temperatur aktual mempengaruhi jumlah peminjaman sepeda dengan kesimpulan sebagai berikut.
            \n1) Pada eksplorasi data, temperatur yang di rasakan manusia memiliki korelasi atau tingkat kesesuaian hampir sempurna dengan temperatur aktual.
            \n2) Sebaran data pada scatterplot hasil visualisasi dan explanatory analysis menunjukkan semakin tinggi nilai dari temperature feeling dan temperatur aktual, maka semakin banyak jumlah pemesanan peminjaman sepeda. 
            Jadi, jumlah pemesanan peminjaman sepeda cenderung semakin banyak apabila kondisi atau nilai temperatur feeling dan aktual juga meningkat.
            \n3) Dengan memahami hubungan antara kondisi temperatur dan pola peminjaman sepeda, perusahaan dapat mengoptimalkan strategi pemasaran maupun pelayanan yang baik dalam mendukung perkembangan bisnis.
            """
        )

#Pada musim apa peminjaman sepeda mencapai jumlah terbanyak pada tahun 2012?
def season_totalbike_df(hour_bike):
    data_2012 = hour_bike[hour_bike['yr'] == 1]
    jumlah_peminjaman_per_musim_2012 = data_2012.groupby(['season', 'yr'])['cnt'].sum().reset_index()
    print(jumlah_peminjaman_per_musim_2012)
    plt.figure(figsize=(8, 5))
    plt.bar(jumlah_peminjaman_per_musim_2012['season'], jumlah_peminjaman_per_musim_2012['cnt'], color='darkblue')
    plt.xlabel('Musim')
    plt.ylabel('Jumlah Peminjaman')
    plt.xticks([1, 2, 3, 4], ['Spring', 'Summer', 'Fall', 'Winter'])
    plt.title('Jumlah Peminjaman Sepeda setiap Musim pada Tahun 2012')

    # Menyimpan visualisasi sebagai file gambar
    plt.savefig('bar.png')
    # Menampilkan gambar di dashboard Streamlit
    st.image('bar.png')

    with st.expander("Lihat Penjelasan"):
        st.write(
            """Berdasarkan hasil analisis data, dapat diketahui hasil analisis sebagai berikut.
            \n1) Pada tahun 2012, musim ke-3 yaitu Fall season (musim gugur) memiliki jumlah peminjaman sepeda terbanyak dengan total 641479.
            \n2) Jumlah peminjaman sepeda antar tiap musim memiliki selisih yang lumayan tinggi, sehingga dengan mengetahui musim yang memiliki jumlah peminjaman sepeda terbanyak di tahun terbaru pada data, musim dapat menjadi salah satu faktor pengaruh terhadap jumlah peminjaman sepeda secara keseluruhan.
            """
        )

def main():

    st.title('Hasil Analisis Bike Sharing :motor_scooter:')
    st.header('1: Hubungan Temperatur Feeling (yang Dirasakan Manusia) dan Temperatur Aktual dengan Jumlah Peminjaman Sepeda')

    #Membaca data hasil analisis dari ipynb
    hour_bike = pd.read_csv('all_data.csv')

    atemp_temp_totalbike_df(hour_bike)
    st.header('2: Perbandingan Jumlah Peminjaman Sepeda Tiap Musim di Tahun 2012')
    season_totalbike_df(hour_bike)


#Menjalankan fungsi main
main()
