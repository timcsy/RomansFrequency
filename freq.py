import re

input_path = 'all.txt'
output_path = 'strong.txt'

with open(input_path, 'r') as f:
    text = f.read()

m = re.findall('\<(\d+)\>', text)

bucket = {}
for n in m:
    if n not in bucket:
        bucket[n] = 1
    else:
        bucket[n] += 1

rank = { k: v for k, v in reversed(sorted(bucket.items(), key=lambda item: item[1])) }

output = ''
for k, v in rank.items():
    output += k + ': ' + str(v) + '\n'

with open(output_path, 'w') as f:
    f.write(output)