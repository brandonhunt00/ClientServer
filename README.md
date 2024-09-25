# Comunicação Cliente-Servidor em Python Usando Sockets

## Índice

- [Visão Geral](#visão-geral)
- [Recursos](#recursos)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Uso](#uso)
  - [Executando o Servidor](#executando-o-servidor)
  - [Executando o Cliente](#executando-o-cliente)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Funcionamento](#funcionamento)
  - [Envio e Recebimento de Mensagens em Bits](#envio-e-recebimento-de-mensagens-em-bits)
  - [Infraestrutura de Rede Local](#infraestrutura-de-rede-local)
- [Considerações de Segurança](#considerações-de-segurança)
- [Contribuição](#contribuição)
- [Licença](#licença)
- [Contato](#contato)

## Visão Geral

Este projeto implementa uma aplicação de comunicação cliente-servidor utilizando sockets em Python. Tanto o cliente quanto o servidor são capazes de enviar mensagens em formato de bits e traduzi-las ao receber. A comunicação ocorre localmente no mesmo computador, facilitando testes e aprendizado sobre comunicação de redes e infraestrutura de sockets.

## Recursos

- **Comunicação Bidirecional**: Envio e recebimento de mensagens entre cliente e servidor.
- **Representação em Bits**: Mensagens são convertidas para bits antes do envio e traduzidas ao serem recebidas.
- **Interface de Terminal**: Interação via terminal para enviar e receber mensagens.
- **Uso Exclusivo em Máquina Local**: Comunicação configurada para operar apenas no computador local (`localhost`).

## Tecnologias Utilizadas

- **Linguagem de Programação**: Python 3.x
- **Bibliotecas**:
  - `socket`: Para criação e gerenciamento de sockets de rede.

## Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:

- Python 3.x instalado no seu sistema. Você pode baixá-lo [aqui](https://www.python.org/downloads/).
- Conhecimentos básicos em Python e conceitos de redes.

## Instalação

1. **Clone o Repositório**
   git clone https://github.com/seu-usuario/comunicacao-sockets-python.git

Navegue até o Diretório do Projeto


cd comunicacao-sockets-python
(Opcional) Crie um Ambiente Virtual

É recomendado usar um ambiente virtual para gerenciar dependências.

bash
Copy code
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
Instale as Dependências

Este projeto utiliza apenas a biblioteca padrão do Python, portanto, nenhuma instalação adicional é necessária.

## Uso

# Executando o Servidor #

Abra um Terminal
Navegue até o Diretório do Projeto

cd comunicacao-sockets-python

Execute o Servidor
python servidor.py

Você verá a mensagem:
yaml

Servidor aguardando conexão na porta 5000...
Executando o Cliente
Abra Outro Terminal

Navegue até o Diretório do Projeto

bash
Copy code
cd comunicacao-sockets-python
Execute o Cliente

bash
Copy code
python cliente.py
Você verá a mensagem:
yaml

Conectado ao servidor localhost na porta 5000.
Troca de Mensagens

Cliente: Digite uma mensagem e pressione Enter.
Servidor: A mensagem recebida será exibida, e você poderá responder digitando sua própria mensagem.
Encerrando a Conexão

Digite sair em qualquer dos terminais para encerrar a comunicação.
Estrutura do Projeto
comunicacao-sockets-python/
├── cliente.py
├── servidor.py
├── README.md
servidor.py: Script que implementa o servidor, escutando por conexões e respondendo às mensagens do cliente.
cliente.py: Script que implementa o cliente, conectando-se ao servidor e enviando mensagens.
README.md: Este arquivo de documentação.
Funcionamento
Envio e Recebimento de Mensagens em Bits
Tanto o cliente quanto o servidor convertem as mensagens de texto para uma representação binária (bits) antes de enviá-las através dos sockets. Ao receber uma mensagem, eles convertem os bits de volta para texto para exibição.

Processo de Envio:

Entrada do Usuário: O usuário digita uma mensagem no terminal.
Codificação: A mensagem é codificada de string para bytes usando UTF-8.
Conversão para Bits: Cada byte é convertido para sua representação binária de 8 bits.
Envio: Os bytes são enviados através do socket.
Processo de Recebimento:

Recebimento de Bytes: O socket recebe os bytes enviados.
Conversão para Bits: Os bytes recebidos são convertidos para uma representação binária de 8 bits.
Decodificação: Os bytes são decodificados de volta para uma string usando UTF-8.
Exibição: A mensagem é exibida no terminal.
Infraestrutura de Rede Local
Mesmo operando no mesmo computador, a comunicação cliente-servidor segue os princípios das redes distribuídas:

Sockets: Interfaces de software que permitem a comunicação entre processos.
TCP/IP: Protocolo de comunicação que garante a entrega confiável das mensagens.
Loopback Interface: Utiliza o endereço localhost (127.0.0.1) para comunicação interna na máquina.
Camadas de Rede Envolvidas:

Camada de Aplicação: Onde os scripts do cliente e servidor operam.
Camada de Transporte: TCP gerencia a conexão e a integridade dos dados.
Camada de Rede: IP gerencia o endereçamento e roteamento.
Camada de Link e Física: Simuladas pela interface de loopback, sem envolver hardware físico real.
Considerações de Segurança
Comunicação Local: A comunicação ocorre apenas no seu computador, reduzindo riscos de interceptação externa.
Entrada de Dados: Este projeto básico não implementa validações ou autenticações. Para aplicações reais, considere implementar medidas de segurança adicionais.
Portas e Firewalls: Como a comunicação é local, configurações de firewall geralmente não bloqueiam a porta utilizada (5000). Contudo, ao expandir para redes externas, ajuste as configurações de firewall conforme necessário.

Fork este Repositório

# Crie uma Branch para sua Feature #
git checkout -b minha-nova-feature

# Commit suas Alterações #
git commit -m 'Adiciona nova feature'

# Faça o Push para sua Branch #
git push origin minha-nova-feature

# Abra um Pull Request #

## Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

# Contribuição #
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests para aprimorar este projeto.

## Contato
Se você tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato:

Nome: Brandon Hunt e Vinícius Beltrão
Email: boh@cesar.school ; vgb@cesar.school
