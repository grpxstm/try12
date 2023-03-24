

import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np
import streamlit_authenticator as stauth

import database as db

"""users = db.fetch_all_users()
usernames = [user["key"]for user in users]
names = [user["name"]for user in users]
hashed_passwords = [user["password"]for user in users]

#test
credentials = {
        "usernames":{
            "rishwin":{
                "name":"rishwin r kanth",
                "password":"$2b$12$uQkEYgDG4Wa46R8K5smYA.iWnMg.Hedx2WSM7UFqYYEnLSx3R57cW"
                },
            
            }
        }

#logout 

#sidebar
#sign up
st.sidebar.header("Sign up if you do not have an account")
if st.sidebar.button('Signup',['Sign up']):
    email = st.sidebar.text_input('Please enter your email address')
    password = st.sidebar.text_input('please enter your password')
    handle = st.sidebar.text_input('please enter your username',value ='default')
    submit = st.sidebar.button('submit')
    if submit:
        user = stauth.create_user_with_email_and_password(email,password)
        st.success('Your account is succesfully created')
        st.ballons()
    #upload_to_database





    

#bg

def add_bg_from_url():
    st.markdown(
         f
         <style>

         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2019/04/24/11/27/flowers-4151900_960_720.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         
         unsafe_allow_html=True
     )

add_bg_from_url() 






authenticator = stauth.Authenticate(credentials, "app_home", "authw", cookie_expiry_days=0)


name, authentication_status, username = authenticator.login("Login", "main")
if authentication_status == False:
    st.error("username/password is incorrect TRY AGAIN")
    #forgetpassword

    
if authentication_status == None:
    st.warning("please enter your username and password")
if authentication_status == True:
    st.sidebar.header("welcome",name)"""
#forgetpassword

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

   st.markdown("Your Streamlit Application Begins here!")
   st.markdown(st.session_state)

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
    authenticator.logout('Logout', 'main')
