import streamlit as st
import requests

st.title("nombre de los astronautas")

people = requests.get("http://api.open-notify.org/astros.json")
json_astronautas = people.json()
st.table(json_astronautas["people"])
