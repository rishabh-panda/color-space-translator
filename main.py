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

            summation = R+G+B
            r = R/summation
            g = G/summation
            b = B/summation

            if r == g == b:
                h = 0

            #numerator = 0.5*((r-g)+(r-b))
            #denominator = math.sqrt((math.pow((r-g),2))+((r-b)*(g-b)))

            elif b <= g:
                # h ranges from [0, pi]
                h = math.acos((0.5*((r-g)+(r-b)))/(math.sqrt((math.pow((r-g),2))+((r-b)*(g-b)))))

            else:
                # h ranges from [pi, 2pi]
                h = (2*math.pi)-math.acos((0.5*((r-g)+(r-b)))/(math.sqrt((math.pow((r-g),2))+((r-b)*(g-b)))))

            # s ranges from [0, 1]
            s = 1-(3*min(r,g,b))

            # converting normalized h, s, i values to their standard ranges for convenience
            # H - [0,360], S - [0,100], I - [0, 255]

            H = h*(180/math.pi)
            S = 100*s
            I = (R+G+B)/3

            H_final = "{:.3f}".format(H)
            S_final = "{:.3f}".format(S)
            I_final = "{:.3f}".format(I)

            st.success(f"Hue (H) = {H_final}")
            st.success(f"Saturation (S) = {S_final}")
            st.success(f"Intensity (I) = {I_final}")

    else:
        st.subheader("HSI to RGB Conversion [ Hue range (0 - 360) degrees ]")

        H = st.number_input("Enter H (Hue in degrees): ", step=0.1)
        S = st.number_input("Enter S (Saturation percentage): ", step=0.1)
        I = st.number_input("Enter I (Intensity percentage): ", step=0.1)

        if st.button("Convert HSI parameters to RGB"):

            h = H*(math.pi/180)
            s = S/100
            i = I/255

            x = i*(1-s)
            y = i*((s*math.cos(h))/(math.cos((math.pi/3)-h)))
            z = 3*i-(x+y)

            if h < (2*math.pi)/3:
                b = x
                r = y
                g = z

            if ((2*math.pi)/3) <= h < ((4*math.pi)/3):
                h = h - (2*math.pi)/3
                r = x
                g = y
                b = z

            if ((4*math.pi)/3) <= h < 2*math.pi:
                h = h - (4*math.pi)/3
                g = x
                b = y
                r = z

            #The result r, g and b are normalized values, which are in the ranges of [0,1],
            #therefore, they should be multiplied by 255 for displaying.

            R = "{:.3f}".format(r*255)
            G = "{:.3f}".format(g*255)
            B = "{:.3f}".format(b*255)

            st.success(f"Red (R) = {R}")
            st.success(f"Green (G) = {G}")
            st.success(f"Blue (B) = {B}")

if __name__ == "__main__":
    main()
