SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;



COMMENT ON DATABASE bristocontacts IS 'bristoSOFT Contacts Management';



CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;



COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;



CREATE TABLE bristo_contacts_ct (
    bristo_contacts_ct_id integer NOT NULL,
    bristo_contacts_ct_co text NOT NULL,
    bristo_contacts_ct_title text NOT NULL,
    bristo_contacts_ct_fname text NOT NULL,
    bristo_contacts_ct_middle text,
    bristo_contacts_ct_lname text NOT NULL,
    bristo_contacts_ct_cred text,
    bristo_contacts_ct_addr1 text NOT NULL,
    bristo_contacts_ct_addr2 text,
    bristo_contacts_ct_city text NOT NULL,
    bristo_contacts_ct_state text NOT NULL,
    bristo_contacts_ct_postal text NOT NULL,
    bristo_contacts_ct_ph_office text NOT NULL,
    bristo_contacts_ct_ph_cell text,
    bristo_contacts_ct_home text,
    bristo_contacts_ct_email1 text NOT NULL,
    bristo_contacts_ct_email2 text,
    bristo_contacts_ct_web text,
    bristo_contacts_ct_web2 text,
    bristo_contacts_ct_picture bytea DEFAULT '\xffd8ffe000104a46494600010100000100010000ffdb008400090607080706090807080a0a090b0d160f0d0c0c0d1b14151016201d2222201d1f1f2428342c242631271f1f2d3d2d3135373a3a3a232b3f443f384334393a37010a0a0a0d0c0d1a0f0f1a37251f253737373737373737373737373737373737373737373737373737373737373737373737373737373737373737373737373737ffc00011080082008203012200021101031101ffc4001a000100030101010000000000000000000000050607010402ffc400361000020102040304080505010000000000000102030405061131122141518191d11314225261a1b1c124324262f023334371e115ffc4001501010100000000000000000000000000000001ffc40014110100000000000000000000000000000000ffda000c03010002110311003f00be000000000000000003a7000000000000000000000000000056b336637672959d84bf11fe4a9bfa3f82f8fd0099c4315b2c392f5bb88c24f686f27dc883af9d2d62dab7b4ad5176ce4a3e6532739d49ca752529ce4f594a4f56cf902e50ced49bfea58d44bb63513faa44be1f9870dbf92853afe8ea3fd15570b7feba19b028d78e145cbd996ad9ce36d7f3954b67ca337ce54fcd17a8b528a945a716b54d6cc80000000000000000000023f1ec43ff00330cab711d3d27e5a7afbcf6fbbee33394a5293949b726f56df565bb3fd67a59505b3e39bf925f565400000a000005df24624ebdb4ec6acb59d05c54f57fa3b3bbee52098ca759d1c7ad92daa7141f7af3488345074e0000000000000000014dcfebf13652ed84d7cd799542e99fa96b6969592fcb51c3c56bf6296500000000024f2cae2c7ec97ef6fc22c8c2772652f498e425a72a54e537f4fb81a09c008000000000000000022f345abbbc12e6315ace09548f77fcd4cd8d75a4d68d6abaaed330c6ac1e1b8956b7d1f027c54df6c5edfcf801e1001400000b8e42b56a9dd5db5a71354e3ddcdfdbc0a84232a938c209ca5269452eacd4309b258761d42d56f08fb4d7593e6fe641eb000000000000000000002173460ef14b353a097ad51e70fdcbac49a00646d38b6a49a69e8d35a6870b1678a54e9e2b4e54e118caa52e29e9d5ead6acae94003d78453856c52d29d58a94255a2a5196cd6a058b26e0cdce3895cc1a8afec45f57d65e5e25c4e24924a292496892ec04000000000000000000da8c5c9bd12e6dbd883cd18d4b0ba10a56da7acd5e69be7c11edd3f9d4a1dd5cdc5dcb8aeab54aaf5d7db936068d758fe176daa9de539496f1a7edbf9111739d284795ada54a8fb6a49417cb52960a3d5895f56c46ee57370d713e492da2ba247940007d4272a738ce0dc65169a6ba347c802db679d24a318deda7134b9d4a52ddf6f0bf3262d733e1371a6b5dd16fa568f0fcf633a006b746ad3af0e3a1521521ef425aa3e8c8e9ca54e7c74e5284bde8bd1f896ccaf986bceea365885475154e54eacb752ec6faea4170074e000000395271a7094e72518c537293d923a56f3b623eaf651b2a4f4a971ce7a7482f37cbb98152c62fe5896235aea5aa527a413e915b23c601400000000000000000ec6528494a0dc649ea9add33800d4305bf8e258752b95a71b5a544ba496fe7de7b4a264bc47d56fdda549694ee392f84d6de3b7817b20000019e66f6de3d5f56de8a297c3d940010a002800000000000000000000faa6dc6ac1c5b4d4934d7435b5b00400001ffd9'::bytea NOT NULL,
    bristo_contacts_ct_fax text
);


