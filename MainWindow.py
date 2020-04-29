import sys, re
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QPushButton, QLabel, QAction, QListWidget, QApplication, QWidget, QLabel
from PyQt5 import uic, QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QImage, QPalette, QBrush, QIcon, QPixmap, QFont
import MiCarnivora


#clase heredada de QMainWindow (constructor de ventanas)

class ventana_principal(QMainWindow):
    #método constructor de la clase
    def __init__(self):
        #iniciar objeto QMainWindow
        QMainWindow.__init__(self)
        #cargar la configuración del archivo .ui en el objeto
        uic.loadUi("MainWindow.ui", self)
        #mostrar ventana maximizada
        self.showMaximized()
        #abrir ventana buscar
        self.dialogo1 = Buscar()
        #self.boton.clicked.connect(self.abrirBuscar)
        #titulo ventana principal
        self.setWindowTitle('Mi Carnívora!')
        #For contact us
        self.cont = Contact()
        self.Contactanos.mousePressEvent = self.conty
        self.ConW.mousePressEvent = self.conty
        #For nephentes
        self.neph = Nephy()
        self.Nephentes.mousePressEvent = self.nepht
        self.NepW.mousePressEvent = self.nepht
        #For Aldrovanda
        self.aldro = Aldro()
        self.Aldrovanda.mousePressEvent = self.aldrT
        self.AldW.mousePressEvent = self.aldrT
        #For Cephalotus
        self.ceph = Ceph()
        self.Cephalotus.mousePressEvent = self.cephT
        self.CepW.mousePressEvent = self.cephT
        #For Triphophyllum
        self.triph = Trip()
        self.Triphyophyllum.mousePressEvent = self.triT
        self.TriW.mousePressEvent = self.triT
        #For Darlingtonia
        self.darli = Darlin()
        self.Darlingtonia.mousePressEvent = self.darT
        self.DarW.mousePressEvent = self.darT
        #For Dionaea
        self.diona = Diona()
        self.Dionaea.mousePressEvent = self.dioT
        self.DioW.mousePressEvent = self.dioT
        #For Drosophyllum
        self.drop = Drosop()
        self.Drosophyllum.mousePressEvent = self.dropT
        self.DrosW.mousePressEvent = self.dropT
        #For Byblis
        self.byb = Byblis()
        self.Byblis.mousePressEvent = self.bybT
        self.BybW.mousePressEvent = self.bybT
        #reproducción
        self.Reprod = reproduccion()
        self.Reproduccion.clicked.connect(self.abrirRepro)
        
  
        #barra de estado
        menu = self.menuBar()
        #menu padre
        menu_archivo = menu.addMenu("&Menú")
        #menu padre
        menu_ayuda = menu.addMenu("&Ayuda")
        #Agregar un elemento a menu_archivo
        menu_archivo_abrir = QAction(QIcon(), "&Buscar",self)
        menu_archivo_abrir.setShortcut("Ctrl+f") #atajo teclado
        menu_archivo_abrir.setStatusTip("Abrir") #Mensaje en la barra de estado
        menu_archivo_abrir.triggered.connect(self.menuArchivoAbrir) #lanzador
        menu_archivo.addAction(menu_archivo_abrir)

        #Agregar un elemento acción al menu_archivo
        menu_archivo_cerrar = QAction(QIcon(), "&Cerrar",self)
        menu_archivo_cerrar.setShortcut("Ctrl+x") #Atajo de teclado
        menu_archivo_cerrar.setStatusTip("Cerrar") #Mensaje de la barra de estado
        menu_archivo_cerrar.triggered.connect(self.menuArchivoCerrar) #Lanzador
        menu_archivo.addAction(menu_archivo_cerrar)


        

        #Agregar un submenu al elemento ayuda
        menu_ayuda_opciones = menu_ayuda.addMenu("&Sobre Nosotros")
        
        menu_ayuda_opciones_proposito = QAction(QIcon(), "&Proposito", self)
        menu_ayuda_opciones_proposito.setStatusTip("Proposito") #Mensaje barra de estado
        menu_ayuda_opciones_proposito.triggered.connect(self.menuSobNos)
        menu_ayuda_opciones.addAction(menu_ayuda_opciones_proposito)
        
        menu_ayuda_opciones_contactanos = QAction(QIcon(), "&Contáctanos", self)
        menu_ayuda_opciones_contactanos.setStatusTip("Contáctanos") #Mensaje barra de estado
        menu_ayuda_opciones_contactanos.triggered.connect(self.menucontacto)
        menu_ayuda_opciones.addAction(menu_ayuda_opciones_contactanos)


        #Agregar un elemento al menu ayuda
        menu_ayuda_opciones_comousar = QAction(QIcon(), "&¿Cómo usar la aplicación?", self)
        menu_ayuda_opciones_comousar.setShortcut("F1") #Atajo de teclado
        menu_ayuda_opciones_comousar.setStatusTip("¿Cómo usar la aplicación") #Mensaje barra de estado
        menu_ayuda_opciones_comousar.triggered.connect(self.menuHelp) #Lanzador
        menu_ayuda.addAction(menu_ayuda_opciones_comousar)

        
    def abrirRepro(self):
        self.Reprod.exec_()

        
    def menuArchivoAbrir(self):
        self.dialogo1.exec_()

    def menuArchivoCerrar(self):
        self.close()

    def menuSobNos(self):
        QMessageBox.information(self, "Cerrar", "Acción Cerrar", QMessageBox.Discard)


    def menuHelp(self):
        QMessageBox.information(self, "PREMIUM", "Está opción solo está disponible para usuarios PREMIUM", QMessageBox.Discard)

    def menucontacto(self):
        self.cont.exec_()

    
        
        
    def closeEvent(self, event):
        resultado = QMessageBox.question(self,"Salir","¿Seguro que quieres salir de la aplicación?,",
        QMessageBox.Yes | QMessageBox.No)
        if resultado == QMessageBox.Yes: event:accept()
        else: event.ignore()


    def abrirBuscar(self, eve):
        self.dialogo1.exec_()

    def nepht(self, eve):
        self.neph.exec_()

    def aldrT(self, eve):
        self.aldro.exec_()

    def cephT(self, eve):
        self.ceph.exec_()

    def triT(self, eve):
        self.triph.exec_()

    def conty(self, eve):
        self.cont.exec_()

    def darT(self, eve):
        self.darli.exec_()

    def dioT(self, eve):
        self.diona.exec_()

    def dropT(self, eve):
        self.drop.exec_()

    def bybT(self, eve):
        self.byb.exec_()
        
