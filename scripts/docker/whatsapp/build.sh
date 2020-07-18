docker build -t whatsappweb scripts/docker/whatsapp/
mkdir -p $HOME/.whatsapp
cp scripts/docker/whatsapp/server.js $HOME/.whatsapp
echo "docker run --name=whatsapp --rm -it -v $HOME/.whatsapp:/var/whatsapp -p 9999:9999 whatsappweb"

