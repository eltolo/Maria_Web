# modulo: fragmenter.py
import logging

# Configuración del logging para errores
log_file = "fragmentation_errors.log"
logging.basicConfig(
    filename=log_file,
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Función para dividir un documento en fragmentos basados en un número máximo de palabras
def dividir_en_fragmentos(texto, max_palabras=500):
    try:
        palabras = texto.split()
        fragmentos = []
        for i in range(0, len(palabras), max_palabras):
            fragmento = " ".join(palabras[i:i+max_palabras])
            fragmentos.append(fragmento)
        return fragmentos
    except Exception as e:
        logging.error(f"Error al fragmentar el texto: {e}")
        return []


# Ejemplo de uso:
# documento = """Paso de los Libres es un departamento de la provincia de Corrientes, en el noreste de Argentina, que ocupa 4893.3 km²,4​ en la región sudeste de la provincia. Ocupa el octavo lugar en superficie entre los departamentos de la provincia. Esta superficie representa el 5,3% del total provincial que es de 88 886 km².

# Limita al norte con el departamento de San Martín; al oeste con los de Mercedes y Curuzú Cuatiá; al sur con el de Monte Caseros; y al este con la República Federativa del Brasil, de la cual está separado por el río Uruguay.

# La cabecera del departamento es la homónima Paso de los Libres, sobre la costa del río Uruguay.

# Población
# Cuenta con 56 989 habitantes (Indec, 2022), lo que representa un incremento promedio anual del 1.4% frente a los 48 642 habitantes (Indec, 2010) del censo anterior.5​
# La mediana de edad se estableció en 29 años.3​

# Gráfica de evolución demográfica de Departamento Paso de los Libres entre 1991 y 2022

# Fuente de los Censos Nacionales del INDEC


# Ruta Nacional 14, principal vía de acceso a Paso de los Libres.
# Localidades
# La mayor parte de la población se concentra en la ciudad cabecera del departamento. El resto es población de carácter rural, dispersa o asentada en pequeñas localidades.1​

# Cabecera
# (Población 2010)	Localidades
# (Población 2010)
# Paso de los Libres (43 251 hab.)	
# Bonpland (1029 hab.)
# Parada Pucheta (328 hab.)
# Tapebicuá (516 hab.)
# Situación geográfica
# El departamento de Paso de los Libres está localizado al sudeste de la provincia de Corrientes, en la denominada Región del Nordeste de la República Argentina.

# Está a 214 km del punto extremo norte provincial (río Paraná, norte de Itatí, a 27° 16' Lat Sur); y a 70 km del punto extremo sur (confluencia del río Mocoretá en el río Uruguay, a 30° 45' Lat Sur); a 210 km del punto extremo oriental (confluencia del arroyo Chimiray, en el río Uruguay a 55° 40' Long Oeste); a 155 km del punto extremo occidental (río Paraná, al sur del departamento de Goya, a 59° 37' Long O) de la provincia de Corrientes.

# Esta situación geográfica ubica al departamento de Paso de los Libres en la línea de transición entre los climas templados y cálidos, con todas sus consecuencias geográficas. Pero también, lo localiza en la frontera más densamente poblada entre Argentina y Brasil.

# Los puntos extremos departamentales son al norte 29° 30' latitud S, al sur 30° 06' lat S, al este 56° 50' Long O, y al oeste 57° 42' Long O. De manera, que el Paralelo 30° de latitud Sur, y el meridiano de 57°, son los puntos de referencia geodésica del departamento Paso de los Libres.

# El departamento libreño tiene una forma general de un triángulo, cuya base está al norte, y el vértice hacia el sur. Así, la superficie de mayor desarrollo es la septentrional, con predominio de lomadas, clima cálido, bañados y arroyos, y la extensión del "malezal"; mientras que la meridional se estrecha con una lomada principal, clima templado, dos pendientes hidrográficas definidas y monte.

# Dimensiones
# El mayor largo de norte-sur, entre la desembocadura del río Miriñay en el río Uruguay, es de 108 km; y el menor entre la desembocadura del Bañado del Chaco en el río Guaviraví, y la desembocadura del río Guaviraví en el río Uruguay, es de 35 km.

# El mayor ancho de este-oeste, entre el Paso San Roquito (río Miriñay) y el Paso Colón (río Guaviraví) es de 70 km; mientras que el menor entre la Estancia Cambay (curva del río Miriñay) y la Estancia San Clemente, es de 10 km; al norte del Destacamento de Gendarmería Nacional, entre la desembocadura del río Miriñay en el río Uruguay.

# Límites
# Al norte tiene un desarrollo de 65 km, desde el Bañado del Chaco -afluente del río Guaviraví- al Bañado Aguará Cuá. Al oeste unos 130 km, a lo largo del río Miriñay. Al sudeste una extensión de 100 km, por el río Uruguay; y al este por el río Guaviraví en un desarrollo de 32 km.

# El perímetro departamental tiene 327 km de límites fluviales, de los cuales 227 km (70%) son límites interdepartamentales y 100 (30%) son límites internacionales con la República Federativa del Brasil.

# El límite internacional con el Brasil está establecido por el canal navegable más profundo, también denominado vaguada (o talweg), que entre Paso de los Libres y Uruguayana, pasa por el centro del río Uruguay.


# Monumento a Madariaga (Paso de los Libres).
# Historia

# Iglesia San José (Paso de los Libres).
# Fundación de la ciudad de Paso de los Libres
# Cuando Joaquín Madariaga asume interinamente el gobierno de la provincia, y después de reorganizar la administración general, convocó el 1 de agosto de 1843 a elecciones, las que se realizaron el 15 del mismo mes, con el objeto de elegir diputados al Congreso General con poderes para nombrar gobernador.

# Constituido este cuerpo el 30 de agosto de 1843, fue presidido por Juan Baltazar Acosta, y eligió a Joaquín Madariaga como gobernador interino de la provincia.

# Una de las primeras leyes que sancionó este Congreso General, fue perpetuar el recuerdo del pasaje de los llamados «108 libertadores», con un hecho que pasara a la posteridad, con todo su significado y valor histórico. Satisfaciendo estos anhelos el Congreso General, sancionó la Ley n.º 840, autorizando al Poder Ejecutivo la creación de un pueblo con la denominación de Paso de los Libres. Esta ley fue promulgada el 12 de septiembre de 1843.

# Después de fundar Paso de los Libres, Joaquín Madariaga designó a su hermano Antonio Madariaga, como delegado político con asiento en este pueblo, justamente por su valor estratégico. El primer comandante militar fue el teniente coronel Bernabé Acuña, que cumplía las funciones de actuales de intendente municipal, juez de paz y comisario policial departamental.


# Edificio de la Municipalidad de Paso de los Libres.

# Costanera de Paso de los Libres, sobre el río Uruguay y con la orilla brasilera a la vista.
# Departamento
# El 7 de marzo de 1917 el gobernador Mariano Indalecio Loza aprobó por decreto el Cuadro comparativo de la subdivisión en Departamentos y Secciones de la Provincia de Corrientes; Límites interdepartamentales e interseccionales, que fijó para el departamento Paso de los Libres los siguientes límites:6​

# Departamento Paso de los Libres - Límites departamentales: Norte: Bañado Guaviravi y bañado Chaco, siguiendo el límite Sur de la propiedad de C. Elena Colomer, entrando en el bañado Pairiry, siguiendo el estero Aguara Kua hasta el río Miriñay (límite Sur de las propiedades de A. M. de Contreras, Cesárea Godoy de Verón, Ruperto Barbosa y Hnos.); Este: Bañado y arroyo Guaviravi y el río Uruguay; Sur: Río Uruguay; Oeste: Arroyo Miriñay.
# El cuadro señaló que el departamento estaba dividido en 5 secciones:
# El Departamento está dividido en cinco Secciones, con los siguientes límites:
# 1ra. Sección: Norte: Arroyo y cañada Kijaty, cañada Horqueta, bañado Kurupi, límite Norte de las propiedades de Basilia Sánchez, Villalba y sucesión Fernando Yaquet, cortando la propiedad de Josefa N. de Niveiro, sigue el arroyo San Felipe hasta el río Uruguay; Este: Río Uruguay; Sur: Arroyo San Joaquín, límite Sur de la propiedad de Cayetano Pérez, siguiendo después en dirección Norte a lo largo de la prolongación del bañado Ayuí (límite Oeste de la propiedad de Leona V. de Gutiérrez) hasta la cañada Mirunga, la que después es línea divisoria hasta el arroyo Miriñay; Oeste: Río Miriñay.
# 2da. y 3ra. Sección: Toda la parte del Departamento al Sur de la 1ra. Sección está dividida en dos partes por una línea divisoria natural que es el arroyo y bañado Ayuí. Esta línea divisoria termina en el mojón Sudoeste de la propiedad de Cayetano Pérez. La parte Este del arroyo y bañado Ayuí comprende la 2da. Sección; y la parte Oeste, la 3ra. Sección;
# 4ta. y 5ta. Sección: En la misma forma se ha dividido la parte Norte de la 1ra. Sección, en dos Secciones, corriendo la línea divisoria en dirección septentrional por el bañado Kijaty y terminando en el mojón Sudeste de la propiedad de Elena Colomet. Al Este de la línea divisoria está la 4ta. Sección, y al Oeste, la 5ta. Sección.
# El 31 de agosto de 1935 fue publicado el decreto del vicegobernador Pedro Resoagli que determinó los límites de los departamentos:

# Departamento Paso de los Libres: Tiene los siguientes límites generales: Norte: Una línea que, iniciándose en el mojón N. O. de la propiedad de Juan Layda, sobre la costa del río Miriñay, en el estero Aguará Cuá, sigue el deslinde Norte de esta propiedad y el de las pertenecientes a Dionisio Roldán y R. Roldán de Vergés, Alejo López Lecube y Juan y José Artola, en el brazo del bañado Guaviravi (Chaco), hasta encontrar el arroyo Guaviravi; Este: El arroyo Guaviravi, desde sus bañados, límite oriental de las propiedades de José y Juan Artola y Luisa Rovira de Rovira, en toda la extensión de su curso, aguas abajo, hasta su desembocadura en el río Uruguay; Sud: El río Uruguay, desde la desembocadura del arroyo Guaviravi, aguas abajo, hasta encontrar la boca del río Miriñay; Oeste: El río Miriñay, desde su desembocadura en el río Uruguay, aguas arriba, hasta el mojón N.O. de la propiedad de Juan Layda, en el estero Aguara Kua."""
#fragmentos = dividir_en_fragmentos(documento, max_palabras=300)
#print(len(fragmentos))
