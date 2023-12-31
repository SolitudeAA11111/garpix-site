Принцип работы алгоритма:
1. Загружаем step by step фотографии укладк
2. Обработка фоторафий (переводим в оттенки серого, убираем тени)
3. Находим контур палета, обрезаем по этому контуру фотографию, принимая стартовую точку за нолевую координату на новом снимке
4. Находим контуры новой коробки с помощью разницы снимков
5. Находим расположение коробки внутри палета при помощи ее координат
6. С помощью overlaping находим уровень коробки (в данной реализации стабильно работает первый и второй уровень, третий и выше возможно не будут работать)
7. Находим стороны коробки при помощи пропорций
8. Отрисовываем коробку 

Документация:
Class PalletDetect - используется для нахождения границ контура палета


Class Pallet - описывает палет, как объект. Для инициализации нужны следующие параметры:
x/y - длина и ширина палета (в алгоритме подразумевается, что палет имеет форму квадрата)
imagePath - путь до изображения палета

find_bounding_box() - находит координаы контура на изображении. Создает следующие атрибуты объекта:
startX/startY - атрибуты для описания стартовой координаты палета
endX/endY - атрибуты для описания конечной координаты палета
dx/dy - арибуты для описания разницы по координатам x/y

Class Box - описывает коробку, как объект. Для инициализации нужны следующие параметры:
id - уникальный номер коробки
x/y/z - длина/ширина/высота (порядок не имеет значения)
imagePath - путь до изображения коробки

find_box_start_point_3d(self, pallet: Pallet, queue) - находит стартовые координаты коробки относительно координат палета для отрисовки. Создает атрибуты:
startPointX/sttartPointY/startPointZ - координаты стартовой точки на изображении. На вход нужно подать объект палета

find_box_sizes_in_3d - переводит реальные размеры сторон коробки в размеры для отрисовки (0.01 от реального размера) для отрисовки в matplotlib. Из-за особенностей 
matplotlib координаты x и y переставлены местами. Создает атрибуты dx/dy/dz, в которых хранятся размеры сторон для отрисовки

find_box_axes(self, pallet: Pallet) - через пропорции координат коробки и координат палета (размеры палета известны заранее) находит стороны, которыми положили 
коробку на палет. Записывает изменения в x, y и z, где x и y отвечают за нижнюю плоскость, параллельную палету. На вход нужно подать объект палета

find_underBoxId(self, packer, lastBoxQueueNumber) - метод для нахождения уровня коробки. Создает атрибут underBoxId, значение которого равно -1, если коробка стоит в 
самом низу, или равно id коробки, если стоит на втором ярусе

get_bounding_box_coordinates(self, previousObject, pallet: Pallet) - находит координаты коробки на изображении. Создает два атрибута - startCoordinate, который 
хранит пару x и y верхней левой координаты, и endCoordinate, который хранит пару x и y нижней правой координаты. На вход нужно подать объект палета и номер шага для нахождения прошлого изображения.

Class Packer - отвечает за очередь укладки коробок. Для инициализации нужны:
pallet - объект палета, на который ставят коробки
queue - очередь укладки коробок, хранит в себе объект палета по умолчанию на 0 позиции

append_box(self, box: Box) - добавляет объект в очередь укладки. На вход необходимо подать объект коробки

Class Painter - создает отрисовщик коробок с помощью библиотеки matplotlib

draw_box(self, box:Box, ax) - отрисовывает коробку. На вход получает объект коробки и объект plt.axes(projection='3d')

Class Model3d - главный класс, который описывает весь алгоритм построения изображения. Для инициализации нужны:
imagePath - путь до папки с изображениями
boxQueue - путь до csv файла с порядком укладки коробок
Также создает атрибуты:
fig = plt.figure() - объект отрисовки 
axGlob = plt.axes(projection='3d') - инициализация осей

get_boxes - создает массив коробок из входного файла. Добавляет атрибут boxes в виде list

get_images - создает массив путей до изображений, отсортированный по порядковым номерам изображений, записывае в атрибут imagePathes в виде list

find_pallet_bounding_box - инициализирует Pallet, создает атрибут pallet

create_packer - инициализирует Packer, создает атрибут packer

create_painter - инициализируе Painter, создает атрибут painter

create_model - создает 3d модель укладки. Добавляет атрибуты packedBoxesInfo и unpacked_cargos_info для выходного файла

create_output_json - создает json файл, в котором содержится информация по укладке коробок и координаты и размеры для отрисовки укладки в 3d модели
