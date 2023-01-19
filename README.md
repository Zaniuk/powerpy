
### Nota: la documentación se encuentra en localhost:8000/swagger o si se hizo el deploy pertinente en <base_url>/swagger

- Aunque me parece una obviedad, los endpoints están separados, siguiendo el SRP. *"No hace falta procesar datos cuando no te los piden"*
- Utilicé select_related para evitar hacer queries innecesarias (se podría optimizar aún más utilizando el método **only**).
- Unifiqué las respuestas de los endpoints, para que siempre devuelvan un diccionario con la misma estructura. (clase ConsumptionResponse)

## Cosas que no hice teniendo en cuenta que es una prueba:

- No hice tests unitarios, de integración ni de performance.
- No hice un sistema de loggers.
- No hice un sistema de autenticación/autorización.
- No versioné la API.
- No utilicé VCS.
- Si bien hice una documentación, es muy básica:
  - Hace falta más información sobre los fields de los endpoints.
  - Hace falta más información sobre los códigos de respuesta.
  - No hay información de los modelos.
