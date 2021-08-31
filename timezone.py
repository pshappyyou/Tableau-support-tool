from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile

import timezone_model as tz_model

class TimeZone(QWidget):
    def __init__(self, parent):
        super(TimeZone, self).__init__(parent)
        QWebEngineProfile.defaultProfile().setPersistentCookiesPolicy(QWebEngineProfile.ForcePersistentCookies)
        self.model = tz_model.TimeZoneModel()
        self.init_Ui()
        self.setup_events()
        self.load_Components()

    def init_Ui(self):
        self.hlay_main = QHBoxLayout()
        self.vlay_timezone = QVBoxLayout()
        self.vlay_timeutil = QVBoxLayout()
        self.gbox_timezone_calc = QGroupBox("TimeZone Calc")
        self.hlay_timezone_calc = QHBoxLayout()

        url = 'https://www.worldtimebuddy.com/'
        self.web_view = QWebEngineView()
        self.web_view.load(QUrl(url))
        self.hlay_timezone_calc.addWidget(self.web_view)
        self.gbox_timezone_calc.setLayout(self.hlay_timezone_calc)

        '''
        self.gbox_timezone_calc_src = QGroupBox("Source")
        self.vlay_timezone_calc_src = QVBoxLayout()
        self.combo_timezone_calc_src = QComboBox()
        self.combo_timezone_calc_src.setEditable(True)
        self.dtedit_timezone_calc_src = QDateTimeEdit()
        self.dtedit_timezone_calc_src.setCalendarPopup(True)
        self.vlay_timezone_calc_src.addWidget(self.combo_timezone_calc_src)
        self.vlay_timezone_calc_src.addWidget(self.dtedit_timezone_calc_src)
        self.gbox_timezone_calc_src.setLayout(self.vlay_timezone_calc_src)

        self.gbox_timezone_calc_dst = QGroupBox("Destination")
        self.vlay_timezone_calc_dst = QVBoxLayout()
        self.combo_timezone_calc_dst = QComboBox()
        self.combo_timezone_calc_dst.setEditable(True)
        self.dtedit_timezone_calc_dst = QDateTimeEdit()
        self.dtedit_timezone_calc_dst.setCalendarPopup(True)
        self.vlay_timezone_calc_dst.addWidget(self.combo_timezone_calc_dst)
        self.vlay_timezone_calc_dst.addWidget(self.dtedit_timezone_calc_dst)
        self.gbox_timezone_calc_dst.setLayout(self.vlay_timezone_calc_dst)

        self.hlay_timezone_calc.addWidget(self.gbox_timezone_calc_src)
        self.hlay_timezone_calc.addWidget(self.gbox_timezone_calc_dst)
        self.gbox_timezone_calc.setLayout(self.hlay_timezone_calc)
        '''

        self.gbox_timezone_pick = QGroupBox("TimeZone Picker")
        self.vlay_timezone_pick = QVBoxLayout()
        self.combo_timezone_pick = QComboBox()
        self.combo_timezone_pick.setEditable(True)
        self.hlay_timezone_pick = QHBoxLayout()
        self.lb_timezone_pick = QLabel("Pick Time")
        self.btn_timezone_pick_add = QPushButton("<< Add")
        self.btn_timezone_pick_pop = QPushButton("Pop >>")
        self.hlay_timezone_pick.addWidget(self.btn_timezone_pick_add)
        self.hlay_timezone_pick.addWidget(self.lb_timezone_pick)
        self.hlay_timezone_pick.addWidget(self.btn_timezone_pick_pop)
        self.vlay_timezone_pick.addWidget(self.combo_timezone_pick)
        self.vlay_timezone_pick.addLayout(self.hlay_timezone_pick)
        self.gbox_timezone_pick.setLayout(self.vlay_timezone_pick)

        self.vlay_timeutil.addWidget(self.gbox_timezone_calc)
        self.vlay_timeutil.addWidget(self.gbox_timezone_pick)
        self.hlay_main.addLayout(self.vlay_timezone)
        self.hlay_main.addLayout(self.vlay_timeutil)
        self.setLayout(self.hlay_main)

    def setup_events(self):
        self.combo_timezone_pick.activated[str].connect(self.update_timezone_picker)
        # self.combo_timezone_calc_src.activated[str].connect(self.update_timezone_calc_src)
        # self.combo_timezone_calc_dst.activated[str].connect(self.update_timezone_calc_dst)
        # self.dtedit_timezone_calc_src.dateTimeChanged.connect(self.sync_timezone_calc_dst)
        self.btn_timezone_pick_add.clicked.connect(self.add_timezone)
        self.btn_timezone_pick_pop.clicked.connect(self.pop_timezone)

    def load_Components(self):
        self.add_time_zone_gbox(self.vlay_timezone, "Australia/Sydney", "Sydney")
        self.add_time_zone_gbox(self.vlay_timezone, "UTC", "UTC")
        self.add_time_zone_gbox(self.vlay_timezone, "Asia/Shanghai", "Asia/Shanghai")
        # self.add_time_zone_gbox(self.vlay_timezone, "Asia/Seoul", "Korea")
        self.add_time_zone_gbox(self.vlay_timezone, "Europe/Dublin", "Europe/Dublin")
        self.add_time_zone_gbox(self.vlay_timezone, "Asia/Kuala_Lumpur", "Asia/Kuala_Lumpur")
        self.add_time_zone_gbox(self.vlay_timezone, "Asia/Singapore", "Asia/Singapore")
        self.add_time_zone_gbox(self.vlay_timezone, "Asia/Kolkata", "Asia/Kolkata")

        self.load_common_timezone_list(self.combo_timezone_pick)
        # self.load_common_timezone_list(self.combo_timezone_calc_src)
        # self.load_common_timezone_list(self.combo_timezone_calc_dst)
        # self.dtedit_timezone_calc_src.setDateTime(QDateTime.currentDateTime())

    def update_timezone_calc_src(self, timezone):
        p_datetime = self.model.get_zone_time(timezone) # "%Y-%m-%d %I:%M:%S %p"
        print(p_datetime)
        q_datetime = QDateTime.fromString(p_datetime, "yyyy-MM-dd hh:mm:ss AP")
        # self.dtedit_timezone_calc_src.setDateTime(q_datetime.toLocalTime())
        self.dtedit_timezone_calc_src.setDate(q_datetime.date())
        self.dtedit_timezone_calc_src.setTime(q_datetime.time())
        print(q_datetime.toString())

    def update_timezone_calc_dst(self, timezone):
        p_datetime = self.model.get_zone_time(timezone)  # "%Y-%m-%d %I:%M:%S %p"
        print(p_datetime)
        q_datetime = QDateTime.fromString(p_datetime, "yyyy-MM-dd hh:mm:ss AP")
        # self.dtedit_timezone_calc_src.setDateTime(q_datetime.toLocalTime())
        self.dtedit_timezone_calc_dst.setDate(q_datetime.date())
        self.dtedit_timezone_calc_dst.setTime(q_datetime.time())
        print(q_datetime.toString())

    def sync_timezone_calc_dst(self):
        print('sync_dst')
        print(self.combo_timezone_calc_src.currentText())
        print(self.combo_timezone_calc_dst.currentText())
        trg_timezone = self.combo_timezone_calc_dst.currentText()
        offset = 1
        print(self.dtedit_timezone_calc_src.dateTime())
        q_datetime = self.dtedit_timezone_calc_src.dateTime()
        datetime_str = q_datetime.toString("yyyy-MM-dd hh:mm:ss AP")
        print(datetime_str)

        if trg_timezone != "":
            dst_datetime = self.model.convert_to_timezone(datetime_str, trg_timezone)
            print('converted time is: ')
            print(dst_datetime)
            q_datetime = QDateTime.fromString(dst_datetime, "yyyy-MM-dd hh:mm:ss AP")
            self.dtedit_timezone_calc_dst.setDate(q_datetime.date())
            self.dtedit_timezone_calc_dst.setTime(q_datetime.time())

    def add_time_zone_gbox(self, vlay, timezone, title):
        hlay_timezone = QHBoxLayout()
        btn_remove_timezone = QPushButton("X")
        btn_remove_timezone.setMaximumWidth(20)
        new_gbox_timezone = TimeZoneGBox(timezone, title)
        hlay_timezone.addWidget(btn_remove_timezone)
        hlay_timezone.addWidget(new_gbox_timezone)
        # vlay.addWidget(new_gbox_timezone)
        vlay.addLayout(hlay_timezone)
        btn_remove_timezone.clicked.connect(lambda : self.remove_timezone(btn_remove_timezone,
                                                                          hlay_timezone,
                                                                          new_gbox_timezone))

    def load_common_timezone_list(self, combobox):
        list = self.model.get_common_timezones()
        combobox.addItem("")
        for a in list:
            combobox.addItem(a)
        # set default value for the combobox
        combobox.lineEdit().setPlaceholderText("Australia/Sydney")
        # combobox.setCurrentText("Australia/Sydney")

    def update_timezone_picker(self, timezone):
        self.model.set_zone(timezone)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timezone_picker_label)
        self.timer.start(1000)

    def update_timezone_picker_label(self):
        a_time = self.model.get_zone_time()
        self.lb_timezone_pick.setText(a_time)

    def add_timezone(self):
        print("Add")
        print(self.combo_timezone_pick.currentText())
        timezone = self.combo_timezone_pick.currentText()
        if timezone != "":
            self.add_time_zone_gbox(self.vlay_timezone, timezone, timezone)
        else:
            print("No Timezone given!")
            self.pop_warning("No timezone value given!")

    def pop_warning(self, message):
        pop_err = QMessageBox()
        pop_err.setIcon(QMessageBox.Warning)
        pop_err.setText("Missing Information")
        pop_err.setInformativeText(message)
        pop_err.setWindowTitle("Warning")
        pop_err.exec_()

    def remove_timezone(self, btn, layout, gbox):
        print("remove")
        layout.setParent(None)
        btn.setParent(None)
        gbox.setParent(None)

    def pop_timezone(self):
        print(self.combo_timezone_pick.currentText())
        timezone = self.combo_timezone_pick.currentText()
        # popup_clock = ClockPopup(timezone)
        popup_clock = ClockPopup(timezone, self)
        popup_clock.show()