ALTER TABLE bristo_contacts_ct OWNER TO jacksonkirka;


COMMENT ON TABLE bristo_contacts_ct IS 'Contacts';



CREATE SEQUENCE bristo_constacts_ct_bristo_contacts_ct_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE bristo_constacts_ct_bristo_contacts_ct_id_seq OWNER TO jacksonkirka;


ALTER SEQUENCE bristo_constacts_ct_bristo_contacts_ct_id_seq OWNED BY bristo_contacts_ct.bristo_contacts_ct_id;



CREATE TABLE bristo_contacts_appt (
    bristo_contacts_appt_id integer NOT NULL,
    bristo_contacts_appt_ct_id integer NOT NULL,
    bristo_contacts_appt_stamp timestamp with time zone DEFAULT now() NOT NULL,
    bristo_contacts_appt_time timestamp with time zone NOT NULL,
    bristo_contacts_appt_complete boolean DEFAULT false NOT NULL,
    bristo_contacts_appt_purpose text COLLATE pg_catalog."en_US.utf8" DEFAULT 'General Meeting'::text NOT NULL
);


ALTER TABLE bristo_contacts_appt OWNER TO jacksonkirka;


COMMENT ON TABLE bristo_contacts_appt IS 'Appointments and Meetings';



CREATE SEQUENCE bristo_contacts_appt_bristo_contacts_appt_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE bristo_contacts_appt_bristo_contacts_appt_id_seq OWNER TO jacksonkirka;


ALTER SEQUENCE bristo_contacts_appt_bristo_contacts_appt_id_seq OWNED BY bristo_contacts_appt.bristo_contacts_appt_id;


CREATE TABLE bristo_contacts_calls (
    bristo_contacts_calls_id integer NOT NULL,
    bristo_contacts_calls_ct_id integer NOT NULL,
    bristo_contacts_calls_stamp timestamp with time zone DEFAULT now() NOT NULL,
    bristo_contacts_calls_phone text COLLATE pg_catalog."en_US.utf8" NOT NULL,
    bristo_contacts_calls_type boolean DEFAULT false NOT NULL,
    bristo_contacts_calls_results text COLLATE pg_catalog."en_US.utf8" DEFAULT 'Left Message'::text NOT NULL,
    bristo_contacts_calls_appt_id integer
);


ALTER TABLE bristo_contacts_calls OWNER TO jacksonkirka;


COMMENT ON TABLE bristo_contacts_calls IS 'Telephone Calls';



CREATE SEQUENCE bristo_contacts_calls_bristo_contacts_calls_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE bristo_contacts_calls_bristo_contacts_calls_id_seq OWNER TO jacksonkirka;



ALTER SEQUENCE bristo_contacts_calls_bristo_contacts_calls_id_seq OWNED BY bristo_contacts_calls.bristo_contacts_calls_id;


