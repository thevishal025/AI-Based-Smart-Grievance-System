with open('c:/copy/app.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if 'def send_otp' in line:
        print(f"Line {i+1}:")
        for j in range(i, min(i+40, len(lines))):
            print(f"{j+1}: {lines[j]}", end='')
