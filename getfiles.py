import requests

javascript = requests.get('https://raw.githubusercontent.com/learnbr/javascript/master/README.md')
python = requests.get('https://raw.githubusercontent.com/learnbr/python/master/README.md')
htmlcss = requests.get('https://raw.githubusercontent.com/learnbr/htmlcss/master/README.md')
swift = requests.get('https://raw.githubusercontent.com/learnbr/swift/master/README.md')
wordpress = requests.get('https://raw.githubusercontent.com/learnbr/wordpress/master/README.md')
java = requests.get('https://raw.githubusercontent.com/learnbr/java/master/README.md')
kotlin = requests.get('https://raw.githubusercontent.com/learnbr/kotlin/master/README.md')
rubyonrails = requests.get('https://raw.githubusercontent.com/learnbr/rubyonrails/master/README.md')
go = requests.get('https://raw.githubusercontent.com/learnbr/go/master/README.md')


prefix = '_posts/'
javascriptFileMD = open(prefix + '2019-10-15-javascript.markdown','a')
javascriptFileMD.write(javascript.text)
javascriptFileMD.close()

pythonFileMD = open(prefix + '2019-10-15-python.markdown','a')
pythonFileMD.write(python.text)
pythonFileMD.close()

htmlcssFileMD = open(prefix + '2019-10-15-htmlcss.markdown','a')
htmlcssFileMD.write(htmlcss.text)
htmlcssFileMD.close()

swiftFileMD = open(prefix + '2019-10-15-swift.markdown','a')
swiftFileMD.write(swift.text)
swiftFileMD.close()

wordpressFileMD = open(prefix + '2019-10-15-wordpress.markdown','a')
wordpressFileMD.write(wordpress.text)
wordpressFileMD.close()

javaFileMD = open(prefix + '2019-10-15-java.markdown','a')
javaFileMD.write(java.text)
javaFileMD.close()

kotlinFileMD = open(prefix + '2019-10-15-kotlin.markdown','a')
kotlinFileMD.write(kotlin.text)
kotlinFileMD.close()

rubyonrailsFileMD = open(prefix + '2019-10-15-rubyonrails.markdown','a')
rubyonrailsFileMD.write(rubyonrails.text)
rubyonrailsFileMD.close()

goFileMD = open(prefix + '2019-10-15-go.markdown','a')
goFileMD.write(go.text)
goFileMD.close()



