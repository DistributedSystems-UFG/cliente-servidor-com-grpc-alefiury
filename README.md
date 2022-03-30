# String Client-Server gRPC/Protocol Buffers

- [Introdução](#Introdução)
- [Dependencias](#Dependências)
- [Vídeo Demonstrativo](#Vídeo-Demonstrativo)

# Introdução

Essa aplicação implementa um par cliente-servidor utilizando gRPC e Protocol Buffers que realiza operações entre duas strings. Tais operações incluem: Concatenação, Distancia de Levenshtein e Checagem de igualdade.

Nessa aplicação, quando conectado com o servidor, o cliente consegue realizar chamadas de métodos, que são implementados no servidor, como se fossem métodos locais. Além disso, cliente e servidor podem se comunicar em diferentes ambientes, ambos podem ter diferentes arquiteturas e/ou implementar seus métodos em diferentes linguagens de programação. Por fim, com a utilização de Protocol Buffers é possível declarar estruturas de dados em um arquivo ```.proto``` que podem ser compiladas para gerar classes de acesso de dados em diferentes linguagens de programação alvo.

# Dependências

- grpc
- protobuf

# Vídeo Demonstrativo

[Link para o Vídeo]()