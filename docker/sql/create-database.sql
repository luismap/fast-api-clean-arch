--Setup database
DROP DATABASE IF EXISTS api_dev;
CREATE DATABASE api_dev;
\c api_dev;

CREATE SCHEMA fast_api
    AUTHORIZATION admin;

--USER SECTION

CREATE SEQUENCE IF NOT EXISTS fast_api.user_user_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1
    ;

ALTER SEQUENCE fast_api.user_user_id_seq
    OWNER TO admin;

CREATE TABLE IF NOT EXISTS fast_api.user
(
    user_id integer NOT NULL DEFAULT nextval('fast_api.user_user_id_seq'::regclass),
    email character varying COLLATE pg_catalog."default" NOT NULL,
    password character varying COLLATE pg_catalog."default" NOT NULL,
    created_at timestamp without time zone DEFAULT now(),
    CONSTRAINT user_pkey PRIMARY KEY (user_id),
    CONSTRAINT user_email_key UNIQUE (email)
)

TABLESPACE pg_default;

CREATE INDEX IF NOT EXISTS ix_fast_api_user_user_id
    ON fast_api.user USING btree
    (user_id ASC NULLS LAST)
    TABLESPACE pg_default;

INSERT INTO fast_api.user (email, password)
VALUES
('luis@gmail.com','$2b$12$R/0WtC6JWjmjYxrr4NOLaOw5tvSPEWDAn1D/J5czuUULsSvNeeQWK'),
('anna@gmail.com','$2b$12$sE3gj6Drk5C5Ttey9QB2ZuUhLa/49ScDKTh66fqU.QUtsclpuPPTS'),
('seb@gmail.com','$2b$12$JdtLVHQDtr4IyvsL2aYWsOTzVwViS7T3odiiJSC99ir/L584ff/CK');


--PRODUCTS SECTION
CREATE SEQUENCE IF NOT EXISTS fast_api.products_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1
    ;

ALTER SEQUENCE fast_api.products_id_seq
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

--POST SECTION

CREATE SEQUENCE IF NOT EXISTS fast_api.posts_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1
    ;

ALTER SEQUENCE fast_api.posts_id_seq
  OWNER TO admin;   

CREATE TABLE IF NOT EXISTS fast_api.posts
(
    id bigint NOT NULL DEFAULT nextval('fast_api.posts_id_seq'::regclass),
    title character varying NOT NULL COLLATE pg_catalog."default",
    content character varying NOT NULL COLLATE pg_catalog."default",
    published boolean DEFAULT false,
    rating integer DEFAULT 0,
    created_at timestamp with time zone DEFAULT now(),
    user_id integer NOT NULL,
    CONSTRAINT posts_pky PRIMARY KEY (id),
    CONSTRAINT user_id_fkey FOREIGN KEY (user_id)
        REFERENCES fast_api.user (user_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)
TABLESPACE pg_default;

ALTER TABLE IF EXISTS fast_api.posts
    OWNER to admin;

INSERT INTO FAST_API.posts (title, content, user_id)
VALUES
('ml', 'is very important machine learning',1),
('medicine', 'about the new content in placebo effect',2),
('robotics', 'the new down of AI',3);

