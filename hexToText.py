import subprocess

vInputText = "Paste HEX below:\n"
vOutputText = "\nBelow result has been in your clipboard already.\nResult:"

vInput = input(vInputText)
vOutput = bytes.fromhex(vInput).decode('utf-8')
subprocess.run(['clip.exe'], input=vOutput.strip().encode('utf-8'), check=True)

print(vOutputText, vOutput, "\n")