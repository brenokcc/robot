const net = require('net');

var client = null;

function receive(text){
    console.log(text)
}

function send(text){
    client.write(text+'≠');
}

var server = net.createServer(function (socket) {
    var name = socket.remoteAddress + ':' + socket.remotePort;
    socket.name = socket.name
    socket.on('data', function (data) {
        var text = new TextDecoder().decode();
        receive(text);
    });
    socket.on('end', function () {
        console.log(socket.name+' desconnected!')
    });
    sockets[name] = socket;
}).listen(9999);

server.close()
