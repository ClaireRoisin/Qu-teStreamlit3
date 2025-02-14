import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu
# Nos données utilisateurs doivent respecter ce format

lesDonneesDesComptes = {'usernames': {'utilisateur': {'name': 'utilisateur',
   'password': 'utilisateurMDP',
   'email': 'utilisateur@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'utilisateur'},
  'root': {'name': 'root',
   'password': 'rootMDP',
   'email': 'admin@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'administrateur'}}}

authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    30, # Le nombre de jours avant que le cookie expire 
)

authenticator.login()

if st.session_state["authentication_status"]:

    with st.sidebar :   
        # Le bouton de déconnexion
       authenticator.logout("Déconnexion")
    
       st.write('Bienvenue root')
       selection = option_menu(
            menu_title=None,
            options = ["Accueil", "Des photos de chats"])
 
    # On indique au programme quoi faire en fonction du choix
    if selection == "Accueil":
        st.title("Bienvenue sur ma page !")
        st.image("bravo.jpg")
    elif selection == "Des photos de chats":
        st.title("Ils sont pas trop choupinous ???")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("chat1.jpg")
        with col2:
            st.image("chat2.jpg")
        with col3:
            st.image("chat3.jpg")


    elif st.session_state["authentication_status"] is False:
        st.error("L'username ou le password est/sont incorrect")
    elif st.session_state["authentication_status"] is None:
       st.warning('Les champs username et mot de passe doivent être remplie')



