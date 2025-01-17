import streamlit as st

from streamlit_option_menu import option_menu

import about, account, home, trending, your_posts

st.set_page_config(page_title="Welcome to Technical Granth", layout="wide")

class MultiApp :
    def __init__(self) :
        self.apps = {
            "Home" : home,
            "Trending" : trending,
            "Your Posts" : your_posts,
            "Account" : account,
            "About" : about
        }

        self.app = st.sidebar.radio("Navigation", list(self.apps.keys()))

    def run(self) :
        with st.sidebar :
            app = option_menu(
                menu_title='Technical Granth', 
                options= ['Home', 'Trending', 'Your Posts', 'Account', 'About'],
                icons= ['🏠', '📈', '📝', '👤', '❓'],
                menu_icon='📚',
                default_index=1,
                styles={"container" : {"padding": "5!important", "back icon": {"color" : "white", 
                    "font-size": "20px", "text-shadow": "0px 1px 0px rgba(0, 0, 0, 0.5)"},}})

        if app== 'Home' :
            home.app()
        if app== 'Trending' :
            trending.app()
        if app== 'Your Posts' :
            your_posts.app()
        if app== 'Account' :
            account.app()
        if app== 'About' :
            about.app()
        
    #run()  # Run the app