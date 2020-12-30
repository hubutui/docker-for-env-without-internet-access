# syntax=docker/dockerfile:1.2
FROM debian:stable-slim

RUN --mount=type=cache,sharing=locked,target=/var/lib/apt \
    --mount=type=cache,sharing=locked,target=/var/cache/apt \
    apt update \
    && apt install -y --no-install-recommends \
    ca-certificates \
    wget

RUN --mount=type=cache,sharing=locked,target=/var/lib/apt \
    --mount=type=cache,sharing=locked,target=/var/cache/apt \
    apt update \
    && apt install -y --no-install-recommends \
    fontconfig \
    fonts-noto-cjk \
    libasound2 \
    libglu1-mesa \
    libglvnd-dev \
    libgssapi-krb5-2 \
    libnss3 \
    libpulse-mainloop-glib0 \
    libsm6 \
    libxcb-icccm4 \
    libxcb-image0 \
    libxcb-keysyms1 \
    libxcb-randr0 \
    libxcb-render-util0 \
    libxcb-shape0 \
    libxcb-xinerama0 \
    libxcb-xkb1 \
    libxcomposite1 \
    libxcursor1 \
    libxi6 \
    libxkbcommon-x11-0 \
    libxrandr2 \
    libxrender1 \
    libxt6 \
    libxtst6 \
    xserver-xorg-core

RUN --mount=type=cache,target=/tmp \
    wget -q -O /tmp/3dslicer.tar.gz "http://download.slicer.org/download?os=linux&stability=release" \
    && mkdir /opt/3dslicer \
    && tar -xzf /tmp/3dslicer.tar.gz -C /opt/3dslicer --strip-components 1

CMD [ "/opt/3dslicer/Slicer" ]
# vim:set ts=2 sw=2 et:
