import streamlit as st

# ==========================================
# LANGUAGE DATABASE (50+ Languages)
# ==========================================
languages = {
    "English": {"code": "en", "flag": "🇬🇧"},
    "Urdu": {"code": "ur", "flag": "🇵🇰"},
    "Hindi": {"code": "hi", "flag": "🇮🇳"},
    "Arabic": {"code": "ar", "flag": "🇸🇦"},
    "Spanish": {"code": "es", "flag": "🇪🇸"},
    "French": {"code": "fr", "flag": "🇫🇷"},
    "German": {"code": "de", "flag": "🇩🇪"},
    "Chinese": {"code": "zh", "flag": "🇨🇳"},
    "Japanese": {"code": "ja", "flag": "🇯🇵"},
    "Korean": {"code": "ko", "flag": "🇰🇷"},
    "Russian": {"code": "ru", "flag": "🇷🇺"},
    "Turkish": {"code": "tr", "flag": "🇹🇷"},
    "Persian": {"code": "fa", "flag": "🇮🇷"},
    "Pashto": {"code": "ps", "flag": "🇦🇫"},
    "Punjabi": {"code": "pa", "flag": "🇮🇳"},
    "Sindhi": {"code": "sd", "flag": "🇵🇰"},
    "Bengali": {"code": "bn", "flag": "🇧🇩"},
    "Portuguese": {"code": "pt", "flag": "🇵🇹"},
    "Italian": {"code": "it", "flag": "🇮🇹"},
    "Dutch": {"code": "nl", "flag": "🇳🇱"},
    "Greek": {"code": "el", "flag": "🇬🇷"},
    "Hebrew": {"code": "he", "flag": "🇮🇱"},
    "Thai": {"code": "th", "flag": "🇹🇭"},
    "Vietnamese": {"code": "vi", "flag": "🇻🇳"},
    "Indonesian": {"code": "id", "flag": "🇮🇩"},
    "Malay": {"code": "ms", "flag": "🇲🇾"},
    "Swahili": {"code": "sw", "flag": "🇹🇿"},
    "Tamil": {"code": "ta", "flag": "🇮🇳"},
    "Telugu": {"code": "te", "flag": "🇮🇳"},
    "Kannada": {"code": "kn", "flag": "🇮🇳"},
    "Malayalam": {"code": "ml", "flag": "🇮🇳"},
    "Gujarati": {"code": "gu", "flag": "🇮🇳"},
    "Marathi": {"code": "mr", "flag": "🇮🇳"},
    "Nepali": {"code": "ne", "flag": "🇳🇵"},
}

