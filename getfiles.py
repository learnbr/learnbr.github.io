import requests


## get content
def getContent(url):
    content = requests.get(url)
    return content

## write content
def writeContent(prefix, fileName, content):
    file = open(prefix + '2019-10-15-'+ fileName +'.markdown','a')
    file.write(content.text)
    file.close()

def mountPosts(postContents):
    for post in postContents:
        content = getContent(post)
        fileName = post.replace('https://raw.githubusercontent.com/learnbr/','').replace('/master/README.md','')
        writeContent('_posts/', fileName, content)


contents = [
    'https://raw.githubusercontent.com/learnbr/javascript/master/README.md', 
    'https://raw.githubusercontent.com/learnbr/javascript/master/README.md',
    'https://raw.githubusercontent.com/learnbr/python/master/README.md',
    'https://raw.githubusercontent.com/learnbr/html-css/master/README.md', 
    'https://raw.githubusercontent.com/learnbr/wordpress/master/README.md',
    'https://raw.githubusercontent.com/learnbr/swift/master/README.md',
    'https://raw.githubusercontent.com/learnbr/java/master/README.md',
    'https://raw.githubusercontent.com/learnbr/kotlin/master/README.md',
    'https://raw.githubusercontent.com/learnbr/rubyonrails/master/README.md',
    'https://raw.githubusercontent.com/learnbr/go/master/README.md',
    'https://raw.githubusercontent.com/learnbr/php/master/README.md',
    'https://raw.githubusercontent.com/learnbr/elixir/master/README.md',
    'https://raw.githubusercontent.com/learnbr/go/master/README.md',
    'https://raw.githubusercontent.com/learnbr/go/master/README.md'
]


mountPosts(contents)
