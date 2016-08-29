--
-- PostgreSQL database dump
--

-- Dumped from database version 9.4.9
-- Dumped by pg_dump version 9.5.4

-- Started on 2016-08-29 11:24:21 EDT

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE bristocontacts;
--
-- TOC entry 3000 (class 1262 OID 16390)
-- Name: bristocontacts; Type: DATABASE; Schema: -; Owner: admin
--

CREATE DATABASE bristocontacts WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.utf8' LC_CTYPE = 'en_US.utf8';


ALTER DATABASE bristocontacts OWNER TO admin;

\connect bristocontacts

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 1 (class 3079 OID 12723)
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- TOC entry 3003 (class 0 OID 0)
-- Dependencies: 1
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


--
-- TOC entry 2 (class 3079 OID 19072)
-- Name: pg_stat_statements; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS pg_stat_statements WITH SCHEMA public;


--
-- TOC entry 3004 (class 0 OID 0)
-- Dependencies: 2
-- Name: EXTENSION pg_stat_statements; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION pg_stat_statements IS 'track execution statistics of all SQL statements executed';


--
-- TOC entry 3 (class 3079 OID 16957)
-- Name: uuid-ossp; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS "uuid-ossp" WITH SCHEMA public;


--
-- TOC entry 3005 (class 0 OID 0)
-- Dependencies: 3
-- Name: EXTENSION "uuid-ossp"; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION "uuid-ossp" IS 'generate universally unique identifiers (UUIDs)';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 175 (class 1259 OID 16391)
-- Name: bristo_contacts_ct; Type: TABLE; Schema: public; Owner: admin
--

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
    bristo_contacts_ct_fax text,
    bristo_contacts_ct_owner text DEFAULT 'jacksonkirka '::text NOT NULL,
    bristo_contacts_ct_available boolean DEFAULT false NOT NULL,
    bristo_contacts_ct_group text COLLATE pg_catalog."en_US.utf8"
);


ALTER TABLE bristo_contacts_ct OWNER TO admin;

--
-- TOC entry 3006 (class 0 OID 0)
-- Dependencies: 175
-- Name: TABLE bristo_contacts_ct; Type: COMMENT; Schema: public; Owner: admin
--

COMMENT ON TABLE bristo_contacts_ct IS 'Contacts';


--
-- TOC entry 176 (class 1259 OID 16401)
-- Name: bristo_constacts_ct_bristo_contacts_ct_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE bristo_constacts_ct_bristo_contacts_ct_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE bristo_constacts_ct_bristo_contacts_ct_id_seq OWNER TO admin;

--
-- TOC entry 3008 (class 0 OID 0)
-- Dependencies: 176
-- Name: bristo_constacts_ct_bristo_contacts_ct_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE bristo_constacts_ct_bristo_contacts_ct_id_seq OWNED BY bristo_contacts_ct.bristo_contacts_ct_id;


--
-- TOC entry 177 (class 1259 OID 16403)
-- Name: bristo_contacts_appt; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE bristo_contacts_appt (
    bristo_contacts_appt_id integer NOT NULL,
    bristo_contacts_appt_ct_id integer NOT NULL,
    bristo_contacts_appt_stamp timestamp with time zone DEFAULT now() NOT NULL,
    bristo_contacts_appt_time timestamp with time zone NOT NULL,
    bristo_contacts_appt_complete boolean DEFAULT false NOT NULL,
    bristo_contacts_appt_purpose text COLLATE pg_catalog."en_US.utf8" DEFAULT 'General Meeting'::text NOT NULL,
    bristo_contacts_appt_owner text DEFAULT 'jacksonkirka '::text NOT NULL
);


ALTER TABLE bristo_contacts_appt OWNER TO admin;

--
-- TOC entry 3010 (class 0 OID 0)
-- Dependencies: 177
-- Name: TABLE bristo_contacts_appt; Type: COMMENT; Schema: public; Owner: admin
--

COMMENT ON TABLE bristo_contacts_appt IS 'Appointments and Meetings';


--
-- TOC entry 178 (class 1259 OID 16413)
-- Name: bristo_contacts_appt_bristo_contacts_appt_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE bristo_contacts_appt_bristo_contacts_appt_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE bristo_contacts_appt_bristo_contacts_appt_id_seq OWNER TO admin;

--
-- TOC entry 3012 (class 0 OID 0)
-- Dependencies: 178
-- Name: bristo_contacts_appt_bristo_contacts_appt_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE bristo_contacts_appt_bristo_contacts_appt_id_seq OWNED BY bristo_contacts_appt.bristo_contacts_appt_id;


