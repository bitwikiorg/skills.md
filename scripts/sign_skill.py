import sys
import re
import subprocess
import os

def sign_skill(path):
    with open(path, 'r') as f:
        content = f.read()

    # NORMALIZE LINE ENDINGS
    content = content.replace('\r\n', '\n')

    parts = content.split('\n---\n')
    if len(parts) < 2:
        print(f"Error: Invalid format in {path}")
        sys.exit(1)

    front = parts[0]
    code = parts[1]

    proc = subprocess.run(
        ['gpg', '--batch', '--yes', '--armor', '--detach-sign'],
        input=code.encode('utf-8'),
        capture_output=True
    )

    if proc.returncode != 0:
        print(f"GPG Error: {proc.stderr.decode()}")
        sys.exit(1)

    sig = proc.stdout.decode('utf-8')
    indented_sig = ''.join([' ' + line + '\n' for line in sig.splitlines()])

    front = re.sub(r'signature: \|\n( .*\n)*', '', front)
    new_front = front.strip() + '\n' + 'signature: |\n' + indented_sig
    new_content = new_front + '\n---\n' + code

    with open(path, 'w') as f:
        f.write(new_content)
    
    print(f"Successfully signed {path}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python3 sign_skill.py <file>")
        sys.exit(1)
    sign_skill(sys.argv[1])
