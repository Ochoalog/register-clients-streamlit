import streamlit as stlit

stlit.title("Cadastro de clientes")

nome = stlit.text_input("Nome do cliente")
endereco = stlit.text_input("Endereço")
dt_nasc = stlit.date_input("Escolha a data de nascimento")
tipo_cliente = stlit.selectbox("Tipo de cliente", 
                               ["Pessoa física", "Pessoa Jurídica"])


cadastrar = stlit.button("Cadastrar cliente")


if cadastrar:
    with open("clientes.csv", "a", encoding="utf8") as arquivo:
        arquivo.write(f"{nome},{endereco},{dt_nasc},{tipo_cliente}\n")
        stlit.success("Cliente cadastrado com sucesso!")