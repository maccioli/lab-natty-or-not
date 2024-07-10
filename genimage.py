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

def criar_prompt(personagem, cenario):
    prompt = "A image of"
    
    if personagem:
        prompt += f" a {personagem}"
    
    if cenario:
        prompt += f" in {cenario}"
    
    return prompt

def gerar_image_url(prompt):
    base_url = "https://image.pollinations.ai/prompt/"
    prompt_formatado = prompt.replace(" ", "%20")
    url = f"{base_url}{prompt_formatado}?width=800&height=600&seed=793"
    return url

def principal():
    personagem, cenario = pegar_parameteros()
    prompt = criar_prompt(personagem, cenario)
    image_url = gerar_image_url(prompt)
    
    print(f"URL da imagem gerada: {image_url}")
    webbrowser.open(image_url)

if __name__ == "__main__":
    principal()