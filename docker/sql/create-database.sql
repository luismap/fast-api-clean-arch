--Setup database
DROP DATABASE IF EXISTS api_dev;
CREATE DATABASE api_dev;
\c api_dev;

CREATE SCHEMA fast_api
    AUTHORIZATION admin;

CREATE SEQUENCE IF NOT EXISTS fast_api.products_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1
    ;

ALTER SEQUENCE fast_api.products_id_seq
    OWNER TO admin;

CREATE SEQUENCE IF NOT EXISTS fast_api.posts_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1
    ;

ALTER SEQUENCE fast_api.posts_id_seq
  OWNER TO admin;    

CREATE TABLE IF NOT EXISTS fast_api.products
(
    id bigint NOT NULL DEFAULT nextval('fast_api.products_id_seq'::regclass),
    price integer NOT NULL,
    name character varying NOT NULL COLLATE pg_catalog."default",
    is_sale boolean DEFAULT false,
    inventory integer DEFAULT 0,
    created_at timestamp with time zone DEFAULT now(),
    CONSTRAINT products_pkey PRIMARY KEY (id)
)
TABLESPACE pg_default;

ALTER TABLE IF EXISTS fast_api.products
    OWNER to admin;

INSERT INTO FAST_API.PRODUCTS ("name",PRICE,INVENTORY,IS_SALE)
VALUES ('socks',20, 10, TRUE),
('tennis racket',10, 2, FALSE),
('remote controller', 5, 3, TRUE),
('pencil', 3, 3, FALSE),
('dictionaries',20, 5, FALSE),
('blockets',20, 5, FALSE),
('wine bottles',20, 5, FALSE),
('magazines',20, 5, FALSE),
('mobile', 34, 21, FALSE);

CREATE TABLE IF NOT EXISTS fast_api.posts
(
    id bigint NOT NULL DEFAULT nextval('fast_api.posts_id_seq'::regclass),
    title character varying NOT NULL COLLATE pg_catalog."default",
    content character varying NOT NULL COLLATE pg_catalog."default",
    published boolean DEFAULT false,
    rating integer DEFAULT 0,
    created_at timestamp with time zone DEFAULT now(),
    CONSTRAINT posts_pkey PRIMARY KEY (id)
)
TABLESPACE pg_default;

ALTER TABLE IF EXISTS fast_api.posts
    OWNER to admin;

INSERT INTO FAST_API.posts (title, content)
VALUES
('ml', 'is very important machine learning'),
('medicine', 'about the new content in placebo effect'),
('robotics', 'the new down of AI');