--
-- TOC entry 190 (class 1259 OID 16603)
-- Name: bristo_contacts_authlog; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE bristo_contacts_authlog (
    bristo_contacts_authlog_id integer NOT NULL,
    bristo_contacts_authlog_stamp timestamp with time zone DEFAULT now() NOT NULL,
    bristo_contacts_authlog_uname text COLLATE pg_catalog."en_US.utf8" NOT NULL,
    bristo_contacts_authlog_in boolean NOT NULL,
    bristo_contacts_authlog_uuid uuid DEFAULT uuid_generate_v4() NOT NULL,
    bristo_contacts_authlog_group boolean NOT NULL,
    bristo_contacts_authlog_grpname text COLLATE pg_catalog."en_US.utf8",
    bristo_contacts_authlog_inet inet DEFAULT inet_client_addr() NOT NULL,
    bristo_contacts_authlog_city text COLLATE pg_catalog."en_US.utf8" NOT NULL,
    bristo_contacts_authlog_region text COLLATE pg_catalog."en_US.utf8" NOT NULL,
    bristo_contacts_authlog_ctry text COLLATE pg_catalog."en_US.utf8" NOT NULL,
    bristo_contacts_authlog_postal text COLLATE pg_catalog."en_US.utf8" NOT NULL,
    bristo_contacts_authlog_success boolean DEFAULT false NOT NULL
);


ALTER TABLE bristo_contacts_authlog OWNER TO admin;

--
-- TOC entry 3014 (class 0 OID 0)
-- Dependencies: 190
-- Name: TABLE bristo_contacts_authlog; Type: COMMENT; Schema: public; Owner: admin
--

COMMENT ON TABLE bristo_contacts_authlog IS 'Authentication Log';


--
-- TOC entry 3015 (class 0 OID 0)
-- Dependencies: 190
-- Name: COLUMN bristo_contacts_authlog.bristo_contacts_authlog_success; Type: COMMENT; Schema: public; Owner: admin
--

COMMENT ON COLUMN bristo_contacts_authlog.bristo_contacts_authlog_success IS 'Login Success';


--
-- TOC entry 189 (class 1259 OID 16601)
-- Name: bristo_contacts_authlog_bristo_contacts_authlog_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE bristo_contacts_authlog_bristo_contacts_authlog_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE bristo_contacts_authlog_bristo_contacts_authlog_id_seq OWNER TO admin;

--
-- TOC entry 3017 (class 0 OID 0)
-- Dependencies: 189
-- Name: bristo_contacts_authlog_bristo_contacts_authlog_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE bristo_contacts_authlog_bristo_contacts_authlog_id_seq OWNED BY bristo_contacts_authlog.bristo_contacts_authlog_id;


--
-- TOC entry 179 (class 1259 OID 16415)
-- Name: bristo_contacts_calls; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE bristo_contacts_calls (
    bristo_contacts_calls_id integer NOT NULL,
    bristo_contacts_calls_ct_id integer NOT NULL,
    bristo_contacts_calls_stamp timestamp with time zone DEFAULT now() NOT NULL,
    bristo_contacts_calls_phone text COLLATE pg_catalog."en_US.utf8" NOT NULL,
    bristo_contacts_calls_type boolean DEFAULT false NOT NULL,
    bristo_contacts_calls_results text COLLATE pg_catalog."en_US.utf8" DEFAULT 'Left Message'::text NOT NULL,
    bristo_contacts_calls_appt_id integer,
    bristo_contacts_calls_owner text DEFAULT 'jacksonkirka '::text NOT NULL
);


ALTER TABLE bristo_contacts_calls OWNER TO admin;

--
-- TOC entry 3019 (class 0 OID 0)
-- Dependencies: 179
-- Name: TABLE bristo_contacts_calls; Type: COMMENT; Schema: public; Owner: admin
--

COMMENT ON TABLE bristo_contacts_calls IS 'Telephone Calls';


--
-- TOC entry 180 (class 1259 OID 16425)
-- Name: bristo_contacts_calls_bristo_contacts_calls_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE bristo_contacts_calls_bristo_contacts_calls_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE bristo_contacts_calls_bristo_contacts_calls_id_seq OWNER TO admin;

--
-- TOC entry 3021 (class 0 OID 0)
-- Dependencies: 180
-- Name: bristo_contacts_calls_bristo_contacts_calls_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE bristo_contacts_calls_bristo_contacts_calls_id_seq OWNED BY bristo_contacts_calls.bristo_contacts_calls_id;


