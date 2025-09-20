import re
import sys

def usage():
    print("Usage: python3 script.py <broken_key_file> -o <fixed_key_file>")
    sys.exit(1)

if len(sys.argv) != 4 or sys.argv[2] != "-o":
    usage()

input_file = sys.argv[1]
output_file = sys.argv[3]

with open(input_file, 'r') as f:
    data = f.read()

if "OPENSSH PRIVATE KEY" in data:
    header = "-----BEGIN OPENSSH PRIVATE KEY-----"
    footer = "-----END OPENSSH PRIVATE KEY-----"
    keybody = re.sub(r'-*BEGIN\s*OPENSSH\s*PRIVATE\s*KEY-*\s*', '', data, flags=re.I)
    keybody = re.sub(r'-*END\s*OPENSSH\s*PRIVATE\s*KEY-*\s*', '', keybody, flags=re.I)
elif "RSA PRIVATE KEY" in data:
    header = "-----BEGIN RSA PRIVATE KEY-----"
    footer = "-----END RSA PRIVATE KEY-----"
    keybody = re.sub(r'-*BEGIN\s*RSA\s*PRIVATE\s*KEY-*\s*', '', data, flags=re.I)
    keybody = re.sub(r'-*END\s*RSA\s*PRIVATE\s*KEY-*\s*', '', keybody, flags=re.I)
else:
    print("Invalid File Format!")
    sys.exit(1)

keybody = keybody.replace(' ', '').replace('\r', '').replace('\n', '')
lines = [keybody[i:i+64] for i in range(0, len(keybody), 64)]

# save
with open(output_file, 'w') as f:
    f.write(header + '\n')
    f.write('\n'.join(lines) + '\n')
    f.write(footer + '\n')

print(f"✔Key fixed! Output: {output_file}")
print(f"Next: chmod 600 {output_file} && ssh-keygen -l -f {output_file}")
