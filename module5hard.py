import hashlib
import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
class Video :
    time_now = 0
    def __init__(self, title, duration, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = Video.time_now
        self.adult_mode = adult_mode
class UrTube:
    def __init__(self):
        self.data_pass = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.data_pass:
            if user in self.data_pass:
                if self.data_pass[nickname].password == hash(password):
                    self.current_user = user
                    print(f"Добро пожаловать, {nickname}!")
                    return True
                else:
                    print("Неверный пароль.")
                    return False
            else:
                print("Пользователь не найден.")
                return False

    def register(self, nickname, password, age):
        for user in self.data_pass:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
        new_user = User(nickname, password, age)
        self.current_user = new_user
        self.data_pass.append(new_user)
    def log_out(self):
        self.current_user = None
    def add(self, *videos):
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)

    def get_videos(self, search_word):
        return [video.title for video in self.videos if search_word.lower() in video.title.lower()]
    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                print(f"Начинаем просмотр видео: {video.title}")
                while video.time_now < video.duration:
                    print(video.time_now)
                    time.sleep(1)
                    video.time_now += 1
                print("Конец видео")
                video.time_now = 0  # после завершения 0
                return
        print("Видео не найдено")

ur = UrTube()
# us1 = User('Max', '123', 48)
# print(us1.nickname, us1.password, us1.age)
# us2 = User('Sergey', '321', 55)
# us3 = User('Daria', '012', 45)
# User('Max', '123', 48)

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
