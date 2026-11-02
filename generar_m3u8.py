import os

# 1. Lista con tus 258 enlaces de Internet Archive
# (Puedes pegar tus URLs aquí o leerlas desde un archivo de texto)
enlaces = [
    "https://archive.org/download/duo-de-temu-videos/tiktokio.com1793479471_twju1tLTou1Qx6OswTol.mp4",
    "https://archive.org/download/duo-de-temu-videos/tiktokio.com1793479577_tJkGm73qggvHxfYCRybQ.mp4",
    "https://archive.org/download/duo-de-temu-videos/tiktokio.com1793479692_1LPgBSFFMOPYLxTSSy0h.mp4",
    "https://archive.org/download/duo-de-temu-videos/tiktokio.com1793479937_4xzIKwvJL1L707IJ76SU.mp4",
    "https://archive.org/download/duo-de-temu-videos/tiktokio.com1793479991_vJ9jQM50lBNLUy7sfLGT.mp4",
    "https://archive.org/download/duo-de-temu-videos/tiktokio.com1793480125_AkeSZ0aYH2bxpJP0QkXj.mp4",
    "https://archive.org/download/duo-de-temu-videos/tiktokio.com1793480195_qWCGVmtIIwVxJVzzRAJq.mp4",
    "https://archive.org/download/duo-de-temu-videos/tiktokio.com1793480253_s1QmT1FcvLnJYOpW9FpX.mp4",
    "https://archive.org/download/duo-de-temu-videos/tiktokio.com1793480335_rMbvYVLnlhj3f4LhbrcK.mp4",
    "https://archive.org/download/duo-de-temu-videos/tiktokio.com1793480445_OLy8atZltgUMN047eOcd.mp4",
    "https://archive.org/download/duo-de-temu-videos/tiktokio.com1793480511_kCZ5QN9pT08PTo8QBB3y.mp4",
    "https://archive.org/download/duo-de-temu-videos/tiktokio.com1793480567_zuB2ZEPaMcasW3nUMfeY.mp4",
    "https://archive.org/download/duo-de-temu-videos/tiktokio.com1793480786_VgXm9RnpqAmNIv5A36cp.mp4",
    "https://archive.org/download/duo-de-temu-videos/tiktokio.com1793480881_ShKWoZyIQkYMUCps8MlX.mp4",
    "https://archive.org/download/duo-de-temu-videos/v09044g40000cveo90fog65mhajavcng.mp4",
    "https://archive.org/download/duo-de-temu-videos/v09044g40000cvi50avog65v2egvaedg.mp4",
    "https://archive.org/download/duo-de-temu-videos/v09044g40000cvi5637og65i8amrivmg.mp4",
    "https://archive.org/download/duo-de-temu-videos/v09044g40000cvkuas7og65iks72akqg.mp4",
    "https://archive.org/download/duo-de-temu-videos/v09044g40000cvnaq9fog65s51vktvhg.mp4",
    "https://archive.org/download/duo-de-temu-videos/v09044g40000cvni6afog65n2in76ud0.mp4",
    "https://archive.org/download/duo-de-temu-videos/v09044g40000cvnvp4fog65s69nco990.mp4",
    "https://archive.org/download/duo-de-temu-videos/v09044g40000cvq3honog65r8dmefo10.mp4",
    "https://archive.org/download/duo-de-temu-videos/v09044g40000cvs8s7fog65j5lhhhqi0.mp4",
    "https://archive.org/download/duo-de-temu-videos/v09044g40000cvtbsvnog65ojsvjbs30.mp4",
    "https://archive.org/download/duo-de-temu-videos/v09044g40000cvu4u6nog65mkems5e0g.mp4",
    "https://archive.org/download/duo-de-temu-videos/v09044g40000cvuqbpfog65vif331700.mp4",
    "https://archive.org/download/duo-de-temu-videos/v09044g40000cvurg3vog65n4263ud5g.mp4",
    "https://archive.org/download/duo-de-temu-videos/v14044g50000d018v0vog65lnjj2gblg.mp4",
    "https://archive.org/download/duo-de-temu-videos/v14044g50000d01a227og65s2lmpte0g.mp4",
    "https://archive.org/download/duo-de-temu-videos/v14044g50000d020a0vog65jar1s4mrg.mp4",
    "https://archive.org/download/duo-de-temu-videos/v14044g50000d022tsfog65m13harb60.mp4",
    "https://archive.org/download/duo-de-temu-videos/v14044g50000d02rtafog65v6b9k1lbg.mp4",
    "https://archive.org/download/duo-de-temu-videos/v14044g50000d03ut8vog65mna9e17ig.mp4",
    "https://archive.org/download/duo-de-temu-videos/v14044g50000d06jbe7og65hojhesiq0.mp4",
    "https://archive.org/download/duo-de-temu-videos/v14044g50000d09bj97og65ve9hc8gtg.mp4",
    "https://archive.org/download/duo-de-temu-videos/v14044g50000d0alvu7og65o3u0kpl10.mp4",
    "https://archive.org/download/duo-de-temu-videos/v14044g50000d0b3cjnog65hpvg538dg.mp4",
    "https://archive.org/download/duo-de-temu-videos/v14044g50000d0b3otvog65r26hv7040.mp4",
    "https://archive.org/download/duo-de-temu-videos/v14044g50000d0ce7qnog65ml60kjqbg.mp4",
    "https://archive.org/download/duo-de-temu-videos/v14044g50000d0chivvog65qlk6m8340.mp4",
    "https://archive.org/download/duo-de-temu-videos/v14044g50000d0ddiavog65tn17v8nu0.mp4",
    "https://archive.org/download/duo-de-temu-videos/v14044g50000d0ddisfog65r0je86gu0.mp4",
    "https://archive.org/download/duo-de-temu-videos/v14044g50000d0dohgfog65j3b22i2lg.mp4",
    "https://archive.org/download/duo-de-temu-videos/v14044g50000d0dosv7og65g54c151eg.mp4",
    "https://archive.org/download/duo-de-temu-videos/v14044g50000d0fcp27og65sfjpnu4kg.mp4",
    "https://archive.org/download/duo-de-temu-videos/v14044g50000d0fmo1nog65p1v9lopv0.mp4",
    "https://archive.org/download/duo-de-temu-videos/v14044g50000d0fnai7og65ro712u1qg.mp4",
    "https://archive.org/download/duo-de-temu-videos/v1c044g50000d08q0afog65p67i8sj0g.mp4"
]

# Duración estimada por defecto en segundos para cada fragmento (ej. 180s / 3 minutos)
# Si no conoces la duración exacta, un promedio de duración funciona para el playlist event.
DURACION_DEFECTO = 180.0 

# 2. Generar el contenido HLS
contenido_m3u8 = [
    "#EXTM3U",
    "#EXT-X-VERSION:3",
    "#EXT-X-TARGETDURATION:3600",
    "#EXT-X-MEDIA-SEQUENCE:0",
    "#EXT-X-PLAYLIST-TYPE:EVENT\n"
]

for url in enlaces:
    contenido_m3u8.append(f"#EXTINF:{DURACION_DEFECTO},")
    contenido_m3u8.append(url)
    contenido_m3u8.append("") # Línea en blanco

# NOTA: Sin #EXT-X-ENDLIST al final para mantener el indicador "EN VIVO"

# 3. Guardar el archivo listo para GitHub Pages
with open("live.m3u8", "w", encoding="utf-8") as f:
    f.write("\n".join(contenido_m3u8))

print(f"¡Éxito! Se ha creado 'live.m3u8' con {len(enlaces)} elementos.")
