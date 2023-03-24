

import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np
import streamlit_authenticator as stauth

import database as db

import streamlit as st
from streamlit_login_auth_ui.widgets import __login__

__login__obj = __login__(auth_token = "pk_prod_WK9CBN31SQMZH8HPMD6KD8H5DFD2",
                    company_name = "grpx",
                    width = 200, height = 250,
                    logout_button_name = 'Logout', hide_menu_bool = False,
                    hide_footer_bool = False,
                    lottie_url = 'https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json')

LOGGED_IN= __login__obj.build_login_ui()
username= __login__obj.get_username()

if LOGGED_IN == True:

   # st.markdown("Your Streamlit Application Begins here!")
    # st.markdown(st.session_state)

    st.set_option('deprecation.showfileUploaderEncoding', False)
    def import_and_predict(image_data, model):
        image = ImageOps.fit(image_data, (100,100),Image.ANTIALIAS)
        image = image.convert('RGB')
        image = np.asarray(image)
        st.image(image, channels='RGB')
        image = (image.astype(np.float32) / 255.0)
        img_reshape = image[np.newaxis,...]
        prediction = model.predict(img_reshape)
        return prediction

    model = tf.keras.models.load_model('my_model2.h5')
    st.write("""
         # ***Glaucoma detector***
         """
         )
    st.write("This is a simple image classification web app to predict glaucoma through fundus image of eye")
    file = st.file_uploader("Please upload an image(jpg) file", type=["jpg"])

    if file is None:
        st.text("You haven't uploaded a jpg image file")
      
    else:
        imageI = Image.open(file)
        prediction = import_and_predict(imageI, model)
        pred = prediction[0][0]
        if(pred > 0.5):
            st.write(
                 """
                 # **Prediction:** You eye is Healthy. Great!!
                 """)
        elif(pred < 0.3):
            st.write("""
                 ## **Prediction:** You are severely affected by Glaucoma."""
                 )

        

        else:
             st.write("""
                 ## **Prediction:** You are affected by Glaucoma. Please consult an ophthalmologist as soon as possible.
                 """)
        
