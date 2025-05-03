import matplotlib.pyplot as plt
import pandas as pd 

df = pd.read_csv("Waveform2.csv")

df_cleaned = df.iloc[1:].reset_index(drop=True)

df_cleaned["X"] = pd.to_numeric(df_cleaned["X"], errors='coerce')
df_cleaned["CH1"] = pd.to_numeric(df_cleaned["CH1"], errors='coerce')

plt.figure(figsize=(10, 5))
plt.plot(df_cleaned["X"], df_cleaned["CH1"], label="CH1 Voltage", color="b")

plt.xlabel("X (Index)")
plt.ylabel("CH1 Voltage (V)")
plt.title("Waveform Data Plot")
plt.legend()
plt.grid()
plt.savefig("waveform plot2")
plt.show()
