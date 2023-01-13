FROM google/gcloud-sdk:412.0.0-alpine

COPY /run.sh /scripts/run.sh
RUN chmod +x /scripts/*

ENV PATH="/scripts/$PATH"

RUN apk add --update --no-cache openjdk-jre && \
    gcloud component install cloud-datastore-emulator  --quiet

CMD ["run.sh"]