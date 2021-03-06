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
----------------------------------------------------------------------------


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
----------------------------------------------------------------------------
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
----------------------------------------------------------------------------

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
----------------------------------------------------------------------------

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
----------------------------------------------------------------

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

## PL SQL Variable Scope (Code Samples)
------------------------VARIABLE SCOPE--------------------------
```sql
begin <<outer>>
DECLARE
  --v_outer VARCHAR2(50) := 'Outer Variable!';
  v_text  VARCHAR2(20) := 'Out-text';
BEGIN 
  DECLARE
    v_text  VARCHAR2(20) := 'In-text';
    v_inner VARCHAR2(30) := 'Inner Variable';
  BEGIN
    --dbms_output.put_line('inside -> ' || v_outer);
    --dbms_output.put_line('inside -> ' || v_inner);
      dbms_output.put_line('inner -> ' || v_text);
      dbms_output.put_line('outer -> ' || outer.v_text);
  END;
  --dbms_output.put_line('inside -> ' || v_inner);
  --dbms_output.put_line(v_outer);
  dbms_output.put_line(v_text);
END;
END outer;
```
----------------------------------------------------------------

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
----------------------------------------------------------------------------

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

----------------------------------------------------------------------------
## Using Bind Variables (Code Samples)
--------------------------BIND VARIABLES--------------------------
```sql
set serveroutput on;
set autoprint on;
/
variable var_text varchar2(30);
/
variable var_number NUMBER;
/
variable var_date DATE;
/
declare
v_text varchar2(30);
begin
:var_text := 'Hello SQL';
:var_number := 20;
v_text := :var_text;
--dbms_output.put_line(v_text);
--dbms_output.put_line(:var_text);
end;
/
print var_text;
/
variable var_sql number;
/
begin 
  :var_sql := 100;
end;
/
select * from employees where employee_id = :var_sql;
```
 
* NOTE: When you run a bind variable creation and select statement together, SQL Developer may return an error. But when you execute them separately, there will be no problem--------
------------------------------------------------------------------

## What are Control Structures & IF Statements (Code Samples)
------------------------------IF STATEMENTS--------------------------------

```sql
DECLARE NUM_N NUMBER := 50;
BEGIN 
    IF NUM_N > 40 THEN
        DBMS_OUTPUT.PUT_LINE(NUM_N || ' IS BIGGER THAN 50');
    ELSE
        DBMS_OUTPUT.PUT_LINE(NUM_N || ' IS SMALLER THAN 50');
    END IF;
END;
```
---------------------------------------------------------------------------
```sql
set serveroutput on;
declare
v_number number := 30;
begin
  if v_number < 10 then
    dbms_output.put_line('I am smaller than 10');
  elsif v_number < 20 then
    dbms_output.put_line('I am smaller than 20');
  elsif v_number < 30 then
    dbms_output.put_line('I am smaller than 30');
  else
    dbms_output.put_line('I am equal or greater than 30');
  end if;
end;
```
---------------------------------------------------------------------------
```sql
declare
v_number number := 5;
v_name varchar2(30) := 'Adam';
begin
  if v_number < 10 or v_name = 'Carol' then
    dbms_output.put_line('HI');
    dbms_output.put_line('I am smaller than 10');
  elsif v_number < 20 then
    dbms_output.put_line('I am smaller than 20');
  elsif v_number < 30 then
    dbms_output.put_line('I am smaller than 30');
  else
    if v_number is null then 
      dbms_output.put_line('The number is null..');
    else
      dbms_output.put_line('I am equal or greater than 30');
    end if;
  end if;
end;
```
---------------------------------------------------------------------------


