from xml.dom.minidom import parse
dom = parse("cardapio.xml")
cardapio = dom.documentElement
pratos = cardapio.getElementsByTagName('prato')
for prato in pratos:
    nome = prato.getAttribute(id)
    descricao = descricao.getElementsByTagName('descricao')[0]
    descricao = descricao.firstChild.nodeValue

    ingredientes_do_pratos = ingredientes.getElementsByTagName('ingredientes')[0]
    origem = elemento_autor.getAttribute('origem')
    autor = elemento_autor.firstChild.nodeValue
    elemento_ano = livro.getElementsByTagName('ano')[0]
    ano = elemento_ano.firstChild.nodeValue

    print("---\n")