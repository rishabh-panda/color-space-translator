# Color Image Processing
---

## **Color Models, Color Space**
- A color model is a specification of a coordinate system within which each color is represented by a single point.
- Hardware-oriented color models; e.g., color monitors and printers, ```RGB```, ```CMY``` (cyan, magenta, yellow), ```CMYK``` (+black)
- Application-oriented color model; ```HSI``` (hue, saturation, intensity)
---
## RGB Color Model
- Each color appears in its primary spectral components of R, G, and B
- Based on a Cartesian coordinate system (cube)
---
## HSI Color Model
- ```RGB``` and similar others are not practical for human interpretation.
- **Hue:** a color attribute that describes a pure color.
- **Saturation:** a measure of the degree to which a pure color is diluted by white light.
- The ```HSI``` space is represented by a vertical intensity axis, the length (saturation) of a vector from the axis to a color point, and the angle (hue) this vector makes with the red axis.
- The power of ```HSI``` color model is to allow independent control over hue,
saturation, and intensity.
---
### 
![image](https://user-images.githubusercontent.com/80598737/156314307-2ecce580-10fc-45f3-9290-f60895c0f8d9.png)

## Converting colors from RGB to HSI
![01 Theta](https://user-images.githubusercontent.com/80598737/156316315-2e7cd3fc-6153-44a1-a4d6-476162ba8e33.png)
![02 Hue](https://user-images.githubusercontent.com/80598737/156316352-db496a10-babb-482b-ab7e-01f16cfc6912.png)
![03 Saturation](https://user-images.githubusercontent.com/80598737/156316365-e1e23b52-4bfc-4c3f-8335-683655e83e2c.png)
![04 Intensity](https://user-images.githubusercontent.com/80598737/156316378-3318cb1f-c0a9-4cc9-9eb5-97b300e16c5e.png)

## Converting colors from HSI to RGB
 **1. RG Sector (0 < H < 120):**
---
![RG-Sector](https://user-images.githubusercontent.com/80598737/156316932-b351aa71-2986-42b5-939e-8867994cfc97.png)
---
 **2. GB Sector (120 < H < 240):**
---
![GB-Sector](https://user-images.githubusercontent.com/80598737/156316954-fb8ff9d9-0e1b-4d06-8ee4-b378fa9c5665.png)
---
**3. BR Sector (240 < H < 360):**
---
![BR-Sector](https://user-images.githubusercontent.com/80598737/156316989-04d50c76-ee01-48a6-9108-1deaf13f4d56.png)
---
---
# Normalization
![Normalization](https://user-images.githubusercontent.com/80598737/156334260-ea3b12d5-5a7a-4f7c-8328-8f841e7cdc19.png)

