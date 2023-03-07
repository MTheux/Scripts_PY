import requests, re
url = 'http://testphp.vulnweb.com/artists.php?artist=2'
filtro = re.search(r'([\w:/\._-]+\?[\w_-]+=)([\w_-]+)', url)
injecao = filtro.groups()[0] + '\''
print(injecao)
header = {'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43'}
req = requests.get(injecao)
html = req.text
if 'mysql_fetch_array()' in html:
    print('Vulneravel')
else:
    print('Não Vulneravel')