CREATE TABLE bristo_contacts_files (
    bristo_contacts_files_id integer NOT NULL,
    bristo_contacts_files_stamp timestamp with time zone DEFAULT now() NOT NULL,
    bristo_contacts_files_ct text COLLATE pg_catalog."en_US.utf8" NOT NULL,
    bristo_contacts_files_name text COLLATE pg_catalog."en_US.utf8" NOT NULL,
    bristo_contacts_files_file bytea NOT NULL,
    bristo_contacts_files_appt_id integer
);


ALTER TABLE bristo_contacts_files OWNER TO jacksonkirka;


COMMENT ON TABLE bristo_contacts_files IS 'Files';


CREATE SEQUENCE bristo_contacts_file_bristo_contacts_file_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE bristo_contacts_file_bristo_contacts_file_id_seq OWNER TO jacksonkirka;


ALTER SEQUENCE bristo_contacts_file_bristo_contacts_file_id_seq OWNED BY bristo_contacts_files.bristo_contacts_files_id;



CREATE TABLE bristo_contacts_notes (
    bristo_contacts_notes_id integer NOT NULL,
    bristo_contacts_notes_stamp timestamp with time zone DEFAULT now() NOT NULL,
    bristo_contacts_notes_ct text NOT NULL,
    bristo_contacts_notes_note text,
    bristo_contacts_notes_appt_id integer
);
ALTER TABLE ONLY bristo_contacts_notes ALTER COLUMN bristo_contacts_notes_ct SET STORAGE PLAIN;


ALTER TABLE bristo_contacts_notes OWNER TO jacksonkirka;


COMMENT ON TABLE bristo_contacts_notes IS 'Notes';



CREATE SEQUENCE bristo_contacts_notes_bristo_contacts_notes_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE bristo_contacts_notes_bristo_contacts_notes_id_seq OWNER TO jacksonkirka;



ALTER SEQUENCE bristo_contacts_notes_bristo_contacts_notes_id_seq OWNED BY bristo_contacts_notes.bristo_contacts_notes_id;


CREATE TABLE bristo_contacts_users (
    bristo_contacts_users_id integer NOT NULL,
    bristo_contacts_users_name text COLLATE pg_catalog."en_US.utf8" NOT NULL,
    bristo_contacts_users_email text COLLATE pg_catalog."en_US.utf8" NOT NULL,
    bristo_contacts_users_webmail text COLLATE pg_catalog."en_US.utf8" NOT NULL
);


ALTER TABLE bristo_contacts_users OWNER TO jacksonkirka;

COMMENT ON TABLE bristo_contacts_users IS 'Users';


CREATE SEQUENCE bristo_contacts_users_bristo_contacts_users_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;

ALTER TABLE bristo_contacts_users_bristo_contacts_users_id_seq OWNER TO jacksonkirka;


ALTER SEQUENCE bristo_contacts_users_bristo_contacts_users_id_seq OWNED BY bristo_contacts_users.bristo_contacts_users_id;


ALTER TABLE ONLY bristo_contacts_appt ALTER COLUMN bristo_contacts_appt_id SET DEFAULT nextval('bristo_contacts_appt_bristo_contacts_appt_id_seq'::regclass);


ALTER TABLE ONLY bristo_contacts_calls ALTER COLUMN bristo_contacts_calls_id SET DEFAULT nextval('bristo_contacts_calls_bristo_contacts_calls_id_seq'::regclass);


ALTER TABLE ONLY bristo_contacts_ct ALTER COLUMN bristo_contacts_ct_id SET DEFAULT nextval('bristo_constacts_ct_bristo_contacts_ct_id_seq'::regclass);


ALTER TABLE ONLY bristo_contacts_files ALTER COLUMN bristo_contacts_files_id SET DEFAULT nextval('bristo_contacts_file_bristo_contacts_file_id_seq'::regclass);


ALTER TABLE ONLY bristo_contacts_notes ALTER COLUMN bristo_contacts_notes_id SET DEFAULT nextval('bristo_contacts_notes_bristo_contacts_notes_id_seq'::regclass);


