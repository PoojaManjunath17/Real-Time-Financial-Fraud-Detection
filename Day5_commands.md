Complete Day 5 command sequence
cd C:\Users\Admin\PycharmProjects\Week2Project

docker compose up -d

docker ps

docker exec -it kafka kafka-topics --list --bootstrap-server localhost:9092

python producer/producer.py

git status

git add .

git commit -m "Day 5: Simulated continuous transaction streaming with Kafka"

git push origin main
