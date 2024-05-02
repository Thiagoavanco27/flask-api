# Dicionario

Um dicionário é muito semelhante a uma lista.

Tomemos a lista [10,20,30]. As posições dela são 0,1 e 2.

lista[0] vale 10, lista[1] vale 20 e lista[2] vale 30.

A diferença entre dicionários e listas é que um dicionário
pode ter as posições que a gente quiser.

Um dicionário pode ter as posições 3, 9 e 11
(sem ter as posições 0,1,2,4,5,6,7,8, nem 10)

Na verdade, como podemos ver no exemplo a seguir,
um dicionário pode ter as posições "marcos", "fabio" e "maria".

(oficialmente, um dicionário não tem "posições",
mas sim chaves)

```python
agenda_exemplo = {}

agenda_exemplo['marcos']=32112232
agenda_exemplo['fabio']=988887788
agenda_exemplo['maria']=44554455
```

## Atividade

1. Crie uma função `consulta` que recebe uma agenda (um dicionário) e uma pessoa => retorna o telefone dessa pessoa.

2. Crie uma função `adiciona` que recebe uma agenda (um dicionário),uma pessoa, um telefone e a idade.

   OBS: Adicionar um item num dicionário é simples 
   `dicionario['chave'] = valor`.

3. Uma terceira feature que precisamos para a nossa agenda é a possibilidade de verificar se uma pessoa já está na base de dados.
   Simplesmente verificar `agenda['pessoa']` não funciona, se você acessar uma pessoa que não existe, o python dará um `KeyError`.
   Precisamos, então usar o seguinte: `'chave' in dicionario.keys()`  
   isso é um teste que retorna `True` se a chave está no dicionário, e `False` caso contrário.


# Criar um teste para a nossa Agenda

Vamos usar `unittest`.

O módulo `unittest` é uma parte padrão da biblioteca padrão do `Python` e não requer instalação adicional.

Ele fornece um framework de teste unitário que permite criar testes para suas funções e classes em Python de forma estruturada e eficiente. Por ser parte da biblioteca padrão, você pode usá-lo em qualquer ambiente Python sem a necessidade de instalar pacotes adicionais.
