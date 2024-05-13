import streamlit as st

option = st.sidebar.selectbox('Main Menu',['Dashboard','About','Kadar b/v','Kadar b/b'])
if option == 'Dashboard':
    st.markdown("<h1 style='text-align: center; color: black ;'>Kelompok 11</h1>", unsafe_allow_html=True)
    st.write('Anggota Kelompok : ')
    st.image('Hallo LPK_20240512_140146_0000.png', caption='')

if option == 'About':
    st.markdown ('<h2 style="color:grey;">Penerapan Konsentrasi Larutan pada Analisis Titrimetri</h2>', unsafe_allow_html=True)
    st.write ('Agar lebih mudah memahami apa itu konsentrasi larutan, sebaiknya kita mengetahui tentang arti larutan itu sendiri. Larutan dalam ilmu kimia mempunyai arti yaitu campuran yang bersifat homogen dengan perbandingan komposisi sesuai dengan komponen penyusunnya. Salah satu contoh larutan dalam kimia adalah H2SO4 (asam sulfat). Jika larutan H2SO4 (asam sulfat) dialiri listrik, maka akan menghantarkan listrik.')
    st.write ('Pada umumnya, suatu larutan terdiri satu jenis zat terlarut dan satu pelarut. Solvent (pelarut) dan Solut (zat yang terlarut) biasanya sudah sering didengar dan disebutkan. Solvent merupakan komponen yang dilihat secara fisik tidak berubah jika larutan terbentuk, sedangkan semua komponen yang ada pada Solut akan larut dalam pelarut.')
    st.write ('Pada praktikum analisis titrimetri, kebanyakan perhitungan yang digunakan untuk menentukan besaran kadar analit menggunakan perhitungan %(b/v) dan %(b/b).')

if option =='Kadar b/v':
    st.markdown("<h1 style='text-align: center; color: choco ;'>Kadar b/v</h1>", unsafe_allow_html=True)
    container = st.container(border=True)
    container.write("satuan konsentrasi ini memiliki definisi terdapat terdapat sejumlah gram sampel didalam 100 mL larutan. %(b/v) dapat didefinisikan juga sebagai %(g/mL). Jadi, untuk perhitungan %(b/v) harus menyisakan satuan gram dan mL dalam akhir perhitungan.")
    st.image('Screenshot (27).png', caption='')
    st.markdown('- KMnO4 diatas dapat diganti sesuai dengan larutan standar yang dijadikan titrant dalam proses titrasi')
    st.markdown('- ion Fe dapat digantikan sesuai dengan unsur yang ingin ditetapkan besaran kadarnya')
    st.markdown('- Volume sampel berarti adalah volume sampel dalam mL yang digunakan sebagai analit atau titrat dalam proses titrasi')
    st.markdown('- 10^-3 yang dimasukan dalam perhitungan diatas digunakan untuk mengganti satuan mg menjadi satuan g')
    st.markdown("<h2 style='text-align: center; color: black;'>perhitungan kadar b/v</h2>", unsafe_allow_html=True)
    volume_titran= st.number_input('masukan nilai volume titran (mL)',)
    normalitas_titran= st.number_input('masukan nilai normalitas titran (N)',)
    bobot_ekuivalen_sampel= st.number_input('masukan nilai bobot ekuivalen sampel (mg/mgrek)',0)
    volume_sampel= st.number_input('masukan nilai volume sampel (mL)',)
    hitung = st.button('hitung kadar b/v')

    if hitung :
        kadar = volume_titran*normalitas_titran*bobot_ekuivalen_sampel/volume_sampel*0.001*100
        st.success(f'perhitungan kadar sampel adalah = {kadar}')

if option =='Kadar b/b':
    st.markdown("<h1 style='text-align: center; color: black;'>Kadar b/b</h1>", unsafe_allow_html=True)
    container = st.container(border=True)
    container.write('satuan konsentrasi ini memiliki definisi terdapat terdapat sejumlah gram sampel didalam 100g pelarut. %(b/b) dapat didefinisikan juga sebagai %(g/g). Jadi, untuk perhitungan %(b/b) harus menyisakan satuan gram dan gram yang tidak perlu dicoret (dihilangkan) dalam akhir perhitungan.')
    st.image('Screenshot (26).png', caption='')
    st.markdown('- AgNO3 diatas dapat diganti sesuai dengan larutan standar yang dijadikan titrant dalam proses titrasi')
    st.markdown('- ion CL dapat digantikan sesuai dengan unsur yang ingin ditetapkan besaran kadarnya')
    st.markdown('- gram (g) sampel berarti adalah massa sampel yang digunakan sebagai analit atau titrat dalam proses titrasi')
    st.markdown("<h2 style='text-align: center; color: black;'>perhitungan kadar b/b</h2>", unsafe_allow_html=True)
    volume_titrant= st.number_input('masukan nilai volume titrant (mL)',)
    normalitas_titrant= st.number_input('masukan nilai normalitas titrant (N)',)
    bobot_ekuivalen_sampel= st.number_input('masukan nilai bobot ekuivalen titrat (mg/mgrek)',0)
    bobot_sampel= st.number_input('masukan nilai bobot sampel (g)',)
    hitung = st.button('hitung kadar b/b') 

    if hitung :
        kadar = volume_titrant*normalitas_titrant*bobot_ekuivalen_sampel/bobot_sampel*0.001*100
        st.success(f'perhitungan kadar sampel adalah = {kadar}')