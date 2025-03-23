

def create(n):
    seq = [0, 1]

    for _ in range(n-2):
        previous_num1 = seq[-1]
        previous_num2 = seq[-2]
        current_num = previous_num1 + previous_num2
        seq.append(current_num)
    return seq


def start(command):

    while command != "Stop":
        data = command.split()
        if data[0] == "Create":
            n = int(data[-1])
            seq = create(n)
            print(*seq)
        elif data[0] == "Locate":
            num = int(data[-1])
            try:
                print(f"The number - {num} is at index {seq.index(num)}")
            except ValueError:
                print(f"The number {num} is not in the sequence")
            except NameError:
                print("Please first create a sequence.")
        command = input()
