import streamlit as st
import qrcode
from io import BytesIO
import uuid
from PIL import Image
from gtts import gTTS
import base64

def generate_qr(data):
    qr=qrcode.QRCode(version=1,box_size=10,border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img=qr.make_image(fill_color="black", back_color="white")
    return img

st.set_page_config(page_title="Metro Ticket Booking",page_icon=" ")
st.title("Metro Ticket Booking with QRcode + Auto Voice")
stations=["Ameerpet","Miyapur","LB Nagar","KPHB","JNTU"]
name=st.text_input("Passenger Name: ")
source=st.selectbox("Source station",stations)
destination=st.selectbox("Destination station",stations)
no_tickets=st.number_input("Number of Tickets",min_value=1,value=1)
price_per_ticket=30
total_amount=no_tickets*price_per_ticket
st.info(f" Total Amount : ${total_amount}")
st.write("Do you need a cab?")
if st.button("No"):

    if name.strip()=="":
        st.error("Please Enter Passenger name.")
    elif source == destination:
        st.error("Source and Destination cannot be same! Please select another destination.")
    else:
        booking_id=str(uuid.uuid4())[:8]

        qr_data =(
             f"BookingUD: {booking_id}\n"
             f"Name: {name}\nFrom: {source}\nTo: {destination}\nTickets: {no_tickets}"
            )
        qr_img = generate_qr(qr_data)

        buf=BytesIO()
        qr_img.save(buf, format="PNG")
        qr_bytes=buf.getvalue()

        st.success("Ticket Booked Succesfully")
        st.write(f"**Booking ID:** {booking_id}")
        st.write(f"**Passenger:** {name}")
        st.write(f"**From:** {source}")
        st.write(f"**To:** {destination}")
        st.write(f"**Tickets:** {no_tickets}")
        st.write(f"**Amount Paid:** ${total_amount}")
        st.image(qr_bytes, width=250)
drop=st.text_input("Enter drop location")

        
if st.button("Yes"):
    if drop.strip()=="":
        st.error("Please Enter Drop Location.")
    if name.strip()=="":
        st.error("Please Enter Passenger name.")
    elif source == destination:
        st.error("Source and Destination cannot be same! Please select another destination.")
    else:
        booking_id=str(uuid.uuid4())[:8]
        qr_data =(
        f"BookingID: {booking_id}\n"
        f"Name: {name}\nFrom: {source}\nTo: {destination}\nTickets: {no_tickets}"
        f"Cab Details:\n"
        f"From: {destination}\n Drop: {drop}"
        )
        qr_img = generate_qr(qr_data)
        buf=BytesIO()
        qr_img.save(buf, format="PNG")
        qr_bytes=buf.getvalue()

        st.success("Ticket Booked Succesfully")
        st.write(f"**Booking ID:** {booking_id}")
        st.write(f"**Passenger:** {name}")
        st.write(f"**From:** {source}")
        st.write(f"**To:** {destination}")
        st.write(f"**Tickets:** {no_tickets}")
        st.write(f"**Cab Source:** {destination}")
        st.write(f"**Cab Drop point:** {drop}")
        st.write(f"**Amount Paid:** ${total_amount}")
        st.image(qr_bytes, width=250)
    

    





