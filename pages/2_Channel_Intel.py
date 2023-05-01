#!/usr/bin/env python3

#import streamlit
import streamlit as st


#content function
def content():
    st.markdown("""

See you soon :)

    """)


if __name__ == "__main__":
    st.title("Coming soon!")
    st.divider()
    # call the content function to display the content of the page
    content()