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
}

# ==========================================
# TRANSLATIONS
# ==========================================
translations = {
    "en": {
        "app_title": "🧪 ChemEngBot",
        "language": "🌐 LANGUAGE",
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
        "quick_ref": "📈 Quick Reference Formulas",
        "reynolds_header": "📊 Reynolds Number Calculator",
        "reynolds_formula": "**Formula:** Re = ρvd/μ",
        "reynolds_info": "💡 Reynolds Number: **Laminar** (<2000), **Transitional** (2000-4000), **Turbulent** (>4000)",
        "density": "📊 Density ρ (kg/m³):",
        "velocity": "💨 Velocity v (m/s):",
        "diameter": "📏 Diameter d (m):",
        "viscosity": "💧 Viscosity μ (Pa·s):",
        "calculate_reynolds": "🔬 Calculate Reynolds Number",
        "laminar": "🟢 **Flow Type:** Laminar Flow",
        "transitional": "🟡 **Flow Type:** Transitional Flow",
        "turbulent": "🔴 **Flow Type:** Turbulent Flow",
        "error_viscosity": "❌ Viscosity must be greater than 0!",
        "heat_header": "🔥 Heat Transfer Calculator",
        "heat_formula": "**Formula:** Q = U × A × ΔT",
        "heat_info": "💡 Heat transfer rate in **Watts (W)** or **kilowatts (kW)**",
        "u_value": "🔧 U (W/m²·K):",
        "area": "📐 Area A (m²):",
        "delta_t": "🌡️ ΔT (K or °C):",
        "calculate_heat": "🔥 Calculate Heat Transfer",
        "pressure_header": "📉 Pressure Drop Calculator",
        "pressure_formula": "**Formula:** ΔP = f × (L/D) × (ρv²/2)",
        "friction": "Friction factor f",
        "length": "Length L (m)",
        "calc_pressure": "Calculate ΔP",
        "temp_header": "🌡️ Temperature Converter",
        "temp_info": "💡 Enter value → Get all 4 scales",
        "input_unit": "Input Unit:",
        "temp_value": "Temperature Value:",
        "convert_temp": "🔄 Convert Temperature",
        "converted_values": "✅ Converted Values:",
        "formulas_header": "📚 Chemical Engineering Formulas",
        "formulas_info": "Select subject → View formulas",
        "choose_subject": "Choose Subject:",
        "concepts_header": "💡 Concepts",
        "footer_name": "👨‍🔧 ZUNAIR SHAHZAD",
        "footer_university": "🎓 Chemical Engineering | UET LAHORE",
        "footer_credit": "🚀 ChemEngBot — Your Chemical Engineering Assistant",
        "footer_copyright": "© 2024 All Rights Reserved",
    },
    "ur": {
        "app_title": "🧪 کیم انج بوٹ",
        "language": "🌐 زبان",
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
        "welcome_subtitle": "کیمیکل انجینئرنگ حسابات کے لیے آپ کا AI ساتھی",
        "quick_ref": "📈 فوری حوالہ فارمولے",
        "reynolds_header": "📊 رینالڈز نمبر کیلکولیٹر",
        "reynolds_formula": "**فارمولا:** Re = ρvd/μ",
        "reynolds_info": "💡 رینالڈز نمبر بہاؤ کی قسم: **لیمینر** (<2000), **ٹربولنٹ** (>4000)",
        "density": "📊 کثافت ρ (kg/m³):",
        "velocity": "💨 رفتار v (m/s):",
        "diameter": "📏 قطر d (m):",
        "viscosity": "💧 وسکاسیٹی μ (Pa·s):",
        "calculate_reynolds": "🔬 رینالڈز نمبر حساب کریں",
        "laminar": "🟢 **بہاؤ:** لیمنر بہاؤ",
        "transitional": "🟡 **بہاؤ:** ٹرانزیشنل بہاؤ",
        "turbulent": "🔴 **بہاؤ:** ٹربولنٹ بہاؤ",
        "error_viscosity": "❌ وسکاسیٹی صفر سے زیادہ ہونی چاہیے!",
        "heat_header": "🔥 حرارت کی منتقلی کیلکولیٹر",
        "heat_formula": "**فارمولا:** Q = U × A × ΔT",
        "heat_info": "💡 حرارت کی منتقلی **واٹ (W)** میں",
        "u_value": "🔧 U (W/m²·K):",
        "area": "📐 رقبہ A (m²):",
        "delta_t": "🌡️ ΔT (K یا °C):",
        "calculate_heat": "🔥 حرارت کی منتقلی حساب کریں",
        "pressure_header": "📉 پریشر ڈراپ کیلکولیٹر",
        "pressure_formula": "**فارمولا:** ΔP = f × (L/D) × (ρv²/2)",
        "friction": "رگڑ عنصر f",
        "length": "لمبائی L (m)",
        "calc_pressure": "ΔP حساب کریں",
        "temp_header": "🌡️ درجہ حرارت کنورٹر",
        "temp_info": "💡 کوئی بھی یونٹ ڈالیں → تمام 4 پیمانے",
        "input_unit": "انپٹ یونٹ:",
        "temp_value": "درجہ حرارت:",
        "convert_temp": "🔄 تبدیل کریں",
        "converted_values": "✅ تبدیل شدہ قیمتیں:",
        "formulas_header": "📚 کیمیکل انجینئرنگ فارمولے",
        "formulas_info": "مضمون منتخب کریں → فارمولے دیکھیں",
        "choose_subject": "مضمون منتخب کریں:",
        "concepts_header": "💡 تصورات",
        "footer_name": "👨‍🔧 زینیر شہزاد",
        "footer_university": "🎓 کیمیکل انجینئرنگ | یو ای ٹی لاہور",
        "footer_credit": "🚀 کیم انج بوٹ — آپ کا کیمیکل انجینئرنگ اسسٹنٹ",
        "footer_copyright": "© 2024 جملہ حقوق محفوظ ہیں",
    },
    "hi": {
        "app_title": "🧪 केम इंज बॉट",
        "language": "🌐 भाषा",
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
        "welcome_subtitle": "रासायनिक इंजीनियरिंग गणनाओं के लिए आपका AI साथी",
        "quick_ref": "📈 त्वरित संदर्भ सूत्र",
        "reynolds_header": "📊 रेनॉल्ड्स संख्या कैलकुलेटर",
        "reynolds_formula": "**सूत्र:** Re = ρvd/μ",
        "reynolds_info": "💡 रेनॉल्ड्स संख्या: **लामिनार** (<2000), **अशांत** (>4000)",
        "density": "📊 घनत्व ρ (kg/m³):",
        "velocity": "💨 वेग v (m/s):",
        "diameter": "📏 व्यास d (m):",
        "viscosity": "💧 श्यानता μ (Pa·s):",
        "calculate_reynolds": "🔬 रेनॉल्ड्स संख्या की गणना करें",
        "laminar": "🟢 **प्रवाह:** लामिनार प्रवाह",
        "transitional": "🟡 **प्रवाह:** ट्रांज़िशनल प्रवाह",
        "turbulent": "🔴 **प्रवाह:** अशांत प्रवाह",
        "error_viscosity": "❌ श्यानता शून्य से अधिक होनी चाहिए!",
        "heat_header": "🔥 ऊष्मा स्थानांतरण कैलकुलेटर",
        "heat_formula": "**सूत्र:** Q = U × A × ΔT",
        "heat_info": "💡 ऊष्मा स्थानांतरण **वाट (W)** में",
        "u_value": "🔧 U (W/m²·K):",
        "area": "📐 क्षेत्रफल A (m²):",
        "delta_t": "🌡️ ΔT (K या °C):",
        "calculate_heat": "🔥 ऊष्मा स्थानांतरण की गणना करें",
        "pressure_header": "📉 दबाव ड्रॉप कैलकुलेटर",
        "pressure_formula": "**सूत्र:** ΔP = f × (L/D) × (ρv²/2)",
        "friction": "घर्षण कारक f",
        "length": "लंबाई L (m)",
        "calc_pressure": "ΔP की गणना करें",
        "temp_header": "🌡️ तापमान परिवर्तक",
        "temp_info": "💡 कोई भी इकाई डालें → सभी 4 पैमाने",
        "input_unit": "इनपुट इकाई:",
        "temp_value": "तापमान मान:",
        "convert_temp": "🔄 तापमान बदलें",
        "converted_values": "✅ परिवर्तित मान:",
        "formulas_header": "📚 रासायनिक इंजीनियरिंग सूत्र",
        "formulas_info": "विषय चुनें → सूत्र देखें",
        "choose_subject": "विषय चुनें:",
        "concepts_header": "💡 अवधारणाएँ",
        "footer_name": "👨‍🔧 ज़ुनैर शहज़ाद",
        "footer_university": "🎓 रासायनिक इंजीनियरिंग | यूईटी लाहौर",
        "footer_credit": "🚀 केम इंज बॉट — आपका रासायनिक इंजीनियरिंग सहायक",
        "footer_copyright": "© 2024 सर्वाधिकार सुरक्षित",
    },
        
    "ar": {
        "app_title": "🧪 كيم إنج بوت",
        "language": "🌐 اللغة",
        "select_feature": "📌 اختر الميزة",
        "home": "🏠 الرئيسية",
        "reynolds": "📊 رقم رينولدز",
        "heat_transfer": "🔥 انتقال الحرارة",
        "pressure_drop": "📉 انخفاض الضغط",
        "ntu": "📐 طريقة NTU",
        "temp_conv": "🌡️ محول درجة الحرارة",
        "formulas": "📚 الصيغ",
        "concepts": "💡 المفاهيم",
        "welcome_title": "🧪 مساعد الهندسة الكيميائية",
        "welcome_subtitle": "رفيقك المدعوم بالذكاء الاصطناعي لحسابات الهندسة الكيميائية",
        "quick_ref": "📈 صيغ مرجعية سريعة",
        "reynolds_header": "📊 حاسبة رقم رينولدز",
        "reynolds_formula": "**الصيغة:** Re = ρvd/μ",
        "reynolds_info": "💡 رقم رينولدز يحدد نوع التدفق",
        "density": "📊 الكثافة ρ (kg/m³):",
        "velocity": "💨 السرعة v (m/s):",
        "diameter": "📏 القطر d (m):",
        "viscosity": "💧 اللزوجة μ (Pa·s):",
        "calculate_reynolds": "🔬 احسب رقم رينولدز",
        "laminar": "🟢 **نوع التدفق:** تدفق طبقي",
        "transitional": "🟡 **نوع التدفق:** تدفق انتقالي",
        "turbulent": "🔴 **نوع التدفق:** تدفق مضطرب",
        "error_viscosity": "❌ يجب أن تكون اللزوجة أكبر من 0!",
        "heat_header": "🔥 حاسبة انتقال الحرارة",
        "heat_formula": "**الصيغة:** Q = U × A × ΔT",
        "heat_info": "💡 معدل انتقال الحرارة بالواط (W)",
        "u_value": "🔧 U (W/m²·K):",
        "area": "📐 المساحة A (m²):",
        "delta_t": "🌡️ ΔT (K أو °C):",
        "calculate_heat": "🔥 احسب انتقال الحرارة",
        "pressure_header": "📉 حاسبة انخفاض الضغط",
        "pressure_formula": "**الصيغة:** ΔP = f × (L/D) × (ρv²/2)",
        "friction": "معامل الاحتكاك f",
        "length": "الطول L (m)",
        "calc_pressure": "احسب ΔP",
        "temp_header": "🌡️ محول درجة الحرارة",
        "temp_info": "💡 أدخل قيمة → احصل على جميع المقاييس الأربعة",
        "input_unit": "وحدة الإدخال:",
        "temp_value": "قيمة درجة الحرارة:",
        "convert_temp": "🔄 حول درجة الحرارة",
        "converted_values": "✅ القيم المحولة:",
        "formulas_header": "📚 صيغ الهندسة الكيميائية",
        "formulas_info": "اختر الموضوع → عرض الصيغ",
        "choose_subject": "اختر الموضوع:",
        "concepts_header": "💡 المفاهيم",
        "footer_name": "👨‍🔧 زنير شهداد",
        "footer_university": "🎓 الهندسة الكيميائية | جامعة لاهور للهندسة",
        "footer_credit": "🚀 كيم إنج بوت — مساعدك في الهندسة الكيميائية",
        "footer_copyright": "© 2024 جميع الحقوق محفوظة",
    },
    "es": {
        "app_title": "🧪 ChemEngBot",
        "language": "🌐 IDIOMA",
        "select_feature": "📌 SELECCIONAR FUNCIÓN",
        "home": "🏠 INICIO",
        "reynolds": "📊 NÚMERO DE REYNOLDS",
        "heat_transfer": "🔥 TRANSFERENCIA DE CALOR",
        "pressure_drop": "📉 CAÍDA DE PRESIÓN",
        "ntu": "📐 MÉTODO NTU",
        "temp_conv": "🌡️ CONVERTIDOR DE TEMPERATURA",
        "formulas": "📚 FÓRMULAS",
        "concepts": "💡 CONCEPTOS",
        "welcome_title": "🧪 Asistente de Ingeniería Química",
        "welcome_subtitle": "Tu compañero impulsado por IA para cálculos de ingeniería química",
        "quick_ref": "📈 Fórmulas de referencia rápida",
        "reynolds_header": "📊 Calculadora del Número de Reynolds",
        "reynolds_formula": "**Fórmula:** Re = ρvd/μ",
        "reynolds_info": "💡 El número de Reynolds determina el tipo de flujo",
        "density": "📊 Densidad ρ (kg/m³):",
        "velocity": "💨 Velocidad v (m/s):",
        "diameter": "📏 Diámetro d (m):",
        "viscosity": "💧 Viscosidad μ (Pa·s):",
        "calculate_reynolds": "🔬 Calcular Número de Reynolds",
        "laminar": "🟢 **Tipo de flujo:** Flujo Laminar",
        "transitional": "🟡 **Tipo de flujo:** Flujo de Transición",
        "turbulent": "🔴 **Tipo de flujo:** Flujo Turbulento",
        "error_viscosity": "❌ ¡La viscosidad debe ser mayor que 0!",
        "heat_header": "🔥 Calculadora de Transferencia de Calor",
        "heat_formula": "**Fórmula:** Q = U × A × ΔT",
        "heat_info": "💡 La tasa de transferencia de calor en **Watts (W)**",
        "u_value": "🔧 U (W/m²·K):",
        "area": "📐 Área A (m²):",
        "delta_t": "🌡️ ΔT (K o °C):",
        "calculate_heat": "🔥 Calcular Transferencia de Calor",
        "pressure_header": "📉 Calculadora de Caída de Presión",
        "pressure_formula": "**Fórmula:** ΔP = f × (L/D) × (ρv²/2)",
        "friction": "Factor de fricción f",
        "length": "Longitud L (m)",
        "calc_pressure": "Calcular ΔP",
        "temp_header": "🌡️ Convertidor de Temperatura",
        "temp_info": "💡 Ingrese un valor → Obtenga las 4 escalas",
        "input_unit": "Unidad de entrada:",
        "temp_value": "Valor de temperatura:",
        "convert_temp": "🔄 Convertir Temperatura",
        "converted_values": "✅ Valores convertidos:",
        "formulas_header": "📚 Fórmulas de Ingeniería Química",
        "formulas_info": "Seleccione tema → Ver fórmulas",
        "choose_subject": "Seleccione tema:",
        "concepts_header": "💡 Conceptos",
        "footer_name": "👨‍🔧 ZUNAIR SHAHZAD",
        "footer_university": "🎓 Ingeniería Química | UET LAHORE",
        "footer_credit": "🚀 ChemEngBot — Tu Asistente de Ingeniería Química",
        "footer_copyright": "© 2024 Todos los derechos reservados",
    },
    "fr": {
        "app_title": "🧪 ChemEngBot",
        "language": "🌐 LANGUE",
        "select_feature": "📌 SÉLECTIONNER UNE FONCTION",
        "home": "🏠 ACCUEIL",
        "reynolds": "📊 NOMBRE DE REYNOLDS",
        "heat_transfer": "🔥 TRANSFERT DE CHALEUR",
        "pressure_drop": "📉 PERTE DE CHARGE",
        "ntu": "📐 MÉTHODE NTU",
        "temp_conv": "🌡️ CONVERTISSEUR DE TEMPÉRATURE",
        "formulas": "📚 FORMULES",
        "concepts": "💡 CONCEPTS",
        "welcome_title": "🧪 Assistant en Génie Chimique",
        "welcome_subtitle": "Votre compagnon alimenté par l'IA pour les calculs de génie chimique",
        "quick_ref": "📈 Formules de référence rapide",
        "reynolds_header": "📊 Calculateur du Nombre de Reynolds",
        "reynolds_formula": "**Formule:** Re = ρvd/μ",
        "reynolds_info": "💡 Le nombre de Reynolds détermine le type d'écoulement",
        "density": "📊 Densité ρ (kg/m³):",
        "velocity": "💨 Vitesse v (m/s):",
        "diameter": "📏 Diamètre d (m):",
        "viscosity": "💧 Viscosité μ (Pa·s):",
        "calculate_reynolds": "🔬 Calculer le Nombre de Reynolds",
        "laminar": "🟢 **Type d'écoulement:** Écoulement Laminaire",
        "transitional": "🟡 **Type d'écoulement:** Écoulement de Transition",
        "turbulent": "🔴 **Type d'écoulement:** Écoulement Turbulent",
        "error_viscosity": "❌ La viscosité doit être supérieure à 0 !",
        "heat_header": "🔥 Calculateur de Transfert de Chaleur",
        "heat_formula": "**Formule:** Q = U × A × ΔT",
        "heat_info": "💡 Le taux de transfert de chaleur en **Watts (W)**",
        "u_value": "🔧 U (W/m²·K):",
        "area": "📐 Surface A (m²):",
        "delta_t": "🌡️ ΔT (K ou °C):",
        "calculate_heat": "🔥 Calculer le Transfert de Chaleur",
        "pressure_header": "📉 Calculateur de Perte de Charge",
        "pressure_formula": "**Formule:** ΔP = f × (L/D) × (ρv²/2)",
        "friction": "Facteur de frottement f",
        "length": "Longueur L (m)",
        "calc_pressure": "Calculer ΔP",
        "temp_header": "🌡️ Convertisseur de Température",
        "temp_info": "💡 Entrez une valeur → Obtenez les 4 échelles",
        "input_unit": "Unité d'entrée :",
        "temp_value": "Valeur de température :",
        "convert_temp": "🔄 Convertir la Température",
        "converted_values": "✅ Valeurs converties :",
        "formulas_header": "📚 Formules de Génie Chimique",
        "formulas_info": "Sélectionnez un sujet → Voir les formules",
        "choose_subject": "Choisissez un sujet :",
        "concepts_header": "💡 Concepts",
        "footer_name": "👨‍🔧 ZUNAIR SHAHZAD",
        "footer_university": "🎓 Génie Chimique | UET LAHORE",
        "footer_credit": "🚀 ChemEngBot — Votre Assistant en Génie Chimique",
        "footer_copyright": "© 2024 Tous droits réservés",
    },
        
    "de": {
        "app_title": "🧪 ChemEngBot",
        "language": "🌐 SPRACHE",
        "select_feature": "📌 FUNKTION AUSWÄHLEN",
        "home": "🏠 STARTSEITE",
        "reynolds": "📊 REYNOLDS-ZAHL",
        "heat_transfer": "🔥 WÄRMEÜBERTRAGUNG",
        "pressure_drop": "📉 DRUCKVERLUST",
        "ntu": "📐 NTU-METHODE",
        "temp_conv": "🌡️ TEMPERATURUMRECHNER",
        "formulas": "📚 FORMELN",
        "concepts": "💡 KONZEPTE",
        "welcome_title": "🧪 Chemieingenieurwesen-Assistent",
        "welcome_subtitle": "Ihr KI-gestützter Begleiter für chemietechnische Berechnungen",
        "quick_ref": "📈 Kurzreferenz-Formeln",
        "reynolds_header": "📊 Reynolds-Zahl Rechner",
        "reynolds_formula": "**Formel:** Re = ρvd/μ",
        "reynolds_info": "💡 Reynolds-Zahl bestimmt Strömungsart: **Laminar** (<2000), **Turbulent** (>4000)",
        "density": "📊 Dichte ρ (kg/m³):",
        "velocity": "💨 Geschwindigkeit v (m/s):",
        "diameter": "📏 Durchmesser d (m):",
        "viscosity": "💧 Viskosität μ (Pa·s):",
        "calculate_reynolds": "🔬 Reynolds-Zahl berechnen",
        "laminar": "🟢 **Strömungsart:** Laminare Strömung",
        "transitional": "🟡 **Strömungsart:** Übergangsströmung",
        "turbulent": "🔴 **Strömungsart:** Turbulente Strömung",
        "error_viscosity": "❌ Viskosität muss größer als 0 sein!",
        "heat_header": "🔥 Wärmeübertragungs-Rechner",
        "heat_formula": "**Formel:** Q = U × A × ΔT",
        "heat_info": "💡 Wärmeübertragungsrate in **Watt (W)**",
        "u_value": "🔧 U (W/m²·K):",
        "area": "📐 Fläche A (m²):",
        "delta_t": "🌡️ ΔT (K oder °C):",
        "calculate_heat": "🔥 Wärmeübertragung berechnen",
        "pressure_header": "📉 Druckverlust-Rechner",
        "pressure_formula": "**Formel:** ΔP = f × (L/D) × (ρv²/2)",
        "friction": "Reibungsfaktor f",
        "length": "Länge L (m)",
        "calc_pressure": "ΔP berechnen",
        "temp_header": "🌡️ Temperaturumrechner",
        "temp_info": "💡 Wert eingeben → Alle 4 Skalen erhalten",
        "input_unit": "Eingabeeinheit:",
        "temp_value": "Temperaturwert:",
        "convert_temp": "🔄 Temperatur umrechnen",
        "converted_values": "✅ Umgerechnete Werte:",
        "formulas_header": "📚 Chemieingenieurwesen-Formeln",
        "formulas_info": "Thema auswählen → Formeln anzeigen",
        "choose_subject": "Thema auswählen:",
        "concepts_header": "💡 Konzepte",
        "footer_name": "👨‍🔧 ZUNAIR SHAHZAD",
        "footer_university": "🎓 Chemieingenieurwesen | UET LAHORE",
        "footer_credit": "🚀 ChemEngBot — Ihr Chemieingenieurwesen-Assistent",
        "footer_copyright": "© 2024 Alle Rechte vorbehalten",
    },
    "zh": {
        "app_title": "🧪 化学工程机器人",
        "language": "🌐 语言",
        "select_feature": "📌 选择功能",
        "home": "🏠 首页",
        "reynolds": "📊 雷诺数",
        "heat_transfer": "🔥 传热",
        "pressure_drop": "📉 压降",
        "ntu": "📐 NTU方法",
        "temp_conv": "🌡️ 温度转换器",
        "formulas": "📚 公式",
        "concepts": "💡 概念",
        "welcome_title": "🧪 化学工程助手机器人",
        "welcome_subtitle": "您的化学工程计算AI助手",
        "quick_ref": "📈 快速参考公式",
        "reynolds_header": "📊 雷诺数计算器",
        "reynolds_formula": "**公式:** Re = ρvd/μ",
        "reynolds_info": "💡 雷诺数确定流动类型: **层流** (<2000), **湍流** (>4000)",
        "density": "📊 密度 ρ (kg/m³):",
        "velocity": "💨 速度 v (m/s):",
        "diameter": "📏 直径 d (m):",
        "viscosity": "💧 粘度 μ (Pa·s):",
        "calculate_reynolds": "🔬 计算雷诺数",
        "laminar": "🟢 **流动类型:** 层流",
        "transitional": "🟡 **流动类型:** 过渡流",
        "turbulent": "🔴 **流动类型:** 湍流",
        "error_viscosity": "❌ 粘度必须大于0！",
        "heat_header": "🔥 传热计算器",
        "heat_formula": "**公式:** Q = U × A × ΔT",
        "heat_info": "💡 传热速率单位为 **瓦特 (W)**",
        "u_value": "🔧 U (W/m²·K):",
        "area": "📐 面积 A (m²):",
        "delta_t": "🌡️ ΔT (K 或 °C):",
        "calculate_heat": "🔥 计算传热",
        "pressure_header": "📉 压降计算器",
        "pressure_formula": "**公式:** ΔP = f × (L/D) × (ρv²/2)",
        "friction": "摩擦系数 f",
        "length": "长度 L (m)",
        "calc_pressure": "计算 ΔP",
        "temp_header": "🌡️ 温度转换器",
        "temp_info": "💡 输入值 → 获得所有4种单位",
        "input_unit": "输入单位:",
        "temp_value": "温度值:",
        "convert_temp": "🔄 转换温度",
        "converted_values": "✅ 转换后的值:",
        "formulas_header": "📚 化学工程公式",
        "formulas_info": "选择主题 → 查看公式",
        "choose_subject": "选择主题:",
        "concepts_header": "💡 概念",
        "footer_name": "👨‍🔧 祖奈尔·沙赫扎德",
        "footer_university": "🎓 化学工程 | 拉合尔工程技术大学",
        "footer_credit": "🚀 化学工程机器人 — 您的化学工程助手",
        "footer_copyright": "© 2024 保留所有权利",
    },
    "ja": {
        "app_title": "🧪 化学工学ボット",
        "language": "🌐 言語",
        "select_feature": "📌 機能を選択",
        "home": "🏠 ホーム",
        "reynolds": "📊 レイノルズ数",
        "heat_transfer": "🔥 熱伝達",
        "pressure_drop": "📉 圧力損失",
        "ntu": "📐 NTU法",
        "temp_conv": "🌡️ 温度変換器",
        "formulas": "📚 公式",
        "concepts": "💡 概念",
        "welcome_title": "🧪 化学工学アシスタントボット",
        "welcome_subtitle": "化学工学計算のためのAI搭載コンパニオン",
        "quick_ref": "📈 クイックリファレンス公式",
        "reynolds_header": "📊 レイノルズ数計算機",
        "reynolds_formula": "**公式:** Re = ρvd/μ",
        "reynolds_info": "💡 レイノルズ数は流れの種類を決定: **層流** (<2000), **乱流** (>4000)",
        "density": "📊 密度 ρ (kg/m³):",
        "velocity": "💨 速度 v (m/s):",
        "diameter": "📏 直径 d (m):",
        "viscosity": "💧 粘度 μ (Pa·s):",
        "calculate_reynolds": "🔬 レイノルズ数を計算",
        "laminar": "🟢 **流れの種類:** 層流",
        "transitional": "🟡 **流れの種類:** 遷移流",
        "turbulent": "🔴 **流れの種類:** 乱流",
        "error_viscosity": "❌ 粘度は0より大きくなければなりません！",
        "heat_header": "🔥 熱伝達計算機",
        "heat_formula": "**公式:** Q = U × A × ΔT",
        "heat_info": "💡 熱伝達率の単位は **ワット (W)**",
        "u_value": "🔧 U (W/m²·K):",
        "area": "📐 面積 A (m²):",
        "delta_t": "🌡️ ΔT (K または °C):",
        "calculate_heat": "🔥 熱伝達を計算",
        "pressure_header": "📉 圧力損失計算機",
        "pressure_formula": "**公式:** ΔP = f × (L/D) × (ρv²/2)",
        "friction": "摩擦係数 f",
        "length": "長さ L (m)",
        "calc_pressure": "ΔPを計算",
        "temp_header": "🌡️ 温度変換器",
        "temp_info": "💡 値を入力 → すべての4つの単位を取得",
        "input_unit": "入力単位:",
        "temp_value": "温度値:",
        "convert_temp": "🔄 温度を変換",
        "converted_values": "✅ 変換された値:",
        "formulas_header": "📚 化学工学公式",
        "formulas_info": "テーマを選択 → 公式を表示",
        "choose_subject": "テーマを選択:",
        "concepts_header": "💡 概念",
        "footer_name": "👨‍🔧 ズナイア・シャーザド",
        "footer_university": "🎓 化学工学 | UETラホール",
        "footer_credit": "🚀 化学工学ボット — あなたの化学工学アシスタント",
        "footer_copyright": "© 2024 全著作権所有",
    },
    "ko": {
        "app_title": "🧪 화학공학 봇",
        "language": "🌐 언어",
        "select_feature": "📌 기능 선택",
        "home": "🏠 홈",
        "reynolds": "📊 레이놀즈 수",
        "heat_transfer": "🔥 열전달",
        "pressure_drop": "📉 압력 강하",
        "ntu": "📐 NTU 방법",
        "temp_conv": "🌡️ 온도 변환기",
        "formulas": "📚 공식",
        "concepts": "💡 개념",
        "welcome_title": "🧪 화학공학 어시스턴트 봇",
        "welcome_subtitle": "화학공학 계산을 위한 AI 기반 동반자",
        "quick_ref": "📈 빠른 참조 공식",
        "reynolds_header": "📊 레이놀즈 수 계산기",
        "reynolds_formula": "**공식:** Re = ρvd/μ",
        "reynolds_info": "💡 레이놀즈 수는 유동 유형 결정: **층류** (<2000), **난류** (>4000)",
        "density": "📊 밀도 ρ (kg/m³):",
        "velocity": "💨 속도 v (m/s):",
        "diameter": "📏 직경 d (m):",
        "viscosity": "💧 점도 μ (Pa·s):",
        "calculate_reynolds": "🔬 레이놀즈 수 계산",
        "laminar": "🟢 **유동 유형:** 층류",
        "transitional": "🟡 **유동 유형:** 천이 유동",
        "turbulent": "🔴 **유동 유형:** 난류",
        "error_viscosity": "❌ 점도는 0보다 커야 합니다!",
        "heat_header": "🔥 열전달 계산기",
        "heat_formula": "**공식:** Q = U × A × ΔT",
        "heat_info": "💡 열전달률 단위는 **와트 (W)**",
        "u_value": "🔧 U (W/m²·K):",
        "area": "📐 면적 A (m²):",
        "delta_t": "🌡️ ΔT (K 또는 °C):",
        "calculate_heat": "🔥 열전달 계산",
        "pressure_header": "📉 압력 강하 계산기",
        "pressure_formula": "**공식:** ΔP = f × (L/D) × (ρv²/2)",
        "friction": "마찰 계수 f",
        "length": "길이 L (m)",
        "calc_pressure": "ΔP 계산",
        "temp_header": "🌡️ 온도 변환기",
        "temp_info": "💡 값 입력 → 모든 4가지 단위 얻기",
        "input_unit": "입력 단위:",
        "temp_value": "온도 값:",
        "convert_temp": "🔄 온도 변환",
        "converted_values": "✅ 변환된 값:",
        "formulas_header": "📚 화학공학 공식",
        "formulas_info": "주제 선택 → 공식 보기",
        "choose_subject": "주제 선택:",
        "concepts_header": "💡 개념",
        "footer_name": "👨‍🔧 주나이르 샤자드",
        "footer_university": "🎓 화학공학 | UET 라호르",
        "footer_credit": "🚀 화학공학 봇 — 당신의 화학공학 어시스턴트",
        "footer_copyright": "© 2024 모든 권리 보유",
    },
    "ru": {
        "app_title": "🧪 ХимИнжБот",
        "language": "🌐 ЯЗЫК",
        "select_feature": "📌 ВЫБРАТЬ ФУНКЦИЮ",
        "home": "🏠 ГЛАВНАЯ",
        "reynolds": "📊 ЧИСЛО РЕЙНОЛЬДСА",
        "heat_transfer": "🔥 ТЕПЛОПЕРЕДАЧА",
        "pressure_drop": "📉 ПЕРЕПАД ДАВЛЕНИЯ",
        "ntu": "📐 МЕТОД NTU",
        "temp_conv": "🌡️ КОНВЕРТЕР ТЕМПЕРАТУРЫ",
        "formulas": "📚 ФОРМУЛЫ",
        "concepts": "💡 КОНЦЕПЦИИ",
        "welcome_title": "🧪 Ассистент по химической технологии",
        "welcome_subtitle": "Ваш ИИ-помощник для расчетов в химической технологии",
        "quick_ref": "📈 Краткие справочные формулы",
        "reynolds_header": "📊 Калькулятор числа Рейнольдса",
        "reynolds_formula": "**Формула:** Re = ρvd/μ",
        "reynolds_info": "💡 Число Рейнольдса определяет тип потока: **ламинарный** (<2000), **турбулентный** (>4000)",
        "density": "📊 Плотность ρ (кг/м³):",
        "velocity": "💨 Скорость v (м/с):",
        "diameter": "📏 Диаметр d (м):",
        "viscosity": "💧 Вязкость μ (Па·с):",
        "calculate_reynolds": "🔬 Вычислить число Рейнольдса",
        "laminar": "🟢 **Тип потока:** Ламинарный поток",
        "transitional": "🟡 **Тип потока:** Переходный поток",
        "turbulent": "🔴 **Тип потока:** Турбулентный поток",
        "error_viscosity": "❌ Вязкость должна быть больше 0!",
        "heat_header": "🔥 Калькулятор теплопередачи",
        "heat_formula": "**Формула:** Q = U × A × ΔT",
        "heat_info": "💡 Скорость теплопередачи в **Ваттах (Вт)**",
        "u_value": "🔧 U (Вт/м²·К):",
        "area": "📐 Площадь A (м²):",
        "delta_t": "🌡️ ΔT (К или °C):",
        "calculate_heat": "🔥 Вычислить теплопередачу",
        "pressure_header": "📉 Калькулятор перепада давления",
        "pressure_formula": "**Формула:** ΔP = f × (L/D) × (ρv²/2)",
        "friction": "Коэффициент трения f",
        "length": "Длина L (м)",
        "calc_pressure": "Вычислить ΔP",
        "temp_header": "🌡️ Конвертер температуры",
        "temp_info": "💡 Введите значение → Получите все 4 шкалы",
        "input_unit": "Единица ввода:",
        "temp_value": "Значение температуры:",
        "convert_temp": "🔄 Конвертировать температуру",
        "converted_values": "✅ Преобразованные значения:",
        "formulas_header": "📚 Формулы химической технологии",
        "formulas_info": "Выберите тему → Просмотр формул",
        "choose_subject": "Выберите тему:",
        "concepts_header": "💡 Концепции",
        "footer_name": "👨‍🔧 ЗУНАИР ШАХЗАД",
        "footer_university": "🎓 Химическая технология | УЕТ ЛАХОР",
        "footer_credit": "🚀 ХимИнжБот — Ваш помощник по химической технологии",
        "footer_copyright": "© 2024 Все права защищены",
    },
    "tr": {
        "app_title": "🧪 Kimya Müh Botu",
        "language": "🌐 DİL",
        "select_feature": "📌 ÖZELLİK SEÇ",
        "home": "🏠 ANA SAYFA",
        "reynolds": "📊 REYNOLDS SAYISI",
        "heat_transfer": "🔥 ISI TRANSFERİ",
        "pressure_drop": "📉 BASINÇ DÜŞÜŞÜ",
        "ntu": "📐 NTU YÖNTEMİ",
        "temp_conv": "🌡️ SICAKLIK DÖNÜŞTÜRÜCÜ",
        "formulas": "📚 FORMÜLLER",
        "concepts": "💡 KAVRAMLAR",
        "welcome_title": "🧪 Kimya Mühendisliği Asistan Botu",
        "welcome_subtitle": "Kimya mühendisliği hesaplamaları için yapay zeka destekli arkadaşınız",
        "quick_ref": "📈 Hızlı Referans Formülleri",
        "reynolds_header": "📊 Reynolds Sayısı Hesaplayıcı",
        "reynolds_formula": "**Formül:** Re = ρvd/μ",
        "reynolds_info": "💡 Reynolds Sayısı akış türünü belirler: **Laminer** (<2000), **Türbülanslı** (>4000)",
        "density": "📊 Yoğunluk ρ (kg/m³):",
        "velocity": "💨 Hız v (m/s):",
        "diameter": "📏 Çap d (m):",
        "viscosity": "💧 Viskozite μ (Pa·s):",
        "calculate_reynolds": "🔬 Reynolds Sayısını Hesapla",
        "laminar": "🟢 **Akış Türü:** Laminer Akış",
        "transitional": "🟡 **Akış Türü:** Geçiş Akışı",
        "turbulent": "🔴 **Akış Türü:** Türbülanslı Akış",
        "error_viscosity": "❌ Viskozite 0'dan büyük olmalıdır!",
        "heat_header": "🔥 Isı Transferi Hesaplayıcı",
        "heat_formula": "**Formül:** Q = U × A × ΔT",
        "heat_info": "💡 Isı transfer hızı **Watt (W)** cinsindendir",
        "u_value": "🔧 U (W/m²·K):",
        "area": "📐 Alan A (m²):",
        "delta_t": "🌡️ ΔT (K veya °C):",
        "calculate_heat": "🔥 Isı Transferini Hesapla",
        "pressure_header": "📉 Basınç Düşüşü Hesaplayıcı",
        "pressure_formula": "**Formül:** ΔP = f × (L/D) × (ρv²/2)",
        "friction": "Sürtünme faktörü f",
        "length": "Uzunluk L (m)",
        "calc_pressure": "ΔP Hesapla",
        "temp_header": "🌡️ Sıcaklık Dönüştürücü",
        "temp_info": "💡 Değer girin → 4 ölçeğin tümünü alın",
        "input_unit": "Giriş Birimi:",
        "temp_value": "Sıcaklık Değeri:",
        "convert_temp": "🔄 Sıcaklığı Dönüştür",
        "converted_values": "✅ Dönüştürülen Değerler:",
        "formulas_header": "📚 Kimya Mühendisliği Formülleri",
        "formulas_info": "Konu seçin → Formülleri görüntüleyin",
        "choose_subject": "Konu Seçin:",
        "concepts_header": "💡 Kavramlar",
        "footer_name": "👨‍🔧 ZUNAIR SHAHZAD",
        "footer_university": "🎓 Kimya Mühendisliği | UET LAHORE",
        "footer_credit": "🚀 Kimya Müh Botu — Kimya Mühendisliği Asistanınız",
        "footer_copyright": "© 2024 Tüm Hakları Saklıdır",
    }
}

