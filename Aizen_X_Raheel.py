import re,os,sys,time
from colorama import init, Fore, Style
import pyfiglet

# Initialize colorama
init(autoreset=True)

def clear_screen():
    os.system("clear")  # Use "cls" on Windows

def show_typing_banner(text, delay=0.2):
    for i in range(1, len(text) + 1):
        banner = pyfiglet.figlet_format(text[:i], font="slant")
        clear_screen()
        print(Fore.YELLOW + Style.BRIGHT + banner)
        time.sleep(delay)

def bouncing_dots(duration=3):
    print(Fore.GREEN + "\nLoading", end="", flush=True)
    start_time = time.time()
    while time.time() - start_time < duration:
        for dots in [".  ", ".. ", "..."]:
            sys.stdout.write("\r" + Fore.GREEN + "Loading" + dots)
            sys.stdout.flush()
            time.sleep(0.4)
    print("\r" + Fore.GREEN + "Loading... Done!      ")

def show_info_footer():
   # print(Fore.RED + "=" * 50)
    print()
    print(Style.BRIGHT + Fore.RED + "Tool Version : " + Fore.YELLOW + "1.0\n")
    print(Style.BRIGHT + Fore.RED + "Target App   : " + Fore.YELLOW + "Mile Ai\n")
    print(Style.BRIGHT + Fore.RED + "Owner        : " + Fore.YELLOW + "AIZEN X RAHEEL\n")
    
    print()
    print(Fore.RED + "=" * 50)
clear_screen()
show_typing_banner("LOOSERS")
print(Fore.RED + "=" * 50)
#bouncing_dots()



show_info_footer()
def extract_and_format(file_path, escaped_template, output_file):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Extract task_sub_id
    task_sub_id_match = re.search(r'"task_sub_id"\s*:\s*(\d+)', content)
    task_sub_id = task_sub_id_match.group(1) if task_sub_id_match else "0"

    # Match task/contact blocks
    task_blocks = re.findall(r'\{[^{}]*"account"\s*:\s*"[^"]+"[^{}]*\}', content)
    results = []

    for block in task_blocks:
        template = escaped_template  # fresh copy per contact

        account     = re.search(r'"account"\s*:\s*"([^"]+)"', block)
        account_id  = re.search(r'"account_id"\s*:\s*(\d+)', block)
        detail_id   = re.search(r'"detail_id"\s*:\s*(\d+)', block)
        link        = re.search(r'"link"\s*:\s*"([^"]+)"', block)
        text        = re.search(r'"text"\s*:\s*"([^"]+)"', block)

        # Replace each field using exact placeholders
        if account:
            template = template.replace('\\"account\\":\\"+923412869243\\"', f'\\"account\\":\\"{account.group(1)}\\"')
        if account_id:
            template = template.replace('\\"account_id\\":72265565', f'\\"account_id\\":{account_id.group(1)}')
        if detail_id:
            template = template.replace('\\"detail_id\\":73925500', f'\\"detail_id\\":{detail_id.group(1)}')
        if link:
            template = template.replace('\\"link\\":\\"https://whatsapp.com/channel/0029VbBL4UJL7UVXTlPTKF0w\\"',
                                        f'\\"link\\":\\"{link.group(1)}\\"')
        if text:
            template = template.replace('\\"text\\":\\"https://whatsapp.com/channel/0029VbBL4UJL7UVXTlPTKF0w\\"',
                                        f'\\"text\\":\\"{text.group(1)}\\"')

        # Always fix result_text
        template = re.sub(r'\\"result_text\\":\\".*?\\"', r'\\"result_text\\":\\"检验并删除成功\\"', template)

        results.append(template)

    # Final JSON output
    final_output = f'''{{
  "task_id": 4,
  "task_sub_id": {task_sub_id},
  "ex_account": "Chand Bhai (You)",
  "has_continuous_fail": 0,
  "task_data": "[{",".join(results)}]"
}}'''

    # Write to file
    with open(output_file, 'w', encoding='utf-8') as out_file:
        out_file.write(final_output)
    time.sleep(5)

    print(Style.BRIGHT + Fore.GREEN + "\nHACK INJECTED SUCCESSFULLY.✅🔥🤑\n\n\n    ")
    return final_output

# Escaped template (no edits needed)
escaped_template_string = r'{\"link\":\"https://whatsapp.com/channel/0029VbBL4UJL7UVXTlPTKF0w\",\"text\":\"https://whatsapp.com/channel/0029VbBL4UJL7UVXTlPTKF0w\",\"account\":\"+923412869243\",\"detail_id\":73925500,\"account_id\":72265565,\"addedContact\":true,\"selected\":true,\"taskFinish\":true,\"sended\":true,\"result_text\":\"检验并删除成功\",\"status\":1}'

# Run and write output
extract_and_format('task_fetched.txt', escaped_template_string, 'submitted_data.txt')