--
-- TOC entry 181 (class 1259 OID 16427)
-- Name: bristo_contacts_files; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE bristo_contacts_files (
    bristo_contacts_files_id integer NOT NULL,
    bristo_contacts_files_stamp timestamp with time zone DEFAULT now() NOT NULL,
    bristo_contacts_files_ct text COLLATE pg_catalog."en_US.utf8" NOT NULL,
    bristo_contacts_files_name text COLLATE pg_catalog."en_US.utf8" NOT NULL,
    bristo_contacts_files_file bytea NOT NULL,
    bristo_contacts_files_appt_id integer,
    bristo_contacts_files_owner text DEFAULT 'jacksonkirka '::text NOT NULL
);


ALTER TABLE bristo_contacts_files OWNER TO admin;

--
-- TOC entry 3023 (class 0 OID 0)
-- Dependencies: 181
-- Name: TABLE bristo_contacts_files; Type: COMMENT; Schema: public; Owner: admin
--

COMMENT ON TABLE bristo_contacts_files IS 'Files';


--
-- TOC entry 182 (class 1259 OID 16435)
-- Name: bristo_contacts_file_bristo_contacts_file_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE bristo_contacts_file_bristo_contacts_file_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE bristo_contacts_file_bristo_contacts_file_id_seq OWNER TO admin;

--
-- TOC entry 3025 (class 0 OID 0)
-- Dependencies: 182
-- Name: bristo_contacts_file_bristo_contacts_file_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE bristo_contacts_file_bristo_contacts_file_id_seq OWNED BY bristo_contacts_files.bristo_contacts_files_id;


--
-- TOC entry 188 (class 1259 OID 16544)
-- Name: bristo_contacts_groups; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE bristo_contacts_groups (
    bristo_contacts_groups_id integer NOT NULL,
    bristo_contacts_groups_stamp timestamp with time zone DEFAULT now() NOT NULL,
    bristo_contacts_groups_group text COLLATE pg_catalog."en_US.utf8" NOT NULL,
    bristo_contacts_groups_owner text NOT NULL,
    bristo_contacts_groups_pwd text COLLATE pg_catalog."en_US.utf8" NOT NULL,
    bristo_contacts_groups_desc text,
    bristo_contacts_groups_pic bytea,
    bristo_contacts_groups_addr1 text,
    bristo_contacts_groups_addr2 text,
    bristo_contacts_groups_city text,
    bristo_contacts_groups_state text,
    bristo_contacts_groups_postal text,
    bristo_contacts_groups_web1 text,
    bristo_contacts_groups_web2 text,
    bristo_contacts_groups_phone text,
    bristo_contacts_groups_fax text
);


ALTER TABLE bristo_contacts_groups OWNER TO admin;

--
-- TOC entry 3027 (class 0 OID 0)
-- Dependencies: 188
-- Name: TABLE bristo_contacts_groups; Type: COMMENT; Schema: public; Owner: admin
--

COMMENT ON TABLE bristo_contacts_groups IS 'Groups';


--
-- TOC entry 187 (class 1259 OID 16542)
-- Name: bristo_contacts_groups_bristo_contacts_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE bristo_contacts_groups_bristo_contacts_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE bristo_contacts_groups_bristo_contacts_groups_id_seq OWNER TO admin;

--
-- TOC entry 3029 (class 0 OID 0)
-- Dependencies: 187
-- Name: bristo_contacts_groups_bristo_contacts_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE bristo_contacts_groups_bristo_contacts_groups_id_seq OWNED BY bristo_contacts_groups.bristo_contacts_groups_id;


--
-- TOC entry 183 (class 1259 OID 16437)
-- Name: bristo_contacts_notes; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE bristo_contacts_notes (
    bristo_contacts_notes_id integer NOT NULL,
    bristo_contacts_notes_stamp timestamp with time zone DEFAULT now() NOT NULL,
    bristo_contacts_notes_ct text NOT NULL,
    bristo_contacts_notes_note text,
    bristo_contacts_notes_appt_id integer,
    bristo_contacts_notes_owner text DEFAULT 'jacksonkirka '::text NOT NULL
);
ALTER TABLE ONLY bristo_contacts_notes ALTER COLUMN bristo_contacts_notes_ct SET STORAGE PLAIN;


ALTER TABLE bristo_contacts_notes OWNER TO admin;

--
-- TOC entry 3031 (class 0 OID 0)
-- Dependencies: 183
-- Name: TABLE bristo_contacts_notes; Type: COMMENT; Schema: public; Owner: admin
--

COMMENT ON TABLE bristo_contacts_notes IS 'Notes';


