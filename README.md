# Servidor
Servidor do socket
O codigo #Servidor estabelece uma conexão com o codigo #Client atravez de um HORT e PORT especificos.
Para manter a conexão entre o cliente e o servidor aberta, foi adicionando um loop infinito no servidor que fica aguardando novas mensagens do cliente. 
Dessa forma, o servidor não fecha a conexão após atender uma única requisição.
Mas continua esperando por novas mensagens e respondendo a elas enquanto a conexão permanecer aberta.
Temos dois loops: um externo que aguarda por novas conexões e um interno que aguarda por novas mensagens do cliente. 
Enquanto a conexão permanecer aberta, o loop interno continuará recebendo e processando mensagens do cliente.
Quando a conexão for fechada, o loop interno é encerrado e o servidor volta a aguardar por novas conexões.