class Contact(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("Contactus.ui",self)
        self.nombre.textChanged.connect(self.validar_nombre)
        self.email.textChanged.connect(self.validar_email)
        self.enviar.clicked.connect(self.validar_formulario)
        self.setMinimumSize(517,699)
        self.setMaximumSize(517,699)
        self.setWindowTitle('Contáctanos') 

    def validar_nombre(self):
        nombre = self.nombre.text()
        validar = re.match('^[a-z\sáéíóúàèìòùäëïöüñ]+$', nombre, re.I)
        if nombre == "":
            self.nombre.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.nombre.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.nombre.setStyleSheet("border: 2px solid green;")
            return True

    def validar_email(self):
        email = self.email.text()
        validar = re.match('^[a-zA-Z0-9\._-]+@[a-zA-Z0-9-]{2,}[.][a-zA-Z]{2,4}$', email, re.I)
        if email == "":
            self.email.setStyleSheet("border: 2px solid yellow;")
            return False
        elif not validar:
            self.email.setStyleSheet("border: 2px solid red;")
            return False
        else:
            self.email.setStyleSheet("border: 2px solid green;")
            return True

    def validar_formulario(self):
        if self.validar_nombre() and self.validar_email():
            QMessageBox.information(self, "Enviado", "Mensaje enviado correctamente !", QMessageBox.Discard)
        else:
            QMessageBox.warning(self,"No se pudo envíar su mensaje", "Por favor envíe un correo a davidnon@utp.edu.co", QMessageBox.Discard)
            


    
class Buscar(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("Buscar.ui",self)
        self.setMinimumSize(198,89)
        self.setMaximumSize(198,89)

class reproduccion(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("reproduccion.ui",self)
        self.setMinimumSize(800,600)
        self.setMaximumSize(800,600)
        

class Nephy(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("ListaN.ui",self)
        self.setMinimumSize(800,600)
        self.setMaximumSize(800,600)
        self.setWindowTitle('Nephentes') 
        nephentes = ['Abalata', 'Adnata', 'Aenigma', 'Alata', 'Alba', 'Albomarginata',
                     'Alpicola', 'Alzapan', 'Amabilis', 'Ampullaria', 'Anamensis', 'Andamana',
                     'Angasanensis', 'Appendiculata', 'Aptera', 'Argentii', 'Aristolochioides',
                     'Attenboroughii', 'Baramensis', 'Barcelonae', 'Beccariana', 'Bellii',
                     'Benstonei', 'Bicalcarata', 'Bokorensis', 'Bongso', 'Burbidgeae', 'Boschiana',
                     'Burkei', 'Campanulata', 'Carunculata', 'Carunculata var. robusta', 'Ceciliae',
                     'Chang', 'Chaniana', 'Clipeata', 'Copelandii', 'Cornuta', 'Curtisii',
                     'Danseri', 'Deaniana', 'Densiflora', 'Diatas', 'Distillatoria', 'Dubia', 'Edwardsiana',
                     'Edwardsiana subsp. macrophylla', 'Ephippiata', 'Epiphytica', 'Eustachya', 'Eymae',
                     'Faizaliana', 'Fallax', 'Flava', 'Fusca', 'Gantungensis', 'Geoffrayi', 'Glabrata',
                     'Glandulifera', 'Graciliflora', 'Gracilis', 'Gracillima', 'Gymnamphora', 'Galmahera',
                     'Hamata', 'Hamiguitanensis', 'Hemsleyana', 'Hirsuta', 'Hispida', 'Holdenii', 'Hurrelliana',
                     'Inermis', 'Insignis', 'Izumiae', 'Jacquelineae', 'Jamban', 'Justinae', 'Kampotiana',
                     'Kerrii', 'Khasiana', 'Klossii', 'Kongkandana', 'Krabiensis', 'Lamii', 'Lavicola', 'Leonardoi',
                     'Lingulata', 'Longifolia', 'Lowii', 'Macfarlanei', 'Macrophylla', 'Macrovulgaris', 'Madagascariensis',
                     'Mantalingajanensis', 'Mapuluensis', 'Masoalensis', 'Maxima', 'Maxima var. superba', 'Merrilliana',
                     'Mikei', 'Mindanaoensis', 'Minima', 'Mira', 'Mirabilis', 'Mirabilis var. echinostoma',
                     'Mirabilis var. globosa', 'Mirabilis var. rowanae', 'Mirabilis var. smilesii', 'Mollis',
                     'Monticola', 'Muluensis', 'Murudensis', 'Naga', 'Naquiyuddinii', 'Nebularum', 'Negros', 'Neoguineensis',
                     'Nigra', 'Northiana', 'Ovata', 'Palawanensis', 'Paniculata', 'Pantaronensis', 'Papuana', 'Parvula',
                     'Pectinata', 'Peltata', 'Pervillei', 'Petiolata', 'Philippinensis', 'Pilosa', 'Pitopangii', 'Platychila',
                     'Pulchra', 'Pyriformis', 'Rafflesiana', 'Rafflesiana var. alata', 'Rafflesiana var. elongata', 'Rafflesiana var. gigantea',
                     'Rafflesiana var. nivea', 'Rajah', 'Ramispina', 'Ramos', 'Reinwardtiana', 'Reinwardtiana var. samarindaensis',
                     'Rhombicaulis', 'Rigidifolia', 'Robcantleyi', 'Ronchinii', 'Rosea', 'Rowanae', 'Samar', 'Sanguinea',
                     'Saranganiensis', 'Sharifah-hapsahii', 'Sibuyanensis', 'Singalana', 'Smilesii', 'Spathulata', 'Spectabilis',
                     'Stenophylla', 'Sumagaya', 'Sumatrana', 'Suratensis', 'Surigaoensis', 'Talaandig', 'Talangensis', 'Tenax',
                     'Tentaculata', 'Tenuis', 'Thai', 'Thorelii', 'Tobaica', 'Tomoriana', 'Treubiana', 'Truncata',
                     'Ultra', 'Undulatifolia', 'Veitchii', 'Ventricosa', 'Vieillardii', 'Villosa', 'Viridis', 'Vogelii',
                     'Weda', 'Xiphioides', 'Zakriana', 'Zygon']
        self.listarNep.addItems(nephentes)
        self.listarNep.itemClicked.connect(self.getItemsNep)
           
    def getItemsNep(self):
        items = self.listarNep.selectedItems()
        #array para guardar los items selecciondos
        selected = []
        for x in range(len(items)):
            selected.append(self.listarNep.selectedItems()[x].text())
        pixmap = QPixmap("".join(selected)+"1.jpg")
        self.ShowNep.setPixmap(pixmap)
        pixmap = QPixmap("".join(selected)+"2.jpg")
        self.ShowNep2.setPixmap(pixmap)
        pixmap = QPixmap("".join(selected)+"3.jpg")
        self.labeltextoNep.setPixmap(pixmap)
        self.labelnombreNep.setText("".join(selected))
                
class Aldro(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("ListaAldro.ui",self)
        self.setMinimumSize(800,600)
        self.setMaximumSize(800,600)
        self.setWindowTitle('Aldrovanda') 
        aldrovanda = ['Vesiculosa']
        self.listarAldr.addItems(aldrovanda)
        self.listarAldr.itemClicked.connect(self.getItemsAldr)
           
    def getItemsAldr(self):
        items = self.listarAldr.selectedItems()
        #array para guardar los items selecciondos
        selected = []
        for x in range(len(items)):
            selected.append(self.listarAldr.selectedItems()[x].text())
        pixmap = QPixmap("".join(selected)+"1.jpg")
        self.ShowAldr.setPixmap(pixmap)
        pixmap = QPixmap("".join(selected)+"2.jpg")
        self.ShowAldr2.setPixmap(pixmap)
        pixmap = QPixmap("".join(selected)+"3.jpg")
        self.labeltextoAldr.setPixmap(pixmap)
        self.labelnombreAldr.setText("".join(selected))

class Ceph(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("ListaCepha.ui",self)
        self.setMinimumSize(800,600)
        self.setMaximumSize(800,600)
        self.setWindowTitle('Cephalotus') 
        cephalo = ['Follicularis']
        self.listarCepha.addItems(cephalo)
        self.listarCepha.itemClicked.connect(self.getItemsCeph)
           
    def getItemsCeph(self):
        items = self.listarCepha.selectedItems()
        #array para guardar los items selecciondos
        selected = []
        for x in range(len(items)):
            selected.append(self.listarCepha.selectedItems()[x].text())
        pixmap = QPixmap("".join(selected)+"1.jpg")
        self.ShowCepha.setPixmap(pixmap)
        pixmap = QPixmap("".join(selected)+"2.jpg")
        self.ShowCepha2.setPixmap(pixmap)
        pixmap = QPixmap("".join(selected)+"3.jpg")
        self.labeltextoCepha.setPixmap(pixmap)
        self.labelnombreCepha.setText("".join(selected))

class Trip(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("ListaTriph.ui",self)
        self.setMinimumSize(800,600)
        self.setMaximumSize(800,600)
        self.setWindowTitle('Triphyophyllum ') 
        triphyophyllum  = ['Peltatum']
        self.listarTrip.addItems(triphyophyllum)
        self.listarTrip.itemClicked.connect(self.getItemsTriph)
           
    def getItemsTriph(self):
        items = self.listarTrip.selectedItems()
        #array para guardar los items selecciondos
        selected = []
        for x in range(len(items)):
            selected.append(self.listarTrip.selectedItems()[x].text())
        pixmap = QPixmap("".join(selected)+"1.jpg")
        self.ShowTrip.setPixmap(pixmap)
        pixmap = QPixmap("".join(selected)+"2.jpg")
        self.ShowTrip2.setPixmap(pixmap)
        pixmap = QPixmap("".join(selected)+"3.jpg")
        self.labeltextoTrip.setPixmap(pixmap)
        self.labelnombreTrip.setText("".join(selected))

class Darlin(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("ListaDar.ui",self)
        self.setMinimumSize(800,600)
        self.setMaximumSize(800,600)
        self.setWindowTitle('Darlingtonia ') 
        darlingtonia  = ['Californica', 'Californica f. Viridiflora']
        self.listarDar.addItems(darlingtonia)
        self.listarDar.itemClicked.connect(self.getItemsDar)
           
    def getItemsDar(self):
        items = self.listarDar.selectedItems()
        #array para guardar los items selecciondos
        selected = []
        for x in range(len(items)):
            selected.append(self.listarDar.selectedItems()[x].text())
        pixmap = QPixmap("".join(selected)+"1.jpg")
        self.ShowDar.setPixmap(pixmap)
        pixmap = QPixmap("".join(selected)+"2.jpg")
        self.ShowDar2.setPixmap(pixmap)
        pixmap = QPixmap("".join(selected)+"3.jpg")
        self.labeltextoDar.setPixmap(pixmap)
        self.labelnombreDar.setText("".join(selected))

class Diona(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("ListaDiona.ui",self)
        self.setMinimumSize(800,600)
        self.setMaximumSize(800,600)
        self.setWindowTitle('Dionaea') 
        dionaea  = ['Muscipula', 'Muscipula f. Erecta', 'Muscipula f. Erigée', 'Muscipula f. Filiformis', 'Muscipula f. Linearis', 'Muscipula f. Verte', 'Muscipula f. Viridis']
        self.listarDion.addItems(dionaea)
        self.listarDion.itemClicked.connect(self.getItemsDion)
           
    def getItemsDion(self):
        items = self.listarDion.selectedItems()
        #array para guardar los items selecciondos
        selected = []
        for x in range(len(items)):
            selected.append(self.listarDion.selectedItems()[x].text())
        pixmap = QPixmap("".join(selected)+"1.jpg")
        self.ShowDion.setPixmap(pixmap)
        pixmap = QPixmap("".join(selected)+"2.jpg")
        self.ShowDion2.setPixmap(pixmap)
        pixmap = QPixmap("".join(selected)+"3.jpg")
        self.labeltextoDion.setPixmap(pixmap)
        self.labelnombreDion.setText("".join(selected))

class Drosop(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("ListaDrosop.ui",self)
        self.setMinimumSize(800,600)
        self.setMaximumSize(800,600)
        self.setWindowTitle('Drosophyllum') 
        drosophyllum  = ['Lusitanicum']
        self.listarDrop.addItems(drosophyllum)
        self.listarDrop.itemClicked.connect(self.getItemsDrop)
           
    def getItemsDrop(self):
        items = self.listarDrop.selectedItems()
        #array para guardar los items selecciondos
        selected = []
        for x in range(len(items)):
            selected.append(self.listarDrop.selectedItems()[x].text())
        pixmap = QPixmap("".join(selected)+"1.jpg")
        self.ShowDrop.setPixmap(pixmap)
        pixmap = QPixmap("".join(selected)+"2.jpg")
        self.ShowDrop2.setPixmap(pixmap)
        pixmap = QPixmap("".join(selected)+"3.jpg")
        self.labeltextoDrop.setPixmap(pixmap)
        self.labelnombreDrop.setText("".join(selected))

class Byblis(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("ListaByblis.ui",self)
        self.setMinimumSize(800,600)
        self.setMaximumSize(800,600)
        self.setWindowTitle('Byblis') 
        byblis  = ['Aquatica', 'Filifolia', 'Gigantea', 'Guehoi', 'Lamellata', 'Liniflora',
                   'Liniflora subsp. Occidentalis', 'Pilbarana', 'Rorida']
        self.listarByblis.addItems(byblis)
        self.listarByblis.itemClicked.connect(self.getItemsByblis)
           
    def getItemsByblis(self):
        items = self.listarByblis.selectedItems()
        #array para guardar los items selecciondos
        selected = []
        for x in range(len(items)):
            selected.append(self.listarByblis.selectedItems()[x].text())
        pixmap = QPixmap("".join(selected)+"1.jpg")
        self.ShowByblis.setPixmap(pixmap)
        pixmap = QPixmap("".join(selected)+"2.jpg")
        self.ShowByblis2.setPixmap(pixmap)
        pixmap = QPixmap("".join(selected)+"3.jpg")
        self.labeltextoByblis.setPixmap(pixmap)
        self.labelnombreByblis.setText("".join(selected))
    

    
        

#instanciar para iniciar la aplicación
app = QApplication(sys.argv)

#crear objeto de clase
_ventana = ventana_principal()
#mostrar ventana
_ventana.show()
#ejecutamos la aplicación
app.exec_()


