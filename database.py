from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Date, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import MetaData

db = SQLAlchemy()

metadata = MetaData()

class Utente(db.Model):
    __tablename__ = 'utente'
    metadata = metadata
    mail = Column(String(50), primary_key=True, name="mail")
    nome = Column(String(50), nullable=False, name="nome")
    cognome = Column(String(50), nullable=False, name="cognome")
    data_di_nascita = Column(Date, nullable=False, name="data_di_nascita")
    password = Column(String(128), nullable=False, name="password")
    telefono = Column(String(10), unique=True, name="telefono")
    carrello = relationship("Carrello", back_populates="utente", uselist=False)

class Carrello(db.Model):
    __tablename__ = 'carrello'
    metadata = metadata
    id_carrello = Column(String(10), primary_key=True, name="id_carrello")
    mail_proprietario = Column(String(50), ForeignKey('utente.mail'), nullable=False, name="mail_proprietario")
    utente = relationship("Utente", back_populates="carrello")
    articoli = relationship("Contiene", back_populates="carrello")

class Articolo(db.Model):
    __tablename__ = 'articolo'
    metadata = metadata
    nome_articolo = Column(String(80), primary_key=True, name="nome_articolo")
    prezzo = Column(Numeric(10, 2), nullable=False, name="prezzo")
    numero_pezzi_disponibili = Column(Numeric(10, 2), nullable=False, name="numero_pezzi_disponibili")
    carrelli = relationship("Contiene", back_populates="articolo")
    materiali = relationship("Materiali", back_populates="articolo")
    varianti = relationship("Variante", back_populates="articolo")
    ordini = relationship("CheContiene", back_populates="articolo")

class Contiene(db.Model):
    __tablename__ = 'contiene'
    metadata = metadata
    id_carrello = Column(String(10), ForeignKey('carrello.id_carrello'), primary_key=True, name="id_carrello")
    nome_articolo = Column(String(80), ForeignKey('articolo.nome_articolo'), primary_key=True, name="nome_articolo")
    data_aggiunta = Column(Date, nullable=False, name="data_aggiunta")
    data_rimozione = Column(Date, name="data_rimozione")
    carrello = relationship("Carrello", back_populates="articoli")
    articolo = relationship("Articolo", back_populates="carrelli")

class Materiali(db.Model):
    __tablename__ = 'materiali'
    metadata = metadata
    nome_articolo = Column(String(80), ForeignKey('articolo.nome_articolo'), primary_key=True, name="nome_articolo")
    materiale_1 = Column(String(40), nullable=False, name="materiale_1")
    materiale_2 = Column(String(40), name="materiale_2")
    materiale_3 = Column(String(40), name="materiale_3")
    materiale_4 = Column(String(40), name="materiale_4")
    materiale_5 = Column(String(40), name="materiale_5")
    articolo = relationship("Articolo", back_populates="materiali")

class Variante(db.Model):
    __tablename__ = 'variante'
    metadata = metadata
    colore = Column(String(30), primary_key=True, name="colore")
    taglia = Column(String(4), primary_key=True, name="taglia")
    nome_articolo = Column(String(80), ForeignKey('articolo.nome_articolo'), primary_key=True, name="nome_articolo")
    articolo = relationship("Articolo", back_populates="varianti")

class Ordine(db.Model):
    __tablename__ = 'ordine'
    metadata = metadata
    id_ordine = Column(String(10), primary_key=True, name="id_ordine")
    data_ordine = Column(Date, nullable=False, name="data_ordine")
    data_spedizione = Column(Date, name="data_spedizione")
    data_consegna = Column(Date, name="data_consegna")
    prezzo_ordine = Column(Numeric(10, 2), nullable=False, name="prezzo_ordine")
    metodo_di_pagamento = Column(String(30), nullable=False, name="metodo_di_pagamento")
    numero_pezzi = Column(Numeric(10, 2), nullable=False, name="numero_pezzi")
    via = Column(String(50), nullable=False, name="via")
    civico = Column(Numeric(10, 2), nullable=False, name="civico")
    cap = Column(String(5), nullable=False, name="cap")
    citta = Column(String(60), nullable=False, name="citta")
    mail_utente_cliente = Column(String(50), ForeignKey('utente.mail'), nullable=False, name="mail_utente_cliente")
    utente = relationship("Utente")
    articoli = relationship("CheContiene", back_populates="ordine")

class CheContiene(db.Model):
    __tablename__ = 'che_contiene'
    metadata = metadata
    nome_articolo = Column(String(80), ForeignKey('articolo.nome_articolo'), primary_key=True, name="nome_articolo")
    id_ordine = Column(String(10), ForeignKey('ordine.id_ordine'), primary_key=True, name="id_ordine")
    articolo = relationship("Articolo", back_populates="ordini")
    ordine = relationship("Ordine", back_populates="articoli")

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite+pysqlite:///mydatabase.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        metadata.create_all(db.engine, tables=[
            Utente.__table__,
            Carrello.__table__,
            Articolo.__table__,
            Contiene.__table__,
            Materiali.__table__,
            Variante.__table__,
            Ordine.__table__,
            CheContiene.__table__
        ])