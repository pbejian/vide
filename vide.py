import streamlit as st
import codecs
import this

S = codecs.decode(this.s, 'rot13')
T = S.split("\n")

st.write(f"""
### {T[0]}
""")

T = S.split("\n")
for L in T[1:]:
    st.write(L)