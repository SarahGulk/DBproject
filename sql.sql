reate table employee (
employee_id char(20) primary key ,
name char(20)
);                                                                                                                                                                 
                                                                                                                                                                   create table company(
company_id int primary key,
company_name varchar(100),                                                                                                                                         
company_address char(100),
debt_amount float,
debt_offer float,
phone_number char(20),
interest varchar(10),
notes char (200)
);

create table CurrentCase (
case_number int,
company_id int ,
case_company char(200),
last_date char(20),
percentage float,
employee_id char(20),
notes char(200),
primary key (case_number, company_id),
foreign key (company_id) references company(company_id),
foreign key (employee_id) references employee(employee_id)
);

insert into employee(employee_id, name)
values ('jgulkowitz', 'Jacob Gulkowitz');

insert into employee(employee_id, name)
values ('dreiss', 'David Reiss');

insert into employee(employee_id, name)
values ('agulkowitz', 'Abraham Gulkowitz');

insert into employee(employee_id, name)
alues ('epacher', 'Eric Pacher');

insert into company(company_id, company_name, company_address, debt_amount, debt_offer, phone_number, interest, notes)
VALUES  ('0001', 'All Weld Mobile Welding','15 Robinson Drive Mansfeild PA, 16933', '7804', '702.36',null ,'No',null);

insert into company(company_id, company_name, company_address, debt_amount, debt_offer, phone_number, interest, notes)
VALUES  ('0002', 'Allison Crane and Rigging','2817 Lycoming Creek Road Williamsport PA 17701', '15692.5', '1412.33','(800) 232-2977','Yes','8/16 mail documents? m\
issing');

insert into company(company_id, company_name, company_address, debt_amount, debt_offer, phone_number, interest, notes)
VALUES  ('0003', 'American Truck Stop','PO Box 807009 Kansas City MO 641884', '485696.93', '43712.72','(570) 659-5301','Yes','10/20-call next week to speak to Bil\
l the owner');

insert into company(company_id, company_name, company_address, debt_amount, debt_offer, phone_number, interest, notes)
VALUES  ('0004', 'Assurant Employee Benifits','2720 South Main Street Mansfeild PA 16933', '4015.92', '361.43','(816) 474-2345','No','An Insurance Company');

insert into company(company_id, company_name, company_address, debt_amount, debt_offer, phone_number, interest, notes)
VALUES  ('0005', 'B&K Equipment LLC','PO Box 741 Wyalusing, PA 18853', '4015.92', '54799.59','(570) 746-6262','No','8/16 speak to gloria        10/20-not interest\
ed');
insert into CurrentCase(case_number, company_id, case_company, last_date, percentage, employee_id, notes)
values ('001','001','Tri-State Trucking Company', 'January 20, 2018','0.09','epacher','null');

insert into CurrentCase(case_number, company_id, case_company, last_date, percentage, employee_id, notes)
values ('001','002','Tri-State Trucking Company', 'August 16, 2017','0.09','epacher','null');

insert into CurrentCase(case_number, company_id, case_company,  last_date,  percentage, employee_id, notes)
values ('001','003','Tri-State Trucking Company', 'October 20, 2017', '0.09','epacher','null');

insert into CurrentCase(case_number, company_id, case_company,  last_date,  percentage, employee_id, notes)
values ('001','004','Tri-State Trucking Company',  'January 20, 2018', '0.09','epacher','null');

insert into CurrentCase(case_number, company_id, case_company,  last_date, percentage, employee_id, notes)
values ('001','005','Tri-State Trucking Company',  'October 20, 2018', '0.09','epacher','null');
