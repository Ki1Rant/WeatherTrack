import sys
from PyQt6 import uic
from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtWidgets import QApplication, QMainWindow
from weather_api.init import WeatherServices
from ui.ui_main_window import Ui_WeatherTracker

class WeatherThread(QThread, WeatherServices):
    weather_result = pyqtSignal(dict)
    error_occured = pyqtSignal(str)

    def __init__(self, city):
        super().__init__()
        self.city = city
        self.weather_service = WeatherServices()

    def run(self):
        try:
            weather_data = self.weather_service.get_weather(self.city)
            self.weather_result.emit(weather_data)
        except Exception as e:
            self.error_occured.emit(str(e))

class WeatherApp(QMainWindow, Ui_WeatherTracker):
    def __init__(self):
        super().__init__()

        self.ui = Ui_WeatherTracker()
        self.ui.setupUi(self)

        self.weather_thread = None

        self.setup_city_combo()
        self.ui.CityBox.currentIndexChanged.connect(self.on_city_changed)

    def setup_city_combo(self):
        popular_cities = [
            ("Москва", "Moscow"),
            ("Санкт-Петербург", "Saint Petersburg"),
            ("Новосибирск", "Novosibirsk"),
            ("Екатеринбург", "Yekaterinburg"),
            ("Казань", "Kazan"),
            ("Нижний Новгород", "Nizhny Novgorod"),
            ("Волгоград", "Volgograd")
        ]

        for city_name, city_id in popular_cities:
            self.ui.CityBox.addItem(city_name, city_id)

        self.ui.CityBox.setCurrentIndex(0)

    def on_city_changed(self, index):
        if index != -1:
            self.load_weather()


    def load_weather(self):
        city_name = self.ui.CityBox.currentText()

        if self.weather_thread and self.weather_thread.isRunning():
             self.weather_thread.terminate()
             self.weather_thread.wait()

        self.weather_thread = WeatherThread(city_name)
        self.weather_thread.weather_result.connect(self.display_weather)
        self.weather_thread.start()


    def display_weather(self, weather_data):
        try:
            self.ui.Temp.setText(f"{int(weather_data['temperature'])}°C")
            self.ui.otherStat.setText(f"""
            Ощущается как:{int(weather_data['feels_like'])}
            На улице:{weather_data['description']}
            Влажность:{weather_data['humidity']}
            Давление:{weather_data['pressure']}
            Скорость ветра:{weather_data['wind_speed']}
            """)
        except AttributeError as e:
            print(f"Ошибка обновления интерфейса: {e}")
            print("Проверьте имена виджетов в UI файле")



def main():
    app = QApplication(sys.argv)

    # Создание и отображение главного окна
    window = WeatherApp()
    window.show()

    # Запуск основного цикла
    sys.exit(app.exec())


if __name__ == "__main__":
    main()