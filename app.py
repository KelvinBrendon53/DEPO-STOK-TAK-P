import streamlit as st
import gspread
import pandas as pd

# Servis hesabı bağlantısı
gc = gspread.service_account(filename='service_account.json')
sh = gc.open("DEPO STOK TAKİP 24.06.2026")

st.title("DEPO STOK TAKİP")

# 1. Adım: Kullanıcının hangi sayfayı görmek istediğini seçmesini sağla
secilen_sayfa = st.selectbox("Görüntülemek istediğin tabloyu seç:", ["STOK LİSTESİ", "MALZEME SARFİYAT TABLOSU"])

# 2. Adım: Seçime göre veriyi çek
worksheet = sh.worksheet(secilen_sayfa)
data = worksheet.get_all_records()
df = pd.DataFrame(data)

# 3. Adım: Tabloyu ekrana bas
st.dataframe(df)

# Ekstra: Eğer veriyi indirmek istersen
st.download_button("Veriyi İndir (CSV)", df.to_csv(), "veri.csv")