## Case Expressions (Code Samples)
----------------------------CASE EXPRESSIONS--------------------------------
```sql
declare
  v_job_code varchar2(10) := 'SA_MAN';
  v_salary_increase number;
begin
  v_salary_increase := case v_job_code 
    when 'SA_MAN' then 0.2
    when 'SA_REP' then 0.3
    else 0
  end;
  dbms_output.put_line('Your salary increase is : '|| v_salary_increase);
end;
```
-------------------------SEARCHED CASE EXPRESSION----------------------------
```sql
declare
  v_job_code varchar2(10) := 'IT_PROG';
  v_department varchar2(10) := 'IT';
  v_salary_increase number;
begin
  v_salary_increase := case  
    when v_job_code = 'SA_MAN' then 0.2
    when v_department = 'IT' and v_job_code = 'IT_PROG' then 0.3
    else 0
  end;
  dbms_output.put_line('Your salary increase is : '|| v_salary_increase);
end;
```
---------------------------CASE STATEMENTS------------------------------------
```sql
declare
  v_job_code varchar2(10) := 'IT_PROG';
  v_department varchar2(10) := 'IT';
  v_salary_increase number;
begin
  case  
    when v_job_code = 'SA_MAN' then 
      v_salary_increase := 0.2;
      dbms_output.put_line('The salary increase for a Sales Manager is : '|| v_salary_increase);
    when v_department = 'IT' and v_job_code = 'IT_PROG' then 
      v_salary_increase := 0.2;
      dbms_output.put_line('The salary increase for a Sales Manager is : '|| v_salary_increase);
    else 
      v_salary_increase := 0;
      dbms_output.put_line('The salary increase for this job code is : '|| v_salary_increase);
  end CASE;
end;
```
-------------------------------------------------------------------------------
## Basic Loops (Code Samples)
-------------------------BASIC LOOPS--------------------------
```sql
declare
v_counter number(2) := 1;
begin
  loop
    dbms_output.put_line('My counter is : '|| v_counter);
    v_counter := v_counter + 1;
    --if v_counter = 10 then
    --  dbms_output.put_line('Now I reached : '|| v_counter);
    --  exit;
    --end if;
    exit when v_counter > 10;
  end loop;
end;
```
--------------------------------------------------------------
```sql
DECLARE NUM_N NUMBER := 50;
BEGIN 
    LOOP
        DBMS_OUTPUT.PUT_LINE(NUM_N || ' IS THE VALUE');
        NUM_N := NUM_N -1;
        IF NUM_N < 30 THEN
            EXIT;
        END IF;
    END LOOP;
END;
```
--------------------------------------------------------------
```sql
DECLARE NUM_N NUMBER := 50;
BEGIN 
    LOOP
        DBMS_OUTPUT.PUT_LINE(NUM_N || ' IS THE VALUE');
        NUM_N := NUM_N -1;
        EXIT WHEN NUM_N < 40;
    END LOOP;
END;
```
--------------------------------------------------------------

## While Loops (Code Samples)
```sql
------------------------------WHILE LOOPS-------------------------------
declare
v_counter number(2) := 1;
begin
  while v_counter <= 10 loop
    dbms_output.put_line('My counter is : '|| v_counter);
    v_counter := v_counter + 1;
   -- exit when v_counter > 3;
  end loop;
end;
```
-------------------------------------------------------------------------

```sql
DECLARE NUM_N NUMBER := 50;
BEGIN 
    WHILE NUM_N > 35 LOOP
        DBMS_OUTPUT.PUT_LINE(NUM_N || ' IS THE VALUE');
        NUM_N := NUM_N -1;
    END LOOP;
END;
```
-------------------------------------------------------------------------

## For Loops (Code Samples)
-----------------------------FOR LOOPS-----------------------------
```sql
begin
  for i in REVERSE 1..3 loop
    dbms_output.put_line('My counter is : '|| i);
  end loop;
end;
```
-------------------------------------------------------------------
```sql
DECLARE NUM_N NUMBER := 50;
BEGIN 
    FOR i IN
        0..10 LOOP
        DBMS_OUTPUT.PUT_LINE(i * 2);
    END LOOP;
END;
```
-------------------------------------------------------------------------
```sql
DECLARE NUM_N NUMBER := 50;
BEGIN 
    FOR i IN REVERSE
        0..10 LOOP
        DBMS_OUTPUT.PUT_LINE(i * 2);
    END LOOP;
END;
```


## Nested Loops & Loop Labeling (Code Samples)
-------------------------------NESTED LOOPS-----------------------------------
```sql
declare
 v_inner number := 1;
begin
 for v_outer in 1..5 loop
  dbms_output.put_line('My outer value is : ' || v_outer );
    v_inner := 1;
    loop
      v_inner := v_inner+1;
      dbms_output.put_line('  My inner value is : ' || v_inner );
      exit when v_inner*v_outer >= 15;
    end loop;
 end loop;
end;
```
--------------------------------------------------------------------------------
### NESTED LOOPS WITH LABELS
```sql
declare
 v_inner number := 1;
begin
<<outer_loop>>
 for v_outer in 1..5 loop
  dbms_output.put_line('My outer value is : ' || v_outer );
    v_inner := 1;
    <<inner_loop>>
    loop
      v_inner := v_inner+1;
      dbms_output.put_line('  My inner value is : ' || v_inner );
      exit outer_loop when v_inner*v_outer >= 16;
      exit when v_inner*v_outer >= 15;
    end loop inner_loop;
 end loop outer_loop;
end;
```
--------------------------------------------------------------------------------