--
-- TOC entry 184 (class 1259 OID 16445)
-- Name: bristo_contacts_notes_bristo_contacts_notes_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE bristo_contacts_notes_bristo_contacts_notes_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE bristo_contacts_notes_bristo_contacts_notes_id_seq OWNER TO admin;

--
-- TOC entry 3033 (class 0 OID 0)
-- Dependencies: 184
-- Name: bristo_contacts_notes_bristo_contacts_notes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE bristo_contacts_notes_bristo_contacts_notes_id_seq OWNED BY bristo_contacts_notes.bristo_contacts_notes_id;


--
-- TOC entry 185 (class 1259 OID 16447)
-- Name: bristo_contacts_users; Type: TABLE; Schema: public; Owner: admin
--

CREATE TABLE bristo_contacts_users (
    bristo_contacts_users_id integer NOT NULL,
    bristo_contacts_users_name text COLLATE pg_catalog."en_US.utf8" NOT NULL,
    bristo_contacts_users_email text COLLATE pg_catalog."en_US.utf8" NOT NULL,
    bristo_contacts_users_webmail text COLLATE pg_catalog."en_US.utf8" DEFAULT 'https://mail.google.com/mail/u/0/#search/'::text NOT NULL,
    bristo_contacts_users_pwd text COLLATE pg_catalog."en_US.utf8" DEFAULT 'fd158ad01731e26682c7f11e48aa70ed50c3baac8809aaf50f5c19854206e91a:51b1c01c9a8e4c4da1005928b2ef5710'::text NOT NULL,
    bristo_contacts_users_stamp timestamp with time zone DEFAULT now() NOT NULL,
    bristo_contacts_users_expires date
);


ALTER TABLE bristo_contacts_users OWNER TO admin;

--
-- TOC entry 3035 (class 0 OID 0)
-- Dependencies: 185
-- Name: TABLE bristo_contacts_users; Type: COMMENT; Schema: public; Owner: admin
--

COMMENT ON TABLE bristo_contacts_users IS 'Users';


--
-- TOC entry 186 (class 1259 OID 16453)
-- Name: bristo_contacts_users_bristo_contacts_users_id_seq; Type: SEQUENCE; Schema: public; Owner: admin
--

CREATE SEQUENCE bristo_contacts_users_bristo_contacts_users_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE bristo_contacts_users_bristo_contacts_users_id_seq OWNER TO admin;

--
-- TOC entry 3037 (class 0 OID 0)
-- Dependencies: 186
-- Name: bristo_contacts_users_bristo_contacts_users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: admin
--

ALTER SEQUENCE bristo_contacts_users_bristo_contacts_users_id_seq OWNED BY bristo_contacts_users.bristo_contacts_users_id;


--
-- TOC entry 2823 (class 2604 OID 16455)
-- Name: bristo_contacts_appt_id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY bristo_contacts_appt ALTER COLUMN bristo_contacts_appt_id SET DEFAULT nextval('bristo_contacts_appt_bristo_contacts_appt_id_seq'::regclass);


--
-- TOC entry 2841 (class 2604 OID 16606)
-- Name: bristo_contacts_authlog_id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY bristo_contacts_authlog ALTER COLUMN bristo_contacts_authlog_id SET DEFAULT nextval('bristo_contacts_authlog_bristo_contacts_authlog_id_seq'::regclass);


--
-- TOC entry 2828 (class 2604 OID 16456)
-- Name: bristo_contacts_calls_id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY bristo_contacts_calls ALTER COLUMN bristo_contacts_calls_id SET DEFAULT nextval('bristo_contacts_calls_bristo_contacts_calls_id_seq'::regclass);


--
-- TOC entry 2817 (class 2604 OID 16457)
-- Name: bristo_contacts_ct_id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY bristo_contacts_ct ALTER COLUMN bristo_contacts_ct_id SET DEFAULT nextval('bristo_constacts_ct_bristo_contacts_ct_id_seq'::regclass);


--
-- TOC entry 2831 (class 2604 OID 16458)
-- Name: bristo_contacts_files_id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY bristo_contacts_files ALTER COLUMN bristo_contacts_files_id SET DEFAULT nextval('bristo_contacts_file_bristo_contacts_file_id_seq'::regclass);


--
-- TOC entry 2839 (class 2604 OID 16547)
-- Name: bristo_contacts_groups_id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY bristo_contacts_groups ALTER COLUMN bristo_contacts_groups_id SET DEFAULT nextval('bristo_contacts_groups_bristo_contacts_groups_id_seq'::regclass);


