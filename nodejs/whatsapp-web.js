const qrcode = require('qrcode-terminal');
const { Client } = require('whatsapp-web.js');
const net = require('net');
const fs = require('fs')
const SESSION_FILE_PATH = './session.json';

var session = null;
var proxy = null;
if(fs.existsSync(SESSION_FILE_PATH)) { session = require(SESSION_FILE_PATH); }
var options = {session: session, puppeteer: { headless: true, args: ['--no-sandbox', '--disable-setuid-sandbox',]}}

const whatsapp = new Client(options);
whatsapp.on('authenticated', (session) => {
    fs.writeFile(SESSION_FILE_PATH, JSON.stringify(session), function (err) {
        if (err) {console.error(err);}
    });
});
whatsapp.on('qr', qr => { qrcode.generate(qr, {small: true}); });
whatsapp.on('ready', () => { console.log('Whatsapp is ready!'); });
whatsapp.on('message', message => {
    console.log('<<<< ' + message.from + ' : ' + message.body);
    var json = JSON.stringify({from: message.from, body: message.body});
    console.log(json);
    if(proxy){
        console.log('Is connected!');
        proxy.write(json+'≠');
    }
});
whatsapp.initialize();

var server = net.createServer(function (socket) {
    proxy = socket;
    console.log('Connected!');
    socket.on('data', function (data) {
        var text = new TextDecoder().decode(data);
        console.log(text);
        var message = JSON.parse(text);
        console.log('>>>> ' + message.to + ' : ' + message.body);
        whatsapp.sendMessage(message.to, message.body);
    });
    socket.on('end', function () {
        console.log('Disconnected!');
        proxy = null;
    });
}).listen(9999);

// server.close()

// require('./whatsapp-web')