## Continue Statement (Code Samples)
----------------------------CONTINUE STATEMENT----------------------------------
```sql
declare
 v_inner number := 1;
begin
 for v_outer in 1..10 loop
  dbms_output.put_line('My outer value is : ' || v_outer );
    v_inner := 1;
    while v_inner*v_outer < 15 loop
      v_inner := v_inner+1;
      continue when mod(v_inner*v_outer,3) = 0;
      dbms_output.put_line('  My inner value is : ' || v_inner );
    end loop;
 end loop;
end;
```
---------------------------------------------------------------------------------
```sql
declare
 v_inner number := 1;
begin
<<outer_loop>>
 for v_outer in 1..10 loop
  dbms_output.put_line('My outer value is : ' || v_outer );
    v_inner := 1;
    <<inner_loop>>
    loop
      v_inner := v_inner+1;
      continue outer_loop when v_inner = 10;
      dbms_output.put_line('  My inner value is : ' || v_inner );
    end loop inner_loop;
 end loop outer_loop;
end;
```
----------------------------------------------------------------------------------
```sql
DECLARE NUM_N NUMBER := 50;
BEGIN 
    FOR i IN REVERSE
        0..10 LOOP
        IF I=5 THEN
            CONTINUE;
        END IF;
        DBMS_OUTPUT.PUT_LINE(i * 2);
    END LOOP;
END;
```
--------------------------------------------------------------------------------
```sql
DECLARE NUM_N NUMBER := 50;
BEGIN 
    FOR i IN REVERSE
        0..10 LOOP
        CONTINUE WHEN (I=5 OR I=10);
        DBMS_OUTPUT.PUT_LINE(i * 2);
    END LOOP;
END;
```
--------------------------------------------------------------------------------
```sql
DECLARE NUM_N NUMBER := 50;
BEGIN 
    FOR i IN REVERSE
        0..10 LOOP
        CONTINUE WHEN (REMAINDER(I, 2)=0);
        DBMS_OUTPUT.PUT_LINE(i * 2);
    END LOOP;
END;
```
--------------------------------------------------------------------------------

## GOTO Statement (Code Samples)
------------------------------GOTO STATEMENT----------------------------------
```sql
DECLARE
  v_searched_number NUMBER := 22;
  v_is_prime boolean := true;
BEGIN
  FOR x in 2..v_searched_number-1 LOOP
    IF v_searched_number MOD x = 0 THEN
      dbms_output.put_line(v_searched_number|| ' is not a prime number..');
      v_is_prime := false;
      GOTO end_point;
    END IF;
  END LOOP;
  if v_is_prime then
    dbms_output.put_line(v_searched_number|| ' is a prime number..');
  end if;
<<end_point>>
  dbms_output.put_line('Check complete..');
END;
```
-------------------------------------------------------------------------------
```sql
DECLARE
  v_searched_number NUMBER := 32457;
  v_is_prime boolean := true;
  x number := 2;
BEGIN
  <<start_point>>
    IF v_searched_number MOD x = 0 THEN
      dbms_output.put_line(v_searched_number|| ' is not a prime number..');
      v_is_prime := false;
      GOTO end_point;
    END IF;
  x := x+1;
  if x = v_searched_number then
   goto prime_point;
  end if;
  goto start_point;
  <<prime_point>>
  if v_is_prime then
    dbms_output.put_line(v_searched_number|| ' is a prime number..');
  end if;
<<end_point>>
  dbms_output.put_line('Check complete..');
END;
```
---------------------------------------------------------------------------------

# Using SQL in PL/SQL

