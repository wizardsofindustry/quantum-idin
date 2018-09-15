FROM wizardsofindustry/quantum:latest

RUN mkdir /var/lib/idin
RUN mkdir /var/spool/aorta

COPY . /app
COPY etc/ /etc/idin/

WORKDIR /app
RUN python3 setup.py install

ENV QUANTUM_DEPLOYMENT_ENV development
ENV AORTA_SPOOL_DIR /var/spool/aorta
ENV IDIN_SECRET_KEY 70422360908e67dbbe1ac7bcf98f16b194ae51e779f690d9598c2d596c6e4bb4
ENV IDIN_DEBUG 1
ENV IDIN_IOC_DEFAULTS /etc/idin/ioc.conf
ENV IDIN_IOC_DIR /etc/idin/ioc.conf.d/
ENV IDIN_RDBMS_DSN postgresql+psycopg2://idin:idin@rdbms:5432/idin
ENV IDIN_RUNTIME service

ENV SQ_TESTING_PHASE lint
RUN ./bin/run-tests

ENTRYPOINT ["./bin/docker-entrypoint"]
