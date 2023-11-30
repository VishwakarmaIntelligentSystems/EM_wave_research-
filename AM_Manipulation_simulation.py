import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
print("All packages imported")

st.set_option('deprecation.showPyplotGlobalUse', False)
#Carrier wave c(t)=A_c*cos(2*pi*f_c*t)
#Modulating wave m(t)=A_m*cos(2*pi*f_m*t)
#Modulated wave s(t)=A_c[1+mu*cos(2*pi*f_m*t)]cos(2*pi*f_c*t)

st.title("Amplitude Modulation Simulator")

A_c = st.slider('Enter carrier amplitude: ')
f_c = st.slider('Enter carrier frquency: ')
A_m = st.slider('Enter message amplitude: ')
f_m = st.slider('Enter message frquency: ')
modulation_index = st.number_input('Enter modulation index: ')


t = np.linspace(0,1,1000)
carrier = A_c*np.cos(2*np.pi*f_c*t)
modulator = A_m*np.cos(2*np.pi*f_m*t)
product = A_c*(1+modulation_index*np.cos(2*np.pi*f_m*t))*np.cos(2*np.pi*f_c*t)


plt.subplot(3,1,1)
plt.title('Amplitude Modulation')
plt.plot(modulator,'g')
plt.ylabel('Amplitude')
plt.xlabel('Message signal')

plt.subplot(3,1,2)
plt.plot(carrier, 'r')
plt.ylabel('Amplitude')
plt.xlabel('Carrier signal')

plt.subplot(3,1,3)
plt.plot(product, color="purple")
plt.ylabel('Amplitude')
plt.xlabel('AM signal')

plt.subplots_adjust(hspace=1)
plt.rc('font', size=15)
fig = plt.gcf()
st.pyplot(fig.set_size_inches(16, 9))