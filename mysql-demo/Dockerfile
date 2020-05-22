FROM mysql:latest
LABEL org="One-Off Coder"
LABEL author="Jee Vang, Ph.D."
LABEL email="info@oneoffcoder.com"
LABEL website="https://www.oneoffcoder.com"
LABEL facebook="https://www.facebook.com/oneoffcoder"
LABEL twitter="https://twitter.com/oneoffcoder"
LABEL instagram="https://www.instagram.com/oneoffcoder/"
LABEL youtube="https://www.youtube.com/channel/UCCCv8Glpb2dq2mhUj5mcHCQ"
LABEL linkedin="https://www.linkedin.com/company/one-off-coder"

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install git wget -y \
    && apt-get clean

RUN git clone https://github.com/datacharmer/test_db.git /tmp/test_db \
    && cp /tmp/test_db/employees.sql /docker-entrypoint-initdb.d/employees.sql \
    && cp /tmp/test_db/*.dump /docker-entrypoint-initdb.d \
    && sed -i 's|load_departments.dump|/docker-entrypoint-initdb.d/load_departments.dump|g' /docker-entrypoint-initdb.d/employees.sql \
    && sed -i 's|load_employees.dump|/docker-entrypoint-initdb.d/load_employees.dump|g' /docker-entrypoint-initdb.d/employees.sql \
    && sed -i 's|load_dept_emp.dump|/docker-entrypoint-initdb.d/load_dept_emp.dump|g' /docker-entrypoint-initdb.d/employees.sql \
    && sed -i 's|load_dept_manager.dump|/docker-entrypoint-initdb.d/load_dept_manager.dump|g' /docker-entrypoint-initdb.d/employees.sql \
    && sed -i 's|load_titles.dump|/docker-entrypoint-initdb.d/load_titles.dump|g' /docker-entrypoint-initdb.d/employees.sql \
    && sed -i 's|load_salaries1.dump|/docker-entrypoint-initdb.d/load_salaries1.dump|g' /docker-entrypoint-initdb.d/employees.sql \
    && sed -i 's|load_salaries2.dump|/docker-entrypoint-initdb.d/load_salaries2.dump|g' /docker-entrypoint-initdb.d/employees.sql \
    && sed -i 's|load_salaries3.dump|/docker-entrypoint-initdb.d/load_salaries3.dump|g' /docker-entrypoint-initdb.d/employees.sql \
    && sed -i 's|source show_elapsed.sql|# source show_elapsed.sql|g' /docker-entrypoint-initdb.d/employees.sql \
    && git clone https://github.com/dalers/mywind.git /tmp/mywind \
    && cp /tmp/mywind/northwind.sql /docker-entrypoint-initdb.d/northwind-00.sql \
    && cp /tmp/mywind/northwind-data.sql /docker-entrypoint-initdb.d/northwind-01.sql

RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*