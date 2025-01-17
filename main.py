import streamlit as st

from streamlit_option_menu import option_menu

import about, account, home, trending, your_posts

st.set_page_config(page_title="Welcome to Technical Granth")

class MultiApp :
    def __init__(self) :
        self.apps = []
        def add_app(self, title, function) :
            self.apps.append({
                "title" : title,
                "function" : function
            })  
    def run(self) :
        with st.sidebar: 
            app = option_menu(
                menu_title='Technical Granth', 
                options= ['Home', 'Trending', 'Your Posts', 'Account', 'About'],
                icons= ['🏠', '📈', '📝', '👤', '❓'],
                menu_icon='📚',
                default_index=1,
                styles={"container" : {"padding": "5!important", "back icon": {"color" : "white", 
                    "font-size": "20px","nav-link": {"color": "white", "font-size": "20px"}}}}) 
              
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
            