--
-- TOC entry 2834 (class 2604 OID 16459)
-- Name: bristo_contacts_notes_id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY bristo_contacts_notes ALTER COLUMN bristo_contacts_notes_id SET DEFAULT nextval('bristo_contacts_notes_bristo_contacts_notes_id_seq'::regclass);


--
-- TOC entry 2835 (class 2604 OID 16460)
-- Name: bristo_contacts_users_id; Type: DEFAULT; Schema: public; Owner: admin
--

ALTER TABLE ONLY bristo_contacts_users ALTER COLUMN bristo_contacts_users_id SET DEFAULT nextval('bristo_contacts_users_bristo_contacts_users_id_seq'::regclass);


--
-- TOC entry 2856 (class 2606 OID 16497)
-- Name: bristo_contacts_appt_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY bristo_contacts_appt
    ADD CONSTRAINT bristo_contacts_appt_pkey PRIMARY KEY (bristo_contacts_appt_id);


--
-- TOC entry 2881 (class 2606 OID 16609)
-- Name: bristo_contacts_authlog_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY bristo_contacts_authlog
    ADD CONSTRAINT bristo_contacts_authlog_pkey PRIMARY KEY (bristo_contacts_authlog_id);


--
-- TOC entry 2859 (class 2606 OID 16499)
-- Name: bristo_contacts_calls_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY bristo_contacts_calls
    ADD CONSTRAINT bristo_contacts_calls_pkey PRIMARY KEY (bristo_contacts_calls_id);


--
-- TOC entry 2848 (class 2606 OID 16501)
-- Name: bristo_contacts_ct_id_unq; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY bristo_contacts_ct
    ADD CONSTRAINT bristo_contacts_ct_id_unq UNIQUE (bristo_contacts_ct_id);


--
-- TOC entry 2851 (class 2606 OID 16503)
-- Name: bristo_contacts_ct_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY bristo_contacts_ct
    ADD CONSTRAINT bristo_contacts_ct_pkey PRIMARY KEY (bristo_contacts_ct_ph_office);


--
-- TOC entry 2862 (class 2606 OID 16505)
-- Name: bristo_contacts_file_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY bristo_contacts_files
    ADD CONSTRAINT bristo_contacts_file_pkey PRIMARY KEY (bristo_contacts_files_id);


--
-- TOC entry 2876 (class 2606 OID 16980)
-- Name: bristo_contacts_gourps_unq; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY bristo_contacts_groups
    ADD CONSTRAINT bristo_contacts_gourps_unq UNIQUE (bristo_contacts_groups_group);


--
-- TOC entry 2879 (class 2606 OID 16553)
-- Name: bristo_contacts_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY bristo_contacts_groups
    ADD CONSTRAINT bristo_contacts_groups_pkey PRIMARY KEY (bristo_contacts_groups_id);


--
-- TOC entry 2867 (class 2606 OID 16507)
-- Name: bristo_contacts_notes_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY bristo_contacts_notes
    ADD CONSTRAINT bristo_contacts_notes_pkey PRIMARY KEY (bristo_contacts_notes_id);


--
-- TOC entry 2869 (class 2606 OID 18000)
-- Name: bristo_contacts_users_email_unq; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY bristo_contacts_users
    ADD CONSTRAINT bristo_contacts_users_email_unq UNIQUE (bristo_contacts_users_email);


--
-- TOC entry 2872 (class 2606 OID 17995)
-- Name: bristo_contacts_users_name_unq; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY bristo_contacts_users
    ADD CONSTRAINT bristo_contacts_users_name_unq UNIQUE (bristo_contacts_users_name);


--
-- TOC entry 2874 (class 2606 OID 16509)
-- Name: bristo_contacts_users_pkey; Type: CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY bristo_contacts_users
    ADD CONSTRAINT bristo_contacts_users_pkey PRIMARY KEY (bristo_contacts_users_id);


--
-- TOC entry 2854 (class 1259 OID 16510)
-- Name: bristo_contacts_appt_owner_idx; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX bristo_contacts_appt_owner_idx ON bristo_contacts_appt USING btree (bristo_contacts_appt_owner);


--
-- TOC entry 2857 (class 1259 OID 16511)
-- Name: bristo_contacts_calls_owner_idx; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX bristo_contacts_calls_owner_idx ON bristo_contacts_calls USING btree (bristo_contacts_calls_owner);


--
-- TOC entry 2860 (class 1259 OID 16512)
-- Name: bristo_contacts_calls_results_idx; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX bristo_contacts_calls_results_idx ON bristo_contacts_calls USING btree (bristo_contacts_calls_results text_pattern_ops);


