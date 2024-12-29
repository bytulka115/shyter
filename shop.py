from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import *
from file import *

from file import read_from_file


def open_shop():
    window = QDialog()
    catalog = [
        {
            "name": "skin 1",
            "kartinka": "png-clipart-eren-jaeger-render-attack-on-titans-eren.png",
            "price": 200
        },
        {
            "name": "skin 2",
            "kartinka": "png-transparent-counter-strike-source-counter-strike-global-offensive-counter-strike-1-6-counter-strike-online-counter-strike-thumbnail.png",
            "price": 250
        },
        {
            "name": "skin 2",
            "kartinka": "png-klev-club-a3xx-p-kolt-bravo-stars-png-17.png",
            "price": 500
        },
    ]
    data = read_from_file()
    score_lbl = QLabel("Score: " + str(data['score']))
    main_line = QVBoxLayout()
    main_line.addWidget(score_lbl)

    h1 = QHBoxLayout()
    def buy_func(p, skin):
        data = read_from_file()
        print(p)
        if data["score"] >= p:
            data["score"] -= p
            data["skin"] = skin
        write_in_file(data)

    for element in catalog:
        v1 = QVBoxLayout()
        name = QLabel(element['name'])
        katinka = QLabel("kartinka")
        pixmap = QPixmap(element['kartinka'])
        pixmap = pixmap.scaledToWidth(100)
        katinka.setPixmap(pixmap)
        price = QLabel(str(element['price']))
        buy_btn = QPushButton("BUY")
        buy_btn.clicked.connect(lambda _,
                                       my_price=element['price'],
                                       skin=element['kartinka']:
                                buy_func(my_price,skin))
        v1.addWidget(name)
        v1.addWidget(katinka)
        v1.addWidget(price)
        v1.addWidget(buy_btn)
        h1.addLayout(v1)
    main_line.addLayout(h1)
    window.setLayout(main_line)
    window.exec()