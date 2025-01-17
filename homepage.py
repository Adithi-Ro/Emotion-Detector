import streamlit as st

st.title("EMOTION DETECTION")
st.subheader("FIND OUT WHAT EVERYONE IS TRULY FEELING")

tab1, tab2, tab3 = st.tabs(["Home Page", "Uploader", "About Me"])

with tab1:
    col1, col2= st.columns(2)

    with col1:
        st.header('HAPPY')
        st.text("A feeling of joy, delight or glee. It is often accompanied with the feeling of warmth, satsifaction and fullness.")
        #sad
        st.image("https://media.istockphoto.com/id/184964831/photo/stressed-man-rubs-neck.jpg?s=612x612&w=0&k=20&c=JjQB5-aNIjqrapnvEc8qUNLgjnnBzpFqgFvt0jHQHKA=",width = 250)
        st.header("FEAR")
        st.text("An unpleasent emotion that ocurrs when one is worried about something dangerous, painful or bad.")
        #anger
        st.image('https://t3.ftcdn.net/jpg/01/97/66/74/360_F_197667405_ZWvFfmYWXANFZjUBumNvwcp9dr8Vcfb1.jpg')
        st.header("SURPRISED")
        st.text('this is how happy/ scared surprised people feel')
        #disgusted
        st.image("https://img.freepik.com/premium-photo/disgusted-man-gesturing-stop-avoiding-something-white-background_116547-20121.jpg")
        st.header("NEUTRAL")
        st.test("emotion less face)
    with col2: 
        #happy
        st.image("https://t3.ftcdn.net/jpg/06/70/88/30/360_F_670883093_z8u6KtjZ38hAPSGTudNzz5LBB3o75aDD.jpg", width = 450)
        st.header("SAD")
        st.text("The showing of sorrow, unhappiness, grief. It is a type of depression characterized by a reacurent seasonal pattern.")
        #fear
        st.image("https://t4.ftcdn.net/jpg/04/33/83/81/360_F_433838132_9U7VyzfhCXDKAFU4Z0wbBhiCWSeNnsQm.jpg")
        st.header("ANGER")
        st.text("A feeling of hostility, agitiation or frustration directed to someone or something that one belives have done them wrong.")    
        # surprised
        st.image("https://img.freepik.com/free-photo/bugged-eyed-terrifc-girlfriend-with-curly-hair-freckled-skin-opens-mouth-widely_273609-18496.jpg?semt=ais_hybrid")
        st.header("DISGUSTED")
        st.text("disgusted people feel like this")
        #netural
        st.image("https://t3.ftcdn.net/jpg/03/42/85/16/360_F_342851651_BV9SYWnoTPSu3kq6e82zG7H8eEt20wd1.jpg")


with tab2:
    uploaded_files = st.file_uploader(
    "Choose a CSV file", accept_multiple_files=True
)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)

    st.header("YOU ARE FEELING")

with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
    
