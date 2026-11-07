# Máquina

- Entorno: contenedor en la nube (Claude Code remoto), no la computadora del creador.
- La clave de ElevenLabs no vive en `.env.local`: está guardada como secreto de red del entorno y el proxy la inyecta en
  el header `xi-api-key` de cada pedido a api.elevenlabs.io. `.env.local` sólo tiene el marcador `proxy-injected`
  para que `doctor` y `voz.mjs` arranquen. Por eso `motor/clave.mjs` no se usa aquí.
- Node no pasa por el proxy por defecto: ejecutar `voz.mjs` (y cualquier script que llame a ElevenLabs) con
  `NODE_USE_ENV_PROXY=1`. Sin eso, ElevenLabs responde 401.
- La clave no tiene permiso para `/v1/user/subscription` (401): el saldo de caracteres se revisa en elevenlabs.io.
- `proyectos/` y `salida/` están en `.gitignore`; el contenedor es efímero, así que lo terminado se entrega como archivo.
