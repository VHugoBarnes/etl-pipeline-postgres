-- Crear base de datos
CREATE DATABASE sales_dwh;

CREATE TABLE public.dim_card (
	id_card int4 NOT NULL,
	card varchar(30) NOT NULL,
	CONSTRAINT dim_card_pk PRIMARY KEY (id_card)
);

CREATE TABLE public.dim_country (
	id_country int4 NOT NULL,
	country varchar(50) NOT NULL,
	CONSTRAINT dim_country_pk PRIMARY KEY (id_country)
);

CREATE TABLE public.dim_date_sale (
	id_date_sale int4 NOT NULL,
	date_sale date NOT NULL,
	CONSTRAINT dim_date_sale_pk PRIMARY KEY (id_date_sale)
);

CREATE TABLE public.dim_gender (
	id_gender int4 NOT NULL,
	gender varchar(20) NOT NULL,
	CONSTRAINT dim_gender_pk PRIMARY KEY (id_gender)
);

CREATE TABLE public.dim_job_title (
	id_job_title int4 NOT NULL,
	job_title varchar(50) NOT NULL,
	CONSTRAINT dim_job_title_pk PRIMARY KEY (id_job_title)
);

CREATE TABLE public.fact_table (
	id_date_sale int4 NOT NULL,
	id_card int4 NOT NULL,
	id_gender int4 NOT NULL,
	id_job_title int4 NOT NULL,
	id_country int4 NOT NULL,
	min_sale_paid numeric(2) NOT NULL,
	max_sale_paid numeric(2) NOT NULL,
	count_sale_paid numeric(2) NOT NULL,
	sum_sale_paid numeric(2) NOT NULL,
	avg_sale_paid numeric(2) NOT NULL,
	stddev_sale_paid numeric(2) NOT NULL,
	CONSTRAINT fact_table_fk FOREIGN KEY (id_date_sale) REFERENCES public.dim_date_sale(id_date_sale),
	CONSTRAINT fact_table_fk_1 FOREIGN KEY (id_card) REFERENCES public.dim_card(id_card),
	CONSTRAINT fact_table_fk_2 FOREIGN KEY (id_gender) REFERENCES public.dim_gender(id_gender),
	CONSTRAINT fact_table_fk_3 FOREIGN KEY (id_job_title) REFERENCES public.dim_job_title(id_job_title),
	CONSTRAINT fact_table_fk_4 FOREIGN KEY (id_country) REFERENCES public.dim_country(id_country)
);

ALTER TABLE public.fact_table ALTER COLUMN min_sale_paid TYPE numeric(10,2) USING min_sale_paid::numeric;
ALTER TABLE public.fact_table ALTER COLUMN max_sale_paid TYPE numeric(10,2) USING max_sale_paid::numeric;
ALTER TABLE public.fact_table ALTER COLUMN count_sale_paid TYPE numeric(10,2) USING count_sale_paid::numeric;
ALTER TABLE public.fact_table ALTER COLUMN sum_sale_paid TYPE numeric(10,2) USING sum_sale_paid::numeric;
ALTER TABLE public.fact_table ALTER COLUMN avg_sale_paid TYPE numeric(10,2) USING avg_sale_paid::numeric;

-- Fin de creación de tablas y base de datos para el dwh

----------------------------------------------------------------------------------------------------

-- Query para la base de datos sale
select ca.card , cl.country, sa.date_sale, cl.gender, cl.job_title, min(sa.sale_paid) as min_sale_paid, max(sa.sale_paid) as max_sale_paid, count(sa.sale_paid) as count_sale_paid, sum(sa.sale_paid) as sum_sale_paid, avg(sa.sale_paid) as avg_sale_paid
from sale sa
inner join card ca on ca.id_card = sa.id_card
inner join client cl on cl.id_client = ca.id_client
group by ca.card, cl.country, sa.date_sale, cl.gender, cl.job_title, sa.sale_paid
order by ca.card, cl.country, sa.date_sale, cl.gender, cl.job_title, sa.sale_paid;