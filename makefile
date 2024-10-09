run:
	docker build -t vysor .
	docker run -p 5000:5000 vysor