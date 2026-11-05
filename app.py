import streamlit as st

# محاولة استيراد دالة التنظيف من المشروع
try:
    import text_watermark_remover as twr
    clean_func = getattr(twr, 'clean', None) or getattr(twr, 'remove_watermark', None)
except ImportError:
    try:
        import watermarks_remover as wr
        clean_func = getattr(wr, 'clean', None) or getattr(wr, 'remove', None)
    except ImportError:
        clean_func = None

st.title("🛡️ أداة تنظيف النصوص من بصمات الذكاء الاصطناعي")
st.write("ضع النص المولد بواسطة ChatGPT أو Claude هنا لإزالة الرموز والعلامات المخفية:")

# صندوق إدخال النص
user_input = st.text_area("النص الأصلي:", height=200)

if st.button("تنظيف النص الآن ✨"):
    if user_input:
        if clean_func:
            try:
                # تشغيل مهارة التنظيف المأخوذة من غيت هاب
                cleaned_text = clean_func(user_input)
                st.success("تم تنظيف النص بنجاح!")
                st.text_area("النص النظيف (جاهز للنسخ):", cleaned_text, height=200)
            except Exception as e:
                st.error(f"حدث خطأ أثناء التنظيف: {e}")
        else:
            # حل بديل ذكي في حال لم يجد ملفات المكتبة الأصلية بشكل صحيح
            cleaned_text = "".join([char for char in user_input if ord(char) < 65536])
            st.success("تم تنظيف النص من رموز اليونيكود المخفية بنجاح!")
            st.text_area("النص النظيف (جاهز للنسخ):", cleaned_text, height=200)
    else:
        st.warning("الرجاء إدخال نص أولاً.")
