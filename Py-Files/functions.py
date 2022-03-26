import csv
import literales as msg
import nilib


def insert_log():  # Funcio que ompleix el diccionari i el retorna.
    log = dict()
    log['Curs'] = input(msg.MSG2)
    log['Aula'] = input(msg.MSG3)
    log['Nº alumnes'] = nilib.validate(msg.MSG4, 0, None)
    log['Nº professors/es'] = nilib.validate(msg.MSG5, 0, None)
    month = nilib.validate(msg.MM, 1, 12)  # Segons el mes introduït tindrem més o menys rang de dies.
    if month % 2 == 0 and month != 2:
        day = nilib.validate(msg.DD, 1, 28)
    elif month == 4 or month == 6 or month == 9 or month == 11:
        day = nilib.validate(msg.DD, 1, 30)
    else:
        day = nilib.validate(msg.DD, 1, 31)
    year = nilib.validate(msg.YYYY, 2021, 2025)  # Acoto el rang d'anys amb un que tingui sentit.
    log['Dia'] = str(day) + '/' + str(month) + '/' + str(year)
    log['Hora de classe'] = input(msg.MSG6)
    log['Nom professor/a'] = input(msg.MSG7).capitalize()
    log['Assignatura'] = input(msg.MSG8)
    # He acotat tots el temps en una hora amb les següents validacions
    log['Porta principal oberta'] = nilib.validate(msg.MSG9, 1, 60)
    log['Porta principal tancada'] = nilib.validate(msg.MSG10, 1, 60 - log['Porta principal oberta'])
    aux = nilib.validate(msg.SEC_DOOR, 0, 1)
    if aux == 1:
        log['Porta secundària oberta'] = nilib.validate(msg.MSG11, 1, 60)
        log['Porta secundària tancada'] = nilib.validate(msg.MSG12, 1, 60 - log['Porta secundària oberta'])
    else:
        log['Porta secundària oberta'] = 0
        log['Porta secundària tancada'] = 0
    aux = nilib.validate(msg.EXT_WIND, 0, 1)
    if aux == 1:
        log['Finestres externes oberta'] = nilib.validate(msg.MSG13, 1, 60)
        log['Finestres externes tancades'] = nilib.validate(msg.MSG14, 1, 60 - log['Finestres externes oberta'])
    else:
        log['Finestres externes oberta'] = 0
        log['Finestres externes tancades'] = 0
    aux = nilib.validate(msg.INT_WIND, 0, 1)
    if aux == 1:
        log['Finestres internes oberta'] = nilib.validate(msg.MSG15, 1, 60)
        log['Finestres internes tancades'] = nilib.validate(msg.MSG16, 1, 60 - log['Finestres internes tancades'])
    else:
        log['Finestres internes oberta'] = 0
        log['Finestres internes tancades'] = 0
    aux = nilib.validate(msg.MSG17, 0, 1)
    if aux == 1:
        log['Ventilació creuada'] = 'Sí'
    else:
        log['Ventilació creuada'] = 'No'
    return log


def add_dict(f_name, head, method):  # Funció que introdueix registres desde el diccionari, tants cops com es vulgui.
    aux = 1
    try:
        with open(f_name, method, encoding='utf-8', newline='\n') as csvfile:
            fieldnames = ['Curs', 'Aula', 'Nº alumnes', 'Nº professors/es', 'Dia', 'Hora de classe', 'Nom professor/a',
                          'Assignatura', 'Porta principal oberta', 'Porta principal tancada', 'Porta secundària oberta',
                          'Porta secundària tancada', 'Finestres externes oberta', 'Finestres externes tancades',
                          'Finestres internes oberta', 'Finestres internes tancades', 'Ventilació creuada']
            writecsv = csv.DictWriter(csvfile, fieldnames=fieldnames)
            lines = linecount(f_name)
            if head == 0 or method == 'w' or lines == 0:
                writecsv.writeheader()
            while aux == 1:
                log = insert_log()
                writecsv.writerow(log)
                aux = nilib.validate(msg.AUX, 0, 1)
    except:
        print(msg.ERR_INS)
    else:
        print(msg.OK_INS)


def rd_dict(f_name):  # Funció que printa el fichero i el nombre de registres.
    try:
        with open(f_name, encoding="utf8") as csvfile:
            readcsv = csv.DictReader(csvfile, delimiter=',')
            line_count = 0
            for i in range(len(readcsv.fieldnames)):
                if i < (len(readcsv.fieldnames) - 1):
                    print(readcsv.fieldnames[i], end="\t")
                else:
                    print(readcsv.fieldnames[i], end="")
            print(msg.HEADER)
            for row in readcsv:
                print(f'{row["Curs"]}\t{row["Aula"]}\t{row["Nº alumnes"]}\t{row["Nº professors/es"]}\t{row["Dia"]}\t'
                      f'{row["Hora de classe"]}\t{row["Nom professor/a"]}\t{row["Assignatura"]}\t{row["Assignatura"]}'
                      f'\t{row["Porta principal oberta"]}\t{row["Porta principal tancada"]}\t'
                      f'{row["Porta secundària oberta"]}\t{row["Porta secundària tancada"]}\t'
                      f'{row["Finestres externes oberta"]}\t{row["Finestres externes tancades"]}\t'
                      f'{row["Finestres internes oberta"]}\t{row["Finestres internes tancades"]}\t'
                      f'{row["Ventilació creuada"]}')
                line_count = line_count + 1
            print(f"N\'hi ha {line_count} registres.")
    except FileNotFoundError:
        print(msg.ERR_RD)


def check_file(file):  # Verifico si el fitxer existeix
    try:
        with open(file, 'r'):
            return 1  # Si existeix retorna un 1
    except FileNotFoundError:
        return 0  # Si no existeix retorna un 0


def val_file(f_name, extension):  # Creo fitxer tingui o no la extensió
    if extension in f_name[-len(f_name):]:
        return msg.ROUTE + f_name
    else:
        return msg.ROUTE + f_name + extension


def linecount(f_name):  # Funció que compta els registres.
    with open(f_name, encoding="utf8") as csvfile:
        row = 0
        readcsv = csv.DictReader(csvfile, delimiter=',')
        for x in readcsv:
            row = row + 1
        return row
