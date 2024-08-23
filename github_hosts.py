import os
import time
from selenium import webdriver


def re_hosts(ip_addresses, host_name):
    res = []
    with open('C:\Windows\System32\drivers\etc\hosts', mode='r') as file:
        for line in file.readlines():
            if line.startswith('#') or len(line.split(maxsplit=1)) <= 1 or line.split(maxsplit=1)[1] != f'{host_name}\n':
                res.append(line)
    while res[-1] == '\n':
        res.pop()
    res.append('\n')
    for ip_add in ip_addresses:
        res.append(f'{ip_add}\t{host_name}\n')
    with open('C:\Windows\System32\drivers\etc\hosts', mode='w') as file:
        file.writelines(res)
    os.system('ipconfig/flushdns')


def get_ips(host_name, timeout=5):
    driver = webdriver.Chrome('C:\MyProgram\chromedriver-win64\chromedriver.exe')
    driver.get(f'https://ping.chinaz.com/{host_name}')
    completed = driver.find_element_by_id("gjd")
    total = completed.find_element_by_xpath('../label')
    wait_time = 0
    while not completed.text or not total.text or int(completed.text) < int(total.text):
        time.sleep(0.5)
        wait_time += 0.5
        if wait_time > timeout:
            print(f'timeout={timeout}s, get {int(completed.text)}/{int(total.text)} responses')
            break
    elements = driver.find_element_by_id("ipliststr").find_elements_by_tag_name("a")
    res = [ele.text for ele in elements]
    driver.quit()
    return res


def run():
    host_name = 'github.com'
    ips = get_ips(host_name)
    re_hosts(ips, host_name)


if __name__ == "__main__":
    run()
