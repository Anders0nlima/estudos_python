1- adicionar

1.1- adicionar por unidades:
insert into alunos values(25, "Rafael", "Geografia", 5.3, 7.0, 4.2, 7.0);
insert into alunos values(default, "Gabriel", "Quimica", 1.0, 4.9, 5.8, 7.9); (quando o id e primary key)

1.2- adicionar por grupos:
insert into alunos values
(26, "Mariana", "História", 6.5, 8.0, 7.2, 6.8),
(27, "Lucas", "Matemática", 4.9, 6.3, 5.7, 7.1),
(28, "Ana", "Português", 7.8, 8.5, 6.9, 9.0),
(29, "Bruno", "Ciências", 5.2, 6.0, 4.8, 6.7)
;

2-deletar 
2.1- deletar somente uma linha 
delete from alunos where id = 26;

2.2- deletar todo mundo no tabela de dados 
truncate table alunos;

3- atualizar
3.1- atualiza o nota1 para 10  
update alunos set 
nota1 = 10
where id = 30;

4- salvar a tebela
4.1- salvo as informações em uma tabela nova (aluno_back)
create table aluno_back as 
select * from alunos

4- deletar um banco de dados
4.1- apagar a tebla salva anteriomente
drop table aluno_back;

-----------------------------------------------------------------------------------------
construindo nosso banco relacional:
file > new model > começa a criar a ORM ai (arquivos no wtt)
depois de criar vai em export e clica na primeira opção 
depois cria uma file para ela criando nos 3 pontinhos e depois e so avançar tudo
depois vai em open a sql scrip file in a new query tab (cando superio esquerdo) e abre a file que voce criou e da run, isso vai rodar todo o codigo que voce faz usando o ORM
depois e so atualizar que a tebela vai aparcer

isso faz com que eu gere de maneria que nao tenha erro, e mais rapido, alem de mais seguro, pois ao desenhar(ORM eu posso ter mais segurança na interreação do banco de dados)


