# -*- coding: utf-8 -*-
"""PROJETO INTEGRADOR

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XtP4k7ITVxMpmOIsoLL2Ci7QP-z_R3W6
"""

#utilizou conceitos de codigo limpo, nesse codigo foram utilizados nomes de variaveis objetivos e simples, para reduzir a poluição do codigo, utilizamos tambem uma identação semelhante a todos

class Usuario: # Codificando classes, essa classe serve para facilitar o login futuramente
  def __init__(self, nome, senha): # Codificando os metodos construtores, o metodo construtor vai englobar a senha de emergencia, usuario e senha
    self. __senha_emergencia = 000000 # Codificando atributo estático, esse atributo é estatico pois nao muda e tem seu valor previamente atribuido, serve para ter uma senha de recap, atribuida previamente no aparelho
    self.nome = nome # Codificando atributos, o atributo nome vai servir para controlar o acesso e notificar o nome do usuario
    self.__senha = senha # Codificando atributos protegidos e/ou privado, o atributo senha vai servir para o usuario ter permissao para usar a fechadura, é privado pois o acesso é limitado
  def mudar_nome(self, novo_nome): # Codificando metodos, esse metodo serve para alterar o nome em caso de erro ou esqueciemento
     self.nome = novo_nome
     return self.nome
  def __mudar_senha(self, nova_senha): # Codificando metodos protegidos e/ou privados, esse metodo serve para alterar a senha em caso de esquecimento, é privado pois o acesso a senha é limitado
     self.__senha = nova_senha
     return self.__senha
  @staticmethod
  def __mudar_senha_emergencia(senha_nova): # Codificando metodos estaticos, esse metodo serve para alterar a senha de emergencia, esse metodo é estatico pois o atributo senha é fornecido anteriormente, é privado pois a senha de emergencia é limitada apenas aos donos
    self.__senha_emergencia = senha_nova
    return self.__senha_emergencia
  def get_nome(self): # Este metodo serve para acessar o nome, de maneira que não tenha alterações
    return self.nome
  def __get_senha(self): # Este metodo serve para acessar a senha , de maneira que não tenha alterações, é privado pois a senha é privada
     return self.__senha

#Instanciando objetos, foram instanciados os objetos user 1 e user 2, os quais possuem todos os atributos
user1 = Usuario('vinicius_custodio', 061004)
user2 = Usuario ('leonardo_jotta', 130505)