from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np
import copy

samplerate, data = wavfile.read('c:/example_-1000.wav')
old_data = copy.deepcopy(data)
data = data * 100
'''
for i in range(len(data)):
    if abs(data[i]) <= 1000:
        data[i] = data[i] * 0.25
    elif abs(data[i]) <= 2000:
        data[i] = data[i] * 0.5
    elif abs(data[i]) <= 3000:
        data[i] = data[i] * 0.75
'''
#data = data * 1000
print(data)
print(type(data))
print(data.shape)
#print("number of channels = ", data.shape[1])
length = data.shape[0] / samplerate
print("length = {}s".format(length))

time = np.linspace(0., length, data.shape[0])
plt.plot(time, old_data, time, data, label="Left channel")
#plt.plot(time, data[:, 1], label="Right channel")
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()

wavfile.write("example_+1000.wav", samplerate, data.astype(np.int16))