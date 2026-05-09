/* A Bison parser, made by GNU Bison 3.0.4.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015 Free Software Foundation, Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

#ifndef YY_YY_QUOTE_FMT_PARSE_H_INCLUDED
# define YY_YY_QUOTE_FMT_PARSE_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token type.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    SHOW_NEWSGROUPS = 258,
    SHOW_DATE = 259,
    SHOW_FROM = 260,
    SHOW_FULLNAME = 261,
    SHOW_FIRST_NAME = 262,
    SHOW_SENDER_INITIAL = 263,
    SHOW_SUBJECT = 264,
    SHOW_TO = 265,
    SHOW_MESSAGEID = 266,
    SHOW_PERCENT = 267,
    SHOW_CC = 268,
    SHOW_REFERENCES = 269,
    SHOW_MESSAGE = 270,
    SHOW_QUOTED_MESSAGE = 271,
    SHOW_BACKSLASH = 272,
    SHOW_TAB = 273,
    SHOW_QUOTED_MESSAGE_NO_SIGNATURE = 274,
    SHOW_MESSAGE_NO_SIGNATURE = 275,
    SHOW_EOL = 276,
    SHOW_QUESTION_MARK = 277,
    SHOW_OPARENT = 278,
    SHOW_CPARENT = 279,
    QUERY_DATE = 280,
    QUERY_FROM = 281,
    QUERY_FULLNAME = 282,
    QUERY_SUBJECT = 283,
    QUERY_TO = 284,
    QUERY_NEWSGROUPS = 285,
    QUERY_MESSAGEID = 286,
    QUERY_CC = 287,
    QUERY_REFERENCES = 288,
    OPARENT = 289,
    CPARENT = 290,
    CHARACTER = 291
  };
#endif
/* Tokens.  */
#define SHOW_NEWSGROUPS 258
#define SHOW_DATE 259
#define SHOW_FROM 260
#define SHOW_FULLNAME 261
#define SHOW_FIRST_NAME 262
#define SHOW_SENDER_INITIAL 263
#define SHOW_SUBJECT 264
#define SHOW_TO 265
#define SHOW_MESSAGEID 266
#define SHOW_PERCENT 267
#define SHOW_CC 268
#define SHOW_REFERENCES 269
#define SHOW_MESSAGE 270
#define SHOW_QUOTED_MESSAGE 271
#define SHOW_BACKSLASH 272
#define SHOW_TAB 273
#define SHOW_QUOTED_MESSAGE_NO_SIGNATURE 274
#define SHOW_MESSAGE_NO_SIGNATURE 275
#define SHOW_EOL 276
#define SHOW_QUESTION_MARK 277
#define SHOW_OPARENT 278
#define SHOW_CPARENT 279
#define QUERY_DATE 280
#define QUERY_FROM 281
#define QUERY_FULLNAME 282
#define QUERY_SUBJECT 283
#define QUERY_TO 284
#define QUERY_NEWSGROUPS 285
#define QUERY_MESSAGEID 286
#define QUERY_CC 287
#define QUERY_REFERENCES 288
#define OPARENT 289
#define CPARENT 290
#define CHARACTER 291

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED

union YYSTYPE
{
#line 129 "quote_fmt_parse.y" /* yacc.c:1909  */

	char chr;

#line 130 "quote_fmt_parse.h" /* yacc.c:1909  */
};

typedef union YYSTYPE YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;

int yyparse (void);

#endif /* !YY_YY_QUOTE_FMT_PARSE_H_INCLUDED  */
