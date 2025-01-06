FROM python:3.13-slim AS builder
WORKDIR /usr/src/zeldaspeedruns
RUN useradd -M -U zeldaspeedruns

# Install dependencies
RUN apt-get update -y && \
    apt-get dist-upgrade -y && \
    apt-get install --no-install-recommends -y \
    netcat-traditional \
    gcc \
    libpq-dev \
    python3-dev

# Copy over our source files.
COPY . /usr/src/zeldaspeedruns
RUN mkdir -p /usr/share/zeldaspeedruns/static \
    && chown -R zeldaspeedruns:zeldaspeedruns /usr/src/zeldaspeedruns \
    && chown -R zeldaspeedruns:zeldaspeedruns /usr/share/zeldaspeedruns/static

RUN pip3 install -r requirements.txt --no-cache-dir --root-user-action=ignore

# Run the server
FROM builder AS web
USER zeldaspeedruns
EXPOSE 8000
ENTRYPOINT [".docker/entrypoint.sh"]
