Данное задание сделано в целях знакомства с технологией Docker.

# Описание

Producer посылает строки из stdin в RabbitMQ, откуда их достает Consumer и кладет в Database.

# Запуск

Необходимо запустить 
./run.sh
После установления соединения Consumer'a с RabbitMQ и Database, можно подключать Producer'a командой
./Producer/run.sh