# ==========================================
# GET TRANSLATION FUNCTION
# ==========================================
def _(key):
    lang = st.session_state.get("language", "en")
    return translations.get(lang, translations["en"]).get(key, key)

# ==========================================
# INITIALIZE
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
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a3c6e 0%, #0e2a4f 100%);
    }
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        font-weight: bold;
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
    }
    .footer-university {
        font-size: 1.2rem !important;
        color: #ccc !important;
    }
    .footer-credit {
        font-size: 1rem !important;
        color: #aaa !important;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# SIDEBAR
# ==========================================
# ==========================================
# SIDEBAR
# ==========================================
with st.sidebar:
    col1, col2 = st.columns([2, 1])
    with col1:
        st.image("https://img.icons8.com/color/96/chemical-plant.png", width=70)
        st.markdown("# 🧪 ChemEngBot")
    with col2:
        # Load image
        import base64
        from PIL import Image
        import io
        
        # Open image
        img = Image.open("images/zunair.jpeg")
        
        # Convert to base64
        buffered = io.BytesIO()
        img.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        
        # Display circle image
        st.markdown(f"""
        <div style="display: flex; justify-content: center; align-items: center;">
            <img src="data:image/jpeg;base64,{img_str}" style="width: 110px; height: 110px; border-radius: 50%; object-fit: cover; border: 4px solid #4CAF50; box-shadow: 0 4px 10px rgba(0,0,0,0.2);">
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # ========== LANGUAGE SELECTOR ==========
    st.markdown(f"### {_('language')}")
    
    current_lang = st.session_state.get("language", "en")
    lang_options = [f"{info['flag']} {name}" for name, info in languages.items()]
    
    # Find current display
    current_display = "🇬🇧 English"
    for lang_name, info in languages.items():
        if info["code"] == current_lang:
            current_display = f"{info['flag']} {lang_name}"
            break
    
    selected_lang = st.selectbox("", lang_options, index=lang_options.index(current_display) if current_display in lang_options else 0, label_visibility="collapsed")
    
    for lang_name, info in languages.items():
        if f"{info['flag']} {lang_name}" == selected_lang:
            st.session_state.language = info["code"]
    
    st.markdown("---")
    
    # ========== NAVIGATION ==========
    feature = st.radio(
        _("select_feature"),
        [_("home"), _("reynolds"), _("heat_transfer"), _("pressure_drop"), _("ntu"), _("temp_conv"), _("formulas"), _("concepts")],
        index=0
    )
    
    st.markdown("---")
    st.markdown(f"""
    <div style="text-align: center;">
        <p style="font-size: 1.5rem; font-weight: bold; color: #4CAF50;">👨‍🔧 ZUNAIR SHAHZAD</p>
        <p style="font-size: 1rem; color: #ccc;">🎓 Chemical Engineering</p>
        <p style="font-size: 1.1rem; color: #4CAF50; font-weight: bold;">UET LAHORE</p>
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# MAIN CONTENT (Simplified)
# ==========================================

if feature == _("home"):
    st.markdown(f'<p class="main-header">{_("welcome_title")}</p>', unsafe_allow_html=True)
    st.markdown(f'<p class="sub-header">{_("welcome_subtitle")}</p>', unsafe_allow_html=True)
    st.markdown("---")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown(f"""
        ### 👋 Welcome to ChemEngBot!
        
        Your personal **Chemical Engineering Assistant** that helps you with:
        
        | ✅ | Feature | Description |
        |---|---|---|
        | 📊 | **Reynolds Number** | Calculate flow characteristics |
        | 🔥 | **Heat Transfer** | Q = UAΔT |
        | 📉 | **Pressure Drop** | Pressure losses in pipes |
        | 📐 | **NTU Method** | Heat exchanger effectiveness |
        
        **Select any feature from the sidebar!**
        """)
    with col2:
        st.image("https://img.icons8.com/color/200/chemical-plant.png")
    
    st.markdown("---")
    st.subheader(_("quick_ref"))
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Reynolds Number", "Re = ρvd/μ")
    c2.metric("Heat Transfer", "Q = UAΔT")
    c3.metric("Pressure Drop", "ΔP = f(L/D)(ρv²/2)")
    c4.metric("NTU", "NTU = UA/C_min")

elif feature == _("reynolds"):
    st.header(_("reynolds_header"))
    st.markdown(_("reynolds_formula"))
    st.info(_("reynolds_info"))
    
    c1, c2 = st.columns(2)
    with c1:
        rho = st.number_input(_("density"), value=1000.0, step=10.0)
        v = st.number_input(_("velocity"), value=1.0, step=0.1)
    with c2:
        d = st.number_input(_("diameter"), value=0.05, step=0.01)
        mu = st.number_input(_("viscosity"), value=0.001, step=0.0001, format="%.4f")
    
    if st.button(_("calculate_reynolds"), type="primary"):
        if mu > 0:
            Re = (rho * v * d) / mu
            st.success(f"### ✅ Reynolds Number = {Re:,.2f}")
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
    
    c1, c2 = st.columns(2)
    with c1:
        U = st.number_input(_("u_value"), value=500.0)
        A = st.number_input(_("area"), value=10.0)
    with c2:
        dT = st.number_input(_("delta_t"), value=50.0)
    
    if st.button(_("calculate_heat"), type="primary"):
        Q = U * A * dT
        st.success(f"### ✅ Q = {Q:,.2f} W")
        st.info(f"#### = {Q/1000:.2f} kW")

elif feature == _("pressure_drop"):
    st.header(_("pressure_header"))
    st.markdown(_("pressure_formula"))
    
    c1, c2 = st.columns(2)
    with c1:
        f = st.number_input(_("friction"), value=0.02)
        L = st.number_input(_("length"), value=100.0)
    with c2:
        d = st.number_input("Diameter d (m)", value=0.1)
        rho = st.number_input("Density ρ", value=1000.0)
        v = st.number_input("Velocity v (m/s)", value=2.0)
    
    if st.button(_("calc_pressure")):
        dp = f * (L / d) * (rho * v**2 / 2)
        st.success(f"### ✅ ΔP = {dp:.0f} Pa")

elif feature == _("temp_conv"):
    st.header(_("temp_header"))
    st.info(_("temp_info"))
    
    unit = st.selectbox(_("input_unit"), ["Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)", "Rankine (°R)"])
    val = st.number_input(_("temp_value"), value=25.0)
    
    if st.button(_("convert_temp"), type="primary"):
        if "Celsius" in unit:
            c = val
        elif "Fahrenheit" in unit:
            c = (val - 32) * 5/9
        elif "Kelvin" in unit:
            c = val - 273.15
        else:
            c = (val - 491.67) * 5/9
        
        st.success(_("converted_values"))
        a, b, cc, d = st.columns(4)
        a.metric("°C", f"{c:.2f}")
        b.metric("°F", f"{c*9/5+32:.2f}")
        cc.metric("K", f"{c+273.15:.2f}")
        d.metric("°R", f"{(c*9/5+32)+459.67:.2f}")

elif feature == _("ntu"):
    st.header(_("ntu"))
    st.markdown("**NTU = UA/C_min**")
    U = st.number_input("U", value=500.0)
    A = st.number_input("A", value=10.0)
    Cmin = st.number_input("C_min", value=1000.0)
    if st.button("Calculate NTU"):
        st.success(f"NTU = {(U*A)/Cmin:.2f}")

elif feature == _("formulas"):
    st.header(_("formulas_header"))
    st.info(_("formulas_info"))
    try:
        from formulas_data import formulas_data
        subject = st.selectbox(_("choose_subject"), list(formulas_data.keys()))
        if subject:
            for f in formulas_data[subject]:
                with st.expander(f"📐 {f['name']}"):
                    st.markdown(f"**Desc:** {f['desc']}")
                    st.markdown(f"**Params:** {f['params']}")
                    st.markdown(f"**Eq:** `{f['eq']}`")
    except:
        st.warning("Formulas data not found")

elif feature == _("concepts"):
    st.header(_("concepts_header"))
    st.markdown("""
    - **Reynolds Number**: Flow type (Laminar/Turbulent)
    - **Heat Transfer**: Q = UAΔT
    - **Pressure Drop**: Energy loss in pipes
    - **NTU**: Heat exchanger performance
    """)

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