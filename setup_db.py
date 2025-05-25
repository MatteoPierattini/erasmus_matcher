from app import app, db
from app.models import University, Course

with app.app_context():
    db.drop_all()
    db.create_all()

    # Università
    u1 = University(name="Università di Milano")
    u2 = University(name="Università di Barcellona")
    u3 = University(name="Università di Berlino")

    db.session.add_all([u1, u2, u3])
    db.session.commit()

    # Corsi con syllabus realistici e lunghi
    corsi = [
        # Università di Milano
        Course(
            name="Fondamenti di Programmazione",
            syllabus=(
                "Il corso introduce le basi della programmazione utilizzando Python. Gli argomenti includono variabili, tipi di dato, "
                "strutture condizionali e iterative, funzioni, strutture dati come liste e dizionari, e gestione degli errori. "
                "È prevista una parte pratica significativa con esercizi settimanali e progetti. Vengono presentati anche concetti base "
                "di programmazione orientata agli oggetti. L’obiettivo è fornire agli studenti una solida base per affrontare problemi computazionali reali."
            ),
            university=u1
        ),
        Course(
            name="Elettronica Analogica",
            syllabus=(
                "Il corso tratta i fondamenti dell’elettronica analogica. Si parte dai semiconduttori, diodi, e transistor bipolari, "
                "per arrivare alla progettazione di circuiti con amplificatori operazionali, filtri attivi e alimentatori stabilizzati. "
                "Durante il corso si svolgono simulazioni con software CAD e laboratori con componenti reali. La parte teorica è accompagnata "
                "da una forte componente applicativa, per preparare gli studenti alla progettazione pratica di circuiti."
            ),
            university=u1
        ),
        Course(
            name="Reti di Calcolatori",
            syllabus=(
                "Il corso fornisce una panoramica sui principali protocolli delle reti di computer. Si analizzano i livelli OSI e TCP/IP, "
                "con focus su Ethernet, IP, TCP, UDP, DNS e HTTP. Si discutono anche concetti di sicurezza, gestione degli indirizzi, e routing. "
                "Le esercitazioni pratiche includono configurazione di router e analisi del traffico di rete con Wireshark."
            ),
            university=u1
        ),

        # Università di Barcellona
        Course(
            name="Introducción a la Programación",
            syllabus=(
                "Este curso introduce los fundamentos de la programación usando Python. Se abordan estructuras básicas como variables, "
                "condicionales, bucles, funciones y manejo de errores. También se enseña el uso de estructuras de datos como listas, diccionarios y tuplas. "
                "Se incluye un módulo sobre programación orientada a objetos. Los estudiantes realizarán varios proyectos prácticos diseñados "
                "para resolver problemas del mundo real relacionados con datos y automatización."
            ),
            university=u2
        ),
        Course(
            name="Fundamentos de Telecomunicaciones",
            syllabus=(
                "El curso cubre principios esenciales de las telecomunicaciones analógicas y digitales. Incluye modulación, transmisión de señales, "
                "teoría de la información, y codificación de canales. Se introducen tecnologías modernas como 5G, fibra óptica y redes satelitales. "
                "Además de teoría, se realizan prácticas en laboratorio donde los estudiantes configuran y analizan sistemas reales de transmisión."
            ),
            university=u2
        ),
        Course(
            name="Arquitectura de Computadores",
            syllabus=(
                "Este curso analiza la estructura interna de los sistemas computacionales modernos. Cubre organización de la CPU, jerarquía de memoria, "
                "conjuntos de instrucciones, ejecución de instrucciones y pipelines. Se estudian arquitecturas RISC y CISC. "
                "El curso incluye simulaciones prácticas para visualizar el flujo de datos e instrucciones en microprocesadores reales."
            ),
            university=u2
        ),

        # Università di Berlino
        Course(
            name="Programmieren I",
            syllabus=(
                "Dieser Kurs bietet eine Einführung in die Programmierung mit Python. Themen sind Datentypen, Kontrollstrukturen, Funktionen, Listen, "
                "Wörterbücher, Fehlerbehandlung und grundlegende Objektorientierung. Die Studierenden lösen praktische Aufgaben und entwickeln einfache Programme "
                "zur Datenanalyse und Automatisierung alltäglicher Prozesse."
            ),
            university=u3
        ),
        Course(
            name="Signalverarbeitung",
            syllabus=(
                "Der Kurs behandelt die Grundlagen der digitalen Signalverarbeitung. Inhalte sind Fourier-Transformation, Filterdesign, "
                "digitale Filter, Spektralanalyse und Anwendungen in der Sprach- und Bildverarbeitung. "
                "Neben der Theorie führen die Studierenden praktische Analysen mit MATLAB oder Python durch."
            ),
            university=u3
        ),
        Course(
            name="Rechnerarchitektur",
            syllabus=(
                "In diesem Kurs werden die Prinzipien der Rechnerarchitektur behandelt. Es werden die Komponenten eines Rechnersystems wie ALU, Register, "
                "Cache, Speicherhierarchie und Bus-Systeme untersucht. Der Kurs beinhaltet eine Einführung in Assembler-Programmierung und Performance-Optimierung. "
                "Die Studierenden arbeiten mit Simulatoren, um das Verhalten moderner Prozessoren zu analysieren."
            ),
            university=u3
        ),
    ]

    db.session.add_all(corsi)
    db.session.commit()

    print("✅ Database ricreato e popolato con syllabus estesi.")