--
-- TOC entry 2846 (class 1259 OID 16513)
-- Name: bristo_contacts_ct_co_idx; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX bristo_contacts_ct_co_idx ON bristo_contacts_ct USING btree (bristo_contacts_ct_co COLLATE "en_US.utf8" text_pattern_ops);


--
-- TOC entry 2849 (class 1259 OID 16514)
-- Name: bristo_contacts_ct_owner_idx; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX bristo_contacts_ct_owner_idx ON bristo_contacts_ct USING btree (bristo_contacts_ct_owner);


--
-- TOC entry 2852 (class 1259 OID 16515)
-- Name: bristo_contacts_email1_idx; Type: INDEX; Schema: public; Owner: admin
--

CREATE UNIQUE INDEX bristo_contacts_email1_idx ON bristo_contacts_ct USING btree (bristo_contacts_ct_email1 COLLATE "en_US.utf8" text_pattern_ops);


--
-- TOC entry 2863 (class 1259 OID 16516)
-- Name: bristo_contacts_files_name_idx; Type: INDEX; Schema: public; Owner: admin
--

CREATE UNIQUE INDEX bristo_contacts_files_name_idx ON bristo_contacts_files USING btree (bristo_contacts_files_name text_pattern_ops);


--
-- TOC entry 2864 (class 1259 OID 16517)
-- Name: bristo_contacts_files_owner; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX bristo_contacts_files_owner ON bristo_contacts_files USING btree (bristo_contacts_files_owner);


--
-- TOC entry 2853 (class 1259 OID 16518)
-- Name: bristo_contacts_full_name_idx; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX bristo_contacts_full_name_idx ON bristo_contacts_ct USING btree (bristo_contacts_ct_fname COLLATE "en_US.utf8" text_pattern_ops, bristo_contacts_ct_middle COLLATE "en_US.utf8" text_pattern_ops, bristo_contacts_ct_lname COLLATE "en_US.utf8" text_pattern_ops);


--
-- TOC entry 2877 (class 1259 OID 16554)
-- Name: bristo_contacts_groups_idx; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX bristo_contacts_groups_idx ON bristo_contacts_groups USING btree (bristo_contacts_groups_group text_pattern_ops);


--
-- TOC entry 2865 (class 1259 OID 16519)
-- Name: bristo_contacts_notes_idx; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX bristo_contacts_notes_idx ON bristo_contacts_notes USING btree (bristo_contacts_notes_owner);


--
-- TOC entry 2870 (class 1259 OID 16520)
-- Name: bristo_contacts_users_idx; Type: INDEX; Schema: public; Owner: admin
--

CREATE INDEX bristo_contacts_users_idx ON bristo_contacts_users USING btree (bristo_contacts_users_email text_pattern_ops);


--
-- TOC entry 2882 (class 2606 OID 16521)
-- Name: bristo_contacts_appt_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY bristo_contacts_appt
    ADD CONSTRAINT bristo_contacts_appt_fkey FOREIGN KEY (bristo_contacts_appt_ct_id) REFERENCES bristo_contacts_ct(bristo_contacts_ct_id) MATCH FULL;


--
-- TOC entry 2883 (class 2606 OID 16526)
-- Name: bristo_contacts_calls_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY bristo_contacts_calls
    ADD CONSTRAINT bristo_contacts_calls_fkey FOREIGN KEY (bristo_contacts_calls_ct_id) REFERENCES bristo_contacts_ct(bristo_contacts_ct_id) MATCH FULL;


--
-- TOC entry 2884 (class 2606 OID 16531)
-- Name: bristo_contacts_file_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY bristo_contacts_files
    ADD CONSTRAINT bristo_contacts_file_fkey FOREIGN KEY (bristo_contacts_files_ct) REFERENCES bristo_contacts_ct(bristo_contacts_ct_ph_office) MATCH FULL;


--
-- TOC entry 2885 (class 2606 OID 16536)
-- Name: bristo_contacts_notes_fkey; Type: FK CONSTRAINT; Schema: public; Owner: admin
--

ALTER TABLE ONLY bristo_contacts_notes
    ADD CONSTRAINT bristo_contacts_notes_fkey FOREIGN KEY (bristo_contacts_notes_ct) REFERENCES bristo_contacts_ct(bristo_contacts_ct_ph_office);


