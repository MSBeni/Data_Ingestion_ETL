## Sample Queries:

```sql
-- SET SERVEROUTPUT ON;
DECLARE
    V_DATE TIMESTAMP WITH TIME ZONE NOT NULL := SYSTIMESTAMP;
BEGIN
    DBMS_OUTPUT.PUT_LINE(V_DATE || ' Beginner to Advanced ...');
END;

-- SET SERVEROUTPUT ON;
DECLARE
    V_DATE INTERVAL DAY(4) TO SECOND(2) := '24 02:05:21.012';
BEGIN
    DBMS_OUTPUT.PUT_LINE(V_DATE || ' Beginner to Advanced ...');
END;
```


## Declaring & Initializing & Using Variables (Code Samples)
-----------------------===================-----------------------
-----------------------DECLARING VARIABLES-----------------------
-----------------------===================-----------------------
```sql
SET SERVEROUTPUT ON;
DECLARE 
    v varchar2(20) := 2 + 25 * 3;
BEGIN
    dbms_output.put_line(v);
END;
-----------------------===================-----------------------
DECLARE 
    v_text varchar2(50) NOT NULL DEFAULT 'Hello';
    v_number1 number := 50;
    v_number2 number(2) := 50.42;
    v_number3 number(10,2) := 50.42;
    v_number4 PLS_INTEGER := 50;
    v_number5 BINARY_float := 50.42;
    v_DATE1 DATE := '22-NOV-18 12:01:32';
    v_DATE2 timestamp := systimestamp;
    v_DATE3 timestamp(9) WITH TIME ZONE := systimestamp;
    v_DATE4 interval day(4) to second (3) := '124 02:05:21.012 ';
    v_DATE5 interval year to month := '12-3';
BEGIN
    V_TEXT := 'PL/SQL' || 'Course';
    DBMS_OUTPUT.PUT_LINE(V_TEXT);
    DBMS_OUTPUT.PUT_LINE(v_number1);
    DBMS_OUTPUT.PUT_LINE(v_number2);
    DBMS_OUTPUT.PUT_LINE(v_number3);
    DBMS_OUTPUT.PUT_LINE(v_number4);
    DBMS_OUTPUT.PUT_LINE(v_number5);
    DBMS_OUTPUT.PUT_LINE(v_DATE1);
    DBMS_OUTPUT.PUT_LINE(v_DATE2);
    DBMS_OUTPUT.PUT_LINE(v_DATE3);
    DBMS_OUTPUT.PUT_LINE(v_DATE4);
    DBMS_OUTPUT.PUT_LINE(v_DATE5);
    END;
```
----------------==================================---------------
----------------USING BOOLEAN DATA TYPE in PL/SQL----------------
----------------==================================---------------
```sql
DECLARE
    v_boolean boolean := true;
BEGIN
    dbms_output.put_line(sys.diutil.bool_to_int(v_boolean));
END;
```
----------------==================================---------------

# SHOWING TABLE SCHEMA
```
DESC HR.EMPLOYEES;
```


## Using %Type Attribute (Code Samples)
---------------------%TYPE ATTRIBUTE---------------------
```sql
desc employees;
declare
V_TYPE employees.JOB_ID%TYPE;
V_TYPE2 V_TYPE%TYPE;
V_TYPE3 employees.JOB_ID%TYPE ;
begin
v_type := 'IT_PROG';
v_type2 := 'SA_MAN';
v_type3 := NULL;
dbms_output.put_line(v_type);
dbms_output.put_line(v_type2);
dbms_output.put_line('HELLO' || v_type3);
end;
```
---------------------------------------------------------
---------------------------------------------------------
```SQL
-- DESC HR.EMPLOYEES;
DECLARE
    V_TYPE HR.EMPLOYEES.EMPLOYEE_ID%TYPE;
    V_TYPE2 V_TYPE%TYPE;
    V_TYPE3 HR.EMPLOYEES.JOB_ID%TYPE;
BEGIN
    V_TYPE := 123;
    V_TYPE2 := 25;
    V_TYPE3 := 'HUMAN';
    DBMS_OUTPUT.PUT_LINE(V_TYPE);
    DBMS_OUTPUT.PUT_LINE(V_TYPE2);
    DBMS_OUTPUT.PUT_LINE(V_TYPE3 ||  'yes!....');
END;
```
----------------==================================---------------

## PL/SQL Delimiters and Commenting (Code Samples)
------------------DELIMITERS AND COMMENTING------------------
```sql
DECLARE
V_TEXT VARCHAR2(10):= 'PL/SQL';
BEGIN
--This is a single line comment
/* This is a 
    multi line
    comment */
--DBMS_OUTPUT.PUT_LINE(V_TEXT || ' is a good language');
null;
END;
```
-------------------------------------------------------------

```sql
-- DESC HR.EMPLOYEES;
DECLARE
    V_TEXT VARCHAR(50) := 'OUTER-VAR';
    V_TEST HR.EMPLOYEES.FIRST_NAME%TYPE := 'HASAN';
BEGIN
    DECLARE
        INNER_TEXT VARCHAR(50) := 'INNER-VAR';
    BEGIN
        DBMS_OUTPUT.PUT_LINE(INNER_TEXT || ' INSIDE');
    END;
    DBMS_OUTPUT.PUT_LINE(V_TEXT || ' OUTSIDE');
    DBMS_OUTPUT.PUT_LINE(V_TEST || ' WITH TYPE FROM EMPLOYEES');
END;
```

```sql
BEGIN <<OUTER>>
DECLARE
    V_TEXT VARCHAR(50) := 'OUTER-VAR';
    V_TEST HR.EMPLOYEES.FIRST_NAME%TYPE := 'HASAN';
BEGIN
    DECLARE
        INNER_TEXT VARCHAR(50) := 'INNER-VAR';
    BEGIN
        DBMS_OUTPUT.PUT_LINE(INNER_TEXT || ' INSIDE');
        DBMS_OUTPUT.PUT_LINE(OUTER.V_TEXT || ' ENTERED FROM OUTSIDE TO INSIDE');
    END;
    DBMS_OUTPUT.PUT_LINE(V_TEXT || ' OUTSIDE');
    DBMS_OUTPUT.PUT_LINE(V_TEST || ' WITH TYPE FROM EMPLOYEES');
END;
END;
```

```sql
```