# ==========================================
# TRANSLATIONS
# ==========================================
translations = {
    "en": {
        "app_title": "🧪 ChemEngBot",
        "select_feature": "📌 SELECT FEATURE",
        "home": "🏠 HOME",
        "reynolds": "📊 REYNOLDS NUMBER",
        "heat_transfer": "🔥 HEAT TRANSFER",
        "pressure_drop": "📉 PRESSURE DROP",
        "ntu": "📐 NTU METHOD",
        "temp_conv": "🌡️ TEMPERATURE CONVERTER",
        "formulas": "📚 FORMULAS",
        "concepts": "💡 CONCEPTS",
        "welcome_title": "🧪 Chemical Engineering Assistant Bot",
        "welcome_subtitle": "Your AI-Powered Companion for Chemical Engineering Calculations",
        "welcome_text": "### 👋 Welcome to ChemEngBot!\n\nYour personal **Chemical Engineering Assistant** that helps you with:\n\n| ✅ | Feature | Description |\n|---|---|---|\n| 📊 | **Reynolds Number** | Calculate flow characteristics (Laminar/Turbulent) |\n| 🔥 | **Heat Transfer** | Compute heat transfer rates using Q = UAΔT |\n| 📉 | **Pressure Drop** | Calculate pressure losses in pipes |\n| 📐 | **NTU Method** | Heat exchanger effectiveness calculation |\n| 📚 | **Formulas** | View common engineering formulas |\n| 💡 | **Concepts** | Learn engineering concepts |\n\n**Select any feature from the sidebar to get started!**",
        "quick_ref": "📈 Quick Reference Formulas",
        "reynolds_header": "📊 Reynolds Number Calculator",
        "reynolds_formula": "**Formula:** Re = ρvd/μ",
        "reynolds_info": "💡 Reynolds Number determines flow type: **Laminar** (<2000), **Transitional** (2000-4000), **Turbulent** (>4000)",
        "density": "📊 Density ρ (kg/m³):",
        "velocity": "💨 Velocity v (m/s):",
        "diameter": "📏 Diameter d (m):",
        "viscosity": "💧 Viscosity μ (Pa·s):",
        "calculate_reynolds": "🔬 Calculate Reynolds Number",
        "result_reynolds": "### ✅ Reynolds Number = **{value}**",
        "laminar": "🟢 **Flow Type:** Laminar Flow (Smooth, steady)",
        "transitional": "🟡 **Flow Type:** Transitional Flow (Unstable)",
        "turbulent": "🔴 **Flow Type:** Turbulent Flow (Chaotic, mixing)",
        "error_viscosity": "❌ Viscosity must be greater than 0!",
        "heat_header": "🔥 Heat Transfer Calculator",
        "heat_formula": "**Formula:** Q = U × A × ΔT",
        "heat_info": "💡 Heat transfer rate is measured in **Watts (W)** or **kilowatts (kW)**",
        "u_value": "🔧 U (W/m²·K):",
        "area": "📐 Area A (m²):",
        "delta_t": "🌡️ ΔT (K or °C):",
        "calculate_heat": "🔥 Calculate Heat Transfer",
        "result_heat": "### ✅ Heat Transfer Rate = **{value} W**",
        "result_heat_kw": "#### 📊 = {value} kW",
        "pressure_header": "📉 Pressure Drop Calculator",
        "pressure_formula": "**Formula:** ΔP = f × (L/D) × (ρv²/2)",
        "friction": "Friction factor f",
        "length": "Length L (m)",
        "calc_pressure": "Calculate ΔP",
        "result_pressure": "ΔP = {value} Pa",
        "temp_header": "🌡️ Temperature Converter",
        "temp_info": "💡 Enter value in any unit → Get all 4 scales instantly!",
        "input_unit": "Input Unit:",
        "temp_value": "Temperature Value:",
        "convert_temp": "🔄 Convert Temperature",
        "converted_values": "✅ **Converted Values:**",
        "formulas_header": "📚 Chemical Engineering Formulas",
        "formulas_info": "Select subject → View 25+ detailed formulas",
        "choose_subject": "Choose Subject:",
        "concepts_header": "💡 Concepts",
        "concepts_text": """
**Engineering Terms:**
- **Reynolds Number**: Flow type (Laminar/Turbulent)
- **Heat Transfer**: Q = UAΔT
- **Pressure Drop**: Energy loss in pipes
- **NTU**: Heat exchanger performance
""",
        "footer_name": "👨‍🔧 ZUNAIR SHAHZAD",
        "footer_university": "🎓 Chemical Engineering | UET LAHORE",
        "footer_credit": "🚀 ChemEngBot — Your Chemical Engineering Assistant",
        "footer_copyright": "© 2024 All Rights Reserved",
        "language": "🌐 LANGUAGE"
    },
    "ur": {
        "app_title": "🧪 کیم انج بوٹ",
        "select_feature": "📌 فیچر منتخب کریں",
        "home": "🏠 ہوم",
        "reynolds": "📊 رینالڈز نمبر",
        "heat_transfer": "🔥 حرارت کی منتقلی",
        "pressure_drop": "📉 پریشر ڈراپ",
        "ntu": "📐 این ٹی یو طریقہ",
        "temp_conv": "🌡️ درجہ حرارت کنورٹر",
        "formulas": "📚 فارمولے",
        "concepts": "💡 تصورات",
        "welcome_title": "🧪 کیمیکل انجینئرنگ اسسٹنٹ بوٹ",
        "welcome_subtitle": "کیمیکل انجینئرنگ حسابات کے لیے آپ کا AI پاورڈ ساتھی",
        "quick_ref": "📈 فوری حوالہ فارمولے",
        "reynolds_header": "📊 رینالڈز نمبر کیلکولیٹر",
        "reynolds_formula": "**فارمولا:** Re = ρvd/μ",
        "reynolds_info": "💡 رینالڈز نمبر بہاؤ کی قسم بتاتا ہے: **لیمینر** (<2000), **ٹرانزیشنل** (2000-4000), **ٹربولنٹ** (>4000)",
        "density": "📊 کثافت ρ (kg/m³):",
        "velocity": "💨 رفتار v (m/s):",
        "diameter": "📏 قطر d (m):",
        "viscosity": "💧 وسکاسیٹی μ (Pa·s):",
        "calculate_reynolds": "🔬 رینالڈز نمبر حساب کریں",
        "result_reynolds": "### ✅ رینالڈز نمبر = **{value}**",
        "laminar": "🟢 **بہاؤ کی قسم:** لیمنر بہاؤ (ہموار، مستحکم)",
        "transitional": "🟡 **بہاؤ کی قسم:** ٹرانزیشنل بہاؤ (غیر مستحکم)",
        "turbulent": "🔴 **بہاؤ کی قسم:** ٹربولنٹ بہاؤ (انتھائی، مکسنگ)",
        "error_viscosity": "❌ وسکاسیٹی صفر سے زیادہ ہونی چاہیے!",
        "heat_header": "🔥 حرارت کی منتقلی کیلکولیٹر",
        "heat_formula": "**فارمولا:** Q = U × A × ΔT",
        "heat_info": "💡 حرارت کی منتقلی کی شرح **واٹ (W)** یا **کلوواٹ (kW)** میں ماپا جاتا ہے",
        "u_value": "🔧 U (W/m²·K):",
        "area": "📐 رقبہ A (m²):",
        "delta_t": "🌡️ ΔT (K یا °C):",
        "calculate_heat": "🔥 حرارت کی منتقلی حساب کریں",
        "result_heat": "### ✅ حرارت کی منتقلی کی شرح = **{value} W**",
        "result_heat_kw": "#### 📊 = {value} kW",
        "pressure_header": "📉 پریشر ڈراپ کیلکولیٹر",
        "pressure_formula": "**فارمولا:** ΔP = f × (L/D) × (ρv²/2)",
        "friction": "رگڑ عنصر f",
        "length": "لمبائی L (m)",
        "calc_pressure": "ΔP حساب کریں",
        "result_pressure": "ΔP = {value} Pa",
        "temp_header": "🌡️ درجہ حرارت کنورٹر",
        "temp_info": "💡 کسی بھی یونٹ میں قیمت ڈالیں → تمام 4 پیمانے فوری حاصل کریں!",
        "input_unit": "انپٹ یونٹ:",
        "temp_value": "درجہ حرارت کی قیمت:",
        "convert_temp": "🔄 درجہ حرارت تبدیل کریں",
        "converted_values": "✅ **تبدیل شدہ قیمتیں:**",
        "formulas_header": "📚 کیمیکل انجینئرنگ فارمولے",
        "formulas_info": "مضمون منتخب کریں → 25+ تفصیلی فارمولے دیکھیں",
        "choose_subject": "مضمون منتخب کریں:",
        "concepts_header": "💡 تصورات",
        "concepts_text": """
**انجینئرنگ اصطلاحات:**
- **رینالڈز نمبر**: بہاؤ کی قسم (لیمینر/ٹربولنٹ)
- **حرارت کی منتقلی**: Q = UAΔT
- **پریشر ڈراپ**: پائپوں میں توانائی کا نقصان
- **NTU**: ہیٹ ایکسچینجر کی کارکردگی
""",
        "footer_name": "👨‍🔧 زینیر شہزاد",
        "footer_university": "🎓 کیمیکل انجینئرنگ | یو ای ٹی لاہور",
        "footer_credit": "🚀 کیم انج بوٹ — آپ کا کیمیکل انجینئرنگ اسسٹنٹ",
        "footer_copyright": "© 2024 جملہ حقوق محفوظ ہیں",
        "language": "🌐 زبان"
    },
    "hi": {
        "app_title": "🧪 केम इंज बॉट",
        "select_feature": "📌 सुविधा चुनें",
        "home": "🏠 होम",
        "reynolds": "📊 रेनॉल्ड्स संख्या",
        "heat_transfer": "🔥 ऊष्मा स्थानांतरण",
        "pressure_drop": "📉 दबाव में गिरावट",
        "ntu": "📐 एनटीयू विधि",
        "temp_conv": "🌡️ तापमान परिवर्तक",
        "formulas": "📚 सूत्र",
        "concepts": "💡 अवधारणाएँ",
        "welcome_title": "🧪 रासायनिक इंजीनियरिंग सहायक बॉट",
        "welcome_subtitle": "रासायनिक इंजीनियरिंग गणनाओं के लिए आपका AI संचालित साथी",
        "quick_ref": "📈 त्वरित संदर्भ सूत्र",
        "reynolds_header": "📊 रेनॉल्ड्स संख्या कैलकुलेटर",
        "reynolds_formula": "**सूत्र:** Re = ρvd/μ",
        "reynolds_info": "💡 रेनॉल्ड्स संख्या प्रवाह प्रकार बताती है: **लैमिनर** (<2000), **ट्रांज़िशनल** (2000-4000), **टर्बुलेंट** (>4000)",
        "density": "📊 घनत्व ρ (kg/m³):",
        "velocity": "💨 वेग v (m/s):",
        "diameter": "📏 व्यास d (m):",
        "viscosity": "💧 श्यानता μ (Pa·s):",
        "calculate_reynolds": "🔬 रेनॉल्ड्स संख्या की गणना करें",
        "result_reynolds": "### ✅ रेनॉल्ड्स संख्या = **{value}**",
        "laminar": "🟢 **प्रवाह प्रकार:** लैमिनर प्रवाह (सहज, स्थिर)",
        "transitional": "🟡 **प्रवाह प्रकार:** ट्रांज़िशनल प्रवाह (अस्थिर)",
        "turbulent": "🔴 **प्रवाह प्रकार:** टर्बुलेंट प्रवाह (अव्यवस्थित, मिश्रण)",
        "error_viscosity": "❌ श्यानता शून्य से अधिक होनी चाहिए!",
        "heat_header": "🔥 ऊष्मा स्थानांतरण कैलकुलेटर",
        "heat_formula": "**सूत्र:** Q = U × A × ΔT",
        "heat_info": "💡 ऊष्मा स्थानांतरण दर **वाट (W)** या **किलोवाट (kW)** में मापी जाती है",
        "u_value": "🔧 U (W/m²·K):",
        "area": "📐 क्षेत्रफल A (m²):",
        "delta_t": "🌡️ ΔT (K या °C):",
        "calculate_heat": "🔥 ऊष्मा स्थानांतरण की गणना करें",
        "result_heat": "### ✅ ऊष्मा स्थानांतरण दर = **{value} W**",
        "result_heat_kw": "#### 📊 = {value} kW",
        "pressure_header": "📉 दबाव ड्रॉप कैलकुलेटर",
        "pressure_formula": "**सूत्र:** ΔP = f × (L/D) × (ρv²/2)",
        "friction": "घर्षण कारक f",
        "length": "लंबाई L (m)",
        "calc_pressure": "ΔP की गणना करें",
        "result_pressure": "ΔP = {value} Pa",
        "temp_header": "🌡️ तापमान परिवर्तक",
        "temp_info": "💡 किसी भी इकाई में मान दर्ज करें → सभी 4 पैमाने तुरंत प्राप्त करें!",
        "input_unit": "इनपुट इकाई:",
        "temp_value": "तापमान मान:",
        "convert_temp": "🔄 तापमान बदलें",
        "converted_values": "✅ **परिवर्तित मान:**",
        "formulas_header": "📚 रासायनिक इंजीनियरिंग सूत्र",
        "formulas_info": "विषय चुनें → 25+ विस्तृत सूत्र देखें",
        "choose_subject": "विषय चुनें:",
        "concepts_header": "💡 अवधारणाएँ",
        "concepts_text": """
**इंजीनियरिंग शब्द:**
- **रेनॉल्ड्स संख्या**: प्रवाह प्रकार (लैमिनर/टर्बुलेंट)
- **ऊष्मा स्थानांतरण**: Q = UAΔT
- **दबाव ड्रॉप**: पाइपों में ऊर्जा हानि
- **NTU**: हीट एक्सचेंजर प्रदर्शन
""",
        "footer_name": "👨‍🔧 ज़ुनैर शहज़ाद",
        "footer_university": "🎓 रासायनिक इंजीनियरिंग | यूईटी लाहौर",
        "footer_credit": "🚀 केम इंज बॉट — आपका रासायनिक इंजीनियरिंग सहायक",
        "footer_copyright": "© 2024 सर्वाधिकार सुरक्षित",
        "language": "🌐 भाषा"
    }
}