ALTER TABLE ONLY bristo_contacts_users ALTER COLUMN bristo_contacts_users_id SET DEFAULT nextval('bristo_contacts_users_bristo_contacts_users_id_seq'::regclass);


ALTER TABLE ONLY bristo_contacts_appt
    ADD CONSTRAINT bristo_contacts_appt_pkey PRIMARY KEY (bristo_contacts_appt_id);


ALTER TABLE ONLY bristo_contacts_calls
    ADD CONSTRAINT bristo_contacts_calls_pkey PRIMARY KEY (bristo_contacts_calls_id);


ALTER TABLE ONLY bristo_contacts_ct
    ADD CONSTRAINT bristo_contacts_ct_id_unq UNIQUE (bristo_contacts_ct_id);


ALTER TABLE ONLY bristo_contacts_ct
    ADD CONSTRAINT bristo_contacts_ct_pkey PRIMARY KEY (bristo_contacts_ct_ph_office);


ALTER TABLE ONLY bristo_contacts_files
    ADD CONSTRAINT bristo_contacts_file_pkey PRIMARY KEY (bristo_contacts_files_id);



ALTER TABLE ONLY bristo_contacts_notes
    ADD CONSTRAINT bristo_contacts_notes_pkey PRIMARY KEY (bristo_contacts_notes_id);


ALTER TABLE ONLY bristo_contacts_users
    ADD CONSTRAINT bristo_contacts_users_pkey PRIMARY KEY (bristo_contacts_users_id);


CREATE INDEX bristo_contacts_calls_results_idx ON bristo_contacts_calls USING btree (bristo_contacts_calls_results text_pattern_ops);



CREATE INDEX bristo_contacts_ct_co_idx ON bristo_contacts_ct USING btree (bristo_contacts_ct_co COLLATE "en_US.utf8" text_pattern_ops);


CREATE UNIQUE INDEX bristo_contacts_email1_idx ON bristo_contacts_ct USING btree (bristo_contacts_ct_email1 COLLATE "en_US.utf8" text_pattern_ops);



CREATE UNIQUE INDEX bristo_contacts_files_name_idx ON bristo_contacts_files USING btree (bristo_contacts_files_name text_pattern_ops);



CREATE INDEX bristo_contacts_full_name_idx ON bristo_contacts_ct USING btree (bristo_contacts_ct_fname COLLATE "en_US.utf8" text_pattern_ops, bristo_contacts_ct_middle COLLATE "en_US.utf8" text_pattern_ops, bristo_contacts_ct_lname COLLATE "en_US.utf8" text_pattern_ops);


CREATE INDEX bristo_contacts_users_idx ON bristo_contacts_users USING btree (bristo_contacts_users_email text_pattern_ops);



ALTER TABLE ONLY bristo_contacts_appt
    ADD CONSTRAINT bristo_contacts_appt_fkey FOREIGN KEY (bristo_contacts_appt_ct_id) REFERENCES bristo_contacts_ct(bristo_contacts_ct_id) MATCH FULL;


ALTER TABLE ONLY bristo_contacts_calls
    ADD CONSTRAINT bristo_contacts_calls_fkey FOREIGN KEY (bristo_contacts_calls_ct_id) REFERENCES bristo_contacts_ct(bristo_contacts_ct_id) MATCH FULL;



ALTER TABLE ONLY bristo_contacts_files
    ADD CONSTRAINT bristo_contacts_file_fkey FOREIGN KEY (bristo_contacts_files_ct) REFERENCES bristo_contacts_ct(bristo_contacts_ct_ph_office) MATCH FULL;



ALTER TABLE ONLY bristo_contacts_notes
    ADD CONSTRAINT bristo_contacts_notes_fkey FOREIGN KEY (bristo_contacts_notes_ct) REFERENCES bristo_contacts_ct(bristo_contacts_ct_ph_office);

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;

