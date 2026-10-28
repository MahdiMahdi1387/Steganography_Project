from stegano import lsb
import streamlit as st
from PIL import Image

st.set_page_config(page_title='Stegano Project')
option = st.sidebar.selectbox('Select your option: ',
                              ('Hide Text', 'Reveal Text'))

if option == 'Hide Text':
    host_pic = st.file_uploader('Select your image', type=['png', 'jpg'])
    secret_text = st.text_area('Enter your text to hide')

    if st.button('HIDE'):
        if host_pic and secret_text:

            temp_img = Image.open(host_pic)
            final_img = lsb.hide(temp_img, secret_text)
            final_img.save('./final_image_pars.png')
            st.success('Data hid in your picture.')

elif option == 'Reveal Text':
    final_secreted_image = st.file_uploader('Select image for reveal',
                                            type=['png'])

    if st.button('REVEAL'):
        if final_secreted_image:
            temp_image = Image.open(final_secreted_image)

            secret_txt_reveal = lsb.reveal(temp_image)

            if secret_txt_reveal is not None:
                st.write(secret_txt_reveal)
                st.success('Data revealed successfully.')
            else:
                st.write('text can not excract')
