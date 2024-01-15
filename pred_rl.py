import pickle
import streamlit as st

model = pickle.load(open('kernel_terbaik_rbf.sav', 'rb'))

st.title('Prediksi Total Produksi Rumput Laut Eucheuma Cottonii di Desa Lontar')

tahun = st.text_input('Input Tahun Prediksi')
bulan = st.text_input('Input Bulan Prediksi')
arus = st.number_input('Input Arus Prediksi')
suhu = st.text_input('Input Suhu Prediksi')
modal = st.text_input('Input Modal Prediksi')

predict = ''

if st.button ('Prediksi'):
    predict = model.predict(
        [[tahun,bulan,arus,suhu,modal]]
    )
    st.write('Prediksi Total Produksi Rumput Laut Eucheuma Cottonii : ', predict)
    st.write ('Ketepatan Prediksi : 94,57%')