--
-- TOC entry 3002 (class 0 OID 0)
-- Dependencies: 8
-- Name: public; Type: ACL; Schema: -; Owner: focker
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM focker;
GRANT ALL ON SCHEMA public TO focker;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- TOC entry 3007 (class 0 OID 0)
-- Dependencies: 175
-- Name: bristo_contacts_ct; Type: ACL; Schema: public; Owner: admin
--

REVOKE ALL ON TABLE bristo_contacts_ct FROM PUBLIC;
REVOKE ALL ON TABLE bristo_contacts_ct FROM admin;
GRANT ALL ON TABLE bristo_contacts_ct TO admin;
GRANT SELECT,INSERT,UPDATE ON TABLE bristo_contacts_ct TO bristousers;


--
-- TOC entry 3009 (class 0 OID 0)
-- Dependencies: 176
-- Name: bristo_constacts_ct_bristo_contacts_ct_id_seq; Type: ACL; Schema: public; Owner: admin
--

REVOKE ALL ON SEQUENCE bristo_constacts_ct_bristo_contacts_ct_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE bristo_constacts_ct_bristo_contacts_ct_id_seq FROM admin;
GRANT ALL ON SEQUENCE bristo_constacts_ct_bristo_contacts_ct_id_seq TO admin;
GRANT SELECT,UPDATE ON SEQUENCE bristo_constacts_ct_bristo_contacts_ct_id_seq TO bristousers;


--
-- TOC entry 3011 (class 0 OID 0)
-- Dependencies: 177
-- Name: bristo_contacts_appt; Type: ACL; Schema: public; Owner: admin
--

REVOKE ALL ON TABLE bristo_contacts_appt FROM PUBLIC;
REVOKE ALL ON TABLE bristo_contacts_appt FROM admin;
GRANT ALL ON TABLE bristo_contacts_appt TO admin;
GRANT SELECT,INSERT,UPDATE ON TABLE bristo_contacts_appt TO bristousers;


--
-- TOC entry 3013 (class 0 OID 0)
-- Dependencies: 178
-- Name: bristo_contacts_appt_bristo_contacts_appt_id_seq; Type: ACL; Schema: public; Owner: admin
--

REVOKE ALL ON SEQUENCE bristo_contacts_appt_bristo_contacts_appt_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE bristo_contacts_appt_bristo_contacts_appt_id_seq FROM admin;
GRANT ALL ON SEQUENCE bristo_contacts_appt_bristo_contacts_appt_id_seq TO admin;
GRANT SELECT,UPDATE ON SEQUENCE bristo_contacts_appt_bristo_contacts_appt_id_seq TO bristousers;


--
-- TOC entry 3016 (class 0 OID 0)
-- Dependencies: 190
-- Name: bristo_contacts_authlog; Type: ACL; Schema: public; Owner: admin
--

REVOKE ALL ON TABLE bristo_contacts_authlog FROM PUBLIC;
REVOKE ALL ON TABLE bristo_contacts_authlog FROM admin;
GRANT ALL ON TABLE bristo_contacts_authlog TO admin;
GRANT SELECT,INSERT,UPDATE ON TABLE bristo_contacts_authlog TO bristousers;


--
-- TOC entry 3018 (class 0 OID 0)
-- Dependencies: 189
-- Name: bristo_contacts_authlog_bristo_contacts_authlog_id_seq; Type: ACL; Schema: public; Owner: admin
--

REVOKE ALL ON SEQUENCE bristo_contacts_authlog_bristo_contacts_authlog_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE bristo_contacts_authlog_bristo_contacts_authlog_id_seq FROM admin;
GRANT ALL ON SEQUENCE bristo_contacts_authlog_bristo_contacts_authlog_id_seq TO admin;
GRANT SELECT,UPDATE ON SEQUENCE bristo_contacts_authlog_bristo_contacts_authlog_id_seq TO bristousers;


--
-- TOC entry 3020 (class 0 OID 0)
-- Dependencies: 179
-- Name: bristo_contacts_calls; Type: ACL; Schema: public; Owner: admin
--

REVOKE ALL ON TABLE bristo_contacts_calls FROM PUBLIC;
REVOKE ALL ON TABLE bristo_contacts_calls FROM admin;
GRANT ALL ON TABLE bristo_contacts_calls TO admin;
GRANT SELECT,INSERT,UPDATE ON TABLE bristo_contacts_calls TO bristousers;


--
-- TOC entry 3022 (class 0 OID 0)
-- Dependencies: 180
-- Name: bristo_contacts_calls_bristo_contacts_calls_id_seq; Type: ACL; Schema: public; Owner: admin
--

