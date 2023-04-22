import itertools
import subprocess

def test_bomb():
    # 前五个阶段的密码
    passwords = [
        "Crikey! I have lost my mojo!\n",
        "0 1 1 2 3 5\n",
        "0 q 436\n",
        "6 6\n",
        "mfcdhg\n"
    ]

    # 穷举1-6的排列组合
    for input_numbers in itertools.permutations(range(1, 7)):
        phase_6_input = " ".join(str(num) for num in input_numbers) + "\n"

        # 尝试运行bomb程序
        process = subprocess.Popen("./bomb", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output, _ = process.communicate("".join(passwords) + phase_6_input)

        # 检查输出是否包含成功解除炸弹的信息
        if "Congratulations! You've defused the bomb!" in output:
            print("Success! The correct input for phase 6 is:", phase_6_input.strip())
            break

test_bomb()

