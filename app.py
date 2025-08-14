
import streamlit as st

USERNAME = "ahmedgaberpetro-svg"   # غيّرها لو اسم حسابك مختلف
REPO = "ahmedgaber"      # غيّره لو سميت الريبو غير ذلك

import streamlit as st

import streamlit as st

# روابط الأيقونات والمانيفست من الريبو الجديد عبر jsDelivr
ICON32   = "https://cdn.jsdelivr.net/gh/ahmedgaberpetro-svg/sawaqit-app@main/icon-32.png"
ICON192  = "https://cdn.jsdelivr.net/gh/ahmedgaberpetro-svg/sawaqit-app@main/icon-192.png"
ICON512  = "https://cdn.jsdelivr.net/gh/ahmedgaberpetro-svg/sawaqit-app@main/icon-512.png"
APPLE    = "https://cdn.jsdelivr.net/gh/ahmedgaberpetro-svg/sawaqit-app@main/apple-touch-icon.png"
MANIFEST = "https://cdn.jsdelivr.net/gh/ahmedgaberpetro-svg/sawaqit-app@main/manifest.webmanifest"

st.set_page_config(page_title="Sawaqit", page_icon=ICON32)

# حقن أيقونات + مانيفست في <head>
st.markdown(
    f"""
    <link rel="apple-touch-icon" href="{APPLE}">
    <link rel="icon" type="image/png" sizes="32x32"  href="{ICON32}">
    <link rel="icon" type="image/png" sizes="192x192" href="{ICON192}">
    <link rel="icon" type="image/png" sizes="512x512" href="{ICON512}">
    <link rel="manifest" href="{MANIFEST}">
    <meta name="theme-color" content="#0ea5e9">
    """,
    unsafe_allow_html=True,
)
)

)

st.title("Sawaqit — توزيع السواقط")
st.caption("نسخة ويب قابلة للتثبيت (إضافة للشاشة الرئيسية).")

st.info("كل شيء جاهز. ارفع الملفات على GitHub ثم انشر من Streamlit Cloud.")

with st.expander("خطوات النشر بإيجاز"):
    st.write("1) أنشئ ريبو عام باسم **sawaqit-pwa** تحت المستخدم **ahmedgaber** (بدون مسافات).")
    st.write("2) ارفع الملفات كما هي (app.py, requirements.txt, manifest.webmanifest, icons/, .streamlit/).")
    st.write("3) ادخل share.streamlit.io → New app → اختر الريبو والفرع main، الملف app.py.")
    st.write("4) افتح الرابط على الموبايل ثم Add to Home screen.")