REVOKE ALL ON SEQUENCE bristo_contacts_calls_bristo_contacts_calls_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE bristo_contacts_calls_bristo_contacts_calls_id_seq FROM admin;
GRANT ALL ON SEQUENCE bristo_contacts_calls_bristo_contacts_calls_id_seq TO admin;
GRANT SELECT,UPDATE ON SEQUENCE bristo_contacts_calls_bristo_contacts_calls_id_seq TO bristousers;


--
-- TOC entry 3024 (class 0 OID 0)
-- Dependencies: 181
-- Name: bristo_contacts_files; Type: ACL; Schema: public; Owner: admin
--

REVOKE ALL ON TABLE bristo_contacts_files FROM PUBLIC;
REVOKE ALL ON TABLE bristo_contacts_files FROM admin;
GRANT ALL ON TABLE bristo_contacts_files TO admin;
GRANT SELECT,INSERT,UPDATE ON TABLE bristo_contacts_files TO bristousers;


--
-- TOC entry 3026 (class 0 OID 0)
-- Dependencies: 182
-- Name: bristo_contacts_file_bristo_contacts_file_id_seq; Type: ACL; Schema: public; Owner: admin
--

REVOKE ALL ON SEQUENCE bristo_contacts_file_bristo_contacts_file_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE bristo_contacts_file_bristo_contacts_file_id_seq FROM admin;
GRANT ALL ON SEQUENCE bristo_contacts_file_bristo_contacts_file_id_seq TO admin;
GRANT SELECT,UPDATE ON SEQUENCE bristo_contacts_file_bristo_contacts_file_id_seq TO bristousers;


--
-- TOC entry 3028 (class 0 OID 0)
-- Dependencies: 188
-- Name: bristo_contacts_groups; Type: ACL; Schema: public; Owner: admin
--

REVOKE ALL ON TABLE bristo_contacts_groups FROM PUBLIC;
REVOKE ALL ON TABLE bristo_contacts_groups FROM admin;
GRANT ALL ON TABLE bristo_contacts_groups TO admin;
GRANT SELECT,INSERT,UPDATE ON TABLE bristo_contacts_groups TO bristousers;


--
-- TOC entry 3030 (class 0 OID 0)
-- Dependencies: 187
-- Name: bristo_contacts_groups_bristo_contacts_groups_id_seq; Type: ACL; Schema: public; Owner: admin
--

REVOKE ALL ON SEQUENCE bristo_contacts_groups_bristo_contacts_groups_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE bristo_contacts_groups_bristo_contacts_groups_id_seq FROM admin;
GRANT ALL ON SEQUENCE bristo_contacts_groups_bristo_contacts_groups_id_seq TO admin;
GRANT SELECT,UPDATE ON SEQUENCE bristo_contacts_groups_bristo_contacts_groups_id_seq TO bristousers;


--
-- TOC entry 3032 (class 0 OID 0)
-- Dependencies: 183
-- Name: bristo_contacts_notes; Type: ACL; Schema: public; Owner: admin
--

REVOKE ALL ON TABLE bristo_contacts_notes FROM PUBLIC;
REVOKE ALL ON TABLE bristo_contacts_notes FROM admin;
GRANT ALL ON TABLE bristo_contacts_notes TO admin;
GRANT SELECT,INSERT,UPDATE ON TABLE bristo_contacts_notes TO bristousers;


--
-- TOC entry 3034 (class 0 OID 0)
-- Dependencies: 184
-- Name: bristo_contacts_notes_bristo_contacts_notes_id_seq; Type: ACL; Schema: public; Owner: admin
--

REVOKE ALL ON SEQUENCE bristo_contacts_notes_bristo_contacts_notes_id_seq FROM PUBLIC;
REVOKE ALL ON SEQUENCE bristo_contacts_notes_bristo_contacts_notes_id_seq FROM admin;
GRANT ALL ON SEQUENCE bristo_contacts_notes_bristo_contacts_notes_id_seq TO admin;
GRANT SELECT,UPDATE ON SEQUENCE bristo_contacts_notes_bristo_contacts_notes_id_seq TO bristousers;


--
-- TOC entry 3036 (class 0 OID 0)
-- Dependencies: 185
-- Name: bristo_contacts_users; Type: ACL; Schema: public; Owner: admin
--

REVOKE ALL ON TABLE bristo_contacts_users FROM PUBLIC;
REVOKE ALL ON TABLE bristo_contacts_users FROM admin;
GRANT ALL ON TABLE bristo_contacts_users TO admin;
GRANT SELECT ON TABLE bristo_contacts_users TO bristousers;


-- Completed on 2016-08-29 11:24:27 EDT

--
-- PostgreSQL database dump complete
--
