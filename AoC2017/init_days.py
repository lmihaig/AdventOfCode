import os
import requests

cwd = os.getcwd()
year = cwd[-4:]

session_cookie = open('../cookie.txt').readline()

for i in range(1, 26):
    url = f"http://adventofcode.com/{year}/day/{i}"
    os.mkdir(cwd+f"/day{i}")

    with open(cwd+f"\\day{i}\\day{i}.py", "w") as script_file:
        script_file.write(f"# {url}")

    response = requests.get(url+"/input", cookies={"session": session_cookie}).text
    with open(cwd+f"\\day{i}\\input.txt", "w") as input_file:
        input_file.write(str(response))
