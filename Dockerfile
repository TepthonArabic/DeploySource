FROM RRYR7/thesource:slim-buster

RUN git clone https://github.com/RRYR7/thesource.git /root/Tepthon

WORKDIR /root/Tepthon

RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/Tepthon/bin:$PATH"

CMD ["python3","-m","Tepthon"]
