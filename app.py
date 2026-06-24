import streamlit as st
import gspread
import pandas as pd

# Sayfa ayarları
st.set_page_config(page_title="Depo Stok Takip", layout="wide")

# 1. Bağlantı Ayarları (Cache ile performanslı hale getirdik)
@st.cache_resource
def get_gspread_client():
    # Secrets dosyanızdaki tanımlı isim
    gcp_credentials = st.secrets["gcp_service_account"]
    # service_account_from_dict kullanarak doğrudan kimlik bilgilerini veriyoruz
    return gspread.service_account_from_dict(gcp_credentials)

def main():
    st.title("📦 DEPO STOK TAKİP PANELİ")
    
    try:
        # Bağlantıyı al
        gc = get_gspread_client()
        
        # Google Sheets dosyanızın adı (Tırnak içindeki ismi kontrol edin)
        sh = gc.open("DEPO STOK TAKİP 24.06.2026")
        
        # Sayfaları otomatik listele
        worksheet_list = [ws.title for ws in sh.worksheets()]
        secilen_sayfa = st.selectbox("Görüntülemek istediğin tabloyu seç:", worksheet_list)
        
        # Seçime göre veriyi çek
        worksheet = sh.worksheet(secilen_sayfa)
        data = worksheet.get_all_records()
        df = pd.DataFrame(data)
        
        # Tabloyu göster
        st.subheader(f"Sayfa: {secilen_sayfa}")
        st.dataframe(df, use_container_width=True)
        
        # İndirme Butonu
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Veriyi CSV Olarak İndir",
            data=csv,
            file_name=f'{secilen_sayfa}.csv',
            mime='text/csv',
        )

    except Exception as e:
        st.error("Verilere ulaşılamadı. Lütfen Google API yetkilerini ve dosya ismini kontrol edin.")
        st.write(f"Hata detayı: {e}")

if __name__ == "__main__":
    main()
