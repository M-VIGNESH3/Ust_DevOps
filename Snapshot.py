import subprocess

result = subprocess.run(['echo', 'Hello from Emil'], capture_output=True, text=True)
print(result.stdout)
