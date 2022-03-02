import streamlit as st
from PIL import Image
import math

def main():
    st.title("Color Image Processing")
    img = Image.open("colorimage.jpg")
    st.image(img)

    menu = ["RGB to HSI", "HSI to RGB"]
    choice = st.sidebar.selectbox("Select Converter", menu)

    if choice == "RGB to HSI":
        st.subheader("RGB to HSI Conversion [ RGB input range (0 - 255) ]")

        R = st.number_input("Enter R (Red): ", step=1)
        G = st.number_input("Enter G (Green): ", step=1)
        B = st.number_input("Enter B (Blue): ", step=1)

        if st.button("Convert RGB parameters to HSI"):

            numerator = 0.5*((R-G)+(R-B))
            denominator = math.sqrt((math.pow((R-G),2))+((R-B)*(G-B)))

            #theta in terms of radians
            theta = math.acos(numerator/denominator)

            #defining Hue (H)
            if B <= G:
                H = theta

            if B > G:
                H = (360-theta)

            #defining Saturation (S)
            S = 1-(3*(min(R,G,B))/(R+G+B))

            #defining Intensity (I)
            I = (R+G+B)/3

            H = "{:.3f}".format(H)
            S = "{:.3f}".format(S)
            I = "{:.3f}".format(I)

            st.success(f"Hue (H) = {H}")
            st.success(f"Saturation (S) = {S}")
            st.success(f"Intensity (I) = {I}")

    else:
        st.subheader("HSI to RGB Conversion [ Hue range (0 - 360) degrees ]")

        H = st.number_input("Enter H (Hue in degrees): ", step=0.1)
        S = st.number_input("Enter S (Saturation percentage): ", step=0.1)
        I = st.number_input("Enter I (Intensity percentage): ", step=0.1)

        if st.button("Convert HSI parameters to RGB"):

            #RG sector (0 <= H < 120 degrees)
            if (0 <= H) and (H < 120):
                #degrees-radian transition
                H = H*(math.pi/180)

                B = I*(1-S)
                R = I*(1+(S*math.cos(H)/math.cos((math.pi/3)-H)))
                G = 3*I-(R+B)

            #GB sector (120 < H < 240 degrees)
            if (120 <= H) and (H < 240):
                # degrees-radian transition
                H = H*(math.pi/180)
                H = H-(120*(math.pi/180))

                R = I*(1-S)
                G = I*(1+(S*math.cos(H)/math.cos((math.pi/3)-H)))
                B = 3*I-(R+G)

            #BR sector (240 < H < 360 degrees)
            if (240 <= H) and (H <= 360):
                # degrees-radian transition
                H = H*(math.pi/180)
                H = H-(240*(math.pi/180))

                G = I*(1-S)
                B = I*(1+(S*math.cos(H)/math.cos((math.pi/3)-H)))
                R = 3*I-(G+B)

            #linear normalization of RGB values to [0, 255] range
            new_max = 255
            new_min = 0
            R_norm = ((R - min(R, G, B))*((new_max-new_min)/(max(R, G, B)-min(R, G, B))))+new_min
            G_norm = ((G - min(R, G, B))*((new_max-new_min)/(max(R, G, B)-min(R, G, B))))+new_min
            B_norm = ((B - min(R, G, B))*((new_max-new_min)/(max(R, G, B)-min(R, G, B))))+new_min

            R = "{:.3f}".format(R_norm)
            G = "{:.3f}".format(G_norm)
            B = "{:.3f}".format(B_norm)

            st.success(f"Red (R) = {R}")
            st.success(f"Green (G) = {G}")
            st.success(f"Blue (B) = {B}")

if __name__ == "__main__":
    main()
