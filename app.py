import streamlit as st
import gspread
import pandas as pd

# 1. Artık dosyayı değil, Streamlit'in güvenli hafızasındaki 'secrets'ı kullanıyoruz
gcp_service_account = st.secrets["gcp_service_account"]

# 2. Dosya okumak yerine dictionary (sözlük) yöntemini kullanıyoruz
gc = gspread.service_account_from_dict(gcp_service_account)

# 3. Dosyanızın adını buraya yazın
sh = gc.open("Google_Sheets_Dosyanızın_Adı") 

# ... kodun geri kalanı ...
