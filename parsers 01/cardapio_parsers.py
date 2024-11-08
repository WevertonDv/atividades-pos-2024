from xml.dom.minidom import parse

dom = parse("cardapio.xml")

cardapio = dom.documentElement

pratos = cardapio.getElementsByTagName('prato')

for prato in pratos:
    nome = prato.getAttribute(id)
    nome = prato.getElementsByTagName('nome')[0]
    nome = nome.firstChild.nodeValue
    
    descricao = prato.getElementsByTagName('descricao')[0]
    descricao = descricao.firstChild.nodeValue
    
    ingredientes_do_pratos = prato.getElementsByTagName('ingredientes')[0]
    ingredientes_do_pratos = prato.firstChild.nodeValue

    preco = prato.getAttribute('preco')

    calorias = prato.getAttribute('calorias')[0]
    calorias = calorias.firstChild.nodeValue

    tempoPreparo = prato.getAttribute('tempo de preparo')
    tempoPreparo = prato.firstChild.nodeValue

    print("---\n")

    print ("nome do prato:",nome)
    print ("descrição:",descricao)
    print ("ingredientes:",ingredientes_do_pratos)
    print ("preço:",preco)
    print ("calorias:",calorias)
    print ("tempo de peparo:",tempoPreparo)
