string = "X-DSPAM-Confidence:    0.8475"

exval = string.find(":")
num = string[exval +1:]
final = float(num)
print(final)
