# liver-server-python
Um servidor que atualiza a pagina do cliente  quando algum arquivo é salvo.

Comando para execução:
```
# sudo python3 keylog.py & ; python3 server.py
```
> Execute nas pasta onde deseja rodar o server, assim sendo necessario te-los na pasta onde quer executar.

A ideia é ter um atualizador baseado quando o desenvolvedor pressionou "ctrl+s".

## Funcionamento

Com o handler customizado, foi feito uma injeção de um script que ira fazer um "EventSource" para /update, que, enquando o usuario não pressionar a combinão de teclas "ctrl+s", ira ter uma resposta em branco; quando pressionado "ctrl+s" o script, atraves do acesso ao arquivos "cache", ira saber se deve responder o  EventSource.
Respondido o EventSource, o Js no cliente ira atualizar a pagina.
