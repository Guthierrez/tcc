from selenium import webdriver
from scrapy.selector import Selector
import time
import sqlite3
import winsound
import sys

def saveSourceOnFile(source):
	filename = 'teste.html'
	with open(filename, 'wb') as file:
		file.write(source)

def hasCaptcha(selector):
	if selector.xpath('//img[@src="http://www.reclameaqui.com.br/indices/lista_reclamacoes/captcha.php"]'):
		return True
	else:
		return False

def submitCaptcha(browser):
	winsound.Beep(500, 2000)
	input = browser.find_element_by_id('captcha')
	value = raw_input('Digite o valor da captcha: ')
	input.send_keys(value)
	input.submit()

def getPageSelectorFromSourceCode(browser):
	sourceCode = (browser.page_source).encode('utf-8')
	selector = Selector(text=sourceCode)
	return selector

def getPostData(selector, id, empresa):
	title = selector.xpath('.//div[@class="titulo-reclamacao-leitura"]/blockquote/h1/b/text()').extract_first()
	locale = selector.xpath('.//div[@class="titulo-reclamacao-leitura"]/blockquote/p/text()').extract_first()
	content = selector.xpath('.//div[@class="box-conteudo-reclamacao"]/text()').extract()
	content = ' '.join(content).encode('utf-8').strip().replace('\n', ' ')
	print(locale)
	return (title, content, id, empresa, locale)

def savePostData(conn, data):
	cursor = conn.cursor()
	cursor.executemany("""INSERT INTO reclamacoes VALUES (?, ?, ?, ?, ?)""", [data])
	conn.commit()

def postIsNotPersisted(id):
	conn = sqlite3.connect("reclamacoes.db")
	cursor = conn.cursor()
	sql = "SELECT * FROM reclamacoes WHERE codigo = ?"
	cursor.execute(sql, (id,))
	result = cursor.fetchall()
	return not result

browser = webdriver.Firefox()
empresa = sys.argv[1]
num = 1
conn = sqlite3.connect("reclamacoes.db")
conn.text_factory = str()
for i in range(1, 300):
	browser.get('http://www.reclameaqui.com.br/busca/?q=shoptime&empresa=Shoptime&pagina='+str(i))
	time.sleep(2)
	page = getPageSelectorFromSourceCode(browser)
	if(hasCaptcha(page)):
		submitCaptcha(browser)
		time.sleep(2)
		page = getPageSelectorFromSourceCode(browser)
	reclamacoes = page.xpath('//div[@class="box-resultado-busca"]/ul/li/h2/a/@href').extract()
	for reclamacao in reclamacoes:
		id = reclamacao.split('/')[3]
		if(postIsNotPersisted(id)):
			browser.get(reclamacao)
			time.sleep(3)
			pageReclamacao = getPageSelectorFromSourceCode(browser)
			data = getPostData(pageReclamacao, id, empresa)
			savePostData(conn, data)
			print('Salvo ' + str(num))
			num = num + 1
browser.close()