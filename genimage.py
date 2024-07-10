import webbrowser

def pegar_parameteros():
    tem_personagem = input("A imagem tem personagem? (sim/não): ").strip().lower()
    personagem_descricao = ""
    if tem_personagem == "sim":
        personagem_descricao = input("Descreva o personagem: ").strip()

    tem_cenario = input("A imagem tem cenário? (sim/não): ").strip().lower()
    cenario_descricao = ""
    if tem_cenario == "sim":
        cenario_descricao = input("Descreva o cenário: ").strip()

    return personagem_descricao, cenario_descricao

