import subprocess
subprocess.check_call(["python", "-m", "pip", "install", "matplotlib"])
import matplotlib.pyplot as plt
plt.plot([1,2,3],[4,5,1])
plt.savefig("matplotlib_test.png")