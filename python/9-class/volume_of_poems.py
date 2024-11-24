import inspect
from time import sleep

from bestiary.knight import Knight
from bestiary.dragon import Dragon

from weaponry.sword import Sword
from weaponry.shield import Shield
from weaponry.crossbow import Crossbow


def dragons_legend():
    print()
    print("В огне преисподней, под семью горами,")
    print("Родилась бестия проклятая — дракон 🐲")
    print("Его лапищи все остры когтями,")
    print("И изрыгает чудище огонь!")


def knight_without_a_name():
    print("И как то его звали... "
          "\nНо имени ему не дали, "
          "\nОт грусти и тоски он был в запое")
    print()
    print("И так закончилась история героя, "
          "\nБез имени он жил, "
          "\nБез имени он пал, "
          "\nИ даже не на поле боя")
    sleep(0.1)
    raise SystemExit("Спился")


def inglorious_fate(why: str):
    match why:
        case "sword":
            print(" " + Sword.DEFAULT_SWORD_NAME + "...")
            print("Куда ж таким мечом разить дракона...")
        case "shield":
            print("Куда с таким щитом идти к дракону...")
        case "crossbow":
            print("О ужас! О ужас наводящий рок!\n"
                  "Наш рыцарь волей судеб дернул за курок!")

    print("Увечил сам себя стрелой в колено,")
    print("И встал он у ворот, заложником бытского плена")
    sleep(0.1)
    raise SystemExit("О стражниках у ворот не слагают баллад")


def the_only_nobleness():
    expected_params = {'self', 'name'}
    actual_params = set(inspect.signature(Knight.__init__).parameters)

    if expected_params != actual_params:
        print("А что есть главный добротель сэра? Гордость?\n"
              "Не острый меч — смирение и скромность")
        sleep(0.1)
        raise SystemExit("Чтобы стать рыцарем, тебе нужно лишь рыцарское имя 🥀")


def are_you_still_a_knight():
    the_only_nobleness()
    print("Кто? О ком вы говорите? "
          "\nМы тут таких не знаем!")
    sleep(0.1)
    raise SystemExit("В этом мире пока что нет рыцарей и рифмы")


def the_shield_of_crown():
    print("Иль правда... Или ложь...")
    print("Иль числа... Или строки...")
    print("Понять хотел он, все еще ли щит пригож")
    sleep(0.1)
    raise SystemExit("Пал жертвой философских размышлений")


def uneducated_shameful_death():
    print("... Но рыцарь оказался неразумен,\n"
          "Не сдюжил сосчитать до трех\n"
          "Осмеянный толпой он сделался безумен!\n"
          "Расстроился, закрыл глаза и сдох 💀")
    sleep(0.1)
    raise SystemExit("Семью восемь — признайся сам себе, успел ответить за 3 секунды?")


def spoiled_health():
    # "Родился в знатном доме он, жил на раздолье"
    print("Но нету в нем здоровье, упал на копчик и преставился прям в поле")
    sleep(0.1)
    raise SystemExit("Сводка в новостях: рыцарь бесславно погиб от перелома копчика")


def are_you_still_a_human():
    print("Он был не человек, и заперт был в неволе")
    sleep(0.1)
    raise SystemExit("Если здоровье его не людское — какой же он рыцарь?")


def forgotten_his_roots():
    print("Но рыцарь славный занемог,")
    print("Забыл родных, произнести не смог,")
    print("Их имена как велит ему кодекс")
    print("И обратился от драконьего огня он в оникс")
    sleep(0.1)
    raise SystemExit("Все рыцари это знают — не забывай свои корни, помни!")


def dragon_comes():
    print()
    print("Стоит наш рыцарь славный у пещеры,\n"
          "И слышит рёв, вот-вот и ящер нападёт,\n"
          "Всё ближе, нос почуял запах серы,\n"
          "И вот рывок, дракон рычит и рубит лапой,\n"
          "А вдруг он рыцаря убьёт?")


def both_dead():
    print("""
        Нет в мире зла, и нет добра, 
        Нет рыцаря, и нет дракона. 
        Одна лишь в мире тишина, 
        Сверкает лишь щита корона.
        """)
    print()
    print("Ачивка True Neutral — редчайший исход! ")


def forgotten_himself():
    print("Ты зри то зри...")
    print("А я лишь соберусь с мыслями...")
    print("Сейчас скажу я кто я...")
    print("Сюда я вроде шел степями...")
    sleep(0.1)
    raise SystemExit("От скуки рыцарь был сожжён")


def dragon_is_dead():
    print()
    print("Ликуй честной народ, кричи толпа!")
    print("Яиц, детей драконьих бита скорлупа.")
    print("Был ящер папа, или мать,")
    print("Не яйца ли пытался защищать?")
    print("Убит тиран, чудовище — дракон.")
    print("Герою проявить он дал отвагу,")
    print("И лишь для этого он был рожден.")
    print("Герой лишь тих — не зря-ль убил он бедолагу? 🥀")


def hero_is_dead():
    print()
    print("Так был хорош собой, и мил он к люду,")
    print("Был верен клятве, храбрейшим львом он был в бою.")
    print("И весть пойдет, и будут знать повсюду,")
    print("Что Росс Ван Гвидо умер, спасая родину свою")


def coda():
    print()
    print("🥀 И славен был его конструктор 🥀\n"
          "🥀 Его статический и инстанс метод 🥀\n"
          "🥀 Кричал свой гимн он репром гулко 🥀\n"
          "🥀 Баллады мы поем про ООП 🥀\n\n"
          "🥀 Coda. 🥀")
