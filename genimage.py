import webbrowser

def pegar_parameteros():
    tem_personagem = input("A imagem tem personagem? (sim/não): ").strip().lower()
    personagem_descricao = ""
    if tem_personagem == "sim":
        personagem_descricao = input("Descreva o personagem: ").strip()