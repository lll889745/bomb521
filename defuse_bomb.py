import subprocess

def run_bomb(inputs):
    try:
        process = subprocess.Popen(['./bomb'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, _ = process.communicate('\n'.join(inputs))
    except Exception as e:
        print(f"Error: {e}")
        return None
    
    return output

inputs = [
    "Crikey! I have lost my mojo!",
    "0 1 1 2 3 5",
    "0 q 436",
    "6 6 DrEvil",
    "mfcdhg",
    "5 1 4 2 6 3"
]

boom_output = "BOOM!!!\nThe bomb has blown up.\n"

for i in range(1, 1001):
    current_inputs = inputs + [str(i)]
    output = run_bomb(current_inputs)

    if output != boom_output:
        print(f"Safe input found: {i}")
        break

