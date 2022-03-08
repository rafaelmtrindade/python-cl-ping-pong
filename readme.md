# Ping-Pong de Linha de Comando

## Índice

1. <a href="#intro" style="color: inherit">O que é</a>
1. <a href="#install" style="color: inherit">Instalação</a>
1. <a href="#opt" style="color: inherit">Opções</a>
1. <a href="#credits" style="color: inherit">Créditos</a>
1. <a href="#dev" style="color: inherit">Desenvolvimento</a>

## <a id="intro"></a>O que é

Este pequeno projeto surgiu como uma distração em um momento de tédio e acabou se tornando algo bem divertido de fazer.

A ideia principal é criar um jogo de ping-pong para assistir no terminal, tendo resultados variados.

> <span style="font-size: 16px"> Disclaimer:</span> <span style="font-size:15px">**Eu não entendo absolutamente NADA de ping-pong** :)</span>

## <a id="install"></a>Instalação

**Lembrando que esse jogo é do tipo que se assiste, não do que se joga.**

O "jogo" foi todo feito em Python 3.

### Requerimentos

- Python@3.10

### Linux

1. Tendo o Python 3 instalado e o projeto baixado, navegue até a pasta onde baixou o projeto;

   _Exemplo_: projeto baixado na pasta `~/python-cl-ping-pong`:

   ```shell
   $ cd ~/python-cl-ping-pong
   ```

1. Habilite a execução para o arquivo game.py:

   ```shell
   $ chmod +x game.py
   ```

1. Executar o jogo:

   1. Abra o terminal na pasta em que baixou o projeto;
   1. Utilize `./game.py` para abrir o jogo no terminal.

1. (Opcional) Executar o jogo pelo terminal de qualquer lugar:

   1. Adicione o arquivo na pasta /usr/bin para executá-lo de qualquer lugar.

      _Exemplo_: projeto baixado na pasta `~/python-cl-ping-pong`:

      ```shell
      $ cd /usr/bin
      $ sudo ln -s ~/python-cl-ping-pong/game.py pingpong
      ```

   1. Agora para abrir o jogo, é só utilizar o comando `pingpong` no terminal.

### Windows

> <span style="font-size: 16px">**No momento o jogo não funciona corretamente no terminal do Windows.**</span>

## <a id="opt"></a>Opções:

No final do arquivo `game.py` você pode modificar alguns atributos dos jogadores para obter partidas mais interessantes.

Nesse jogo, um set tem 15 pontos, e você pode decidir quantos sets são necessários para que um jogador vença a partida. O valor padrão é 3.

## <a id="credits"></a>Créditos

- A arte em caracteres ASCII utilizada foi tirada <a href="https://ascii.co.uk/art/stickman">daqui</a>.

## <a id="dev"></a>Desenvolvimento

Eventualmente, se eu tiver tempo, algumas ideias que eu gostaria de implementar são:

- outros eventos para ocorrer durante o jogo
- possibilidade de criar e armazenar vários jogadores de forma persistente.
- sistema de progressão para os jogadores, de forma que ganhar jogos possibilite aumentar suas habilidades
- outras habilidades para os jogadores
- efeitos visuais e mais animações
- **possibilidade de jogar pessoalmente** contra o PC ou mesmo outros jogadores localmente.
- maneira de armazenar e consultar pontuações dos jogadores localmente.

Não sei se irei continuar com o projeto, e sei que o código não é dos melhores, mas me diverti bastante até agora.
