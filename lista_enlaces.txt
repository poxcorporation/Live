const video = document.getElementById('live-player');
const streamUrl = 'https://TU_USUARIO.github.io/NOMBRE_REPO/live.m3u8';

if (Hls.isSupported()) {
  const hls = new Hls({
    // Obliga al reproductor a sincronizarse con el punto 'LIVE' más reciente
    liveSyncDurationCount: 3,
    liveMaxLatencyDurationCount: 10,
    startPosition: -1 // Inicia la reproducción desde el último fragmento disponible
  });

  hls.loadSource(streamUrl);
  hls.attachMedia(video);

  hls.on(Hls.Events.MANIFEST_PARSED, function () {
    // Garantiza que vaya al final de la lista de reproducción
    video.currentTime = video.duration;
    video.play();
  });
}
