import streamlit as st
import sqlite3
import pandas as pd

conn=sqlite3.connect("register db",check_same_thread=False)
cursor=conn.cursor()
conn.execute("""
    CREATE TABLE IF NOT EXISTS users
(name TEXT,email TEXT,pwd TEXT)
""" )
conn.commit()
menu=["REGISTER","LIST","LOGIN"]
choice=st.sidebar.selectbox("OPTIONS",menu)
if choice=="REGISTER":
    name=st.text_input("Name: ")
    email=st.text_input("Email: ")
    pwd=st.text_input("Password: ",type="password")
    if st.button("SUBMIT"):
        cursor.execute("INSERT INTO users(name,email,pwd)VALUES(?,?,?)""",(name,email,pwd))
        conn.commit()
        st.success("Sign-up Succesfull!")
if choice=="LIST":
    data=cursor.execute("SELECT * FROM users")
    st.dataframe(data)
if choice=="LOGIN":
    name=st.text_input("Name: ")
    email=st.text_input("Email: ")
    pwd=st.text_input("Password: ",type="password")
    if st.button("LOG IN"):
        cursor.execute(""" SELECT *  FROM users WHERE name=? AND pwd=?""",(name,pwd))
        result=cursor.fetchone()
        if result:
            st.success("Valid user")
            st.balloons()
        else:
            st.error("invalid user")
        
        
    
            
    
        