## Operating Wİth Selected Queries (Code Samples)
------------------------------OPERATING WITH SELECTED QUERIES--------------------------------
```sql
declare
 v_name varchar2(50);
 v_salary employees.salary%type;
begin
  select first_name ||' '|| last_name, salary into v_name, v_salary  from employees where employee_id = 130;
  dbms_output.put_line('The salary of '|| v_name || ' is : '|| v_salary);
end;
```
---------------------------------------------------------------------------------
```sql
declare
 v_name varchar2(50);
 sysdates employees.hire_date%type;
begin
  select first_name ||' '|| last_name, sysdates into v_name, sysdates from employees where employee_id = 130;
  dbms_output.put_line('The salary of '|| v_name || ' is : '|| sysdates);
end;
```
---------------------------------------------------------------------------------
```sql
declare
 v_name varchar2(50);
 v_sysdate employees.hire_date%type;
 employee_id employees.employee_id%type := 130;
begin
  select first_name ||' '|| last_name, sysdate into v_name, v_sysdate from employees where employee_id = employee_id;
  dbms_output.put_line('The salary of '|| v_name || ' is : '|| v_sysdate );
end;
```
---------------------------------------------------------------------------------
```sql
declare
 v_name varchar2(50);
 v_salary employees.salary%type;
 v_employee_id employees.employee_id%type := 130;
begin
  select first_name ||' '|| last_name, salary into v_name, v_salary from employees where employee_id = v_employee_id;
  dbms_output.put_line('The salary of '|| v_name || ' is : '|| v_salary );
end;
```
---------------------------------------------------------------------------------
```sql
-- DESC HR.EMPLOYEES; 
DECLARE
    NAME_S HR.EMPLOYEES.LAST_NAME%TYPE;
    SALARY_S HR.EMPLOYEES.SALARY%TYPE;
BEGIN
FOR I IN 120..130 LOOP
    SELECT FIRST_NAME || ' ' || LAST_NAME, SALARY INTO NAME_S, SALARY_S FROM  HR.EMPLOYEES WHERE EMPLOYEE_ID=I;
    DBMS_OUTPUT.PUT_LINE('SALARY OF ' || NAME_S || ' IS: ' || SALARY_S);
    END LOOP;
END;
```
---------------------------------------------------------------------------------

## DML Operations in PL/SQL (Code Samples)
------------------------------ DML OPERATIONS WITH PL/SQL----------------------------------------
```sql
create table employees_copy as select * from employees;
DECLARE
  v_employee_id pls_integer := 0;
  v_salary_increase number := 400;
begin
  for i in 217..226 loop
        --insert into employees_copy 
      --(employee_id,first_name,last_name,email,hire_date,job_id,salary)
    --values 
      --(i, 'employee#'||i,'temp_emp','abc@xmail.com',sysdate,'IT_PROG',1000);
   --update employees_copy 
     --set salary = salary + v_salary_increase
     --where employee_id = i;
     delete from employees_copy
     where employee_id = i;
  end loop;
end; 
```

## Using Sequences in PL/SQL (Code Samples)
------------------------------OPERATING WITH SELECTED QUERIES--------------------------------
```sql
declare
 v_name varchar2(50);
 v_salary employees.salary%type;
begin
  select first_name ||' '|| last_name, salary into v_name, v_salary  from employees where employee_id = 130;
  dbms_output.put_line('The salary of '|| v_name || ' is : '|| v_salary);
end;
```
------------------------------
```sql
declare
 v_name varchar2(50);
 sysdates employees.hire_date%type;
begin
  select first_name ||' '|| last_name, sysdates into v_name, sysdates from employees where employee_id = 130;
  dbms_output.put_line('The salary of '|| v_name || ' is : '|| sysdates);
end;
```
------------------------------
```sql
declare
 v_name varchar2(50);
 v_sysdate employees.hire_date%type;
 employee_id employees.employee_id%type := 130;
begin
  select first_name ||' '|| last_name, sysdate into v_name, v_sysdate from employees where employee_id = employee_id;
  dbms_output.put_line('The salary of '|| v_name || ' is : '|| v_sysdate );
end;
```
------------------------------
```sql
declare
 v_name varchar2(50);
 v_salary employees.salary%type;
 v_employee_id employees.employee_id%type := 130;
begin
  select first_name ||' '|| last_name, salary into v_name, v_salary from employees where employee_id = v_employee_id;
  dbms_output.put_line('The salary of '|| v_name || ' is : '|| v_salary );
end;
```
------------------------------ DML OPERATIONS WITH PL/SQL----------------------------------------
```sql
create table employees_copy as select * from employees;
DECLARE
  v_employee_id pls_integer := 0;
  v_salary_increase number := 400;
begin
  for i in 217..226 loop
        --insert into employees_copy 
      --(employee_id,first_name,last_name,email,hire_date,job_id,salary)
    --values 
      --(i, 'employee#'||i,'temp_emp','abc@xmail.com',sysdate,'IT_PROG',1000);
   --update employees_copy 
     --set salary = salary + v_salary_increase
     --where employee_id = i;
     delete from employees_copy
     where employee_id = i;
  end loop;
end;
```
----------------------------- USING SEQUENCES IN PL/SQL ----------------------------------------
```sql
create sequence employee_id_seq 
start with 207
increment by 1;
```
-----------------------------
```sql
begin
  for i in 1..10 loop
    insert into employees_copy 
      (employee_id,first_name,last_name,email,hire_date,job_id,salary)
    values 
      (employee_id_seq.nextval, 'employee#'||employee_id_seq.nextval,'temp_emp','abc@xmail.com',sysdate,'IT_PROG',1000);
  end loop;
end; 
```
----------------------------
```sql
declare
  v_seq_num number;
begin
  select employee_id_seq.nextval into v_seq_num from dual;
  dbms_output.put_line(v_seq_num);
end;
```
----------------------------
```
declare
  v_seq_num number;
begin
  select employee_id_seq.nextval into v_seq_num from employees_copy where rownum = 1;
  dbms_output.put_line(v_seq_num);
end;
```
----------------------------
```sql
declare
  v_seq_num number;
begin
  v_seq_num := employee_id_seq.nextval; 
  dbms_output.put_line(v_seq_num);
end;
```
----------------------------
```sql
begin
  dbms_output.put_line(employee_id_seq.nextval);
end;
```
----------------------------
```sql
begin
  dbms_output.put_line(employee_id_seq.currval);
end;
```
----------------------------