# Add more languages with same structure (copy English and translate)

# ==========================================
# GET TRANSLATION FUNCTION
# ==========================================
def _(key, **kwargs):
    """Get translated text for current language"""
    lang = st.session_state.get("language", "en")
    text = translations.get(lang, translations["en"]).get(key, translations["en"].get(key, key))
    if kwargs:
        text = text.format(**kwargs)
    return text

# ==========================================
# INITIALIZE LANGUAGE IN SESSION STATE
# ==========================================
if "language" not in st.session_state:
    st.session_state.language = "en"

# ==========================================
# PAGE CONFIG
# ==========================================
st.set_page_config(
    page_title=_("app_title"),
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# CUSTOM CSS
# ==========================================
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #4CAF50;
        text-align: center;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .card {
        background-color: #f8f9fa;
        padding: 1.2rem;
        border-radius: 12px;
        margin: 0.5rem 0;
        border-left: 4px solid #4CAF50;
        transition: transform 0.2s;
    }
    .card:hover {
        transform: translateY(-3px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a3c6e 0%, #0e2a4f 100%);
    }
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    [data-testid="stSidebar"] .stMarkdown {
        color: white !important;
    }
    [data-testid="stSidebar"] .stRadio div {
        color: white !important;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        font-weight: bold;
        font-size: 1rem;
        padding: 0.5rem 1rem;
        transition: all 0.3s;
    }
    .stButton button:hover {
        background-color: #45a049;
        transform: scale(1.02);
    }
    .stSuccess, .stInfo, .stWarning, .stError {
        border-radius: 10px;
        padding: 1rem;
    }
    .footer {
        text-align: center;
        padding: 2rem;
        margin-top: 3rem;
        border-top: 2px solid #4CAF50;
        background: linear-gradient(135deg, #1a3c6e 0%, #0e2a4f 100%);
        border-radius: 10px;
    }
    .footer-name {
        font-size: 1.8rem !important;
        font-weight: bold !important;
        color: #4CAF50 !important;
        margin-bottom: 0.3rem !important;
    }
    .footer-university {
        font-size: 1.2rem !important;
        color: #ccc !important;
    }
    .footer-credit {
        font-size: 1rem !important;
        color: #aaa !important;
        margin-top: 0.5rem !important;
    }
    [data-testid="stMetricValue"] {
        font-size: 1.2rem;
        font-weight: bold;
        color: #4CAF50;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# SIDEBAR
# ==========================================
with st.sidebar:
    st.image("https://img.icons8.com/color/96/chemical-plant.png", width=80)
    st.markdown(f"# {_('app_title')}")
    st.markdown("---")
    
    # 🌐 LANGUAGE SELECTOR
    st.markdown(f"### {_('language')}")
    lang_options = [f"{info['flag']} {name}" for name, info in languages.items()]
    current_lang_display = next((f"{languages[st.session_state.language]['flag']} {st.session_state.language}" 
                                  for lang_name, info in languages.items() if info['code'] == st.session_state.language), 
                                 "🇬🇧 English")
    
    selected_lang = st.selectbox("", lang_options, index=lang_options.index(current_lang_display) if current_lang_display in lang_options else 0, label_visibility="collapsed")
    
    for lang_name, info in languages.items():
        if f"{info['flag']} {lang_name}" == selected_lang:
            st.session_state.language = info['code']
    
    st.markdown("---")
    
    # Navigation
    feature = st.radio(
        _("select_feature"),
        [
            _("home"),
            _("reynolds"),
            _("heat_transfer"),
            _("pressure_drop"),
            _("ntu"),
            _("temp_conv"),
            _("formulas"),
            _("concepts")
        ],
        index=0
    )
    
    st.markdown("---")
    
    # Developer Info
    st.markdown(f"""
    <div style="text-align: center; padding: 1rem 0;">
        <hr style="border-color: #4CAF50;">
        <p style="font-size: 1.5rem; font-weight: bold; color: #4CAF50; margin: 0.5rem 0;">👨‍🔧 ZUNAIR SHAHZAD</p>
        <p style="font-size: 1rem; color: #ccc; margin: 0;">🎓 Chemical Engineering</p>
        <p style="font-size: 1.1rem; color: #4CAF50; font-weight: bold; margin: 0;">UET LAHORE</p>
        <hr style="border-color: #4CAF50;">
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# MAIN CONTENT
# ==========================================

if feature == _("home"):
    st.markdown(f'<p class="main-header">{_("welcome_title")}</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="sub-header">{_("welcome_subtitle")}</p>', unsafe_allow_html=True)
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown(_("welcome_text"))
    with col2:
        st.image("https://img.icons8.com/color/200/chemical-plant.png")
    
    st.markdown("---")
    st.subheader(_("quick_ref"))
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Reynolds Number", "Re = ρvd/μ")
    with col2:
        st.metric("Heat Transfer", "Q = UAΔT")
    with col3:
        st.metric("Pressure Drop", "ΔP = f(L/D)(ρv²/2)")
    with col4:
        st.metric("NTU", "NTU = UA/C_min")

elif feature == _("reynolds"):
    st.header(_("reynolds_header"))
    st.markdown(_("reynolds_formula"))
    st.info(_("reynolds_info"))
    
    col1, col2 = st.columns(2)
    with col1:
        rho = st.number_input(_("density"), value=1000.0, step=10.0, format="%.2f")
        v = st.number_input(_("velocity"), value=1.0, step=0.1, format="%.2f")
    with col2:
        d = st.number_input(_("diameter"), value=0.05, step=0.01, format="%.3f")
        mu = st.number_input(_("viscosity"), value=0.001, step=0.0001, format="%.4f")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button(_("calculate_reynolds"), type="primary", use_container_width=True):
            if mu > 0:
                Re = (rho * v * d) / mu
                st.success(_("result_reynolds", value=f"{Re:,.2f}"))
                if Re < 2000:
                    st.info(_("laminar"))
                elif Re < 4000:
                    st.warning(_("transitional"))
                else:
                    st.error(_("turbulent"))
            else:
                st.error(_("error_viscosity"))

elif feature == _("heat_transfer"):
    st.header(_("heat_header"))
    st.markdown(_("heat_formula"))
    st.info(_("heat_info"))
    
    col1, col2 = st.columns(2)
    with col1:
        U = st.number_input(_("u_value"), value=500.0, step=50.0)
        A = st.number_input(_("area"), value=10.0, step=1.0)
    with col2:
        dT = st.number_input(_("delta_t"), value=50.0, step=5.0)
    
    if st.button(_("calculate_heat"), type="primary"):
        Q = U * A * dT
        st.success(_("result_heat", value=f"{Q:,.2f}"))
        st.info(_("result_heat_kw", value=f"{Q/1000:.2f}"))

elif feature == _("pressure_drop"):
    st.header(_("pressure_header"))
    st.markdown(_("pressure_formula"))
    
    col1, col2 = st.columns(2)
    with col1:
        f = st.number_input(_("friction"), value=0.02)
        L = st.number_input(_("length"), value=100.0)
    with col2:
        d = st.number_input("Diameter d (m)", value=0.1)
        rho = st.number_input("Density ρ", value=1000.0)
        v = st.number_input("Velocity v (m/s)", value=2.0)
    
    if st.button(_("calc_pressure")):
        delta_p = f * (L / d) * (rho * v**2 / 2)
        st.success(_("result_pressure", value=f"{delta_p:.0f}"))

elif feature == _("temp_conv"):
    st.header(_("temp_header"))
    st.markdown("**Convert between Celsius, Fahrenheit, Kelvin, Rankine**")
    st.info(_("temp_info"))
    
    col1, col2 = st.columns(2)
    with col1:
        input_unit = st.selectbox(_("input_unit"), ["Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)", "Rankine (°R)"])
        temp_value = st.number_input(_("temp_value"), value=25.0, step=1.0)
    
    if st.button(_("convert_temp"), type="primary"):
        if "Celsius" in input_unit:
            c = temp_value
        elif "Fahrenheit" in input_unit:
            c = (temp_value - 32) * 5/9
        elif "Kelvin" in input_unit:
            c = temp_value - 273.15
        elif "Rankine" in input_unit:
            c = (temp_value - 491.67) * 5/9
        
        f = c * 9/5 + 32
        k = c + 273.15
        r = f + 459.67
        
        st.success(_("converted_values"))
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("°C", f"{c:.2f}")
        col2.metric("°F", f"{f:.2f}")
        col3.metric("K", f"{k:.2f}")
        col4.metric("°R", f"{r:.2f}")
        st.info(f"Input: {temp_value} {input_unit.split()[1]} → All scales above")

elif feature == _("ntu"):
    st.header(_("ntu"))
    st.markdown("**NTU = UA/C_min**")
    
    col1, col2 = st.columns(2)
    with col1:
        U = st.number_input("U", value=500.0)
        A = st.number_input("A", value=10.0)
    C_min = st.number_input("C_min", value=1000.0)
    
    if st.button("Calculate NTU"):
        NTU = (U * A) / C_min
        st.success(f"NTU = {NTU:.2f}")

elif feature == _("formulas"):
    try:
        from formulas_data import formulas_data
        st.header(_("formulas_header"))
        st.info(_("formulas_info"))
        
        subject = st.selectbox(_("choose_subject"), list(formulas_data.keys()))
        
        if subject:
            st.subheader(f"📖 {subject}")
            for formula in formulas_data[subject]:
                with st.expander(f"📐 {formula['name']}"):
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown(f"**Description:** {formula['desc']}")
                        st.markdown(f"**Parameters:** {formula['params']}")
                    with col2:
                        st.markdown(f"**Equation:** `{formula['eq']}`")
                        st.info(f"**Unit:** {formula['unit']}\n**Purpose:** {formula['purpose']}")
    except:
        st.header(_("formulas_header"))
        st.info("Formulas data not found. Please check formulas_data.py file.")

elif feature == _("concepts"):
    st.header(_("concepts_header"))
    st.markdown(_("concepts_text"))

# ==========================================
# FOOTER
# ==========================================
st.markdown("---")
st.markdown(f"""
<div class="footer">
    <p class="footer-name">{_("footer_name")}</p>
    <p class="footer-university">{_("footer_university")}</p>
    <p class="footer-credit">{_("footer_credit")}</p>
    <p class="footer-credit">{_("footer_copyright")}</p>
</div>
""", unsafe_allow_html=True)