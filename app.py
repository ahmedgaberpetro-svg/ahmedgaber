
import streamlit as st

USERNAME = "ahmedgaber"   # غيّرها لو اسم حسابك مختلف
REPO = "sawaqit-pwa"      # غيّره لو سميت الريبو غير ذلك

BASE = f"https://cdn.jsdelivr.net/gh/{USERNAME}/{REPO}@main/icons"
ICON32 = f"{BASE}/icon-32.png"
ICON192 = f"{BASE}/icon-192.png"
ICON512 = f"{BASE}/icon-512.png"
APPLE  = f"{BASE}/apple-touch-icon.png"
MANIFEST_URL = f"https://cdn.jsdelivr.net/gh/{USERNAME}/{REPO}@main/manifest.webmanifest"

st.set_page_config(page_title="Sawaqit", page_icon=ICON192, layout="centered")

st.markdown(
    f"""
    <link rel="icon" href="{ICON32}" sizes="32x32" />
    <link rel="apple-touch-icon" href="{APPLE}" />
    <link rel="manifest" href="{MANIFEST_URL}">
    <meta name="theme-color" content="#0f766e">
    """,
    unsafe_allow_html=True,
)

st.title("Sawaqit — توزيع السواقط")
st.caption("نسخة ويب قابلة للتثبيت (إضافة للشاشة الرئيسية).")

st.info("كل شيء جاهز. ارفع الملفات على GitHub ثم انشر من Streamlit Cloud.")

with st.expander("خطوات النشر بإيجاز"):
    st.write("1) أنشئ ريبو عام باسم **sawaqit-pwa** تحت المستخدم **ahmedgaber** (بدون مسافات).")
    st.write("2) ارفع الملفات كما هي (app.py, requirements.txt, manifest.webmanifest, icons/, .streamlit/).")
    st.write("3) ادخل share.streamlit.io → New app → اختر الريبو والفرع main، الملف app.py.")
    st.write("4) افتح الرابط على الموبايل ثم Add to Home screen.")
