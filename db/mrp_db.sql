CREATE DATABASE "MRP"
  WITH ENCODING='UTF8'
       OWNER=postgres
       CONNECTION LIMIT=-1;




create table tb_estoque(
id_estoque integer not null,
qtd_tec_verm integer,
qtd_tec_branco integer,
qtd_tec_preto integer,
qtd_espuma integer,

constraint pk_tb_estoque_id_estoque primary key(id_estoque)
);[

create table tb_cliente(
id_cliente integer not null,
nome varchar(100),

constraint pk_tb_cliente_id_cliente primary key(id_cliente)
);

create table tb_pedido(
id_pedido integer not null,
id_cliente integer not null,
qtd_bojo_branco integer,
qtd_bojo_vermelho integer,
qtd_bojo_preto integer,

constraint pk_tb_pedido_id_pedido primary key(id_pedido),
constraint fk_tb_pedido_id_cliente foreign key(id_cliente) references tb_cliente
);



create table tb_fabrica(
id_fabrica integer not null,
id_estoque integer not null,
id_pedido integer not null,
cidade varchar(60),
estado char(2),

constraint pk_tb_fabrica_id_fabrica primary key(id_fabrica),
constraint fk_tb_fabrica_id_estoque foreign key(id_estoque) references tb_estoque,
constraint fk_tb_fabrica_id_pedido foreign key(id_pedido) references tb_pedido,
);