class TimeZoneGBox(QGroupBox):
    model = tz_model.TimeZoneModel()
    css_1 = '''
        QGroupBox {
            font: bold 20px;background-color: green;text-align: center;}
        QGroupBox:title {
            color: blue;
            border: 3px solid black;}'''
    css_2 = '''
        QLabel {
            border: 3px solid black;font: bold 15px;background-color: yellow;
            text-align: center;
        }'''
    css_3 = """
        QGroupBox {
            font: bold 14px;
            color: black;}
        QGroupBox:title {
            color: black;
            background-color: yellow;
            border: 0px solid black;}"""
    css_4 = "QLabel {font: bold 15px;}"

    def __init__(self, timezone, title, parent=None):
        super(QGroupBox, self).__init__(parent)
        self.timezone = timezone
        self.title = title
        self.setTitle(self.title)
        self.hlay_new_timezone = QHBoxLayout()
        # self.btn_remove_timezone = QPushButton("Remove")
        self.lb_new_timezone = QLabel(self.timezone)
        self.btn_new_timezone = QPushButton("Pop")
        # self.btn_remove_timezone.setMaximumWidth(70)
        self.btn_new_timezone.setMaximumWidth(70)
        # self.hlay_new_timezone.addWidget(self.btn_remove_timezone)
        self.hlay_new_timezone.addWidget(self.lb_new_timezone)
        self.hlay_new_timezone.addWidget(self.btn_new_timezone)
        self.setLayout(self.hlay_new_timezone)

        # self.btn_new_timezone.clicked.connect(self.run_analog_clock)
        # self.btn_remove_timezone.clicked.connect(self.remove_timezone)
        self.btn_new_timezone.clicked.connect(self.clock_popup)
        self.set_style()
        self.tick()

    def set_style(self):
        self.setStyleSheet(self.css_3)
        self.lb_new_timezone.setStyleSheet(self.css_4)
        self.lb_new_timezone.setAlignment(Qt.AlignCenter)

    def tick(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

    def update_time(self):
        self.lb_new_timezone.setText(self.model.get_zone_time(self.timezone))

    def clock_popup(self):
        self.pop = ClockPopup(self.timezone)
        # self.tz = self.timezone
        self.pop.show()

class ClockPopup(QDialog):

    def __init__(self, name, parent=None):
        super(ClockPopup, self).__init__(parent)
        self.model = tz_model.TimeZoneModel()
        self.timezone = name
        self.timezone_id = self.timezone.encode('latin-1')  # convert str to byte
        self.zone = QTimeZone(self.timezone_id)

        self.init_Ui()
        self.start_tik()
        self.config_Ui()

    def init_Ui(self):
        self.resize(300, 300)
        self.setWindowTitle(self.timezone)
        self.countryLabel = QLabel(QLocale().countryToString(self.zone.country()))
        self.datetime = QLabel()
        self.lay = QVBoxLayout()
        self.lay.addWidget(self.countryLabel)
        self.lay.addWidget(self.datetime)
        self.setLayout(self.lay)

    def start_tik(self):
        timer = QTimer(self)
        timer.timeout.connect(self.update)
        timer.start(1000)

    def config_Ui(self):
        # self.lb2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.countryLabel.setAlignment(Qt.AlignCenter)
        self.countryLabel.setStyleSheet("QLabel {color: grey; font: 18pt;}")
        self.datetime.setAlignment(Qt.AlignCenter)
        self.datetime.setStyleSheet("QLabel {font: 12pt bold;}")

        # window
        # self.setWindowIcon(QIcon('Default.png'))
        # self.setWindowTitle('Clock')
        # self.resize(500, 500)

        # hour pointer
        self.hPointer = QPolygon([
            QPoint(7, 8),
            QPoint(-7, 8),
            QPoint(0, -40)
        ])
        # minute pointer
        self.mPointer = QPolygon([
            QPoint(7, 8),
            QPoint(-7, 8),
            QPoint(0, -70)
        ])
        # second pointer
        self.sPointer = QPolygon([
            QPoint(1, 1),
            QPoint(-1, 1),
            QPoint(0, -90)
        ])
        # colors
        self.bColor = QColor('#0000aa')  # hours and minutes
        self.hColor = QColor(127, 0, 127)
        self.mColor = QColor(0, 127, 127, 191)
        self.sColor = QColor('#aa0087')

    def paintEvent(self, event):
        display_date = self.model.get_zonedate(self.timezone)
        display_time = self.model.get_zonetime(self.timezone)
        self.datetime.setText(display_date + "\n" + display_time)

        rec = min(self.width(), self.height())
        tik = QTime.fromString(display_time, "hh:mm:ss AP")
        # tik = QTime.currentTime()

        # painter
        painter = QPainter(self)

        # zipping code to draw pointers
        def drawPointer(color, rotation, pointer):
            painter.setBrush(QBrush(color))
            painter.save()
            painter.rotate(rotation)
            painter.drawConvexPolygon(pointer)
            painter.restore()

        # tune up painter
        painter.setRenderHint(QPainter.Antialiasing)
        painter.translate(self.width() / 2, self.height() / 2)
        painter.scale(rec / 200, rec / 200)
        painter.setPen(Qt.NoPen)
        # draw pointers
        drawPointer(self.hColor, (30 * (tik.hour() + tik.minute() / 60)), self.hPointer)
        drawPointer(self.mColor, (6 * (tik.minute() + tik.second() / 60)), self.mPointer)
        drawPointer(self.sColor, (6 * tik.second()), self.sPointer)
        # draw face
        painter.setPen(QPen(self.hColor))
        for i in range(12):
            painter.drawLine(88, 0, 96, 0)
            painter.rotate(30.0)

        painter.setPen(QPen(self.mColor))
        for j in range(60):
            if (j % 5) != 0:
                painter.drawLine(92, 0, 96, 0)
            painter.rotate(6.0)