# Composite Data Types

## PL/SQL Records (Code Samples)
--------------------------------------------------------------------------------------------------------------------
----------------------------------------------PL/SQL RECORDS--------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------
```sql
declare
  r_emp employees%rowtype;
begin
  select * into r_emp from employees where employee_id = '101';
  --r_emp.salary := 2000;
  dbms_output.put_line(r_emp.first_name||' '||r_emp.last_name|| ' earns '||r_emp.salary||
                       ' and hired at :' || r_emp.hire_date);
end;
```
------------------------------
```sql
declare
  --r_emp employees%rowtype;
  type t_emp is record (first_name varchar2(50),
                        last_name employees.last_name%type,
                        salary employees.salary%type,
                        hire_date date);
  r_emp t_emp;
begin
  select first_name,last_name,salary,hire_date into r_emp 
        from employees where employee_id = '101';
 /* r_emp.first_name := 'Alex';
  r_emp.salary := 2000;
  r_emp.hire_date := '01-JAN-20'; */
  dbms_output.put_line(r_emp.first_name||' '||r_emp.last_name|| ' earns '||r_emp.salary||
                       ' and hired at :' || r_emp.hire_date);
end;
```
-------------------------------
```sql
declare
  type t_edu is record (primary_school varchar2(100),
                        high_school varchar2(100),
                        university varchar2(100),
                        uni_graduate_date date
                        );
  type t_emp is record (first_name varchar2(50),
                        last_name employees.last_name%type,
                        salary employees.salary%type  NOT NULL DEFAULT 1000,
                        hire_date date,
                        dept_id employees.department_id%type,
                        department departments%rowtype,
                        education t_edu
                        );
  r_emp t_emp;
begin
  select first_name,last_name,salary,hire_date,department_id 
        into r_emp.first_name,r_emp.last_name,r_emp.salary,r_emp.hire_date,r_emp.dept_id 
        from employees where employee_id = '146';
  select * into r_emp.department from departments where department_id = r_emp.dept_id;
  r_emp.education.high_school := 'Beverly Hills';
  r_emp.education.university := 'Oxford';
  r_emp.education.uni_graduate_date := '01-JAN-13'; 
  
  dbms_output.put_line(r_emp.first_name||' '||r_emp.last_name|| ' earns '||r_emp.salary||
                       ' and hired at :' || r_emp.hire_date);
  dbms_output.put_line('She graduated from '|| r_emp.education.university|| ' at '||  r_emp.education.uni_graduate_date);
  dbms_output.put_line('Her Department Name is : '|| r_emp.department.department_name);
end;
```
-------------------------------

Easy DML With Records (Code Samples)
--------------------------------------------------------------------------------------------------------------------
-----------------------------------------EASY DML WITH RECORDS------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------
```sql
DECLARE
    R_REMP HR.EMPLOYEES%ROWTYPE;
BEGIN 
    SELECT * INTO R_REMP FROM HR.EMPLOYEES WHERE EMPLOYEE_ID=120;
    DBMS_OUTPUT.PUT_LINE(R_REMP.FIRST_NAME);
    FOR 
END;
```
-----------------------------------------
```sql
create table retired_employees as select * from employees where 1=2;
select * from retired_employees;
/
declare
    r_emp employees%rowtype;
begin
    select * into r_emp from employees where employee_id = 104;
 r_emp.salary := 0;
    r_emp.commission_pct := 0;
    insert into retired_employees values r_emp;
end;
```
-----------------------------------------
```sql
declare
    r_emp employees%rowtype;
begin
    select * into r_emp from employees where employee_id = 104;
    r_emp.salary := 10;
    r_emp.commission_pct := 0;
    --insert into retired_employees values r_emp;
    update retired_employees set row = r_emp where employee_id = 104;
end;
/
delete from retired_employees;
```
-----------------------------------------
